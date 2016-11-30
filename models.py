import sqlite3
from flask import Flask
from flask_mongoalchemy import MongoAlchemy
from flask_bcrypt import Bcrypt
import sys

app = Flask(__name__)
app.config['MONGOALCHEMY_DATABASE'] = 'repository'
db = MongoAlchemy(app)
bcrypt = Bcrypt(app)

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
	print("create", file=sys.stderr)
	conn = sqlite3.connect("users.db")
	cur = conn.cursor()
	values = [username, password, email]
	cur.execute("INSERT INTO users (username, password, email) VALUES (?,?,?)", values)
	conn.commit()
	conn.close()

def retrieveUsers():
	conn = sqlite3.connect("users.db")
	cur = conn.cursor()
	cur.execute("SELECT username, password, email FROM users")
	users = cur.fetchall()
	conn.close()
	return users

def authUser(username, password):
	print("auth", file=sys.stderr)
	conn = sqlite3.connect("users.db")
	cur = conn.cursor()
	auth = cur.execute("SELECT * FROM users") #dislike this current solution, will try and move back to values = [username, password]auth = cur.execute("SELECT * FROM users WHERE username=? AND password=?", values)
	rows = cur.fetchall()
	for row in rows:
		user = row[1]
		print("user {}".format(user), file=sys.stderr)
		passw = row[2]
		print("password {}".format(passw), file=sys.stderr)
		if user == username and bcrypt.check_password_hash(passw, password):
			conn.close()
			return True
		else:
			pass
	conn.close()
	return False