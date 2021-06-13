from flask import Flask, render_template, redirect, url_for, request, Response
from time import sleep
import json
from json import dumps, loads
from flask_sqlalchemy import SQLAlchemy
import os
from src.db import db


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


def modify_tables():
    with app.app_context():
        db.drop_all()
        db.create_all()

if __name__ == '__main__':
    app.run('0.0.0.0',port=5000, threaded = True)
