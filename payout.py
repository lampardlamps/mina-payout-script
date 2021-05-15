################################################################
# This is a POC implementation of the payout system listed at
# https://docs.minaexplorer.com/minaexplorer/calculating-payments
# It is not meant for production use. This will output or store the
# payments which must then be processed seperately e.g. by signing
# the tx using coda sdk and then broadcasting. A better implementation is
# at https://github.com/jrwashburn/mina-pool-payout and recommended
################################################################

from tabulate import tabulate
import Currency
import GraphQL
import Mongo
import os
import math

client = Mongo.Mongo()

################################################################
# Define the payout calculation here
################################################################
public_key = "B62qpJavug1VGCBSttepmXr6nh8fvXY5SigbN44ttYDia65vwbTEcq2"  # Public key of the block producer
staking_epoch = 3  # To ensure we only get blocks from the current staking epoch as the ledger may be different
latest_block = False  # If not set will get the latest block from MinaExplorer or fix the latest height here
fee = 0.025  # The fee percentage to charge
min_height = 15107  # This can be the last known payout or this could vary the query to be a starting date
max_height = 20000
confirmations = 18  # Can set this to any value for min confirmations up to `k`. 15 is recommended.
store = False  # Do we want to store this

# Determine the ledger hash from GraphQL. As we know the staking epoch we can get any block in the epoch
try:
    ledger_hash = GraphQL.getLedgerHash(epoch=staking_epoch)
    ledger_hash = ledger_hash["data"]["blocks"][0] \
                             ["protocolState"]["consensusState"] \
                             ["stakingEpochData"]["ledger"]["hash"]
    print(f"Using ledger hash: {ledger_hash}")
except Exception as e:
    print(e)
    exit("Issue getting ledger_hash from GraphQL")

if not latest_block:
    # Get the latest block height
    latest_block = GraphQL.getLatestHeight()
else:
    latest_block = {'data': {'blocks': [{'blockHeight': latest_block}]}}

if not latest_block:
    exit("Issue getting the latest height")

assert latest_block["data"]["blocks"][0]["blockHeight"] > 1

# Only ever pay out confirmed blocks
max_height = min(max_height, latest_block["data"]["blocks"][0]["blockHeight"] - confirmations)

assert max_height <= latest_block["data"]["blocks"][0]["blockHeight"]

print(
    f"This script will payout from blocks {min_height} to {max_height} in epoch {staking_epoch}"
)

# Initialize variables
total_staking_balance = 0
total_unlocked_staking_balance = 0
locked_account = []
payouts = []
all_blocks_total_rewards = 0
all_blocks_total_fees = 0
store_payout = []
blocks_table = []

# Get the staking ledger for an epoch
try:
    staking_ledger = GraphQL.getStakingLedger({
        "delegate": public_key,
        "ledgerHash": ledger_hash,
    })
except Exception as e:
    print(e)
    exit("Issue getting staking ledger from GraphQL")

if not staking_ledger["data"]["stakes"]:
    exit("We have no stakers")

for s in staking_ledger["data"]["stakes"]:

    # Clean up timed weighting, if no timing info, then the wallet is unlocked;
    if not s["timing"]:
        # print(f"wallet {s['public_key']} is unlocked!")
        timed_weighting = 1
    else:
        print(f'wallet {s["public_key"]} is locked!')
        timed_weighting = s["timing"]["timed_weighting"]

    # only include in the payout addresses if it is unlocked
    if timed_weighting:
        payouts.append({
            "publicKey": s["public_key"],
            "total": 0,
            "staking_balance": s["balance"],
            "timed_weighting": timed_weighting,  # timed_weighting=1 means unlocked, 0 means locked
        })

        # Sum the total of the pool
        total_unlocked_staking_balance += s["balance"]
    else:
        locked_account.append({
            "publicKey": s["public_key"],
            "total": 0,
            "staking_balance": s["balance"],
            "timed_weighting": timed_weighting,  # timed_weighting=1 means unlocked, 0 means locked
        })
    # Sum the total of the pool
    total_staking_balance += s["balance"]

assert (total_unlocked_staking_balance <= total_staking_balance)

# print the information of total and unlocked staking accounts and tokens
staking_info = f"The pool's total staking balance is: {total_staking_balance}. "
if len(locked_account) > 0:
    staking_info += f"However, only {total_unlocked_staking_balance} of it is unlocked, "
else:
    staking_info += f"All of the tokens are unlocked, "

# Who are we going to pay?
staking_info += f"and the block rewards are shared by these {len(payouts)} unlocked accounts."
print(staking_info)

try:
    blocks = GraphQL.getBlocks({
        "creator": public_key,
        "epoch": staking_epoch,
        "blockHeightMin": min_height,
        "blockHeightMax": max_height,
    })
except Exception as e:
    print(e)
    exit("Issue getting blocks from GraphQL")

# #DEBUG
# # print(blocks)
#
if not blocks["data"]["blocks"]:
    exit("Nothing to payout as we didn't win anything")

################################################################
# Start of blocks loop
################################################################
for b in blocks["data"]["blocks"]:

    # # Keep track of payouts per block
    # foundation_payouts = 0
    # other_payouts = 0

    # This will always be defined except when it is not...
    if not b["transactions"]["coinbaseReceiverAccount"]:
        print(
            f"{b['blockHeight']} didn't have a coinbase so won it but no rewards."
        )
        break

    coinbase_receiver = b["transactions"]["coinbaseReceiverAccount"][
        "publicKey"]

    ####################################
    # FEE TRANSFERS
    ####################################
    fee_transfers = list(
        filter(lambda d: d['type'] == "Fee_transfer",
               b["transactions"]["feeTransfer"]))

    fee_transfers_by_coinbase = list(
        filter(lambda d: d['type'] == "Fee_transfer_via_coinbase",
               b["transactions"]["feeTransfer"]))

    total_fee_transfers = sum(int(item['fee']) for item in fee_transfers)
    # Note there can be more than 1 coinbase
    fee_transfer_for_coinbase = sum(
        int(item['fee']) for item in fee_transfers_by_coinbase)

    # Sum all the fee transfers to this account with type of fee_transfer - these are the tx fees
    fee_transfer_to_creator = list(
        filter(lambda d: d['recipient'] == coinbase_receiver, fee_transfers))
    total_fee_transfers_to_creator = sum(
        int(item['fee']) for item in fee_transfer_to_creator)

    # Sum all the fee transfers not to this account with type of fee_transfer - this is snark work for the included tx
    fee_transfer_to_snarkers = total_fee_transfers - total_fee_transfers_to_creator

    # What are the rewards for the block - this is how we used to calculate it
    # this serves as a sense check currently to check logic
    total_rewards_prev_method = int(b["transactions"]["coinbase"]) + int(
        b["txFees"]) - int(b["snarkFees"])

    # Can also define this via fee transfers
    total_rewards = int(
        b["transactions"]["coinbase"]
    ) + total_fee_transfers_to_creator - fee_transfer_for_coinbase

    blocks_table.append([
        b['blockHeight'],
        b["transactions"]["coinbase"], total_fee_transfers_to_creator,
        fee_transfer_to_snarkers, fee_transfer_for_coinbase
    ])

    # print(total_fee_transfers_to_creator,fee_transfer_to_snarkers,fee_transfer_for_coinbase)

    # We calculate rewards multiple ways to sense check
    assert (total_rewards == total_rewards_prev_method)

    total_fees = int(fee * total_rewards)

    all_blocks_total_rewards += total_rewards
    all_blocks_total_fees += total_fees

print(f"all blocks total rewards {all_blocks_total_rewards} and total fees {all_blocks_total_fees}")
#
#     #######################################################
#     # Determine the amount we need to pay the Foundation
#     # This algorithm is according to the published rules
#     # We don't need to account for supercharged rewards or
#     # share the transaction fees, so this is **good** for the pool
#     # as we share all these rewards. We first work out the Foundation
#     # payments and then subtract from the total rewards before sharing
#     # the remainder among the pool
#     #######################################################
#
#     for p in payouts:
#
#         if p["foundation_delegation"]:
#
#             # Only pay foundation a % of the normal coinbase
#             # Round down to the nearest nanomina
#             foundation_block_total = math.floor(
#                 (p["staking_balance"] / total_staking_balance) * coinbase *
#                 (1 - fee))
#
#             p["total"] += foundation_block_total
#
#             store_payout.append({
#                 "publicKey": p["publicKey"],
#                 "blockHeight": b["blockHeight"],
#                 "stateHash": b["stateHash"],
#                 "totalPoolStakes": total_staking_balance,
#                 "stakingBalance": p["staking_balance"],
#                 "dateTime": b["dateTime"],
#                 "coinbase": int(b["transactions"]["coinbase"]),
#                 "totalRewards": total_rewards,
#                 "payout": foundation_block_total,
#                 "epoch": staking_epoch,
#                 "ledgerHash": ledger_hash,
#                 "foundation": True
#             })
#
#             # Track all the Foundation payouts
#             foundation_payouts += foundation_block_total
#         else:
#             # # This was a non foundation address
#             # # So calculate this the other way
#             # supercharged_contribution = (
#             #     (supercharged_weighting - 1) * p["timed_weighting"]) + 1
#             # effective_stake = p["staking_balance"] * supercharged_contribution
#             # # This the effective percentage of the pool disregarding the Foundation element
#             # effective_pool_stakes[p["publicKey"]] = effective_stake
#             # sum_effective_pool_stakes += effective_stake
#
#     # Check here the balances make sense
#     assert (foundation_payouts <= total_rewards)
#
#     # assert (sum_effective_pool_stakes <= 2 * total_staking_balance)
#
#     # What are the remaining rewards we can share? This should always be higher than if we don't share.
#     block_pool_share = total_rewards - (foundation_payouts / (1 - fee))
#
#     # Determine the effective pool weighting based on sum of effective stakes
#     for p in payouts:
#         if not p["foundation_delegation"]:
#             effective_pool_weighting = effective_pool_stakes[
#                 p["publicKey"]] / sum_effective_pool_stakes
#
#             #This must be less than 1 or we have a major issue
#             assert effective_pool_weighting <= 1
#
#             block_total = math.floor(block_pool_share *
#                                      effective_pool_weighting * (1 - fee))
#             p["total"] += block_total
#
#             other_payouts += block_total
#
#             # Store this data in a structured format for later querying and for the payment script, handled seperately
#             store_payout.append({
#                 "publicKey":
#                 p["publicKey"],
#                 "blockHeight":
#                 b["blockHeight"],
#                 "stateHash":
#                 b["stateHash"],
#                 "totalPoolStakes":
#                 total_staking_balance,
#                 "effectivePoolWeighting":
#                 effective_pool_weighting,
#                 "effectivePoolStakes":
#                 effective_pool_stakes[p["publicKey"]],
#                 "superchargedContribution":
#                 supercharged_contribution,
#                 "stakingBalance":
#                 p["staking_balance"],
#                 "sumEffectivePoolStakes":
#                 sum_effective_pool_stakes,
#                 "superChargedWeighting":
#                 supercharged_weighting,
#                 "dateTime":
#                 b["dateTime"],
#                 "coinbase":
#                 int(b["transactions"]["coinbase"]),
#                 "totalRewards":
#                 total_rewards,
#                 "payout":
#                 block_total,
#                 "epoch":
#                 staking_epoch,
#                 "ledgerHash":
#                 ledger_hash
#             })
#
#     # Final check
#     # These are essentially the same but we allow for a tiny bit of nanomina rounding and worst case we never pay more
#     assert (foundation_payouts + other_payouts + total_fees <= total_rewards)
#
# # Store the payouts here so we can generate transactions
# if store:
#
#     if not os.getenv('MONGO_URI'):
#         exit("No Mongo connection string provided")
#
#     try:
#         post_id = client.collection.insert_many(store_payout)
#     except Exception as e:
#         print(e)
#         exit("There was an issue storing a payout")
#
# ################################################################
# # Print some helpful data to the screen
# ################################################################
#
# print(f"We won these {len(blocks_table)} blocks:")
#
# print(
#     tabulate(blocks_table,
#              headers=[
#                  "BlockHeight", "Supercharged Weighting", "Coinbase",
#                  "Producer Fee Transfers", "Snark Fee Transfers",
#                  "Coinbase Fee Transfers"
#              ],
#              tablefmt="pretty"))
#
# print(f"We are paying out {all_blocks_total_rewards} nanomina in this window.")
#
# print("That is " +
#       Currency.Currency(all_blocks_total_rewards,
#                         format=Currency.CurrencyFormat.NANO).decimal_format() +
#       " mina")
#
# print("Our fee is " +
#       Currency.Currency(all_blocks_total_fees,
#                         format=Currency.CurrencyFormat.NANO).decimal_format() +
#       " mina")
#
# payout_table = []
# payout_json = []
#
# for p in payouts:
#     payout_table.append([
#         p["publicKey"],
#         Currency.Currency(
#             p["staking_balance"],
#             format=Currency.CurrencyFormat.WHOLE).decimal_format(), p["total"],
#         Currency.Currency(
#             p["total"], format=Currency.CurrencyFormat.NANO).decimal_format(),
#         p["foundation_delegation"]
#     ])
#
#     payout_json.append({"publicKey": p["publicKey"], "total": p["total"]})
#
# print(
#     tabulate(payout_table,
#              headers=[
#                  "PublicKey", "Staking Balance", "Payout nanomina",
#                  "Payout mina", "Foundation"
#              ],
#              tablefmt="pretty"))

# TIf you want, output the payout json to take to the next stage to sign or use output from table above
#print(payout_json)