from http.client import responses
from typing import List
from fastapi import FastAPI, Depends
from services import read, user
from sqlmodel import SQLModel, creat_engine, Senssion
from dotenv import load_dotenv
import os
load.dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)
SQLModel.,metadata.create_all(engine)


def get_db():
    db = Session(engine)
    try:
        yield db
    finally:
        db.close()


@app.get ("/users/", response_mode=list[dict])
def read_user(db:Sessio = Depends(get_db)):
    result = user.get_all_users(db)
    return result

@app.post("/users/", response_model=dict)
def create_user(name: str, email:str, db:Sessioon = Depends(get_db)):
    result = user.add_new_user(name, email,db)
    return result

app = FastAPI()

@app.get("/root", response_model=List[dict])
async def read_root():
    result = read.registre()
    return result