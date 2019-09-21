import requests
import json
import sys

txsign=sys.argv[1]
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

tdata={
  "rawtx":txsign,
  "token":"GtsborCnkMnN1tkUBGorHMZGN2XVwYMT"
}

t=json.dumps(tdata)
print t

r = requests.post(url='https://api.chainrider.io/v1/dash/testnet/tx/send',
                  data=t, params={}, headers = headers)

print r.text
print r.status_code
