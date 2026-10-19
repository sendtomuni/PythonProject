from sqlalchemy import Column, Integer, String

from Basics.DatabaseConnectivity.Pratice.sqlalchemy import Base

class Department(Base):
    def __init__(self, deptNo, name):
        self.deptNo = deptNo
        self.name = name

    __tablename__ = 'department'

    def __repr__(self):
        return (f'Department {self.name} has id {self.deptNo}')

    deptNo = Column(Integer, primary_key=True)
    name = Column(String(50))


