from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session


def construct_db_url(
    user: str = "postgres",
    password: str = "1234",
    host: str = "localhost",
    port: str = "5432",
    database: str = "db_dicom_market",
    dialect="postgresql",
    driver="psycopg2",
) -> str:

    return f"{dialect}://{user}:{password}@{host}:{port}/{database}"


def get_connection():

    SQLALCHEMY_DATABASE_URL = construct_db_url()
    try:
        # The Engine is the starting point for any SQLAlchemy application. It’s “home base” for the actual database and its DBAPI
        engine = create_engine(SQLALCHEMY_DATABASE_URL)
        print(f"Connection worked on url {SQLALCHEMY_DATABASE_URL}")
        return engine
    except Exception as ex:
        print(
            f"Connection could not be established due to {ex} in url {SQLALCHEMY_DATABASE_URL}"
        )


engine = get_connection()


# each instance of this class will be a Session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

