from flask_wtf import Form 
from wtforms import TextField, TextAreaField, SubmitField, validators, ValidationError, PasswordField

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