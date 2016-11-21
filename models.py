import sqlite3
from flask import Flask
from flask_mongoalchemy import MongoAlchemy
from flask_login import UserMixin

app = Flask(__name__)
app.config['MONGOALCHEMY_DATABASE'] = 'repository'
db = MongoAlchemy(app)

class User(UserMixin):

	username = ""
	email = ""
	password = ""

	def __init__(self, username, password, email):
		self.username =  username
		self.password = password
		self.email = email
		
	def createUser(username, password, email):
		insertUser(username, password, email)
		
	def authUser(username, password):
		conn = sqlite3.connect("users.db")
		cur = conn.cursor()
		auth = cur.execute("SELECT {},{} FROM users".format(username, password))
		conn.close()
		if auth > 0:
			return True
		else:
			return False
		
	def is_authenticated(self):
		return True
 
	def is_active(self):
		return True
 
	def is_anonymous(self):
		return False
 
	def get_id(self):
		return getId(username)

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
	
def getId(username):
	try:
		conn = sqlite3.connect("users.db")
		cur = conn.cursor()
		cur.execute("SELECT id FROM users WHERE username == {}".format(username))
		id = cur.fetchall()
		conn.close()
		return id
	except Exception as e:
		print(e)
		return False
