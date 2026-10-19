from sqlalchemy import *
from Basics.DatabaseConnectivity.Pratice.sqlalchemy import department
from Basics.DatabaseConnectivity.Pratice.sqlalchemy import student


from Basics.DatabaseConnectivity.Pratice.sqlalchemy import Base


class CreateDB:
    def __init__(self):
        engine = create_engine("sqlite:///univ.db", echo=True)
        Base.metadata.create_all(engine)


createDB = CreateDB()