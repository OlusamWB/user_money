from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    bvn: str
    phone: str


class UserDb(UserBase):
    id: str
    password: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: str
