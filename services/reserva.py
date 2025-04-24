from sqlmodel import Session, select
from models.Reserva import Reserva

def add_reserva(id_client:int, id_mesa:int, dia:int, hora:int, db:Session):
    db_reserva = Reserva(id_client=id_client, id_mesa= id_mesa, dia = dia, hora = hora)
    db.add(db_reserva)
    db.commit()
    db.refresh(db_reserva)
    return{"Created reserva successfully"}

def read_reserva():

def update_reserva():

