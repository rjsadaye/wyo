import requests
import pprint
import json
import base64

headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
}

r = requests.get('https://api.chainrider.io/v1/dash/testnet/txs',
                  params={'address': "yZZUvP9F6XNUxPsFun6zeH7UQ6RwRD7S6R", 'token': "GtsborCnkMnN1tkUBGorHMZGN2XVwYMT"}, headers = headers)

jj=r.json()
#print r.json()
#u=json.dump(r, ensure_ascii= True, encoding='utf-8')
pp = pprint.PrettyPrinter(indent=1)
#pp.pprint(jj['txs'][0])
code =jj['txs'][0]['vout'][1]['scriptPubKey']['asm']
parts=code.split(" ")
message=parts[1].decode("hex")
message=base64.b64decode(message)
print message
