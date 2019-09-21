import requests
import sys
import json
import os
import base64

from flask import request, url_for,redirect
from flask_api import FlaskAPI, exceptions, status
from flask import jsonify,json
from flask import Response
# import Tkinter
# import tkMessageBox
# import pytz
from gevent.pywsgi import WSGIServer

def driver(sender,receiver,encoded):
  headers = {
    'Content-Type':'application/json',
    'Accept':'application/json'
  }

  addr1=sender
  addr2=receiver
  encoded_data=encoded


  # addr1=sys.argv[1]
  # addr2=sys.argv[2]
  # encoded_data=sys.argv[3]

  pk='cQpeiT7b6ht9zyrWJtwQ5X9npZdPpT9uRk2Y5AWSgCxbf41gnkjo'


  r = requests.get('https://api.chainrider.io/v1/dash/testnet/addr/'+addr1+'/utxo',
                    params={'token': 'GtsborCnkMnN1tkUBGorHMZGN2XVwYMT'}, headers = headers)

  #print r.json()
  jj=r.json()
  single=jj[0]

  txid=single['txid']
  outindex=single['vout']
  address=single['address']
  script=single['scriptPubKey']
  satoshis=single['satoshis']
  print single

  stream=os.popen('node sendcode.js '+ str(addr1)+' '+ str(addr2) + ' '+str(pk)+' '+str(txid)+' '+ str(outindex)+' '+str(address)+' '+str(script) +' '+str(satoshis)+' '+encoded_data).read()
  print stream

  outarr=stream.split('Transaction: ')
  rawtxidarr=outarr[1].split('>')
  rawtx= rawtxidarr[0]

  headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json'
  }

  tdata={
    "rawtx":rawtx,
    "token":"GtsborCnkMnN1tkUBGorHMZGN2XVwYMT"
  }

  t=json.dumps(tdata)
  print t

  r = requests.post(url='https://api.chainrider.io/v1/dash/testnet/tx/send',
                    data=t, params={}, headers = headers)

  # print r.text
  # print r.status_code
  return r.text+'\n'+r.status_code

@app.route('/submitproof',methods=['POST'])
def submitselloffer():
  if request.method=='POST':
    result = request.form
    sender=result['sender']
    receiver=result['receiver']
    proof=result['proof']
    encoded = base64.b64encode(proof)


if __name__=="__main__":
	app.run(debug=True, host='0.0.0.0', port=5500)