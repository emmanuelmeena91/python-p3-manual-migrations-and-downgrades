import os
import sys
from datetime import datetime
from sqlalchemy import create_engine, desc
from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.ext.declarative import declarative_base

sys.path.append(os.getcwd())

engine = create_engine('sqlite:///migrations_test.db')
Base = declarative_base()



class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer(), primary_key=True)
    name = Column(String(), index=True)
    email = Column(String(55))
    class_grade = Column(Integer())  # Renamed column
    birthday = Column(DateTime())
    enrolled_date = Column(DateTime(), default=datetime.now())

    def __repr__(self):
        return f"Student {self.id}: " \
            + f"{self.name}, " \
            + f"Grade {self.class_grade}"  # Updated reference to renamed column