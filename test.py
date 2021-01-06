import web3
import json
import urllib.request
from pprint import pprint
from web3.contract import ConciseContract
import sys
import time
from web3 import Web3
from web3 import Web3, HTTPProvider
import eth_utils

infura_provider = HTTPProvider( "https://chain.txt.rs")
w3 = Web3( infura_provider)


def convert_hex_to_int(hexnum):
  if hexnum.startswith("0x"):
    hexnum = hexnum[2:]
  return int(hexnum,16)
def process_transfer(data,log):
  data['value'] = int(log['data'],16)
  data['from'] = hex(int(log['topics'][1].hex(),16))
  data['to'] = hex(int(log['topics'][2].hex(),16))


def process_log(log):
  data = {}
  contract_address = log['address']
  log_index = convert_hex_to_int(log['transactionLogIndex'])

  abi_url = 'https://api.etherscan.io/api?module=contract&action=getabi&address={contract_address}&apikey=nokey'.format(contract_address=contract_address)
  fp = urllib.request.urlopen(abi_url)
  mybytes = fp.read()

  mystr = mybytes.decode("utf8")
  abi = json.loads(mystr).get('result',{})
  if abi == 'Contract source code not verified':
    contract = w3.eth.contract( contract_address)
  else:
    contract = w3.eth.contract( contract_address, abi=abi)
  data['contract_address'] = contract_address
  data['tx_id'] = log['transactionHash']
  event_name = contract.events._event_names[log_index]
  data['event_name'] =event_name

  if event_name == 'Transfer':
    process_transfer(data,log)



  tx = w3.eth.getTransactionReceipt(data['tx_id'])
  pprint(dict(tx))
  #//ok so what can we get from each transaction 
# we want to get the caller of the tx
#gas usage
#gas price
#gas cost in eth
#i think that's it i'm tired

  return data



for log in w3.eth.getLogs():
  pprint(log)
  data = process_log(log)
  pprint(data)
  break
