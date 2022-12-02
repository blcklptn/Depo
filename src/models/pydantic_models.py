from db.db import Base
from sqlalchemy import Column, DateTime, String, Integer

from datetime import datetime

class Transport(Base):
    __tablename__ = 'Transport'

    id = Column(Integer, primary_key=True)
    transport_category = Column(String, default=None)
    transport_number = Column(Integer, default=None)

    description = Column(String, default=None)
    status = Column(String, default=None)

    added = Column(DateTime, default=datetime.utcnow)

class Employees(Base):
    __tablename__ = 'Employers'

    id = Column(Integer, primary_key=True)
    firstname = Column(String)
    middlename = Column(String, default=None)
    lastname = Column(String)

    phone_number = Column(String)

    added = Column(DateTime, default=datetime.utcnow)

    
class Schedule(Base):
    __tablename__ = 'Schedule'

    id = Column(Integer, primary_key=True)
    transport_id = Column(Integer)
    before_lunch_1_emp_id = Column(Integer)
    before_lunch_2_emp_id = Column(Integer)

    after_lunch_1_emp_id = Column(Integer)
    after_lunch_2_emp_id = Column(Integer)

    added = Column(DateTime, default=datetime.utcnow)


    


