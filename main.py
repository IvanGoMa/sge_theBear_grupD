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




