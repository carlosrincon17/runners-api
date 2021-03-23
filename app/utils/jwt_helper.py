import jwt
from datetime import timedelta, datetime
from typing import Optional

from app.settings import jwt_setting


class JWTHelper:

    @staticmethod
    def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=jwt_setting.access_token_expire_minutes)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, jwt_setting.secret_key, algorithm=jwt_setting.algorithm)
        return encoded_jwt

    @staticmethod
    def decode_token(jwt_token):
        token_data = jwt.decode(jwt_token.split('Bearer ')[1], jwt_setting.secret_key, algorithms=jwt_setting.algorithm)
        return token_data
