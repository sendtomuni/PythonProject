from sqlalchemy import *
from sqlalchemy.orm import *

from Basics.DatabaseConnectivity.Pratice.sqlalchemy.department import Department
from Basics.DatabaseConnectivity.Pratice.sqlalchemy.student import Students


class Join:
    def __init__(self):
        Engine = create_engine('sqlite:///univ.db', echo=True)
        Session = sessionmaker(bind=Engine)
        self.session = Session()

j = Join()
results = j.session.query(Students, Department).join(Department, Students.deptNo == Department.deptNo).all()

for r in results:
    if isinstance(r[0], Students) and isinstance(r[1], Department):
        print(f'Student name: {r[0].name} Having rollNumber: {r[0].rollNo} residing in {r[0].city} belongs to {r[1].name} department')
    else:
        print(r)