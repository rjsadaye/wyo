import requests
import sys
import json
import os
import base64

from flask import request, url_for,redirect
from flask_api import FlaskAPI, exceptions, status
from flask import jsonify,json
from flask import Response

from gevent.pywsgi import WSGIServer

session={}
app = FlaskAPI(__name__)

#def init_error_handlers(app):
#    if app:
#        @app.errorhandler(404)
#        def handle_error_404(error):
#            flash('Server says: {0}'.format(error), 'error')
#            return render_template('404.html', selected_menu_item=None)
#
#        @app.errorhandler(500)
#        def handle_error_500(error):
#            flash('Server says: {0}'.format(error), 'error')
#            return render_template('500.html', selected_menu_item=None)
#init_error_handlers(app)


@app.route('/submitproof',methods=['POST'])
def submitselloffer():
    if request.method=='POST':
        result = request.data
        stream=os.popen('python getutxo.py '+result['sender']+' '+result['reciever']+' '+result['proof']).read()
        print stream
        return json.dumps(200)
    else:
        return json.dumps(500)


@app.route('/submitusage',methods=['POST'])
def submitoffer():
    if request.method=='POST':
        result = request.data
        stream=os.popen('python rgetutxo.py '+result['sender']+' '+result['reciever']+' '+result['proof']).read()
        print stream
        return json.dumps(200)
    else:
        return json.dumps(500)


if __name__=="__main__":
	app.run(debug=True, host='0.0.0.0', port=5500)
