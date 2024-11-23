import crud, schemas, models
from fastapi import Depends, APIRouter, HTTPException, status
from sqlalchemy.orm import Session
from routers.utils import get_db




tag_user = "User Management"

router = APIRouter()

@router.get("/user/{email}", tags = [tag_user])
def get_user_by_email(email: str, db: Session = Depends(get_db)):
    """Get a user with a specific email from the database"""
    user_obj = crud.get_user_by_email(db=db, email=email)
    return user_obj



@router.put("/user/{id}", tags = [tag_user])
def update_user(id: int, user: schemas.UserUpdate, db: Session = Depends(get_db)):
    """Update user"""

    return crud.update_user(db=db, user= user, id = id)

@router.delete("/user/{id}", tags = [tag_user])
def delete_create(id: int, db: Session = Depends(get_db)):
    """delete user"""
    return crud.delete_user_by_id(db=db, id=id) 
