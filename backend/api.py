from typing import Union
from fastapi import FastAPI, Request, Depends, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from pathlib import Path
from fastapi.middleware.cors import CORSMiddleware
import models ,database, schemas , crud
from sqlalchemy.orm import Session

app: FastAPI = FastAPI()





models.Base.metadata.create_all(bind=database.engine) #creates the tables from db_models

def get_db():
    db:Session = database.SessionLocal() #intantiate a session
    try:
        yield db
    finally:
        db.close()


#APP_PATH = Path(__file__).resolve().parent
#TEMPLATES = Jinja2Templates(directory=str(APP_PATH/"templates"))


origins = [
    "https://127.0.0.1:8000"
    "https://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.post("/users/")
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    """Add a new user to the database"""
    return crud.create_user(db=db, user=user)

@app.delete("/users/")
def delete_create(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.delete(db=db, user=user)



@app.get("/users/") # if response model is moved, then route works
def read_users(db: Session = Depends(get_db)):
    """Get all users from the database"""
    users = crud.get_users(db)
    return users

@app.get("/user/{id}")
def read_user(id: int, db: Session = Depends(get_db) ):
    """Get a user from the database"""
    return crud.get_user(db = db, id = id)

"""ToDos:
# update user information
# delete user
"""

@app.get("/", tags = ["root"])
async def read_root()->dict:
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