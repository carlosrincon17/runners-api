from models.schemas import UserCreate
from fastapi import Request


class BaseController:

    def __init__(self, request: Request):
        self.request = request

