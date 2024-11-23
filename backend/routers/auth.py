import crud, schemas, models
from fastapi import Depends, APIRouter, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from hashlib import blake2b
from routers.utils import get_db, verify_password, get_hashed_password
from passlib.context import CryptContext
from typing import Annotated


router = APIRouter(
    #prefix="/auth",
    tags = ["User Authentication"]
)

@router.post("/users/", status_code=status.HTTP_201_CREATED)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    """Add a new user to the database"""
    return crud.create_user(db=db, user=user)

@router.post("/user",status_code=status.HTTP_202_ACCEPTED)
def authenticate_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    """Check correct authentication"""
    email = user.email
    
    db_user = db.query(models.User).filter(models.User.email == email).first()
    if db_user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"The user {email} does not exist")
    
    if not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"The credentials you entered are not correct")


    return db_user
