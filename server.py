from flask import Flask, request, render_template, redirect, url_for, flash
from flask_wtf import Form 
from wtforms import TextField, TextAreaField, SubmitField, validators, ValidationError, PasswordField
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, login_required, login_user, logout_user
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
		if registerForm.validate() == False:
			return render_template("login.html", registerForm=registerForm, loginForm=loginForm)
		if loginForm.login.data:
			username = loginForm.username.data
			password = bcrypt.generate_password_hash(loginForm.password.data)
			user = models.User.authUser(username, password)
			if user == True:
				login_user(username) #not sure about that argument
				return render_template("index.html")
			else:
				return render_template("login.html", registerForm=registerForm, loginForm=loginForm)
		elif registerForm.register.data:   
			username = registerForm.username.data
			password = bcrypt.generate_password_hash(registerForm.password.data)
			email = registerForm.email.data
			success = models.User.createUser(username, password, email)
			if success == True:
				return render_template("login.html", registerForm=registerForm, loginForm=loginForm) #flash a success message
			else:
				return render_template("login.html", registerForm=registerForm, loginForm=loginForm) #flash an error
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
