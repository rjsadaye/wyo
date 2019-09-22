#!/usr/bin/env python

from flask import Flask, render_template, redirect, url_for, request
import requests
import json
import unicodedata
import base64
import os
#from merkle import merkleTree
#from alicia import alicia_encrypt
app = Flask(__name__)
app.config['SECRET_KEY'] = '3141592653589793238462643383279502884197169399'

headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
}

@app.route('/doctor')
def search():
    info = requests.get('http://localhost:5000/doctor/mvishnoi')
    info = info.json()
    return render_template('show.html', info=info)

@app.route('/')
def student():
  return render_template('index.html')

@app.route('/result', methods=['POST', 'GET'])
def result():
  if request.method == 'POST':
       result = request.form
       print(result)
       endpoint = 'http://23.99.231.16:3000/api/org.acme.nucypher.Patient'
       data = {
           "$class": "org.acme.nucypher.Patient",
           "pid": result['email'],
           "Name": result['name'],
           "gender": result['gender'],
           "claim_data": result['message']
           }
       r = requests.post(url = endpoint, data = data)
       print(r)
       return redirect(url_for('merkle', pid=result['email']))

@app.route('/merkle')
def merkle():
    stream=os.popen('python /home/rsadaye/wyo/txbyaddress.py').read()
    proof=json.loads(stream)
    # pid = request.args['pid']
    # info = requests.get('http://10.218.106.52:3000/api/org.acme.nucypher.Patient/'+pid)
    # info = info.json()
    # data={}
    # for topics in info:
    #     if topics=='$class':
    #         continue
    #     else:
    #         data[topics] = info[topics]
    # mt = merkleTree()
    # merkle_data = mt.merkle_tree(data)
    # with open("../rest_python/nucypher/Merkle_json.json", "w") as write_file:
    #                     json.dump(merkle_data, write_file)
    # mt.post_data(merkle_data[1]["Merkle_root"],pid)
    return render_template('showMerkle.html', owner=proof['Owner'], balance=proof['Balance'])

@app.route('/share')
def share():
  return render_template('fields.html')

@app.route('/doctorview', methods=['POST', 'GET'])
def alicia():    
  if request.method == 'POST':
       result = request.form
       payload={
           'Owner': result['name'],
           'Usage': result['amount']
       }

       payload=json.dumps(payload)
       proof=base64.b64encode(payload)
       data={
           'sender': 'yduqcQw8E2hJDwhhLVPZYcrjVy15fYzjXG',
           'reciever': result['public_key'],
           'proof': proof 
       }
       data=json.dumps(data)

       r=requests.post(url='http://52.168.129.85:5500/submitusage', data = data, headers=headers )
       return render_template('help.html')
    #    for_alicia=[]
    #    for values in result:
    #        if(values!='pid'):
    #            for_alicia.append(values)
    #    print for_alicia
    #    return render_template('help.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5600)
