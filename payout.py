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
import os
import math


################################################################
# Define the payout calculation here
################################################################
public_key = "B62qif7HxYzQCb8v2FN3KgZkS8oevDG2zqYqzkdjSV1Smf6jbEcPVEc"  # Public key of the block producer
staking_epoch = 5  # To ensure we only get blocks from the current staking epoch as the ledger may be different
latest_block = False  # If not set will get the latest block from MinaExplorer or fix the latest height here
fee = 0.0  # The fee percentage to charge
min_height = 25560  # This can be the last known payout or this could vary the query to be a starting date
max_height = 225580
confirmations = 18  # Can set this to any value for min confirmations up to `k`. 15 is recommended.

no_pay_address = [  # my own addresses, no need for payment
    "B62qif7HxYzQCb8v2FN3KgZkS8oevDG2zqYqzkdjSV1Smf6jbEcPVEc",
    "B62qmvHQzJmT2rKE1F9RemenGRG8BfXT1Kurve3eT4iC2HMrWiaVG3H",
]
payment_command = "mina client send-payment -amount amt -receiver rcvr -fee 0.001 -sender " \
                  "SUPERCHARGED_POOL -memo Supercharged_pool"

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
locked_accounts = []
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
    if not s["timing"]:  # wallet unlocked
        timed_weighting = 1
    else:
        timed_weighting = s["timing"]["timed_weighting"]  # wallet is locked

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
        locked_accounts.append({
            "publicKey": s["public_key"],
            "total": 0,
            "staking_balance": s["balance"],
            "timed_weighting": timed_weighting,  # timed_weighting=1 means unlocked, 0 means locked
        })
    # Sum the total of the pool
    total_staking_balance += s["balance"]

assert (total_unlocked_staking_balance <= total_staking_balance)

# print the information of total and unlocked staking accounts and tokens
staking_info = f"\nThe pool's total staking balance is: {total_staking_balance}. \n"
if len(locked_accounts) > 0:
    staking_info += f"However, only {total_unlocked_staking_balance} of it is unlocked, \n"
else:
    staking_info += f"All of the tokens are unlocked, \n"
staking_info += f"and the block rewards are shared by the {len(payouts)} unlocked accounts.\n"
print(staking_info)

################################################################
# Get the blocks info and the total amount of rewards
################################################################

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


if not blocks["data"]["blocks"]:
    exit("Nothing to payout as we didn't win anything")

#  iteration over the blocks to calculate the rewards
for b in blocks["data"]["blocks"]:

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

    # We calculate rewards multiple ways to sense check
    assert (total_rewards == total_rewards_prev_method)

    total_fees = int(fee * total_rewards)
    # update all blocks total rewards and fees info
    all_blocks_total_rewards += total_rewards
    all_blocks_total_fees += total_fees

    # Determine the pool weighting based on sum of stakes of UNLOCKED accounts
    for p in payouts:
        effective_pool_weighting = p["staking_balance"] / total_unlocked_staking_balance

        # This must be less than 1 or we have a major issue
        assert effective_pool_weighting <= 1

        block_total = math.floor(total_rewards *
                                 effective_pool_weighting * (1 - fee))
        p["total"] += block_total

        # Store this data in a structured format for later querying and for the payment script, handled seperately
        store_payout.append({
            "publicKey":
            p["publicKey"],
            "blockHeight":
            b["blockHeight"],
            "stateHash":
            b["stateHash"],
            "totalPoolStakes":
            total_staking_balance,
            "effectivePoolWeighting":
            effective_pool_weighting,
            "effectivePoolStakes":
            p["staking_balance"],
            "stakingBalance":
            p["staking_balance"],
            "dateTime":
            b["dateTime"],
            "coinbase":
            int(b["transactions"]["coinbase"]),
            "totalRewards":
            total_rewards,
            "payout":
            block_total,
            "epoch":
            staking_epoch,
            "ledgerHash":
            ledger_hash
        })


################################################################
# Print some helpful data to the screen
################################################################

print(f"We won these {len(blocks_table)} blocks:")

print(
    tabulate(blocks_table,
             headers=[
                 "BlockHeight", "Coinbase",
                 "Producer Fee Transfers", "Snark Fee Transfers",
                 "Coinbase Fee Transfers"
             ],
             tablefmt="pretty"))

print(f"We have received grand total of "
      f"{Currency.Currency(all_blocks_total_rewards,format=Currency.CurrencyFormat.NANO).decimal_format()} "
      f"mina in this window. ")

print("Our fee at 0% is " +
      Currency.Currency(all_blocks_total_fees,
                        format=Currency.CurrencyFormat.NANO).decimal_format() +
      " mina, and the total payout amount is " +
      Currency.Currency(all_blocks_total_rewards-all_blocks_total_fees,
                        format=Currency.CurrencyFormat.NANO).decimal_format()
      )

payout_table = []
payout_json = []
payout_commands = []

for p in payouts:
    payout_table.append([
        p["publicKey"],
        Currency.Currency(
            p["staking_balance"],
            format=Currency.CurrencyFormat.WHOLE).decimal_format(), True, p["total"],
        Currency.Currency(
            p["total"], format=Currency.CurrencyFormat.NANO).decimal_format(),
    ])

    # only generate payment commands for addresses that are not the node runner's
    if p["publicKey"] not in no_pay_address:
        cur_payment_command = payment_command.replace("amt", Currency.Currency(
            p["total"], format=Currency.CurrencyFormat.NANO).decimal_format())
        cur_payment_command = cur_payment_command.replace("rcvr", p["publicKey"])
        payout_commands.append(cur_payment_command)
        # payout_json.append({"publicKey": p["publicKey"], "total": p["total"]})

for p in locked_accounts:
    payout_table.append([
        p["publicKey"],
        Currency.Currency(
            p["staking_balance"],
            format=Currency.CurrencyFormat.WHOLE).decimal_format(), False, p["total"],
        Currency.Currency(
            p["total"], format=Currency.CurrencyFormat.NANO).decimal_format(),
    ])

print(
    tabulate(payout_table,
             headers=[
                 "PublicKey", "Staking Balance", "Unlocked?", "Payout nanomina",
                 "Payout mina", "Foundation"
             ],
             tablefmt="pretty"))

# TIf you want, output the payout json to take to the next stage to sign or use output from table above
for cmd in payout_commands:
    print(cmd)

