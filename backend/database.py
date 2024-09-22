from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


def construct_db_url(
    user:str = "angelos", password:str ="hashedpwd", host:str = "localhost" , port:str = "8001", database:str= "db", dialect="postgresql", driver="psycopg2"
) -> str:
    
    return "sqlite:///./sql_app.db"

    #return f"{dialect}://{user}:{password}@{host}:{port}/{database}"

def get_connection():
    
    #SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
    SQLALCHEMY_DATABASE_URL = construct_db_url()
    try:
        # The Engine is the starting point for any SQLAlchemy application. It’s “home base” for the actual database and its DBAPI
        engine = create_engine(SQLALCHEMY_DATABASE_URL)
        print(f"Connection worked on url {SQLALCHEMY_DATABASE_URL}")
        return engine
    except Exception as ex:
        print(f"Connection could not be establiushed due to {ex} in url {SQLALCHEMY_DATABASE_URL}")

engine = get_connection()


# each instance of this class will be a Session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


