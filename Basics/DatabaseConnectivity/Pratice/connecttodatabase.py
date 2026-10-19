import sqlite3

conn = sqlite3.connect('learn.db')

cursor = conn.cursor()

cursor.execute("CREATE TABLE department (deptNo INTEGER PRIMARY KEY,name TEXT NOT NULL);")
cursor.execute("CREATE TABLE students (rollNo INTEGER PRIMARY KEY,name TEXT NOT NULL,city TEXT,deptNo INTEGER,FOREIGN KEY (deptNo) REFERENCES department(deptNo));")

conn.commit()

cursor.close()
conn.close()
