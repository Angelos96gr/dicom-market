from sqlalchemy.orm import Session
import models, schemas 
from hashlib import blake2b



def get_users(db:Session) -> None:
    return db.query(models.User).all()

def get_user(db: Session, id:int) -> None:
    return db.query(models.User).filter(models.User.id == id).all()



def create_user(db:Session, user: schemas.UserCreate):
    hashed_pwd = blake2b((user.pwd).encode("utf-8"), digest_size=4).hexdigest()
    db_user = models.User(email=user.email, hashed_password=hashed_pwd) #new entry to be added in db
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db:Session, id: int):
    db.delete(db.query(models.User).filter(models).all())
    db.commit()
    db.refresh()
    pass
"""

def get_user(db: Session, user_id:int):
    return db.query(db_models.User).filter(db_models.User.id==user_id).first()


def get_user_by_email(db: Session, user_email:str):
    return db.query(db_models.User).filter(db_models.User.email==user_email).first()





def get_users(db:Session):
    return db.query(db_models.User).limit(10).all()

def get_items(db:Session):
    return db.query(db_models.Item).limit(10).all()

"""
