from pydantic import BaseModel


class UserCreate(BaseModel):
    name: str
    email: str
    number: str
    password: str


class TokenData(BaseModel):
    user_id: int


class UserLogin(BaseModel):
    name: str
    password: str


class UserInDB(BaseModel):
    hashed_password: str


class UserUpdate(BaseModel):
    name: str
    email: str
    number: str
    new_password: str


class Item(BaseModel):
    name: str
    description: str
    color: str


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password


class UserInDB(BaseModel):
    hashed_password: str


class UserInfo(BaseModel):
    name: str
