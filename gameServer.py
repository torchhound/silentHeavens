from flask import Flask, request, render_template, redirect, url_for, flash
import authServer

DEBUG = True #change in production

app = Flask(__name__)
app.secret_key = "echidna"
        
@app.route('/', methods=["POST", "GET"])
def index():
	while True: #login == False?
		with login.app_context():
			login = login()
		if login == True:
			if request.method == "POST":
				pass
			else:
				return render_template("index.html")
		else:
			pass

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1')
