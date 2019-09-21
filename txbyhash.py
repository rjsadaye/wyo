import requests
import json
import pprint
import sys

headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
}

txhash=sys.argv[1]

r = requests.get('https://api.chainrider.io/v1/dash/testnet/tx/'+txhash,
                  params={'token': "GtsborCnkMnN1tkUBGorHMZGN2XVwYMT"}, headers = headers)
jj = r.json()

pp=pprint.PrettyPrinter(indent=2)
pp.pprint(r.json())

code = jj['vout'][1]['scriptPubKey']['asm']
a1=code.split(" ")
enchex=a1[1]
#print enchex
st=enchex.decode("hex")
print st
#print json.loads(r.json())
