from typing import List
from typing import Optional
from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
import os
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    items = relationship("Item", back_populates="owner")


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="items")
"""

class User(Base): #why have this inheritance
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, index=True)
    pwd = Column(String)

    items = relationship("Item", back_populates="owner")


    def __repr__(self):
        return f"User( id={self.id},email={self.email}, pwd={self.pwd}, items = {self.items})"


class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="items")    

    def __repr__(self):
        return f"Item( id={self.id},title={self.title}, description={self.description}, owner = {self.owner_id})"

"""