from flask import Flask, render_template, request, redirect, jsonify, url_for, flash
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, newUrls
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


# Connect to Database and create database session
engine = create_engine('sqlite:///mpasta.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

def makeurl():
    mynames = ['dragons boy', 'man boys', 'ninja drakess']
    words = ['dragon', 'boy', 'man', 'girl', 'ninja',
             'fighter', 'hell', 'drake', 'master', 'nightfal',
             'harder', 'forbedin', 'f', 'g', 'b', 'cc', 'customer',
             'line', 'svg', 'snake', 'python', 'coder', 'developer',
             'htmls', 'websites', 'servers', 'myservers', 'myserversn',
             'takeservers', 'theservers', 'aservers', 'myserversm',
             'killer', 'montroh', 'hypergens', 'kongfu', 'kontio',
             'myrekon', 'mostrs', 'hpyerkz', 'funkyrock', 'lopto',
             'mahmoud', 'ahmed', 'mohamed', 'keygen', 'super',
             'farmer', 'draven', 'lux', 'daruis', 'zed', 'night',
             'helor', 'kofono', 'hello', 'world']
    words1 = ['dragons', 'boys', 'mans', 'girls', 'ninjas',
             'fighters', 'hells', 'drakess', 'masters', 'nightfals',
             'harders', 'forbedins', 'n', 'c', 'd', 'bb', 'customers'
             'lines', 'sbg', 'snakes', 'pythons', 'coders', 'developers'
             'htmls', 'websites', 'servers', 'myservers', 'as',
              'sd', 'qw', 'er', 'hello', 'get', 'git', 'world', 'qwe',
              'big','host', 'hosters', 'hend', 'amira', 'may', 'mary',
              'kings', 'casser', 'ghj' , 'git']
    first = random.choice(words)
    second = random.choice(words1)
    exist = None
    newurl = None
    newurl = first + second
    exist = session.query(newUrls).filter_by(name=newurl).first()
    if newurl == exist:
        print('This Error taken before')
        exist = True
    else:
        exist = False
        
    return newurl
    
    
    

@app.route('/')
@app.route('/editor', methods=['GET'])
def editor():
        return render_template('index.html')


@app.route('/compiler', methods=['GET', 'POST'])
def compiler():

    if request.method == 'POST':
    
        code=request.form.get('codes')
        user_url = makeurl() 
        output = ""
        output += code
        output += '<br /><br /><a href="/">Run another code</a>'
        output += '<br /><br /><p>Your Code Can be fonded here'
        output += ': <a href="http://127.0.0.1:5000/host/' + user_url + '">' + "/host/" + user_url + '</a>'
        fullurl = 'http://127.0.0.1:5000/host/%s' %user_url
        if output:
            newPage = newUrls(name=user_url, code=output, url=fullurl)
            session.add(newPage)        
        flash('Here are Your Link: %s' % newPage.url)
        session.commit()

        
        return output
        
    else:    
        return render_template('index.html')        
 

@app.route('/host/<string:user_url>/', methods=['GET'])
def getpage(user_url):    
    gettemplate = session.query(newUrls).filter_by(name=user_url).first()
    userpage = gettemplate.code
    return userpage





if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000, threaded=False)