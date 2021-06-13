from json import encoder
from flask import Flask, render_template, redirect, url_for, request, Response
from time import sleep
import json
from json import dumps, loads
from flask_sqlalchemy import SQLAlchemy
import os
from extensions import db
from shortener import Shortener



app = Flask(__name__)

ENV = 'prod'

if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL_DEV')

else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://mqfhaztpztsaxy:d8eef4a0ef77cfa2ee5c16904b8c1d4d1617697b19e1732a42a4d6f3a85d65ba@ec2-34-230-115-172.compute-1.amazonaws.com:5432/ddndq6d5bhsjll"


app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/shortenUrl', methods=['POST'])
def shortenUrl():
    url = request.json['url']
    return_data = {}
    error = False
    if "http:" not in url and "https:" not in url:
        return Response(json.dumps({"message": "There was an error: " + "This application only serves https or http prefixed urls" + " Please try again."}), mimetype='application/json', status='400')

    try:
        url = Shortener.shorten(url)
        print("The URl is ", url)
        return_data['url'] = url
    except Exception as e: 
        print("The following Exception just happened: " + str(e))
        error = e
    if error:
        return Response(json.dumps({"message": "There was an error: " + str(error) + " Please try again."}), mimetype='application/json', status='400')
    else:
        return Response(json.dumps(return_data), mimetype='application/json', status='200')
    
@app.route('/<code>', methods=['GET'])
def resolveUrl(code):
    print("The code for the url is " + code)
    return_data = {}
    error = False
    try:
        resolved_url = Shortener.resolve(code)
        return_data['url'] = resolved_url
    except Exception as e:
        print("The following Exception has happened: " +  str(e))
        error = e

    if error:
        return Response(json.dumps({"message": "There was an error: " + str(error) + " Please try again."}), mimetype='application/json', status='400')
    else:
        print("Redirecting to url "+ resolved_url)
        return redirect(resolved_url)

def modify_tables():
    with app.app_context():
        db.drop_all()
        db.create_all()

if __name__ == '__main__':
    app.run('0.0.0.0',port=5000, threaded = True)


