#!/usr/bin/env python3
from flask import Flask, render_template, request, redirect, jsonify, url_for, flash
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker

from flask import session as login_session
import random
import string

# IMPORTS FOR THIS STEP
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response
import requests
app = Flask(__name__)



@app.route('/')
@app.route('/editor', methods=['GET'])
def editor():
        return render_template('index.html')


@app.route('/compiler', methods=['GET', 'POST'])
def compiler():

    if request.method == 'POST':
        code=request.form.get('codes')
        output = ""
        output += code
        output += '<br /><br /><a href="/">Run another code</a>'
                
        return output
        
    else:    
        return render_template('index.html')        
 







if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000, threaded=False)