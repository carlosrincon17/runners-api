from fastapi import Request


class BaseManagerMock:

    def __init__(self, request: Request):
        self.db = TestingSessionLocal()

