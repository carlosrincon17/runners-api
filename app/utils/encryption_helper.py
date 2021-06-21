import string
import random

from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(secret: str):
    return pwd_context.hash(secret=secret)


def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)


def get_random_token():
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(10))
