import sqlite3

conn = sqlite3.connect("learn.db")

cursor = conn.cursor()

cursor.execute("INSERT INTO department (deptNo, name)"
"VALUES"
    "(10, 'CSE'),"
    "(20, 'ECE'),"
    "(30, 'Civil'),"
    "(40, 'Mech.');")

conn.commit()

cursor.execute("INSERT INTO students (rollNo, name, city, deptNo)"
"VALUES"
    "(1, 'Smith',   'NY',  10),"
    "(2, 'John',    'CA',  10),"
    "(3, 'Ajay',    'DL',  20),"
    "(4, 'Smith',   'WA',  20),"
    "(5, 'Khan',    'MUM', 30),"
    "(6, 'Alex',    'CA',  30),"
    "(7, 'kartina', 'NY',  30),"
    "(8, 'Pavan',   'MUM', 30),"
    "(9, 'Kiran',   'PAR', 10),"
    "(10, 'William','NY',  10),"
    "(11, 'Roger',  'CA',  40),"
    "(12, 'Hannah', 'PAR', 20),"
    "(13, 'Anthony','WA',  20),"
    "(14, 'Keerthi','MUM', 40),"
    "(15, 'Suman',  'DL',  10);")

conn.commit()

cursor.close()

conn.close()