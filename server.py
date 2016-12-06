from flask import Flask, request, render_template, redirect, url_for, flash
from flask_bcrypt import Bcrypt
import sys
import models

DEBUG = True #change in production

app = Flask(__name__)
app.secret_key = "echidna"
bcrypt = Bcrypt(app)

@app.route("/", methods=["GET"])
def default():
	return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():
	print("Login POST", file=sys.stderr)
	username = request.form["username"]
	password = request.form["password"]
	user = models.authUser(username, password)
	if user == True:
		print("Successful login of {}".format(username), file=sys.stderr)
		return redirect(url_for("game"))
	else:
		print("Failed Login", file=sys.stderr)
		error = "Failed Login"
		return render_template("login.html")#, error=error)

@app.route("/register", methods=["POST"])
def register():
	print("Registration POST", file=sys.stderr)
	message = ""   
	username = request.form["username"]
	password = bcrypt.generate_password_hash(request.form["password"])
	email = request.form["email"]
	success = models.insertUser(username, password, email)
	if success == True:
		message = "Success!"
		print("Successful registration of {}".format(username), file=sys.stderr)
		return render_template("login.html")#, message=message) #flash a success message
	else:
		print("Registration Failed", file=sys.stderr)
		message = "Failure..."
		return render_template("login.html")#, message=message) #flash an error

@app.route("/game", methods=["GET"]) #check auth token
def game():
	return render_template("index.html")

@app.route("/cli", methods=["POST"])
def cli():
	userInput = request.form["commands"]
	output = ""
	if userInput == "stats":
		output = "Test output"
	return render_template("index.html", output=output)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')