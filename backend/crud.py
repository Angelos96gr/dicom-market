from sqlalchemy.orm import Session
import models, schemas 

def get_users(db:Session):
    return db.query(models.User).limit(10).all()

def create_user(db:Session, user: schemas.UserCreate):
    hashed_pwd = user.pwd + "hashed"
    db_user = models.User(email=user.email, pwd=hashed_pwd)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user



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
