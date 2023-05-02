from fastapi import FastAPI
from tinydb import TinyDB, Query
from datetime import datetime
from pydantic import BaseModel

app = FastAPI()

db = TinyDB('db.json')

class action(BaseModel):
    action: str
    location: str
    device: str


@app.get("/")
def index() :
    return { "hello world"}

@app.get("/name/{id}")
def name(id : int) :
    return { "name" :item[0]} 

@app.get("/logA/{action}")
def logA(action : str) :
    id = db.insert({'action': action, 'time': datetime.now().strftime("%d/%m/%Y %H:%M:%S")})
    return { "id" : id}


@app.get('/getLog')
def getLog():
    return db.all()