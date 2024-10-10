
import crud, database, schemas
from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from routers.utils import get_db


router = APIRouter(
    prefix="/admin",
    tags = ["Admin Tools"]
)

"""Admin tooling"""
@router.get("/users")
def get_all_users(db:Session= Depends(get_db)):
    return  crud.get_users(db)

@router.get("/user/{id}")
def get_user_by_id(id: int = 1, db:Session= Depends(get_db)):
    return  crud.get_user_by_id(db = db, id = id)

@router.get("/user/")
def get_user_by_email(email: str, db:Session= Depends(get_db)):
    return  crud.get_user_by_email(db = db, email= email)


@router.post("/user")
def create_new_user(user: schemas.UserCreate, db: Session= Depends(get_db)):
    return crud.create_user(user = user, db = db)


@router.delete("/user/{id}")
def delete_user_by_id(id: int, db: Session= Depends(get_db)):
    return crud.delete_user_by_id(id = id, db = db)

@router.put("/user/{id}")
def update_user(id: int, user: schemas.UserUpdate, db: Session = Depends(get_db)):
    return crud.update_user(db=db, user= user, id = id)