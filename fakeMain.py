from fastapi import FastAPI, Depends
from services import empleat_service, client_service, event_service
from models import Empleat
from sqlmodel import SQLModel, create_engine, Session
from dotenv import load_dotenv
import os

#from sge_theBear_grupD.services import event_service

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

#####--------Endpoints Client-------###############

#read clients
@app.get("/clients/", response_model= list[dict])
def read_clients(db:Session = Depends(get_db)):
    result = client_service.get_all_clients(db)
    return result

@app.get("/client/", response_model= dict)
def read_client(id:int, db:Session = Depends(get_db)):
    result = client_service.get_client(id, db)
    return result

#añadir client
@app.post("/clients/", response_model=dict)
def create_client(id:int,nom_complet:str, telefono:int, db:Session = Depends(get_db)):
    result = client_service.add_new_client(nom_complet, telefono, db)
    return result

#actualizar client
@app.put("/clients/", response_model=dict)
async def update_client(id: int, nom_complet:str, telefono:int, db:Session = Depends(get_db)):
    result = client_service.update_client(id, nom_complet, telefono, db)
    return result

#borrar client
@app.delete("/clients/", response_model=dict)
async def delete_client(id: int, db:Session = Depends(get_db)):
    result = client_service.delete_client(id, db)
    return result


#####--------Endpoints Event-------###############

#read event
@app.get("/events/", response_model= list[dict])
def read_events(db:Session = Depends(get_db)):
    result = event_service.get_all_events(db)
    return result

@app.get("/event/", response_model= dict)
def read_event(id:int, db:Session = Depends(get_db)):
    result = event_service.get_event(id, db)
    return result

#añadir event
@app.post("/events/", response_model=dict)
def create_event(id:int,dia:int, hora:int, mes:int, any:int, descripcio:str, db:Session = Depends(get_db)):
    result = event_service.add_new_event(id, dia, hora, mes, any,descripcio, db)
    return result

#actualizar event
@app.put("/events/", response_model=dict)
async def update_event(id: int, dia:int, hora:int, mes:int, any:int, descripcio:str, db:Session = Depends(get_db)):
    result = event_service.update_event(id, dia, hora, mes, any, descripcio, db)
    return result

#borrar event
@app.delete("/events/", response_model=dict)
async def delete_event(id: int, db:Session = Depends(get_db)):
    result = event_service.delete_event(id, db)
    return result

