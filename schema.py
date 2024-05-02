from pydantic import BaseModel


class userCreate(BaseModel):
    name: str
    email: str
    number: str
    password: str
    
class TokenData(BaseModel):
    name: str | None = None

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


class UserInDB(BaseModel):
    hashed_password: str