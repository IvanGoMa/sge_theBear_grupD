from fastapi import FastAPI, Depends
from sqlmodel import SQLModel, create_engine, Session
from dotenv import load_dotenv
from services import user
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)

SQLModel.metadata.create_all(engine)

"""@app.get("/users/", response_model= list[dict])
def get_db():
    db = Session(engine)
    try:
        yield db
    finally:
        db.close()"""

@app.post("/users/", response_model=dict)
def create_user(name: str, email: str, deb:Session = Depends(get_db))):
    result = user.add_new_user(name, email, db)
    return result