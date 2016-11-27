from flask import Flask, request, render_template, redirect, url_for, flash

DEBUG = True #change in production

app = Flask(__name__)
app.secret_key = "echidna"
        
@app.route('/', methods=["POST", "GET"])
def index():
	if request.method == "POST":
		pass
	else:
		return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1')
