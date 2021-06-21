from sqlalchemy.orm import relationship

from sqlalchemy import Boolean, Column, Integer, String, Date, DECIMAL, Text, ForeignKey, DateTime

from app.database import Base


class User(Base):

    __tablename__ = "users"

    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    is_admin = Column(Boolean, default=False)
    first_name = Column(String)
    last_name = Column(String)
    document_number = Column(String(10))
    birth_date = Column(Date)
    phone_number = Column(String(20))
    city = Column(String(50))
    state = Column(String(50))
    gender = Column(String(1))
    address = Column(String(255))
    shirt_size = Column(String(2))
    token_recovery = Column(String(20))
    last_recovery_date = Column(DateTime)
    event_registrations = relationship("EventRegistration", back_populates="user")


class Event(Base):

    __tablename__ = 'events'

    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    distance = Column(String(55))
    event_set = Column(Integer)
    start_date = Column(Date)
    end_date = Column(Date)
    start_enrollment_date = Column(Date)
    end_enrollment_date = Column(Date)
    description = Column(Text)
    event_registrations = relationship("EventRegistration", back_populates="event")


class RegistrationType(Base):

    __tablename__ = 'registration_types'

    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    name = Column(String(55))
    description = Column(Text)
    limits = Column(Text)
    amount = Column(DECIMAL(precision=10, scale=0))
    status = Column(String)
    color = Column(String)
    event_registrations = relationship("EventRegistration", back_populates="registration_type")


class EventRegistration(Base):

    __tablename__ = 'event_registrations'

    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User")
    status = Column(String(50))
    enrollment_date = Column(Date)
    payment_date = Column(DateTime)
    payment_evidence = Column(String)
    registration_type_id = Column(Integer, ForeignKey('registration_types.id'))
    registration_type = relationship("RegistrationType")
    event_id = Column(Integer, ForeignKey('events.id'))
    event = relationship("Event")
