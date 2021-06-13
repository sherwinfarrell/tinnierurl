from json import encoder
from flask import Flask, render_template, redirect, url_for, request, Response
from time import sleep
import json
from json import dumps, loads
from flask_sqlalchemy import SQLAlchemy
import os
from .db import db
from .shortener import Shortener
from ..app import app


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



