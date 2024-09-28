from fastapi import HTTPException
from sqlalchemy.orm import Session
import models, schemas
from hashlib import blake2b
from starlette import status


def get_users(db: Session) -> None:
    return db.query(models.User).all()

def get_user_by_email(db:Session, email:str)-> None:

    query_result = db.query(models.User).filter(models.User.email == email).all()

    if query_result is None:
        raise HTTPException(status_code=401, detail=f"The user with email {email} does not exist")
    print("Printing return of get_user", query_result)
    return query_result

def get_user_by_id(db: Session, id: int) -> None:
    query_result = db.query(models.User).filter(models.User.id == id).all()

    if query_result is None:
        raise HTTPException(status_code=401, detail=f"The user with id {id} does not exist")
        print("Printing return of get_user", query_result)
    return query_result


def create_user(db: Session, user: schemas.UserCreate):
    hashed_pwd = blake2b((user.password).encode("utf-8"), digest_size=4).hexdigest()
    db_query = db.query(models.User).filter(models.User.email == user.email).first()

    if db_query:
        raise HTTPException(status_code=409, detail=f"The user {user.email} already exists")
    db_user = models.User(
        email=user.email, hashed_password=hashed_pwd
    )  # new entry to be added in db
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def update_user(
    id: int, db: Session, user: schemas.UserUpdate
):  # allow changing ONLY password
    db_user = db.query(models.User).filter(models.User.id == id)
    user_to_update = db_user.first()
    if user_to_update is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {id} could not be deleted. Please check that the user exists in the database",
        )

    hashed_pwd = blake2b((user.password).encode("utf-8"), digest_size=4).hexdigest()
    updated_user = {
        "email": user_to_update.email,
        "hashed_password": hashed_pwd,
    }  # creates a user dict with same keys to be overwritten as in the target db_user object
    db_user.update(updated_user, synchronize_session=False)
    db.commit()

    return user_to_update


def delete_user_by_id(db: Session, id: int):
    db_user = db.query(models.User).filter(models.User.id == id)
    user_to_delete = db_user.first()

    if user_to_delete is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"User with id {id} could not be deleted. Please check that the user exists in the database",
        )
    db_user.delete(synchronize_session=False)
    db.commit()
    return user_to_delete

