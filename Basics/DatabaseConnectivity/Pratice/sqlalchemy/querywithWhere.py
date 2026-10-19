from sqlalchemy import *
from sqlalchemy.orm import *

from Basics.DatabaseConnectivity.Pratice.sqlalchemy.student import Students


class QueryWithWhere:
    def __init__(self):
        Engine = create_engine('sqlite:///univ.db', echo=True)
        Session = sessionmaker(bind=Engine)
        self.session = Session()

q = QueryWithWhere()

statement = select(Students).where(Students.rollNo == 10)
students = q.session.execute(statement).scalars().all()

for student in students:
    print(students)

print('*' * 30)

students = q.session.query(Students).filter(Students.rollNo.between(10, 14)).all()
for student in students:
    print(student)

q.session.close()
