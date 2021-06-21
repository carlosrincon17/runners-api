from datetime import datetime

from app.managers.base import BaseManager
from app.models.models import User, EventRegistration
from app.models.schemas import UserCreate
from app.utils.encryption_helper import get_password_hash


class UserManager(BaseManager):

    def create_user(self, user_create: UserCreate):
        new_user = User(
            first_name=user_create.first_name,
            last_name=user_create.last_name,
            is_active=True,
            email=user_create.email,
            hashed_password=get_password_hash(user_create.password),
            city=user_create.city,
            state=user_create.state,
            address=user_create.address,
            phone_number=user_create.phone_number,
            document_number=user_create.document_number,
            birth_date=user_create.birth_date,
            shirt_size=user_create.shirt_size,
            gender=user_create.gender
        )
        self.db.add(new_user)
        self.db.flush()
        self.db.refresh(new_user)
        return new_user

    def update_recovery_token_data(self, user_id: int, recovery_token: str):
        user = self.get_user(id=user_id)
        user.token_recovery = recovery_token,
        user.last_recovery_date = datetime.utcnow()
        self.db.flush()

    def update_password_data(self, user_id: int, recovery_token: str):
        user = self.get_user(id=user_id)
        user.token_recovery = recovery_token,
        user.last_recovery_date = datetime.utcnow()
        self.db.flush()

    def get_user(self, **args) -> User:
        user = self.db.query(User).filter_by(**args).first()
        return user

    def get_user_by_event_registration_id(self, event_registration_id):
        user = self.db.query(
            User
        ).filter(
            EventRegistration.id == event_registration_id,
            User.id == EventRegistration.user_id
        ).first()
        return user
