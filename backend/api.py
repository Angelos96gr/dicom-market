from typing import Union
from fastapi import FastAPI, Request, Depends, HTTPException, Response
from fastapi.middleware.cors import CORSMiddleware
import models, database, schemas, crud
from sqlalchemy.orm import Session
from hashlib import blake2b


app: FastAPI = FastAPI()


models.Base.metadata.create_all(
    bind=database.engine
)  # creates the tables from db_models


def get_db():
    db: Session = database.SessionLocal()  # intantiate a session
    try:
        yield db
    finally:
        db.close()


# APP_PATH = Path(__file__).resolve().parent
# TEMPLATES = Jinja2Templates(directory=str(APP_PATH/"templates"))


origins = [
    "https://127.0.0.1:8000" "https://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

tag_user = "User Management"
tag_admin = "Admin Management"


@app.get("/users/", tags = [tag_user])  # if response model is moved, then route works
def get_users(db: Session = Depends(get_db)):
    """Get all users from the database"""
    users = crud.get_users(db)
    return users

@app.post("/user", tags = [tag_user])
def authenticate_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    """Check correct authentication"""
    email = user.email
    hashed_pwd = blake2b((user.password).encode("utf-8"), digest_size=4).hexdigest()

    db_user = db.query(models.User).filter(models.User.email == email).first()
    if db_user is None:
        raise HTTPException(status_code=401, detail=f"The user {email} does not exist")
    
    if db_user.hashed_password != hashed_pwd:
        raise HTTPException(status_code=401, detail=f"The credentials you entered are not correct")

    return db_user


@app.get("/user/{email}", tags = [tag_user])
def get_user_by_email(email: str, db: Session = Depends(get_db)):
    """Get a user with a specific email from the database"""
    user_obj = crud.get_user_by_email(db=db, email=email)
    return user_obj


@app.post("/users/", tags = [tag_user])
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    """Add a new user to the database"""
    return crud.create_user(db=db, user=user)

@app.put("/user/{id}", tags = [tag_user])
def update_user(id: int, user: schemas.UserUpdate, db: Session = Depends(get_db)):
    """Update user"""

    return crud.update_user(db=db, user= user, id = id)

@app.delete("/user/{id}", tags = [tag_user])
def delete_create(id: int, db: Session = Depends(get_db)):
    """Update the password of a user"""
    return crud.delete_user_by_id(db=db, id=id) 


"""Admin tooling"""
@app.get("/admin/{id}/user_overview", tags = [tag_admin])
def admin_get_all_users(id: int = 1, db:Session= Depends(get_db)):
    #ToDO admin authentication
    return  crud.get_users(db)

"""ToDos:
# update user information
# delete user
"""


@app.get("/", tags=["root"])
async def read_root() -> dict:
    return {"message": f"Welcome in the root path"}


"""
@app.get("/", response_class=HTMLResponse)
def index(request: Request)-> Union[dict]:
    try:
        return TEMPLATES.TemplateResponse("index.html", {"request": request})
    except:
        print("An exception occured")

@app.get("/items/{item_id}")
def read_item(item_id: int, q:Union[str, None] = None) -> Union[dict]:
    try:
        return {"item_id":item_id, "q":q}
    except:
        print("An exception occured")

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item) -> dict:
    return {"item_name": item.name, "item_id":item_id}



"""
