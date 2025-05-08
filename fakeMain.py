from fastapi import FastAPI, Depends
from services import empleat_service
from models import Empleat
from sqlmodel import SQLModel, create_engine, Session
from dotenv import load_dotenv
import os

app = FastAPI()

'''@app.get("/root", response_model=List[dict])
async def read_root():
    result = read.registre()
    return result'''

#1 Carregar variables d'entorn
load_dotenv()

#2 Configurar la connexió a PostgreSQL
DATABASE_URL = os.getenv("DATABASE_URL") #Obtenir la URL de connexió des de .env
engine = create_engine(DATABASE_URL) #Crear l'engine de connexió. Engine és l'objecte  la connexió a la base de dades

#3 Crear les taules a l abase de dades
SQLModel.metadata.create_all(engine) #agafem la connexió i les taules(models) per crear la base de dades

#4 és similar al cursor
def get_db():
    db = Session(engine)
    try:
        yield db
    finally:
        db.close()

#####--------Endpoints Empleat-------###############

#read empleats
@app.get("/empleats/", response_model= list[dict])
def read_empleats(db:Session = Depends(get_db)):
    result = empleat_service.get_all_empleats(db)
    return result

@app.get("/empleat/", response_model= dict)
def read_empleat(id:int, db:Session = Depends(get_db)):
    result = empleat_service.get_empleat(id, db)
    return result

#añadir empleat

@app.post("/empleats/", response_model=dict)
def create_empleat(id:int,nom_complet:str, telefono:int, cargo:str, db:Session = Depends(get_db)):
    result = empleat_service.add_new_empleat(nom_complet, telefono, cargo, db)
    return result

#actualizar empleat

@app.put("/empleats/", response_model=dict)
async def update_empleat(id: int, nom_complet:str, telefono:int, cargo:str, db:Session = Depends(get_db)):
    result = empleat_service.update_empleat(id, nom_complet, telefono, cargo, db)
    return result

#borrar empleat

@app.delete("/empleats/", response_model=dict)
async def delete_empleat(id: int, db:Session = Depends(get_db)):
    result = empleat_service.delete_empleat(id, db)
    return result