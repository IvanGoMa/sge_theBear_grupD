from sqlmodel import Session, select
from models.Reserva import Reserva

def add_reserva(id:int,id_client:int, id_mesa:int, hora:int, dia:int, mes:int, any:int db:Session):
    db_reserva = Reserva(id = id,id_client=id_client, id_mesa= id_mesa, hora  dia = dia, hora = hora)
    db.add(db_reserva)
    db.commit()
    db.refresh(db_reserva)
    return{"Created reserva successfully"}

def read_reserva():

def update_reserva():

