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

class loginForm(Form):
	username = TextField("Username",  [validators.Required("Please enter your username.")])
	#email = TextField("Email", [validators.Required("Please enter your email address."), validators.Email("Please enter your email address.")])
	password = PasswordField('Password', [validators.Required("Please enter a password.")])
	register = SubmitField(label="Register")
	login = SubmitField(label="Login")
 
	def __init__(self, *args, **kwargs):
		Form.__init__(self, *args, **kwargs)
 
	def validate(self):
		users = models.retrieveUsers()
		if not Form.validate(self):
			return False
	
		nameCheck = str(self.username)
		if nameCheck in users: #check if username has been used before
			self.username.errors.append("That username is already taken")
			return False
		else:
			return True
			
		emailCheck = self.email.lower() 
		if emailCheck in users: #check if email has been used before
			self.email.errors.append("That email is already taken")
			return False
		else:
			return True	
	
@app.route('/', methods=['POST', 'GET'])
def login():
	form = loginForm(csrf_enabled = False) #might need to be changed in production
    if request.method=='POST': 
    	if form.validate() == False:
			return render_template("login.html", form=form)
    	if form.login.data: #split into two forms? One with email and one without
    		username = form.username.data
        	password = bcrypt.generate_password_hash(form.password.data)
            users = models.retrieveUsers()
            if username in users and password in users:
        		return render_template('index.html')
        	else:
        		return render_template("login.html", form=form)
        elif form.register.data:   
        	username = form.username.data
        	password = bcrypt.generate_password_hash(form.password.data)
        	email = form.email.data
        	models.insertUser(username, password, email)
    else:
        return render_template('login.html', form=form)
        
@app.route('/game', methods=["POST", "GET"])
def index():
	if request.method == "POST":
		pass
	else:
		return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
