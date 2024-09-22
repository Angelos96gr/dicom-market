from pydantic import BaseModel
from enum import Enum


class Modality(Enum):
    CT = "ct"
    ECHO = "echo"
    MR = "mr"
    OTHER = "other"


class Description(BaseModel):

    description: dict = {
        "title": str,
        "modality": Modality,
        "study_date": str,
        "UID": str,
    }


class ItemBase(BaseModel):
    title: str
    description: Description


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    pwd: str


class User(UserBase):
    id: int
    items: list[Item] = []

    class Config:
        orm_mode = True
