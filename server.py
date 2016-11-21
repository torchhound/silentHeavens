from flask import Flask, request, render_template, redirect, url_for, flash
from flask_wtf import Form 
from wtforms import TextField, TextAreaField, SubmitField, validators, ValidationError, PasswordField
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, UserMixin, login_required
import models

DEBUG = True #change in production

app = Flask(__name__)
app.secret_key = "echidna"
bcrypt = Bcrypt(app)
loginManager = LoginManager()
loginManager.init_app(app)

class loginForm(Form):
	username = TextField("Username",  [validators.Required("Please enter your username.")])
	password = PasswordField('Password', [validators.Required("Please enter a password.")])
	login = SubmitField(label="Login")
	
	def __init__(self, *args, **kwargs):
		Form.__init__(self, *args, **kwargs)

class registerForm(Form):
	username = TextField("Username",  [validators.Required("Please enter your username.")])
	email = TextField("Email", [validators.Required("Please enter your email address."), validators.Email("Please enter your email address.")])
	password = PasswordField('Password', [validators.Required("Please enter a password.")])
	register = SubmitField(label="Register")
 
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
	loginForm = loginForm(csrf_enabled = False) #needs to be changed in production
	registerForm = registerForm(csrf_enabled = False) #needs to be changed in production
	if request.method=='POST': 
		if registerForm.validate() == False:
			return render_template("login.html", registerForm=registerForm, loginForm=loginForm)
		if loginForm.login.data:
			username = loginForm.username.data
			password = bcrypt.generate_password_hash(loginForm.password.data)
			users = models.retrieveUsers()
			if username in users and password in users:
				return render_template('index.html')
			else:
				return render_template("login.html", registerForm=registerForm, loginForm=loginForm)
		elif registerForm.register.data:   
			username = registerForm.username.data
			password = bcrypt.generate_password_hash(registerForm.password.data)
			email = registerForm.email.data
			models.insertUser(username, password, email) #flash a success message
	else:
		return render_template('login.html', registerForm=registerForm, loginForm=loginForm)
        
@app.route('/game', methods=["POST", "GET"])
def index():
	if request.method == "POST":
		pass
	else:
		return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
