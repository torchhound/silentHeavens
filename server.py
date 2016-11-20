from flask import Flask, request, render_template, redirect, url_for, flash
#from werkzeug.security import generate_password_hash, check_password_hash
#from flask_wtf import Form 
#from wtforms import TextField, TextAreaField, SubmitField, validators, ValidationError, PasswordField
#from flask.ext.bcrypt import Bcrypt
#import sqlite3
#from flask.ext.mongoalchemy import MongoAlchemy
import models

DEBUG = True

app = Flask(__name__)
app.secret_key = "echidna"
bcrypt = Bcrypt(app)

@app.route('/', methods=['POST', 'GET'])
def login():
    if request.method=='POST': #move to wtforms
    	if request.form['submit'] == 'Login':
    		username = request.form['username']
        	password = request.form['password']
            users = models.retrieveUsers()
            if username in users and password in users:
        		return render_template('index.html')
        	else:
        		pass
        elif request.form['submit'] == 'Register':   
        	username = request.form['username']
        	password = request.form['password']
        	models.insertUser(username, password)
    else:
        return render_template('login.html')
        
@app.route('/game', methods=["POST", "GET"])
def index():
	if request.method == "POST":
		pass
	else:
		return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
