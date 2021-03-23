from http import HTTPStatus

import i18n
from fastapi import HTTPException

from app.controllers.base import BaseController
from app.managers.event import EventManager
from app.managers.event_registration import EventRegistrationManager
from app.managers.user import UserManager
from app.models.schemas import UserCreate, JwtToken, Token
from app.utils.encryption_helper import verify_password
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

    def authenticate_user(self, email, password) -> Token:
        user_manager = UserManager(self.request)
        user = user_manager.get_user(email=email)
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
            is_admin=user.is_admin == True
        )



