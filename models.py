import sqlite3
from flask import Flask
from flask.ext.mongoalchemy import MongoAlchemy

app = Flask(__name__)
app.config['MONGOALCHEMY_DATABASE'] = 'repository'
db = MongoAlchemy(app)

class Empire(db.Document):
	username = db.StringField()
	
def addEmpire(username):
	try:
		empire = Empire(username = username)
		empire.save()
	except Exception as e:
		print(e)
		pass
	
def removeEmpire(username):
	try:
		rm = Empire.query.filter(Empire.username == username).first()
		rm.remove()
	except Exception as e:
		print(e)
		pass

def insertUser(username, password, email):
	conn = sqlite3.connect("users.db")
	cur = conn.cursor()
	cur.execute("INSERT INTO users (username, password, email) VALUES ({}, {}, {})".format(username, password, email))
	conn.commit()
	conn.close()

def retrieveUsers():
	conn = sqlite3.connect("users.db")
	cur = conn.cursor()
	cur.execute("SELECT username, password, email FROM users")
	users = cur.fetchall()
	conn.close()
	return users
