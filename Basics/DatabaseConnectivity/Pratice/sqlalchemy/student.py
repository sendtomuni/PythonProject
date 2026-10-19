from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import *
from Basics.DatabaseConnectivity.Pratice.sqlalchemy import Base
from Basics.DatabaseConnectivity.Pratice.sqlalchemy.department import Department


class Students(Base):
    def __init__(self, rollNo, name, city, department):
        self.rollNo = rollNo
        self.name = name
        self.city = city
        if isinstance(department, Department):
            self.deptNo = department.deptNo

    __tablename__ = 'students'

    def __repr__(self):
        return (f'Student name: {self.name} Having rollNumber: {self.rollNo} residing in {self.city} belongs to {self.deptNo}')

    rollNo: Mapped[int] = mapped_column(Integer, primary_key = True)
    name: Mapped[str] = mapped_column(String(50))
    city: Mapped[str] = mapped_column(String(50))
    deptNo: Mapped[int] = mapped_column(Integer, ForeignKey('department.deptNo'))
