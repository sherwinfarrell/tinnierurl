from flask import Flask, render_template, redirect, url_for, request, Response
from time import sleep
import json
from json import dumps, loads
from flask_sqlalchemy import SQLAlchemy
import os
from app.shortener import Shortener
from app.shortener import ENV
from app.db import db
from app.log import CustomLogger


app = Flask(__name__)

cl_logger  = CustomLogger(__name__)
logger = cl_logger.get_logger()


if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL_DEV')

else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL_PROD')



app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)


@app.route('/', methods=['GET'])
def index():
    logger.info("Index request received")
    return render_template('index.html')


@app.route('/shortenUrl', methods=['POST'])
def shortenUrl():
    url = request.json['url']
    logger.info(f"URL received is {str(url)}")
    return_data = {}
    error = False
    if "http://" not in url and "https://" not in url:
        logger.exception("The link is not a valid link for Flask to Handle. Need to have http or https://")
        return Response(json.dumps({"message": "There was an error: " + "This application only serves https or http prefixed urls" + " Please try again."}), mimetype='application/json', status='400')

    try:
        url = Shortener.shorten(url)
        logger.info("The URl is ", url)
        return_data['url'] = url
    except Exception as e: 
        logger.exception("The following Exception just happened: " + str(e))
        error = e
    if error:
        logger.info("Sending Back Exception report")
        return Response(json.dumps({"message": "There was an error: " + str(error) + " Please try again."}), mimetype='application/json', status='400')
    else:
        logger.info("Sending back shortened Route")
        return Response(json.dumps(return_data), mimetype='application/json', status='200')
    
@app.route('/<code>', methods=['GET'])
def resolveUrl(code):
    logger.info("The code for the url is " + code)
    return_data = {}
    error = False
    try:
        resolved_url = Shortener.resolve(code)
        return_data['url'] = resolved_url
    except Exception as e:
        logger.exception("The following Exception has happened: " +  str(e))
        error = e

    if str(error) == "URL is unknown":
        logger.info("Sending back error html as URL wasn't found")
        return render_template('error.html')
    if error:
        logger.info("Sending back general exception error report")
        return Response(json.dumps({"message": "There was an error: " + str(error) + " Please try again."}), mimetype='application/json', status='400')
    else:
        logger.info("Redirecting to url "+ resolved_url)
        return redirect(resolved_url)


def modify_tables():
    with app.app_context():
        logger.info("Dropping Tables")
        db.drop_all()
        logger.info("Dropped Tables")
        db.create_all()
        logger.info("Finished Modifying Tables")

if __name__ == '__main__':
    app.run('0.0.0.0',port=5000, threaded = True)




