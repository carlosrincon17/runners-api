from sqlalchemy.orm import relationship

from database import Base
from sqlalchemy import Boolean, Column, Integer, String, Date, ForeignKey


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


class Event(Base):

    __tablename__ = 'events'

    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    start_date = Column(Date)
    end_date = Column(Date)
    start_enrollment_date = Column(Date)
    end_enrollment_date = Column(Date)


class Test(Base):

    __tablename__ = 'tests'

    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    name = Column(String(10))
    description = Column(String(255), nullable=True)


class Category(Base):

    __tablename__ = 'categories'

    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    name = Column(String(10))
    description = Column(String(255), nullable=True)


# class EventCategoryTest(Base):
#
#     __tablename__ = 'event_category_test'
#
#     id = Column(Integer, autoincrement=True, primary_key=True, index=True)
#     user_id = Column(Integer, ForeignKey('users.id'))
#     event = relationship("Child", back_populates="event_category_tests")
#     test_id = Column(Integer, ForeignKey('tests.id'))
#     test = relationship("Test", back_populates="event_category_tests")
#     category_id = Column(Integer, ForeignKey('categories.id'))
#     category = relationship("Category", back_populates="event_category_tests")
#
#
# class EventEnrollment(Base):
#
#     __tablename__ = 'event_enrollment'
#
#     id = Column(Integer, autoincrement=True, primary_key=True, index=True)
#     user_id = Column(Integer, ForeignKey('users.id'))
#     event = relationship("Child", back_populates="event_category_tests")
#     test_id = Column(Integer, ForeignKey('tests.id'))
#     test = relationship("Test", back_populates="event_category_tests")
#     category_id = Column(Integer, ForeignKey('categories.id'))
#     category = relationship("Category", back_populates="event_category_tests")
