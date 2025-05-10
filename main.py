from typing import List
from fastapi import FastAPI, Depends
from starlette.middleware.cors import CORSMiddleware
from services import empleat_service, client_service, event_service

from services import reserva, venta, jornada, mesa, compra, despeses, menu
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

@app.get("/get_reservas/", response_model = list[dict])
def read_reservas(db:Session = Depends(get_db)):
    result = reserva.read_reservas(db)
    return result

@app.get("/get_reserva/", response_model = dict)
def read_reserva(id:int,db:Session = Depends(get_db)):
    result = reserva.read_reserva(id,db)
    return result

@app.post("/add_reservas/", response_model=dict)
def create_reserva(id:int,id_client:int,id_mesa:int,hora:int,dia:int,mes:int,any:int, db:Session = Depends(get_db)):
    result = reserva.add_reserva(id,id_client,id_mesa,hora,dia,mes,any,db)
    return result

@app.put("/update_reservas", response_model=dict)
def update_reserva(id:int,id_client:int,id_mesa:int,hora:int,dia:int,mes:int,any:int, db:Session = Depends(get_db)):
    result = reserva.update_reserva(id,id_client,id_mesa,hora,dia,mes,any,db)
    return result

@app.delete("/delete_reservas", response_model=dict)
def delete_reserva(id:int,db:Session = Depends(get_db)):
    result = reserva.delete_reserva(id,db)
    return result

# Endpoints venta
@app.get("/get_ventas/", response_model = list[dict])
def read_ventas(db:Session = Depends(get_db)):
    result = venta.read_all_ventas(db)
    return result

@app.get("/get_venta/", response_model = dict)
def read_venta(id_reserva:int,id_menu:int,db:Session = Depends(get_db)):
    result = venta.read_venta(id_reserva,id_menu,db)
    return result

@app.get("/get_ticket/", response_model=list[dict])
def read_ticket(id_reserva:int,db:Session = Depends(get_db)):
    result = venta.read_ticket(id_reserva, db)
    return result

@app.post("/add_ventas/", response_model = dict)
def create_venta(id_reserva:int,id_menu:int,cantidad:int,db:Session = Depends(get_db)):
    result = venta.add_venta(id_reserva, id_menu,cantidad, db)
    return result

@app.put("/update_ventas", response_model= dict)
def update_venta(id_reserva:int,id_menu:int,cantidad:int,db:Session = Depends(get_db)):
    result = venta.update_venta(id_reserva, id_menu, cantidad, db)
    return result


@app.delete("/delete_ventas", response_model=dict)
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
def create_event(id:int,dia:int, hora:int, mes:int, anyo:int, descripcio:str, db:Session = Depends(get_db)):
    result = event_service.add_new_event(id, dia, hora, mes, anyo, descripcio, db)
    return result

#actualizar event
@app.put("/events/", response_model=dict)
async def update_event(id: int, dia:int, hora:int, mes:int, anyo:int, descripcio:str, db:Session = Depends(get_db)):
    result = event_service.update_event(id, dia, hora, mes, anyo, descripcio, db)
    return result

#borrar event
@app.delete("/events/", response_model=dict)
async def delete_event(id: int, db:Session = Depends(get_db)):
    result = event_service.delete_event(id, db)
    return result

# Endpoints para Compra

@app.post("/compra/")
def create_compra_view(id_producte: int, dia: int, hora: int, cantidad: int, db: Session = Depends(get_db)):
    return compra.add_compra(id_producte=id_producte, dia=dia, hora=hora, cantidad=cantidad, db=db)


@app.get("/compra/")
def get_compra_view(id_producte: int, dia: int = 1, db: Session = Depends(get_db)):
    return compra.read_compra(id_producte, dia, db)


@app.get("/compres/")
def get_all_compras_view(db: Session = Depends(get_db)):
    return compra.read_all_compras(db=db)


@app.get("/compra/")
def get_ticket_view(id_producte: int, db: Session = Depends(get_db)):
    return compra.read_ticket(id_producte=id_producte, db=db)


@app.put("/compra/")
def update_compra_view(id_producte: int, dia: int, cantidad: int, db: Session = Depends(get_db)):
    return compra.update_compra(id_producte=id_producte, dia=dia, cantidad=cantidad, db=db)


@app.delete("/compra/")
def delete_compra_view(id_producte: int, dia: int, db: Session = Depends(get_db)):
    return compra.delete_compra(id_producte=id_producte, dia=dia, db=db)


# Endpoints despesa

@app.post("/despesa/")
def create_despesa_view(id_empleat: int, dia: int, hora: int, cantidad: int, descripcion: str, db: Session = Depends(get_db)):
    return despeses.add_despeses(id_empleat=id_empleat, dia=dia, hora=hora, cantidad=cantidad, descripcion=descripcion, db=db)


@app.get("/despesa/")
def get_despesa_view(id_empleat: int, dia: int, db: Session = Depends(get_db)):
    return despeses.read_despeses(id_empleat=id_empleat, dia=dia, db=db)


@app.put("/despesa/")
def update_despesa_view(id_empleat: int, dia: int, cantidad: int, db: Session = Depends(get_db)):
    return despeses.update_despeses(id_empleat=id_empleat, dia=dia, cantidad=cantidad, db=db)


@app.delete("/despesa/")
def delete_despesa_view(id_empleat: int, dia: int, db: Session = Depends(get_db)):
    return despeses.delete_despeses(id_empleat=id_empleat, dia=dia, db=db)


# Endpoints menú
@app.post("/menu/")
def create_menu_view(id: int, nom: str, preu: float, db: Session = Depends(get_db)):
    return menu.add_menu(id=id, nom=nom, preu=preu, db=db)

@app.get("/menu/{id}")
def get_menu_view(id: int, db: Session = Depends(get_db)):
    return menu.read_menu(id=id, db=db)

@app.get("/menu/")
def get_all_menus_view(db: Session = Depends(get_db)):
    return menu.read_all_menus(db=db)

@app.put("/menu/{id}")
def update_menu_view(id: int, nom: str, preu: float, db: Session = Depends(get_db)):
    return menu.update_menu(id=id, nom=nom, preu=preu, db=db)

@app.delete("/menu/{id}")
def delete_menu_view(id: int, db: Session = Depends(get_db)):
    return menu.delete_menu(id=id, db=db)

