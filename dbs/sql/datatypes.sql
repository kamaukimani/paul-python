-- FIRST COLUMN -> unique
--sql SQL SYNTAX variable in smal
CREATE TABLE IF NOT EXISTS student(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT,
    dob TEXT,
    phone INTEGER,
    marks REAL
);

INSERT INTO student (name,email,dob,phone,marks)
VALUES ('paul','paul@gmail.com','22-08-2002','0712345678',98);
SELECT* FROM student