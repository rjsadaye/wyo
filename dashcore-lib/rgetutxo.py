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

session={}
app = FlaskAPI(__name__)

def handle_error_404(error):
    flash('Server says: {0}'.format(error), 'error')
    return render_template('404.html', selected_menu_item=None)


def handle_error_500(error):
    flash('Server says: {0}'.format(error), 'error')
    return render_template('500.html', selected_menu_item=None)


def init_error_handlers(app):
    if app:
        app.errorhandler(404)(handle_error_404)
        app.errorhandler(500)(handle_error_500)




# addr1=sender
# addr2=receiver
# encoded_data=encoded


addr1=sys.argv[1]
addr2=sys.argv[2]
encoded_data=sys.argv[3]

# def driver(sender, receiver, encoded):
#   print "Here"

headers = {
'Content-Type':'application/json',
'Accept':'application/json'
}
pk='cMszCbzTUCzYCanQRHeXY5FC1E6qrYWWezHNLB8HbPA7rDNCRHVN'


r = requests.get('https://api.chainrider.io/v1/dash/testnet/addr/'+addr1+'/utxo',
                  params={'token': 'GtsborCnkMnN1tkUBGorHMZGN2XVwYMT'}, headers = headers)


#print r.json()

jj=r.json()
for i in jj:
    if i['satoshis']>0:
        single=jj[0]
        txid=single['txid']
        outindex=single['vout']
        address=single['address']
        script=single['scriptPubKey']
        satoshis=single['satoshis']
        print single

        
#single=jj[0]

#txid=single['txid']
#outindex=single['vout']
#address=single['address']
#script=single['scriptPubKey']
#satoshis=single['satoshis']
#print single

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
print r.text+'\n'+str(r.status_code)
out=os.popen('python /home/rsadaye/wyo/rtxbyadress.py').read()
print out

  # return json.dumps({'success':True}), 200, {'ContentType':'application/json'}
  # return json.dumps({'success':False}), 400, {'ContentType':'application/json'}

# @app.route('/submitproof',methods=['POST'])
# def submitselloffer():
#   init_error_handlers(app)
#   if request.method=='POST':
#     result = request.data
#     #print result['sender']
#     #result=result.json()
#    # print json.loads(result)
#     #sender=result['sender']
#     #receiver=result['receiver']
#     #proof=result['proof']
#    # print proof
#     #encoded = base64.b64encode(proof)
#     #return json.dumps('200')
#     sender = result['sender']
#     print sender
#     receiver = result['receiver']
#     print receiver
#     encoded = base64.b64encode(result['encoded'])
#     print encoded
#     headers = {
#     'Content-Type':'application/json',
#     'Accept':'application/json'
#     }
#     pk='cQpeiT7b6ht9zyrWJtwQ5X9npZdPpT9uRk2Y5AWSgCxbf41gnkjo'


#     r = requests.get('https://api.chainrider.io/v1/dash/testnet/addr/'+addr1+'/utxo',
#                       params={'token': 'GtsborCnkMnN1tkUBGorHMZGN2XVwYMT'}, headers = headers)

#     if r.status_code == 200:
#     #print r.json()
#       jj=r.json()
#       single=jj[0]

#       txid=single['txid']
#       outindex=single['vout']
#       address=single['address']
#       script=single['scriptPubKey']
#       satoshis=single['satoshis']
#       print single

#       stream=os.popen('node sendcode.js '+ str(addr1)+' '+ str(addr2) + ' '+str(pk)+' '+str(txid)+' '+ str(outindex)+' '+str(address)+' '+str(script) +' '+str(satoshis)+' '+encoded_data).read()
#       print stream

#       outarr=stream.split('Transaction: ')
#       rawtxidarr=outarr[1].split('>')
#       rawtx= rawtxidarr[0]

#       headers = {
#         'Content-Type': 'application/json',
#         'Accept': 'application/json'
#       }

#       tdata={
#         "rawtx":rawtx,
#         "token":"GtsborCnkMnN1tkUBGorHMZGN2XVwYMT"
#       }

#       t=json.dumps(tdata)
#       print t

#       r = requests.post(url='https://api.chainrider.io/v1/dash/testnet/tx/send',
#                         data=t, params={}, headers = headers)

#       if r.status_code == 200:
#       # print r.text
#       # print r.status_code
#       #print r.text+'\n'+str(r.status_code)
#         return json.dumps({'success':True}), 200, {'ContentType':'application/json'}
#     return driver(result['sender'],result['receiver'],base64.b64encode['encoded'])


# if __name__=="__main__":
# 	app.run(debug=True, host='0.0.0.0', port=5500)
