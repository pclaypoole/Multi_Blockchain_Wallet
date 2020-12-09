import subprocess
import json
from constants import BTC, ETH, BTCTEST
import os 
from pprint import pprint 
from web3 import Web3, middleware
from web3.gas_strategies.time_based import medium_gas_price_strategy

mnemonic = os.getenv('MNEMONIC', 'letter floor critic cluster step soda helmet odor news mercy wise enhance explain empower speak')

def derive_wallets(coin, mnemonic):
    command = f'php derive -g --mnemonic="{mnemonic}" --cols=path,address,privkey,pubkey --coin="{coin}" --numderive=3 --format=json'

    p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    output, err = p.communicate()
    p_status = p.wait()
    keys = json.loads(output)
    return keys

def priv_key_to_account(coin, priv_key):
    if coin == ETH:
        return Account.privateKeyToAccount(priv_key)
    elif coin == BTCTEST:
        return PrivateKeyTestnet(priv_key)

def create_tx(coin, account, to, amount):
    value = Web3.toWei(amount, "ether")
    gas_estimate = web3.eth.estimateGas({'to': to, 
    'from': account["address"], 
    'value': amount})

    if coin == ETH:
        return {"to": to, 
        "from": account, 
        "value": value, 
        "gas": gas_estimate, 
        "gasPrice":, 
        "nonce": , 
        "chainID": }
    if coin == BTCTEST 
        return PrivateKeyTestnet.prepare_transaction(account.address, [(to, amount, BTC)])

def send_tx(coin, account, to, amount):
    if coin == ETH: 
        return w3.eth.sendRawTransaction(signed.rawTransaction)
    if coin == BTCTEST: 
        return NetworkAPI.broadcast_tx_testnet(signed)

create_tx(ETH, account = coins[ETH][0]["address"], to, 50)
coins = {ETH: derive_wallets(ETH, mnemonic),
        BTCTEST: derive_wallets(BTCTEST, mnemonic),
        }

print(coins[ETH][0]["address"])
#pprint(coins)






