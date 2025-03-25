from fastapi import FastAPI
from sqlmodel import SQLModel, create_engine, Session
from dotenv import load_dotenv
import os

#connecció fastapi
app = FastAPI()

@app.get("/user/read/", response_model=list[dict])
async def read_user():
    return {"Message": "Read user succesfully"}


#creació de db amb sqlmodel
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)

SQLModel.metadata.create_all(engine)


def get_db():
    db = Session(engine)
    try:
        yield db
    finally:
        db.close()



