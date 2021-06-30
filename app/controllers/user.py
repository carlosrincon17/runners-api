import json
from datetime import datetime, timedelta
from http import HTTPStatus

import i18n
from fastapi import HTTPException

from app.controllers.base import BaseController
from app.managers.event import EventManager
from app.managers.event_registration import EventRegistrationManager
from app.managers.user import UserManager
from app.models.models import User
from app.models.schemas import UserCreate, JwtToken, Token, UpdatePasswordRequest
from app.utils.encryption_helper import verify_password, get_random_token
from app.utils.jwt_helper import JWTHelper
from app.utils.mail_helper import MailHelper


class UserController(BaseController):

    async def create_user(self, user_create: UserCreate):
        user_manager = UserManager(self.request)
        db_user = user_manager.get_user(email=user_create.email)
        if db_user:
            raise HTTPException(status_code=HTTPStatus.CONFLICT.value, detail=i18n.t('errors.users.existing_user'))
        new_user = user_manager.create_user(user_create=user_create)
        event_registration_manager = EventRegistrationManager(self.request)
        event_manager = EventManager(self.request)
        selected_event = event_manager.get_event(distance=user_create.distance.upper())
        if not selected_event:
            raise HTTPException(status_code=HTTPStatus.CONFLICT.value, detail=i18n.t('errors.users.invalid_event'))
        event_registration_manager.create_event_registration(
            user_id=new_user.id,
            registration_type_id=user_create.registration_type_id,
            event_id=selected_event.id
        )
        registration_data = {
            'first_name': new_user.first_name,
            'full_name': "{} {}".format(new_user.first_name, new_user.last_name),
            'phone': "{}".format(new_user.phone_number),
            'address': "{}, {}, {}".format(new_user.address, new_user.city, new_user.state),
            'document_number': "{}".format(new_user.document_number)
        }
        await MailHelper().send_welcome_email(registration_data=registration_data, user_email=new_user.email)
        return new_user

    def get_user(self, user_id):
        user_manager = UserManager(self.request)
        return user_manager.get_user(id=user_id)

    def authenticate_user(self, email: str, password: str) -> Token:
        user = self.__get_user_by_email(email=email)
        if not user or not verify_password(plain_password=password, hashed_password=user.hashed_password):
            raise HTTPException(
                status_code=HTTPStatus.UNAUTHORIZED.value,
                detail=i18n.t('errors.users.auth.unauthorized')
            )
        token_data = JwtToken(
            user_id=user.id,
            email=user.email
        )
        return Token(
            access_token=JWTHelper.create_access_token(token_data.dict()),
            token_type="Bearer",
            is_admin=user.is_admin is True
        )

    async def recovery_password(self, email: str):
        user = self.__get_user_by_email(email=email)
        if not user:
            raise HTTPException(
                status_code=HTTPStatus.NOT_FOUND.value,
                detail=i18n.t('errors.users.not_found')
            )
        user_manager = UserManager(self.request)
        recovery_token = get_random_token()
        user_manager.update_recovery_token_data(
            user_id=user.id,
            recovery_token=recovery_token
        )
        recovery_password_data = {
            'first_name': user.first_name,
            'link': f"/recovery-password/{recovery_token}"
        }
        await MailHelper().send_reset_password_email(
            recovery_password_data=recovery_password_data,
            user_email=user.email
        )
        return user

    def validate_recovery_password_token(self, recovery_token: str):
        user_manager = UserManager(self.request)
        user = user_manager.get_user(token_recovery=recovery_token)
        if not user:
            raise HTTPException(
                status_code=HTTPStatus.UNAUTHORIZED.value,
                detail=i18n.t('errors.users.recovery_password.invalid_token')
            )
        final_recovery_date = user.last_recovery_date + timedelta(hours=24)
        if datetime.utcnow() > final_recovery_date:
            raise HTTPException(
                status_code=HTTPStatus.UNAUTHORIZED.value,
                detail=i18n.t('errors.users.recovery_password.token_expired')
            )

    def update_password(self, recovery_token: str, update_password_request: UpdatePasswordRequest):
        user_manager = UserManager(self.request)
        user_manager.update_password(
            token=recovery_token,
            password=update_password_request.password
        )

    def __get_user_by_email(self, email: str) -> User:
        user_manager = UserManager(self.request)
        user = user_manager.get_user(email=email)
        return user

