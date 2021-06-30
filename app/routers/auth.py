from fastapi import APIRouter, Request

from app.controllers.user import UserController
from app.models.schemas import Token, OAuth2PasswordRequest, RecoveryPasswordRequest, UpdatePasswordRequest

router = APIRouter()


@router.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequest, request: Request):
    user_controller = UserController(request=request)
    return user_controller.authenticate_user(email=form_data.email, password=form_data.password)


@router.post("/recovery-password")
async def login_for_access_token(form_data: RecoveryPasswordRequest, request: Request):
    user_controller = UserController(request=request)
    await user_controller.recovery_password(email=form_data.email)
    return None


@router.get("/recovery-password/{recovery_token}")
async def login_for_access_token(recovery_token: str, request: Request):
    user_controller = UserController(request=request)
    user_controller.validate_recovery_password_token(recovery_token=recovery_token)
    return None


@router.post("/update-password/{recovery_token}")
async def update_password(recovery_token: str, update_password_request: UpdatePasswordRequest, request: Request):
    user_controller = UserController(request=request)
    user_controller.validate_recovery_password_token(recovery_token=recovery_token)
    user_controller.update_password(
        recovery_token=recovery_token,
        update_password_request=update_password_request
    )
    return None

