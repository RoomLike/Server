INSERT INTO Users
(
	UserID, UserName, Password
)
VALUES
(
	1, "Curtis", "1"
),
(
	2, "Sophia", "2"
),
(
	3, "Travis", "3"
),
(
	4, "Karyn", "4"
),
(
	5, "Emily", "5"
),
(
	6, "Nik", "6"
);

INSERT INTO Groups
(
	GroupName
)
VALUES
(
	"Champs"
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
	GroupID, MakerID, `Text`, ObjectType, DibsUser, CompletedUser, TimeCreated, Amount 
)
VALUES
(
	1, 1, "Dishes", "Chore", NULL, NULL, date('now'), NULL
),
(
	1, 2, "Vacuum", "Chore", NULL, NULL, date('now'), NULL
),
(
	1, 3, "Laundry", "Chore", NULL, NULL, date('now'), NULL
),
(
	1, 4, "Toilet Paper", "GroceryItem", NULL, NULL, date('now'), NULL
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

INSERT INTO Objects
(
	GroupID, MakerID, ObjectType, Text, TimeCreated
)
VALUES
(
	1, 1, "Message", "Going to soops", datetime('now')
),
(
	1, 2, "Message", "Get me some cookies", datetime('now')
),
(
	1, 4, "Message", "Get me some lettuce", datetime('now')
);
