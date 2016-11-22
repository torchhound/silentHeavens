from flask import Flask, request, render_template, redirect, url_for, flash
from flask_wtf import Form 
from wtforms import TextField, TextAreaField, SubmitField, validators, ValidationError, PasswordField
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, login_required, login_user, logout_user
import sys
import models
import forms

DEBUG = True #change in production

app = Flask(__name__)
app.secret_key = "echidna"
bcrypt = Bcrypt(app)
loginManager = LoginManager()
loginManager.init_app(app)

@loginManager.user_loader
def load_user(username):
	try:
		return models.getId(username)
	except:
		return None	
	
@app.route('/', methods=['POST', 'GET'])
def login():
	loginForm = forms.loginForm(csrf_enabled = False) #needs to be changed in production
	registerForm = forms.registerForm(csrf_enabled = False) #needs to be changed in production
	if request.method == "POST": 
		if loginForm.login.data:
			username = loginForm.username.data
			password = bcrypt.generate_password_hash(loginForm.password.data)
			user = models.User.authUser(username, password)
			if user == True:
				print("Successful login of {}".format(username), file=sys.stderr)
				login_user(username) #not sure about that argument
				return render_template("index.html")
			else:
				error = "Failed Login"
				return render_template("login.html", registerForm=registerForm, loginForm=loginForm, error=error)
		elif registerForm.validate() == False: #potentially unnecessary
			message = "Failure..."
			return render_template("login.html", registerForm=registerForm, loginForm=loginForm, message=message)
		elif registerForm.register.data:
			message = ""   
			username = registerForm.username.data
			password = bcrypt.generate_password_hash(registerForm.password.data)
			email = registerForm.email.data
			success = models.User.createUser(username, password, email)
			if success == True:
				message = "Success!"
				print("Successful registration of {}".format(username), file=sys.stderr)
				return render_template("login.html", registerForm=registerForm, loginForm=loginForm, message=message) #flash a success message
			else:
				message = "Failure..."
				return render_template("login.html", registerForm=registerForm, loginForm=loginForm, message=message) #flash an error
	else:
		return render_template("login.html", registerForm=registerForm, loginForm=loginForm)
        
@app.route('/game', methods=["POST", "GET"])
def index():
	if request.method == "POST":
		pass
	else:
		return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
