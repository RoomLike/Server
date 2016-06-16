#!/usr/bin/python

import bottle
import bottle.ext.sqlite
from bottle import response
import sqlite3
from json import dumps

app = bottle.Bottle()

@app.route('/user/:userName/:password')
def user(userName, password):
	conn = sqlite3.connect('/home/tinyiota/development/RoomLike/Server/Server/db/test.db')
	cursor = conn.cursor()
        cursor.execute('SELECT Users.UserID, Users.UserName, Users.Password, UsersGroups.GroupID, Groups.GroupName FROM Users INNER JOIN UsersGroups ON Users.UserID = UsersGroups.UserID INNER JOIN Groups ON UsersGroups.GroupID = Groups.GroupID WHERE UserName = ? AND Password = ?', [userName, password])
	result = ''
	while True:
		row = cursor.fetchone()
		if row == None:
			break
		result = '{"UserID":' + str(row[0]) + ', "UserName":"' + str(row[1]) + '", "Password":"' + str(row[2]) + '", "GroupID":' + str(row[3]) + ', "GroupName":"' + str(row[4]) + '"}'
	cursor.close()
	if len(result) == 0:
		result = 'DNE'
	return result

@app.route('/groups_users/:groupID')
def groups_users(groupID):
	conn = sqlite3.connect('../db/test.db')
	cursor = conn.cursor()
	cursor.execute('SELECT UsersGroups.UserID, Users.UserName FROM UsersGroups INNER JOIN Users ON UsersGroups.UserID = Users.UserID WHERE UsersGroups.GroupID = ?', [groupID])
	result = '{"Users": ['
	while True:
		row = cursor.fetchone()
		if row == None:
			break
		result = result + ' {"UserID": ' + str(row[0]) + ', "UserName": "' + str(row[1]) + '"}'
	cursor.close()
	result = result + "]}"
	return result

@app.route('/objects/:objectType/:groupID')
def get_chores(objectType, groupID):
	conn = sqlite3.connect('../db/test.db')
	cursor = conn.cursor()
	cursor.execute('SELECT Groups.GroupID, Objects.ObjectType, Objects.`Text` FROM GroupsObjects INNER JOIN Groups ON GroupsObjects.GroupID = Groups.GroupID INNER JOIN Objects ON GroupsObjects.ObjectID = Objects.ObjectID WHERE Objects.ObjectType = ? AND GroupsObjects.GroupID = ?', [objectType, groupID])
	result = "{"
	while True:
		row = cursor.fetchone()
		if row == None:
			break
		result = result + '[ObjectType:' + str(row[0]) + ' ' + str(row[1]) + ' ' + str(row[2]) + ']'
	result = result + ']'
	cursor.close()
	return result

@app.route('/add_user/:userID/:userName')
def add_user(userID, userName):
	conn = sqlite3.connect('../db/test.db')
	cursor = conn.cursor()
	cursor.execute('INSERT INTO Users (UserID, UserName) VALUES (?,?)', [userID, userName])
	cursor.close()

@app.route('/add_schedule/:frequency/:objectID/:nextDate/:lastDate/:daysOfWeek/:dayOfMonth/:monthOfYear/:year/:hour/:minute/:isAM/:repeatEvery/:anyDay')
def add_schedule(frequency, objectID, nextDate, lastDate, daysOfWeek, dayOfMonth, monthOfYear, year, hour, minute, isAM, repeatEvery, anyDay):
	conn = sqlite3.connect('../db/test.db')
	cursor = conn.cursor()
	cursor.execute('INSERT INTO Schedules (Frequency, ObjectID, NextDate, LastDate, DaysOfWeek, DayOfMonth, MonthOfYear, Year, Hour, Minute, IsAM, RepeatEvery, AnyDay) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', [frequency, objectID, nextDate, lastDate, daysOfWeek, dayOfMonth, monthOfYear, year, hour, minute, isAM, repeatEvery, anyDay])
	cursor.close()

@app.route('/add_object/:groupID/:makerID/:text/:dibsUser/:completedUser/:scheduleID/:amount')
def add_object(groupID, makerID, text, dibsUser, completedUser, scheduleID, amount):
	conn = sqlite3.connect('../db/test.db')
	cursor = conn.cursor()
	cursor.execute('INSERT INTO Objects (GroupID, MakerID, `Text`, ObjectID, DibsUser, CompletedUser, ScheduleID, TimeCreated, Amount) VALUES (?,?,?,?,?,?,?,?,?)'[groupID, makerID, text, dibsUser, completedUser, scheduleID, date('NOW'), amount])
	cursor.close()

@app.route('/add_user_to_group/:userID/:groupID')
def add_user_to_group(userID, groupID):
	conn = sqlite3.connect('../db/test.db')
	cursor = conn.cursor()
	cursor.execute('INSERT INTO UsersGroups (UserID, GroupID) VALUES (?,?)', [userID, groupID])
	cursor.close()

@app.route('/get_group_list/:groupName')
def get_group_list(groupName):
	conn = sqlite3.connect('../db/test.db')
	cursor = conn.cursor()
	cursor.execute("SELECT * FROM Groups WHERE GroupName LIKE '%" + groupName + "%'")
	result = '{"Groups": ['
	while True:
		row = cursor.fetchone()
		if row == None:
			break
		result = result + ' {"GroupID": ' + str(row[0]) + ', "GroupName": "' + str(row[1]) + '"},'
	cursor.close()
	result = result[0:-1]
	result = result + "]}"
	return result

@app.route('/get_messages/:groupID')
def get_messages(groupID):
	conn = sqlite3.connect('../db/test.db');
	cursor = conn.cursor()
	cursor.execute("SELECT GroupID, MakerID, ObjectID, Text, TimeCreated FROM Objects WHERE GroupID = ? AND ObjectType = 'Message'", [groupID])
	result = '{"Messages":['
	while True:
		row = cursor.fetchone()
		if row == None:
			break;
		result = result + '{"GroupID":' + str(row[0]) + ',"MakerID":' + str(row[1]) + ',"MessageID":' + str(row[2]) + ',"MessageText":"' + str(row[3]) + '","TimeCreated":"' + str(row[4]) + '"},'
	cursor.close()
	result = result[0:-1]
	result = result + ']}'
	return result

@app.route('/insert_message/:groupID/:makerID/:messageText')
def insert_message(groupID, makerID, messageText):
	conn = sqlite3.connect('../db/test.db')
	conn.execute("INSERT INTO Objects (GroupID, MakerID, ObjectType, Text, TimeCreated) VALUES (" + groupID + ", " + makerID + ", 'Message', '" + messageText.replace("|", " ") + "', datetime('now'))")
	conn.commit()

app.run(host = 'localhost', port = 8080, debug = True)
