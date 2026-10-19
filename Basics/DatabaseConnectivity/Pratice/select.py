import sqlite3


conn = sqlite3.connect("learn.db")

cursor = conn.cursor()

rows = cursor.execute("SELECT * FROM department")

ro1 = rows.fetchone()

print(ro1)
print('*' * 10)
rows_2 = cursor.execute("SELECT * FROM department")
ro2 = rows_2.fetchall()

for ro in ro2:
    print(ro)
print('*' * 10)

rows_cityOnly = cursor.execute("SELECT distinct(city) FROM students")
ro_cityOnly = rows_cityOnly.fetchall()
for ro in ro_cityOnly:
    print(ro[0])
print('*' * 10)


rows_cse = cursor.execute("SELECT * FROM students WHERE deptNo in (SELECT deptNo from department WHERE name = 'CSE')")
ro_cse = rows_cse.fetchall()
for ro in ro_cse:
    print(ro)
print('*' * 10)


rows_mum_civil = cursor.execute("SELECT * FROM students WHERE deptNo in (SELECT deptNo from department WHERE name = 'Civil') AND city = 'MUM'")
ro_mum_civil = rows_mum_civil.fetchall()
for ro in ro_mum_civil:
    print(ro)
print('*' * 10)


rows_ece = cursor.execute("SELECT city, count(*) FROM students WHERE deptNo in (SELECT deptNo from department WHERE name = 'ECE') group by city")
ro_ece = rows_ece.fetchall()
for ro in ro_ece:
    print(ro)
print('*' * 10)


rows_ece2 = cursor.execute("SELECT d.name, count(*) FROM students s,department d "
                           "WHERE d.deptNo = s.deptNo "
                           "GROUP BY d.name "
                           "HAVING count(*) > ("
                           "SELECT count(*) FROM students WHERE deptNo in (SELECT deptNo from department WHERE name = 'ECE'))")
ro_ece2 = rows_ece2.fetchall()
for ro in ro_ece2:
    print(ro)
print('*' * 10)

cursor.close()
conn.close()