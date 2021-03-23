from datetime import datetime

from pydantic import BaseModel, validator
from pydantic.networks import EmailStr
from pydantic.schema import date, Optional, List


class Token(BaseModel):
    access_token: str
    token_type: str
    is_admin: bool


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
    state: str
    city: str
    address: str
    gender: Optional[str]
    shirt_size: Optional[str]

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
    color: str


class UserCreate(UserBase):
    password: str
    distance: str
    registration_type_id: int
    distance: str


class JwtToken(BaseModel):
    user_id: int
    email: EmailStr
    exp: Optional[int]


class UserResponse(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True


class EventRegistrationSummary(BaseModel):
    status: str
    total: int


class EventRegistrationFilter(BaseModel):
    status: str


class EventRegistrationRow(BaseModel):
    event_registration_id: Optional[int]
    first_name: str
    last_name: str
    document_number: str
    gender: Optional[str]
    shirt_size: Optional[str]
    user_id: int
    registration_type_id: int
    registration_type_amount: float
    distance: Optional[str]


class EventRegistrationData(BaseModel):
    id: Optional[int]
    status: str
    distance: str
    amount: float
    registration_type_id: int
    payment_file: Optional[str]


class EmailSchema(BaseModel):
    email: List[EmailStr]
