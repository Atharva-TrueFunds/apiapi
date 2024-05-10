from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class User(Base):
    __tablename__ = "User"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    email = Column(String(50))
    number = Column(String(10))
    password = Column(String(100))
    items = relationship("Data_Item", back_populates="user")


class Data_Item(Base):
    __tablename__ = "Item"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    description = Column(String(50))
    color = Column(String(50))
    user_id = Column(Integer, ForeignKey("User.id"))
    user = relationship("User", back_populates="items")
