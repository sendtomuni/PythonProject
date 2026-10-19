from sqlalchemy import *
from sqlalchemy.orm import *

from Basics.DatabaseConnectivity.Pratice.sqlalchemy.department import Department
from Basics.DatabaseConnectivity.Pratice.sqlalchemy.student import Students


class InsertInto:

    def __init__(self):
        self.Engine = create_engine("sqlite:///univ.db", echo=True)


inserInto = InsertInto()
Session = sessionmaker(bind = inserInto.Engine)
session = Session()

d1 = Department(10, "CSE")
d2 = Department(20, "ECE")
d3 = Department(30, "Civil")
d4 = Department(40, "Mech.")

session.add_all([d1, d2, d3, d4])

s1 = Students(1, "Smith", "NY", d1)
s2 = Students(2, "John", "CA", d1)
s3 = Students(3, "Ajay", "DL", d2)
s4 = Students(4, "Smith", "WA", d2)
s5 = Students(5, "Khan", "MUM", d3)
s6 = Students(6, "Alex", "CA", d3)
s7 = Students(7, "kartina", "NY", d3)
s8 = Students(8, "Pavan", "MUM", d3)
s9 = Students(9, "Kiran", "PAR", d1)
s10 = Students(10, "William", "NY", d1)
s11 = Students(11, "Roger", "CA", d4)
s12 = Students(12, "Hannah", "PAR", d2)
s13 = Students(13, "Anthony", "WA", d2)
s14 = Students(14, "Keerthi", "MUM", d4)
s15 = Students(15, "Suman", "DL", d1)

session.add_all([s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15])

session.commit()
session.close()