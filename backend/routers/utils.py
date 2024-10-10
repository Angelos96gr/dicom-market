import database
from sqlalchemy.orm import Session
from passlib.context import CryptContext
import os
from datetime import timedelta, datetime, timezone
from typing import Union, Any
from dotenv import load_dotenv
from jose import jwt


def get_db():
    db: Session = database.SessionLocal()  # intantiate a session
    try:
        yield db
    finally:
        db.close()

load_dotenv()


ACCESS_TOKEN_EXPIRE_MINUTES = timedelta(minutes= 15)
REFRESH_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7 # 7 days
ALGORITHM = "HS256"
JWT_SECRET_KEY = os.environ['JWT_SECRET_KEY']   # should be kept secret
JWT_REFRESH_SECRET_KEY = os.environ['JWT_REFRESH_SECRET_KEY']    # should be kept secret


password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
def get_hashed_password(password: str)-> str:
    return password_context.hash(password)


def verify_password(password: str, hashed_password:str)-> bool:
    return password_context.verify(password, hashed_password)


def create_access_token(username: str, user_id:int):
    encode = {"sub":username, "id":user_id}
    expires = datetime.now(timezone.utc) + ACCESS_TOKEN_EXPIRE_MINUTES
    encode.update({"exp": expires})
    return jwt.encode(encode, JWT_SECRET_KEY, algorithm = ALGORITHM)

