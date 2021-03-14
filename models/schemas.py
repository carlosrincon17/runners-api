from datetime import datetime

from pydantic import BaseModel, validator
from pydantic.networks import EmailStr
from pydantic.schema import date, Optional


class Token(BaseModel):
    access_token: str
    token_type: str


class OAuth2PasswordRequest(BaseModel):
    email: str
    password: str


class UserBase(BaseModel):
    email: EmailStr
    first_name: str
    last_name: str
    document_number: str
    birth_date: date
    phone_number: str
    country: str
    city: str
    address: str
    gender: Optional[str]

    @validator("birth_date", pre=True)
    def parse_birthday(cls, value):
        return datetime.strptime(value, "%d/%m/%Y").date()


class RegistrationTypeBase(BaseModel):
    id: int
    name: str
    description: str
    limits: str
    amount: float
    status: str


class UserCreate(UserBase):
    password: str


class UserResponse(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True
