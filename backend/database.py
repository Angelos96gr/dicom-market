from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session
from dotenv import load_dotenv
import os


load_dotenv()

def construct_db_url(
    type: str = "postgres",
    user: str = os.environ["DATABASE_USER"],
    password: str = os.environ["DATABASE_PWD"],
    host: str = "localhost",
    port: str = "5432",
    database: str = "db_dicom_market",
    dialect="postgresql",
) -> str:

    if (type == "postgres"):
        return f"{dialect}://{user}:{password}@{host}:{port}/{database}"
    elif (type == "sqlite"):
        return "sqlite:///./dcm_test_db.db"
    else:
        raise Exception(f"Incorrect type: {type} of database given. The function supports 'sqlite' and 'postgres' types")

SQLALCHEMY_DATABASE_URL = construct_db_url(type = "postgres")


def get_connection(SQLALCHEMY_DATABASE_URL):

    try:
        # The Engine is the starting point for any SQLAlchemy application. It’s “home base” for the actual database and its DBAPI
        engine = create_engine(SQLALCHEMY_DATABASE_URL)
        print(f"Connection worked on url {SQLALCHEMY_DATABASE_URL}")
        return engine
    except Exception as ex:
        print(
            f"Connection could not be established due to {ex} in url {SQLALCHEMY_DATABASE_URL}"
        )


engine = get_connection(SQLALCHEMY_DATABASE_URL)


# each instance of this class will be a Session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

