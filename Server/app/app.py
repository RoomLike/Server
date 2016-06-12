#!/usr/bin/python

import bottle
import bottle.ext.sqlite
from bottle import SimpleTemplate
import sqlite3

app = bottle.Bottle()

@app.route('/user/:userID')
def user(userID):
	conn = sqlite3.connect('/home/tinyiota/development/RoomLike/Server/Server/db/test.db')
	cursor = conn.cursor()
        cursor.execute('SELECT * FROM Users WHERE UserID = ?', [userID])
	result = ""
	while True:
		row = cursor.fetchone()
		if row == None:
			break
		result = result + ' ' + str(row[0]) + ' ' + str(row[1])
	return result

@app.route('/groups_users/:groupID')
def groups_users(groupID):
	conn = sqlite3.connect('../db/test.db')
	cursor = conn.cursor()
	cursor.execute('SELECT UsersGroups.UserID, Users.UserName FROM UsersGroups INNER JOIN Users ON UsersGroups.UserID = Users.UserID WHERE UsersGroups.GroupID = ?', [groupID])
	result = ""
	while True:
		row = cursor.fetchone()
		if row == None:
			break
		result = result + ' ' + str(row[0]) + ' ' + str(row[1])
	return result

@app.route('/get_chores/:userID')
def get_chores(userID)
	conn = sqlite3.connect('../db/test.db')
	cursor = conn.cursor()
	#edit this part...
	cursor.execute('SELECT UsersGroups.UserID, Users.UserName FROM UsersGroups INNER JOIN Users ON UsersGroups.UserID = Users.UserID WHERE UsersGroups.GroupID = ?', [groupID])
	result = ""
	while True:
		row = cursor.fetchone()
		if row == None:
			break
	result = result + ' ' + str(row[0]) + ' ' + str(row[1])
	return result


app.run(host = 'localhost', port = 8080, debug = True)
