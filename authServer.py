from flask import Flask, request, render_template, redirect, url_for, flash
from flask_wtf import Form 
from wtforms import TextField, TextAreaField, SubmitField, validators, ValidationError, PasswordField
from flask_bcrypt import Bcrypt
import sys
import models
import forms

DEBUG = True #change in production

app = Flask(__name__)
app.secret_key = "echidna"
bcrypt = Bcrypt(app)

@app.route('/', methods=['POST', 'GET'])
def login():
	loginForm = forms.loginForm(csrf_enabled = False) #needs to be changed in production
	registerForm = forms.registerForm(csrf_enabled = False) #needs to be changed in production
	if request.method == "POST": 
		if loginForm.login.data:
			print("Login POST", file=sys.stderr)
			username = loginForm.username.data
			password = loginForm.password.data
			user = models.authUser(username, password)
			if user == True:
				print("Successful login of {}".format(username), file=sys.stderr)
				return True
			else:
				print("Failed Login", file=sys.stderr)
				error = "Failed Login"
				return render_template("login.html", registerForm=registerForm, loginForm=loginForm, error=error)
		elif registerForm.validate() == False: #potentially unnecessary
			message = "Failure..."
			return render_template("login.html", registerForm=registerForm, loginForm=loginForm, message=message)
		elif registerForm.register.data:
			print("Registration POST", file=sys.stderr)
			message = ""   
			username = registerForm.username.data
			password = bcrypt.generate_password_hash(registerForm.password.data)
			email = registerForm.email.data
			success = models.insertUser(username, password, email)
			if success == True:
				message = "Success!"
				print("Successful registration of {}".format(username), file=sys.stderr)
				return render_template("login.html", registerForm=registerForm, loginForm=loginForm, message=message) #flash a success message
			else:
				print("Registration Failed", file=sys.stderr)
				message = "Failure..."
				return render_template("login.html", registerForm=registerForm, loginForm=loginForm, message=message) #flash an error
	else:
		return render_template("login.html", registerForm=registerForm, loginForm=loginForm)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')