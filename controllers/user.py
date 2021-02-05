from http import HTTPStatus

import i18n
from fastapi import HTTPException

from controllers.base import BaseController
from managers.user import UserManager
from models.schemas import UserCreate, Token
from utils.encryption_helper import verify_password
from utils.jwt_helper import JWTHelper


class UserController(BaseController):

    def create_user(self, user_create: UserCreate):
        user_manager = UserManager(self.request)
        db_user = user_manager.get_user(email=user_create.email)
        if db_user:
            raise HTTPException(status_code=HTTPStatus.CONFLICT.value, detail=i18n.t('errors.users.existing_user'))
        return user_manager.create_user(user_create=user_create)

    def authenticate_user(self, email, password) -> Token:
        user_manager = UserManager(self.request)
        user = user_manager.get_user(email=email)
        if not user or not verify_password(plain_password=password, hashed_password=user.hashed_password):
            raise HTTPException(
                status_code=HTTPStatus.UNAUTHORIZED.value,
                detail=i18n.t('errors.users.auth.unauthorized')
            )
        token_data = {
            'user_id': user.id,
            'email': user.email
        }
        return Token(
            access_token=JWTHelper.create_access_token(token_data),
            token_type="Bearer"
        )



