from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from passlib.context import CryptContext
from schema import UserInDB, UserInfo


Base = declarative_base()
DATABASE_URL = "postgresql://postgres:atharva@localhost/test_api"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# def get_user(users, name: str):
#     if name in users:
#         user_dict = users[name]
#         return UserInDB(**user_dict)


# def authenticate_user(get_db, name: str, password: str):
#     user = user(get_db, name)
#     if not user:
#         return False
#     if not verify_password(password, user.hashed_password):
#         return False
#     return user


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)
