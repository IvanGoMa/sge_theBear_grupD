from typing import List
from fastapi import FastAPI, Depends
from starlette.middleware.cors import CORSMiddleware

from services import reserva, venta, jornada, mesa
from sqlmodel import SQLModel, create_engine, Session
from dotenv import load_dotenv
from datetime import datetime
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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


# Endpoints reserva

@app.get("/reservas/", response_model = list[dict])
def read_reservas(db:Session = Depends(get_db)):
    result = reserva.read_reservas(db)
    return result

@app.get("/reserva/", response_model = dict)
def read_reserva(id:int,db:Session = Depends(get_db)):
    result = reserva.read_reserva(id,db)
    return result

@app.post("/reservas/", response_model=str)
def create_reserva(id:int,id_client:int,id_mesa:int,hora:int,dia:int,mes:int,any:int, db:Session = Depends(get_db)):
    result = reserva.add_reserva(id,id_client,id_mesa,hora,dia,mes,any,db)
    return result

@app.put("/reservas", response_model=str)
def update_reserva(id:int,id_client:int,id_mesa:int,hora:int,dia:int,mes:int,any:int, db:Session = Depends(get_db)):
    result = reserva.update_reserva(id,id_client,id_mesa,hora,dia,mes,any,db)
    return result

@app.delete("/reservas", response_model=str)
def delete_reserva(id:int,db:Session = Depends(get_db)):
    result = reserva.delete_reserva(id,db)
    return result

# Endpoints venta
@app.get("/ventas/", response_model = list[dict])
def read_ventas(db:Session = Depends(get_db)):
    result = venta.read_all_ventas(db)
    return result

@app.get("/venta/", response_model = dict)
def read_venta(id_reserva:int,id_menu:int,db:Session = Depends(get_db)):
    result = venta.read_venta(id_reserva,id_menu,db)
    return result

@app.get("/ticket/", response_model=list[dict])
def read_ticket(id_reserva:int,db:Session = Depends(get_db)):
    result = venta.read_ticket(id_reserva, db)
    return result

@app.post("/ventas/", response_model = str)
def create_venta(id_reserva:int,id_menu:int,cantidad:int,db:Session = Depends(get_db)):
    result = venta.add_venta(id_reserva, id_menu,cantidad, db)
    return result

@app.put("/ventas", response_model= str)
def update_venta(id_reserva:int,id_menu:int,cantidad:int,db:Session = Depends(get_db)):
    result = venta.update_venta(id_reserva, id_menu, cantidad, db)
    return result


@app.delete("/ventas", response_model=str)
def delete_venta(id_reserva:int,id_menu:int,db:Session = Depends(get_db)):
    result = venta.delete_venta(id_reserva,id_menu,db)
    return result

#Endpoints Jornada
@app.get("/jornada/", response_model = dict)
def get_jornada(id_empleat:int, dia: int, mes: int, any: int,db:Session = Depends(get_db)):
    result = jornada.get_jornada(id_empleat, dia, mes, any, db)
    return result

@app.get("/jornada/", response_model = list[dict])
def get_jornades(db:Session = Depends(get_db)):
    result = jornada.get_jornades(db)
    return result
