from fastapi import FastAPI, HTTPException, Depends, status
from sqlalchemy.orm import Session
from db import get_db, authenticate_user
from models import User, Item
from schema import userCreate, userLogin, userUpdate, Item
from sqlalchemy.exc import SQLAlchemyError
from passlib.context import CryptContext
from datetime import timedelta
from jwt_utils import (
    create_access_token,
    get_current_user,
)
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import Annotated


from jose import jwt, JWTError

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

app = FastAPI(debug=True, docs_url="/")


@app.get("/user/")
def get_all_User(db: Session = Depends(get_db)):
    return db.query(User).all()


ACCESS_TOKEN_EXPIRE_MINUTES = 30


@app.post("/sign_up")
def create_user(user_data: userCreate, db: Session = Depends(get_db)):
    try:
        db_user = User(
            name=user_data.name,
            email=user_data.email,
            number=user_data.number,
            password=pwd_context.hash(user_data.password),
        )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return {"message": "User created successfully"}
    except SQLAlchemyError as e:
        db.rollback()
        error_msg = f"Error creating user: {str(e)}"
        print(error_msg)
        raise HTTPException(status_code=500, detail="Error creating user")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.post("/login")
def login_user(
    form_data: Annotated[OAuth2PasswordRequestForm , Depends()],
) ->userLogin:
    user = authenticate_user(get_db, form_data.name, form_data.password)

    if not user or not pwd_context.verify(form_data.name, user.password):
        raise HTTPException(status_code=401, detail="Incorrect username or password")

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.id}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/user/{user_id}/")
def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        return user
    raise HTTPException(status_code=404, detail="User not found")


@app.put("/user/{user_id}")
def update_user_by_id(
    user_id: int, user_update: userUpdate, db: Session = Depends(get_db)
):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    db_user.name = user_update.name
    db_user.email = user_update.email
    db_user.number = user_update.number
    if user_update.new_password:
        db_user.password = pwd_context.hash(user_update.new_password)
    db.commit()
    db.refresh(db_user)
    return {
        "message": "User updated successfully",
        "User_Details": db_user,
    }


@app.delete("/user/{user_id}")
def delete_user_by_id(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(db_user)
    db.commit()
    return {"message": "User deleted successfully", "User_Details": db_user}


@app.post("/add_items", response_model=Item)
def add_items(
    create_item: Item,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    try:
        db_item_dict = create_item.dict()
        db_item_dict["user_id"] = current_user.id
        db_item = Item(**db_item_dict)
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        return db_item
    except SQLAlchemyError:
        db.rollback()
        raise HTTPException(status_code=500, detail="Error adding item")
