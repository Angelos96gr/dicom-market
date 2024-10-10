from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session
from backend.database import construct_db_url, get_connection



SQLALCHEMY_DATABASE_URL = construct_db_url(type = "sqlite")



engine = get_connection(SQLALCHEMY_DATABASE_URL)


# each instance of this class will be a Session
test_SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

