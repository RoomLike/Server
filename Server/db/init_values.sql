INSERT INTO Users
(
	UserID, UserName
)
VALUES
(
	1, "Curtis"
),
(
	2, "Sophia"
),
(
	3, "Travis"
),
(
	4, "Karyn"
),
(
	5, "Emily"
);

INSERT INTO Groups
(
	GroupID, GroupName
)
VALUES
(
	1, "Champs"
);

INSERT INTO UsersGroups
(
	UserID, GroupID
)
VALUES
(
	1, 1
),
(
	2, 1
),
(
	3, 1
),
(
	4, 1
);

INSERT INTO Objects
(
	GroupID, MakerID, `Text`, ObjectID, DibsUser, CompletedUser, TimeCreated, Amount 
)
VALUES
(
	1, 1, "Dishes", 1, NULL, NULL, date('now'), NULL
),
(
	1, 2, "Vacuum", 2, NULL, NULL, date('now'), NULL
),
(
	1, 3, "Laundry", 3, NULL, NULL, date('now'), NULL
),
(
	1, 4, "Toilet Paper", 4, NULL, NULL, date('now'), NULL
);

INSERT INTO Schedules
(
	ScheduleID, Frequency, NextDate, LastDate, DaysOfWeek, DayOfMonth, MonthOfYear, Year, Hour, Minute, isAM, RepeatEvery, AnyDay
)
VALUES
(
	1, "Once", NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0, 1
),
(
	2, "Daily", NULL, NULL, NULL, NULL, NULL, NULL, 8, 30, 1, 0, 0
),
(
	3, "Weekly", NULL, NULL, "MWF", NULL, NULL, NULL, NULL, NULL, NULL, 0, 0
),
(
	4, "Once", NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0, 1
);

INSERT INTO ObjectsSchedules
(
	ScheduleID, ObjectID
)
VALUES
(
	1, 1
),
(
	2, 2
),
(
	3, 3
),
(
	4, 4
);
