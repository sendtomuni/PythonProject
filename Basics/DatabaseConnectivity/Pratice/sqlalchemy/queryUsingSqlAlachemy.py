from sqlalchemy import *
from sqlalchemy.orm import *

from Basics.DatabaseConnectivity.Pratice.sqlalchemy.student import Students


class QueryFrom:
    def __init__(self):
        Engine = create_engine('sqlite:///univ.db',echo=True)
        Session = sessionmaker(bind=Engine)
        self.session = Session()

queryfrom = QueryFrom()

students = queryfrom.session.query(Students).all()

for student in students:
    if isinstance(student, Students):
        print(student)

queryfrom.session.close()