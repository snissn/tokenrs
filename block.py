import web3
import sys
import json
import urllib.request
from pprint import pprint
from web3.contract import ConciseContract
import sys
import time
from web3 import Web3
from web3 import Web3, HTTPProvider
import eth_utils

import sql

#infura_provider = HTTPProvider( "https://mainnet.infura.io/utWe5Gr6VnHZBD9iN2D4")
infura_provider = HTTPProvider( "http://10.142.0.6:8545")
w3 = Web3( infura_provider)


def convert_hex_to_int(hexnum):
  if hexnum.startswith("0x"):
    hexnum = hexnum[2:]
  return int(hexnum,16)
def process_transfer(data,log):
  data['value'] = int(log['data'],16)
  try:
      data['from'] = hex(int(log['topics'][1].hex(),16))
  except Exception:
      pass
  try:
      data['to'] = hex(int(log['topics'][2].hex(),16))
  except Exception:
      pass


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
  data['transactionHash'] = log['transactionHash'].hex()
  event_name = contract.events._event_names[log_index]
  data['event_name'] =event_name

  if event_name == 'Transfer':
    process_transfer(data,log)
  return data



       

block = w3.eth.getBlock(6779919)
if block:
    for tx in block['transactions']:
      tx2 = dict(w3.eth.getTransaction(tx))
      #we need to include data from tx2 as well - which has nonce and value sent
      tx = dict(w3.eth.getTransactionReceipt(tx))
      fields = ['blockNumber', 'cumulativeGasUsed','gasUsed','from','to','transactionHash','transactionIndex']
      tx_data = {field:tx[field] for field in fields}
      tx_data['transactionHash'] = tx_data['transactionHash'].hex()
      log = None
      for log in tx['logs']:
          log = process_log(log)
      pprint([tx_data,log,'log'])
print(len(block['transactions']))
