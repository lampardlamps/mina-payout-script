##############################################################################################
# This is an implementation of the payout system of the Supercharged Pool, which is listed at
# https://docs.google.com/document/d/1x_qMqKYF3WMK5GMIgSUWQ6oqKGn8-7uzd6Kd-soaGdE/edit (in English)
# and https://docs.qq.com/doc/DRXZXUnFUcFZvcG5S (in Chinese).
# The main logic is that all the block rewards received by the pool are shared by the wallets
# with ONLY unlocked tokens proportional to their delegation amounts; wallets with locked tokens
# are not paid.
###############################################################################################

from tabulate import tabulate
import Currency
import GraphQL
import os
import math
from datetime import datetime
import time


################################################################
# Define the payout calculation here, need to be manually input
################################################################
public_key = "B62qif7HxYzQCb8v2FN3KgZkS8oevDG2zqYqzkdjSV1Smf6jbEcPVEc"  # Public key of the block producer
staking_epoch = 31  # To ensure we only get blocks from the current staking epoch as the ledger may be different
latest_block = False  # If not set will get the latest block from MinaExplorer or fix the latest height here
fee = 0.0  # The fee percentage to charge
if time.time() > 1630454400:
    fee = 0.025    # fees are 2.5% after 1st Sep
confirmations = 18  # Can set this to any value for min confirmations on the canonical chain. 15 is recommended.
payout_address = "B62qmvHQzJmT2rKE1F9RemenGRG8BfXT1Kurve3eT4iC2HMrWiaVG3H"
nonce = int(GraphQL.getNonce(payout_address))
no_pay_address = [  # node runner's own addresses, no need for payment
    "B62qif7HxYzQCb8v2FN3KgZkS8oevDG2zqYqzkdjSV1Smf6jbEcPVEc",
    "B62qmvHQzJmT2rKE1F9RemenGRG8BfXT1Kurve3eT4iC2HMrWiaVG3H",
    "B62qk2bwhv6KNHyaUjC4ab8XPhAvDDUByaR4dGXqvR8d7duavJVNq8e",
]

# for generating payment commands
payment_command = "mina client send-payment -amount amt -receiver rcvr -fee 0.001 -sender " \
                  "$SUPERCHARGED_POOL -memo Supercharged_pool -nonce "

##################################################################

# initiating files for records keeping
curDate = datetime.today().strftime('%Y-%m-%d')
fileName = os.getcwd()+f'/records/Epoch_{staking_epoch}_'+curDate+".md"
f = open(fileName, "w")
f.write("```\n")

# payment commands
g = open(os.getcwd()+f'/records/commands_epoch_{staking_epoch}.sh', "w")
g.write("export $(cat ~/.mina-env | xargs)\n\n"   # read env for password
        "mina accounts import -privkey-path ~/cb_keys/my-wallet\n\n"
        "export SUPERCHARGED_POOL=B62qmvHQzJmT2rKE1F9RemenGRG8BfXT1Kurve3eT4iC2HMrWiaVG3H\n\n"
        "mina accounts unlock -public-key $SUPERCHARGED_POOL \n\n")

# Determine the ledger hash from GraphQL. As we know the staking epoch we can get any block in the epoch
try:
    ledger_hash = GraphQL.getLedgerHash(epoch=staking_epoch)
    ledger_hash = ledger_hash["data"]["blocks"][0] \
                             ["protocolState"]["consensusState"] \
                             ["stakingEpochData"]["ledger"]["hash"]
    print(f"Using ledger hash: {ledger_hash}")
    f.write(f"Using ledger hash: {ledger_hash}\n")
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

# # Only ever pay out confirmed blocks
# max_height = min(max_height, latest_block["data"]["blocks"][0]["blockHeight"] - confirmations)
# assert max_height <= latest_block["data"]["blocks"][0]["blockHeight"]

print(
    f"This script will payout from blocks in epoch {staking_epoch}"
)
f.write(f"This script will payout from blocks in epoch {staking_epoch}\n")

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
    if timed_weighting and float(s["balance"]) >= 0.5:
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
    staking_info += f"However, only {total_unlocked_staking_balance} of it is eligible, \n"
else:
    staking_info += f"All of the tokens are unlocked, \n"
staking_info += f"and the block rewards are shared by the {len(payouts)} accounts " \
                f"that are both unlocked and have >0.5 MINA balance.\n"
print(staking_info)
f.write(staking_info+"\n")

################################################################
# Get the blocks info and the total amount of rewards
################################################################

try:
    blocks = GraphQL.getBlocks({
        "creator": public_key,
        "epoch": staking_epoch,
    })

    if not blocks["data"]["blocks"]:
        no_block_text = "Unfortunately we didn't produce any canonical block, so there is nothing to payout this epoch."
        f.write(no_block_text)
        f.close()
        exit(no_block_text)

    max_height = blocks["data"]["blocks"][0]['blockHeight']
    assert max_height <= latest_block["data"]["blocks"][0]["blockHeight"]-confirmations

except Exception as e:
    print(e)
    exit("Issue getting blocks from GraphQL")



#  iteration over the blocks to calculate the rewards
for b in blocks["data"]["blocks"]:

    # This will always be defined except when it is not...
    if not b["transactions"]["coinbaseReceiverAccount"]:
        print(
            f"{b['blockHeight']} didn't have a coinbase so won it but no rewards."
        )
        continue

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
f.write(f"We won these {len(blocks_table)} blocks:\n")

print(
    tabulate(blocks_table,
             headers=[
                 "BlockHeight", "Coinbase",
                 "Producer Fee Transfers", "Snark Fee Transfers",
                 "Coinbase Fee Transfers"
             ],
             tablefmt="pretty"))
f.write(
    tabulate(blocks_table,
             headers=[
                 "BlockHeight", "Coinbase",
                 "Producer Fee Transfers", "Snark Fee Transfers",
                 "Coinbase Fee Transfers"
             ],
             tablefmt="pretty"))
f.write("\n")

print(f"We have received grand total of "
      f"{Currency.Currency(all_blocks_total_rewards,format=Currency.CurrencyFormat.NANO).decimal_format()} "
      f"mina in this window. ")
f.write(f"\nWe have received grand total of "
      f"{Currency.Currency(all_blocks_total_rewards,format=Currency.CurrencyFormat.NANO).decimal_format()} "
      f"mina in this window. \n")

print(f"Our fee at {fee*100}% is " +
      Currency.Currency(all_blocks_total_fees,
                        format=Currency.CurrencyFormat.NANO).decimal_format() +
      " mina, and the total payout amount is " +
      Currency.Currency(all_blocks_total_rewards-all_blocks_total_fees,
                        format=Currency.CurrencyFormat.NANO).decimal_format()
      )
apy = round((all_blocks_total_rewards/1e9/total_unlocked_staking_balance)*365*24*60*100/(7140*3),2)
print(f"\nThe estimated APY before fees is {apy}%. \n")

f.write(f"Our fee at {fee*100}% is " +
      Currency.Currency(all_blocks_total_fees,
                        format=Currency.CurrencyFormat.NANO).decimal_format()+" mina, and the total payout amount is " +
      Currency.Currency(all_blocks_total_rewards-all_blocks_total_fees,
                        format=Currency.CurrencyFormat.NANO).decimal_format()
      )
f.write(f"\nThe estimated APY before fees is {apy}%. \n")

# to assert that the currect epoch number is input at the beginning of the programme
if latest_block["data"]["blocks"][0]["blockHeight"] - max_height > 5000:
    exit('We should be paying for the epoch which has just ended, not a previous one. '
         'Check your staking epoch value again!!')

payout_table = []
payout_json = []
payout_commands = []

for p in payouts:
    payout_table.append([
        p["publicKey"],
        Currency.Currency(
            p["staking_balance"],
            format=Currency.CurrencyFormat.WHOLE).decimal_format(), True,
        Currency.Currency(
            p["total"], format=Currency.CurrencyFormat.NANO).decimal_format(),
    ])

    # only generate payment commands for addresses that are not the node runner's
    if p["publicKey"] not in no_pay_address:
        cur_payment_command = payment_command.replace("amt", Currency.Currency(
            p["total"], format=Currency.CurrencyFormat.NANO).decimal_format())
        cur_payment_command = cur_payment_command.replace("rcvr", p["publicKey"])
        cur_payment_command += f"{nonce}"
        nonce += 1
        payout_commands.append(cur_payment_command)
        # payout_json.append({"publicKey": p["publicKey"], "total": p["total"]})

for p in locked_accounts:
    if p["staking_balance"] <= 0.001:
        p["staking_balance"] = 0
    payout_table.append([
        p["publicKey"],
        Currency.Currency(
            p["staking_balance"],
            format=Currency.CurrencyFormat.WHOLE).decimal_format(), False,
        Currency.Currency(
            p["total"], format=Currency.CurrencyFormat.NANO).decimal_format(),
    ])

print(
    tabulate(payout_table,
             headers=[
                 "PublicKey", "Staking Balance", "Unlocked & >=0.5?",
                 "Payout mina"
             ],
             tablefmt="pretty"))
f.write(
    tabulate(payout_table,
             headers=[
                 "PublicKey", "Staking Balance", "Unlocked & >=0.5?",
                 "Payout mina"
             ],
             tablefmt="pretty"))
f.write("\n```")
f.close()

# generate payments commands to be executed elsewhere;
for cmd in payout_commands:
    g.write(cmd+"\n")
    g.write("sleep 1s \n")
    curNonce = cmd.split('-nonce')[1]
    g.write(f"echo current payment with nonce{curNonce} done.\n")
g.close()

