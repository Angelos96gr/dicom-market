from typing import Union
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from pathlib import Path

app: FastAPI = FastAPI()
APP_PATH = Path(__file__).resolve().parent
TEMPLATES = Jinja2Templates(directory=str(APP_PATH/"templates"))


class Item(BaseModel):
    name:str
    price: float
    is_offer: Union[bool, None]= None


@app.get("/", response_class=HTMLResponse)
def index(request: Request)-> Union[dict]:
    print(type(TEMPLATES.TemplateResponse("index.html", {"request": request})))
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