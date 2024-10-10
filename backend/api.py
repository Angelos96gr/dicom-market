from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import models, database
from sqlalchemy.orm import Session
from routers import admin, user_management, auth


app: FastAPI = FastAPI()

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


models.Base.metadata.create_all(
    bind=database.engine
)  # creates the tables from db_models

app.include_router(admin.router)
app.include_router(user_management.router)
app.include_router(auth.router)




# APP_PATH = Path(__file__).resolve().parent
# TEMPLATES = Jinja2Templates(directory=str(APP_PATH/"templates"))





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
