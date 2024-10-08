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
    is_active = Column(Boolean, default=True)  # tbd what is_actve is used for i.e., deactivated user? or someone who hasnt logged in yet?

    items = relationship("Item", back_populates="owner")

    def __str__(self, cls):
        return f"New table entry in {cls.__tablename__} table with user (id: {self.id}, email: {self.email}, items: {self.items})"
    def is_valid(self):
        return (self.email)


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="items")
