from flask import Flask, render_template
app = Flask(__name__)

import functools
import json
import os

import flask

from authlib.client import OAuth2Session
import google.oauth2.credentials
import googleapiclient.discovery

import google_auth


app = flask.Flask(__name__)
app.secret_key = "secret"

app.register_blueprint(google_auth.app)

@app.route('/')
def index():
    if google_auth.is_logged_in():
        return render_template("provider.html")
    return render_template("login.html")

def getEmail():
    user_info = google_auth.get_user_info()
    return user_info['email']
    
@app.route('/list')
def list():
    result = []
    return render_template("dashboard.html", table=result)

@app.route('/family')
def family():
    result = []
    return render_template("dashboard.html", table=result)

@app.route('/upload')
def upload():
    return render_template("upload.html")

@app.route('/user/<username>')
def show_dash(username):
    return render_template("dashboard.html", username=username)

