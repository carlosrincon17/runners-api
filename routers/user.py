from http import HTTPStatus

from fastapi import APIRouter, Request

from controllers.user import UserController
from models.schemas import UserResponse, UserCreate

router = APIRouter()


@router.post("/", responses={
    HTTPStatus.CREATED.value: {'model': UserResponse, 'description': 'User created successfully'},
})
async def create_user(user_create: UserCreate, request: Request):
    user_controller = UserController(request=request)
    return user_controller.create_user(user_create=user_create)