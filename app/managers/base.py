from fastapi import Request


class BaseManager:

    def __init__(self, request: Request):
        self.db = request.state.db

