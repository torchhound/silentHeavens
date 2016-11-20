import sqlite3
#from flask.ext.mongoalchemy import MongoAlchemy

def insertUser(username, password):
	conn = sqlite3.connect("users.db")
	cur = conn.cursor()
	cur.execute("INSERT INTO users (username, password) VALUES ({}, {})".format(username, password))
	conn.commit()
	conn.close()

def retrieveUsers():
	conn = sqlite3.connect("users.db")
	cur = conn.cursor()
	cur.execute("SELECT username, password FROM users")
	users = cur.fetchall()
	conn.close()
	return users
