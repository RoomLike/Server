CREATE TABLE IF NOT EXISTS Users
(
	  UserID INTEGER
	, UserName TEXT
);

CREATE TABLE IF NOT EXISTS Groups
(
	  GroupID INTEGER
	, GroupName TEXT
);

CREATE TABLE IF NOT EXISTS UsersGroups
(
	  UserID INTEGER
	, GroupID INTEGER
	, FOREIGN KEY (UserID) REFERENCES Users (UserID)
	, FOREIGN KEY (GroupID) REFERENCES Groups (GroupID)
);

CREATE TABLE IF NOT EXISTS Objects
(
	  GroupID INTEGER 
	, MakerID INTEGER 
	, `Text` TEXT 
	, ObjectID INTEGER 
	, ObjectType TEXT
	, DibsUser INTEGER 
	, CompletedUser INTEGER 
	, TimeCreated DATE 
	, Amount DOUBLE 
	, FOREIGN KEY (GroupID) REFERENCES Groups(GroupID) 
	, FOREIGN KEY (MakerID) REFERENCES Users(UserID) 
	, FOREIGN KEY (DibsUser) REFERENCES Users(UserID) 
	, FOREIGN KEY (CompletedUser) REFERENCES Users(UserID) 
);

CREATE TABLE IF NOT EXISTS Schedules
(
	  ScheduleID INTEGER 
	, Frequency INTEGER
	, NextDate DATE 
	, LastDate DATE 
	, DaysOfWeek TEXT 
	, DayOfMonth INTEGER 
	, MonthOfYear INTEGER 
	, Year INTEGER 
	, Hour INTEGER 
	, Minute INTEGER 
	, isAM INTEGER 
	, RepeatEvery INTEGER 
	, AnyDay INTEGER 
);

CREATE TABLE IF NOT EXISTS ObjectsSchedules
(
	  ScheduleID INTEGER
	, ObjectID INTEGER
	, FOREIGN KEY (ScheduleID) REFERENCES Schedules (ScheduleID)
	, FOREIGN KEY (ObjectID) REFERENCES Objects (ObjectID)
);

CREATE TABLE IF NOT EXISTS GroupsObjects
(
	  GroupID INTEGER
	, ObjectID INTEGER
	, FOREIGN KEY (GroupID) REFERENCES Groups (GroupID)
	, FOREIGN KEY (ObjectID) REFERENCES `Objects` (ObjectID)
);
