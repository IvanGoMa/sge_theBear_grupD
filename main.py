from typing import List
from fastapi import FastAPI, Depends
from services import prueba
from sqlmodel import SQLModel, create_engine, Session
from dotenv import load_dotenv
from datetime import datetime
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



@app.get("/pruebas/", response_model = list[dict])
async def read_prueba(db:Session = Depends(get_db)):
    result = prueba.get_all_pruebas(db)
    return result

@app.post("/pruebas/", response_model=dict)
def create_prueba(data:datetime, db:Session = Depends(get_db)):
    result = prueba.add_new_prueba(data, db)
    return result

@app.put("/pruebas", response_model=str)
def update_prueba(data:datetime, db:Session = Depends(get_db)):
    result = prueba.update_prueba(data,db)
    return result

@app.delete("/pruebas", response_model=str)
def delete_prueba(data:datetime,db:Session = Depends(get_db)):
    result = prueba.delete_prueba(data,db)
    return result
