from http import HTTPStatus

from fastapi import APIRouter, Request, Depends

from app.controllers.user import UserController
from app.models.schemas import UserResponse, UserCreate, JwtToken
from app.utils.decorators import verify_token

router = APIRouter()


@router.post("/", responses={
    HTTPStatus.CREATED.value: {'model': UserResponse, 'description': 'User created successfully'},
})
async def create_user(user_create: UserCreate, request: Request):
    user_controller = UserController(request=request)
    return await user_controller.create_user(user_create=user_create)


@router.get("/", responses={
    HTTPStatus.OK.value: {'model': UserResponse, 'description': 'User data'},
})
async def get_user(request: Request, jwt_token: JwtToken = Depends(verify_token)):
    user_controller = UserController(request=request)
    return user_controller.get_user(user_id=jwt_token.user_id)
