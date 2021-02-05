from pydantic import BaseModel
from pydantic.networks import EmailStr
from pydantic.schema import date


class Token(BaseModel):
    access_token: str
    token_type: str


class OAuth2PasswordRequest(BaseModel):
    username: str
    password: str


class UserBase(BaseModel):
    email: EmailStr
    first_name: str
    last_name: str
    document_number: str
    birth_date: date
    phone_number: str


class UserCreate(UserBase):
    password: str


class UserResponse(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True
