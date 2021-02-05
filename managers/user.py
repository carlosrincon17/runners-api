from managers.base import BaseManager
from models.models import User
from models.schemas import UserCreate
from utils.encryption_helper import get_password_hash


class UserManager(BaseManager):

    def create_user(self, user_create: UserCreate):
        new_user = User(
            first_name=user_create.first_name,
            last_name=user_create.last_name,
            is_active=True,
            email=user_create.email,
            hashed_password=get_password_hash(user_create.password)
        )
        self.db.add(new_user)
        self.db.flush()
        self.db.refresh(new_user)
        return new_user

    def get_user(self, **args):
        user = self.db.query(User).filter_by(**args).first()
        return user
