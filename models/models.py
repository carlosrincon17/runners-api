from sqlalchemy.orm import relationship

from database import Base
from sqlalchemy import Boolean, Column, Integer, String, Date, DECIMAL, Text


class User(Base):

    __tablename__ = "users"

    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    first_name = Column(String)
    last_name = Column(String)
    document_number = Column(String(10))
    birth_date = Column(Date)
    phone_number = Column(String(20))
    country = Column(String(50))
    city = Column(String(50))
    gender = Column(String(1))
    address = Column(String(255))
    shirt_size = Column(String(2))


class Event(Base):

    __tablename__ = 'events'

    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    start_date = Column(Date)
    end_date = Column(Date)
    start_enrollment_date = Column(Date)
    end_enrollment_date = Column(Date)
    name = Column(String(255))
    description = Column(Text)
    registration_amount = Column(DECIMAL(precision=10, scale=0))
