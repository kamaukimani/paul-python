CREATE TABLE IF NOT EXISTS student(
    id SERIAL PRIMARY KEY,
    name TEXT,
    email TEXT,
    dob DATE,
    phone INTEGER,
    marks REAL,
    is_married BOOLEAN,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);
INSERT INTO student (name,email,dob,phone,marks)
VALUES ('kamau','kamau@gmail.com','2002-08-22',0712345678,100)