import sqlite3
from flask import Flask
from flask_mongoalchemy import MongoAlchemy

app = Flask(__name__)
app.config['MONGOALCHEMY_DATABASE'] = 'repository'
db = MongoAlchemy(app)

class Player(db.Document):
	username = db.StringField()
	
def addPlayer(username):
	try:
		player = Player(username = username)
		player.save()
	except Exception as e:
		print(e)
		pass #return False?
	
def removePlayer(username):
	try:
		rm = Player.query.filter(Player.username == username).first()
		rm.remove()
	except Exception as e:
		print(e)
		pass #return False?

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
