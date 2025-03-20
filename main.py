from typing import List
from fastapi import FastAPI, Depends
from services import read, user, update, delete
from sqlmodel import SQLModel, create_engine, Session
from dotenv import load_dotenv
import os

app = FastAPI()


# 1. importem el .env (database_url). Carregar variable d'entorn
load_dotenv()

# 2. Configurar la connexió a Postgresql
DATABASE_URL = os.getenv("DATABASE_URL") #Obtenir la url de connexió
engine = create_engine(DATABASE_URL) # Crear l'engine de connexió

# 3. Crear les taules a la base de dades
SQLModel.metadata.create_all(engine)

# 4. Retorna una sessió (memòria)
def get_db():
    db = Session(engine)
    try:
        yield db
    finally:
        db.close()

@app.get("/users/", response_model = list[dict])
async def read_user(db:Session = Depends(get_db)):
    result = user.get_all_users(db)
    return result

@app.post("/users/", response_model=dict)
def create_user(name: str, email:str, db:Session = Depends(get_db)):
    result = user.add_new_user(name, email, db)
    return result

@app.put("/users", response_model=str)
def update_user(ide: str, name:str, db:Session = Depends(get_db)):
    result = update.update_user(ide,name,db)
    return result

@app.delete("/users", response_model=str)
def delete_user(ide: str,db:Session = Depends(get_db)):
    result = delete.delete_user(ide,db)
    return result



