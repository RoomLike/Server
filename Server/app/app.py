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

@app.route('/objects/:objectType/:groupID')
def get_chores(objectType, groupID):
	conn = sqlite3.connect('../db/test.db')
	cursor = conn.cursor()
	cursor.execute('SELECT Objects.GroupID, Objects.MakerID, Objects.ObjectType, Objects.`Text`, Objects.ObjectID, Objects.DibsUser, Objects.CompletedUser, Objects.TimeCreated, Objects.Amount FROM Objects WHERE Objects.ObjectType = ? AND Objects.GroupID = ?', [objectType, groupID])
	result = '{"' + objectType + '":['
	while True:
		row = cursor.fetchone()
		if row == None:
			break
		result = result + '{"GroupID":' + str(row[0]) + '", "MakerID":' + str(row[1]) + ', "ObjectType":"' + str(row[2]) + '", "Text":"' + str(row[3]) + '" "ObjectID":' + str(row[4]) + ', "DibsUser":' + str(row[5]) + ', "CompletedUser":' + str(row[6]) + ', "TimeCreated":"' + str(row[7]) + '", "Amount":' + str(row[8]) + '},'
	result = result[0:-1]
	result = result + ']}'
	cursor.close()
	return result

@app.route('/get_all/:groupID')
def get_all(groupID):
	conn = sqlite3.connect('../db/test.db')
	cursor = conn.cursor()
	cursor.execute("SELECT Objects.GroupID, Objects.MakerID, Objects.ObjectType, Objects.`Text`, Objects.ObjectID, Objects.DibsUser, Objects.CompletedUser, Objects.TimeCreated, Objects.Amount FROM Objects WHERE GroupID = ?", [groupID])
	result = '{"Objects":['
	while True:
		row = cursor.fetchone()
		if row == None:
			break
		result = result + '{"GroupID":' + str(row[0]) + '", "MakerID":' + str(row[1]) + ', "ObjectType":"' + str(row[2]) + '", "Text":"' + str(row[3]) + '", "ObjectID":' + str(row[4]) + ', "DibsUser":' + str(row[5]) + ', "CompletedUser":' + str(row[6]) + ', "TimeCreated":"' + str(row[7]) + '", "Amount":' + str(row[8]) + '},'
	result = result[0:-1]
	result = result + '],'
	cursor.execute("SELECT UsersGroups.UserID, Users.UserName, UsersGroups.GroupID, Groups.GroupName FROM UsersGroups INNER JOIN Users ON UsersGroups.UserID = Users.UserID INNER JOIN Groups ON UsersGroups.GroupID = Groups.GroupID WHERE UsersGroups.GroupID = " + groupID)
	result = result + '"Users":['
	while True:
		row = cursor.fetchone()
		if row == None:
			break
		result = result + '{"UserID":' + str(row[0]) + ', "UserName":"' + str(row[1]) + '", "GroupID":' + str(row[2]) + ', "GroupName":"' + str(row[3]) + '"},'
	result = result[0:-1]
	result = result + ']}'
	cursor.close()
	return result

@app.route('/add_user/:userID/:userName')
def add_user(userID, userName):
	conn = sqlite3.connect('../db/test.db')
	cursor = conn.cursor()
	cursor.execute('INSERT INTO Users (UserID, UserName) VALUES (?,?)', [userID, userName])
	cursor.close()

@app.route('/add_schedule/:objectID/:frequency/:nextDate/:lastDate/:daysOfWeek/:dayOfMonth/:monthOfYear/:year/:hour/:minute/:isAM/:repeatEvery/:anyDay')
def add_schedule(objectID, frequency, nextDate, lastDate, daysOfWeek, dayOfMonth, monthOfYear, year, hour, minute, isAM, repeatEvery, anyDay):
	conn = sqlite3.connect('../db/test.db')
	cursor = conn.cursor()
	cursor.execute('INSERT INTO Schedules (Frequency, NextDate, LastDate, DaysOfWeek, DayOfMonth, MonthOfYear, Year, Hour, Minute, IsAM, RepeatEvery, AnyDay) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', [frequency, nextDate, lastDate, daysOfWeek, dayOfMonth, monthOfYear, year, hour, minute, isAM, repeatEvery, anyDay])
	lastID = cursor.lastrowid
	cursor.execute('INSERT INTO ObjectsSchedules (ObjectID, ScheduleID) VALUES (?,?)', [objectID, lastID])
	cursor.close()
	return lastID

@app.route('/add_chore/:groupID/:makerID/:assignedToID/:text')
def add_chore(groupID, makerID, assignedToID, text):
	conn = sqlite3.connect('../db/test.db')
	cursor = conn.cursor()
	cursor.execute('INSERT INTO Objects (GroupID, MakerID, DibsUser, Text, TimeCreated) VALUES (?,?,?,?,?)'[groupID, makerID, assignedToID, text.replace("|", " "), datetime('now')])
	lastID = cursor.lastrowid
	cursor.close()
	return lastID

@app.route('/call_dibs/:objectID/:userID')
def call_dibs(objectID, userID):
	conn = sqlite3.connect('../db/test.db')
	cursor = conn.cursor()
	cursor.execute("UPDATE Objects SET DibsUser = " + userID + " WHERE ObjectID = " + objectID)
	cursor.close()

@app.route('/mark_complete/:objectID/:userID')
def mark_complete(objectID, userID):
        conn = sqlite3.connect('../db/test.db')
        cursor = conn.cursor()
        cursor.execute("UPDATE Objects SET CompletedUser = " + userID + " WHERE ObjectID = " + objectID)
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
                result = result + '{"UserID": ' + str(row[0]) + ', "UserName": "' + str(row[1]) + '"},'
        cursor.close()
	result = result[0:-1]
        result = result + "]}"
        return result

@app.route('/insert_group/:userID/:groupName')
def insert_group(groupName):
	conn = sqlite3.connect('../db/test.db')
	cursor = connection.cursor()
	cursor.execute("INSERT INTO Groups (GroupName) VALUES ('" + groupName.replace("|", " ") + "')")
	lastID = cursor.lastrowid
	cursor.execute("INSERT INTO UsersGroups (UserID, GroupID) VALUES (" + userID + ", " + lastID + ")")
	return lastID

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

@app.route('/get_help')
def get_help():
	conn = sqlite3.connect('../db/test.db')
	cursor = conn.cursor()
	cursor.execute("")
	result = '{"Help":['
	while True:
		row = cursor.fetchone()
		if row == None:
			break;
		result = result + '{"Header":"' + row[0] + '", "Detail":"' + row[1] + '"},'
	cursor.close()
	result = result[0:-1]
	result = result + ']}'
	return result

app.run(host = 'localhost', port = 8080, debug = True)
