from fastapi import Request
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database import Base


class BaseManagerMock:

    def __init__(self, request: Request):
        self.db = TestingSessionLocal()

