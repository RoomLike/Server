#!flask/bin/python

from app import db

class User(db.Model):
	userID = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(64), index=True, unique=False)
	
	def __repr__(self):
		return '<User %r>' % (self.username)
