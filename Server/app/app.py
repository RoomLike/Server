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
	cursor.close()
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
	cursor.close()
	return result

@app.route('/:objectType/:groupID')
def get_chores(objectType, groupID):
	conn = sqlite3.connect('../db/test.db')
	cursor = conn.cursor()
	cursor.execute('SELECT Groups.GroupID, Objects.ObjectType, Objects.`Text` FROM GroupsObjects INNER JOIN Groups ON GroupsObjects.GroupID = Groups.GroupID INNER JOIN Objects ON GroupsObjects.ObjectID = Objects.ObjectID WHERE Objects.ObjectType = ? AND GroupsObjects.GroupID = ?', [objectType, groupID])
	result = ""
	while True:
		row = cursor.fetchone()
		if row == None:
			break
		result = result + ' ' + str(row[0]) + ' ' + str(row[1]) + ' ' + str(row[2])
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

@app.route('/get_group_list/:groupID/:groupName')
def get_group_list(groupID, groupName):
	conn = sqlite3.connect('../db/test.db')
	cursor = conn.cursor()
	if groupID = None:
		cursor.execute('SELECT * FROM Groups WHERE GroupName LIKE "%?%"', [groupName])
	else if groupName = None:
		cursor.execute('SELECT * FROM Groups WHERE GroupID LIKE "%?%"', [groupID])
	else:
		cursor.execute('SELECT * FROM Groups WHERE GroupID LIKE "%?%" AND GroupName LIKE "%?%"', [groupID, groupName])
	result = ""
        while True:
                row = cursor.fetchone()
                if row == None:
                        break
                result = result + ' ' + str(row[0]) + ' ' + str(row[1])
        cursor.close()
        return result

app.run(host = 'localhost', port = 8080, debug = True)
