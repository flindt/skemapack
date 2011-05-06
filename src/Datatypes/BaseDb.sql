BEGIN TRANSACTION;

PRAGMA foreign_keys = ON;

-- metadata table. some blabla mostly for later.
CREATE TABLE metadata (
    id INTEGER PRIMARY KEY, 
    key TEXT, 
    value TEXT
);
INSERT INTO metadata VALUES(1,'Skemapack version',0.1);
INSERT INTO metadata VALUES(2,'Generator','<none>');
INSERT INTO metadata VALUES(3,'Description','Basic db used for initialization');
INSERT INTO metadata VALUES(4,'Basedata origin','BaseDb.sqlite');
INSERT INTO metadata VALUES(5,'Title','No data');

-- table containing all teachers to be used by the system.
CREATE TABLE teachers (
    id INTEGER PRIMARY KEY, 
    initials TEXT, 
    name TEXT
    );
INSERT INTO teachers VALUES(1,'MON','Morten');
INSERT INTO teachers VALUES(2,'PFL','Poul');
COMMIT;

-- table containing class names
CREATE TABLE classes (
    id INTEGER PRIMARY KEY, 
    name TEXT, 
    alias_in_tf TEXT,
    official_denomination TEXT -- The offical name of the class in the schools systems.
    );
INSERT INTO classes VALUES(1, "1. semester network", "1. sem netværk", "asdf1234");
INSERT INTO classes VALUES(2, "2. semester network", "2. sem netværk", "asdf1235");
INSERT INTO classes VALUES(3, "3. semester network", "3. sem netværk", "asdf1236");
INSERT INTO classes VALUES(4, "4. semester network", "4. sem netværk", "asdf1237");

-- table containing semester definitions
CREATE TABLE semesters (
    id INTEGER PRIMARY KEY,
    long_name TEXT,
    Short_name TEXT,
    StartDate date,
    EndDate date                    
    );

-- activity table. 
-- the table with all activities like courses and vacation.
CREATE TABLE activities (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    alias_in_tf TEXT,
    teacher_id INTEGER,
    class_id INTEGER,
    semester_id INTEGER,
    prep_factor REAL,
    FOREIGN KEY(teacher_id) REFERENCES teachers(id)
    FOREIGN KEY(class_id) REFERENCES classes(id)
    --FOREIGN KEY(semester_id) REFERENCES semesters(id)
    );

    