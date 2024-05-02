from pydantic import BaseModel


class userCreate(BaseModel):
    name: str
    email: str
    number: str
    password: str


class userLogin(BaseModel):
    name: str
    password: str


class userUpdate(BaseModel):
    name: str
    email: str
    number: str
    new_password: str


class Item(BaseModel):
    name: str
    description: str
