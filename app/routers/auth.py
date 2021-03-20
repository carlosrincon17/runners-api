from fastapi import APIRouter, Request

from app.controllers.user import UserController
from app.models.schemas import Token, OAuth2PasswordRequest

router = APIRouter()


@router.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequest, request: Request):
    user_controller = UserController(request=request)
    return user_controller.authenticate_user(email=form_data.email, password=form_data.password)