import requests
import pprint
import json
import base64
import os

headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
}

r = requests.get('https://api.chainrider.io/v1/dash/testnet/txs',
                  params={'address': "yduqcQw8E2hJDwhhLVPZYcrjVy15fYzjXG", 'token': "GtsborCnkMnN1tkUBGorHMZGN2XVwYMT"}, headers = headers)

jj=r.json()
#print r.json()
#u=json.dump(r, ensure_ascii= True, encoding='utf-8')
pp = pprint.PrettyPrinter(indent=1)
#pp.pprint(jj['txs'][0])
code =jj['txs'][0]['vout'][1]['scriptPubKey']['asm']
parts=code.split(" ")
message=parts[1].decode("hex")
message=base64.b64decode(message)
#print message['Owner']
message=json.loads(message)
#print message['Owner']
os.chdir('/home/rsadaye/P2P/futures/Solar/application/')
#response=muterun_js('~/P2P/futures/Solar/application/ebalancesolar.js',str(j+1)+" "+str(idata['kW']))
stream=os.popen('node /home/rsadaye/P2P/futures/Solar/application/ebalancesolar.js '+str(1)+' -'+str(message['Usage'])).read()
print stream
a1=stream.split('Account Info : ')
#print a1[1]
a2=a1[1].split('\n ')
#print a2
owner=a2[0]
a3=a2[1].split('ebalance : ')
balance=a3[1]
os.chdir('/home/rsadaye/P2P/futures/Battery/application/')
stream=os.popen('node /home/rsadaye/P2P/futures/Battery/application/storedenergy.js '+str(1)+' '+str(balance)).read()
print stream

