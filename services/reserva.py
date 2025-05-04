from pydantic_core.core_schema import none_schema
from sqlmodel import Session, select
from models.Reserva import Reserva
from schema.reserva_sch import schema,schemas

def add_reserva(id:int,id_client:int, id_mesa:int, hora:int, dia:int, mes:int, any:int, db:Session):
    db_reserva = Reserva(id = id,id_client=id_client, id_mesa= id_mesa, hora = hora, dia = dia, mes = mes, any = any)
    db.add(db_reserva)
    db.commit()
    db.refresh(db_reserva)
    return "Reserva creada"

def read_reserva(id:int,db:Session):
    sql_read = select(Reserva).where(Reserva.id == id)
    reserva = db.exec(sql_read).one()
    return schema(reserva)

def read_reservas(db:Session):
    sql_read= select(Reserva)
    reservas = db.exec(sql_read).all()
    return schemas(reservas)

def update_reserva(id:int,id_client:int, id_mesa:int, hora:int, dia:int, mes:int, any:int, db:Session):
    sql_read = select(Reserva).where(Reserva.id == id)
    reserva = db.exec(sql_read).one()
    reserva.id_client = id_client
    reserva.id_mesa = id_mesa
    reserva.hora = hora
    reserva.dia = dia
    reserva.mes = mes
    reserva.any = any
    db.add(reserva)
    db.commit()
    return "Reserva amb id {} actualitzada".format(id)
def delete_reserva(id:int,db:Session):
    sql_read = select(Reserva).where(Reserva.id == id)
    reserva = db.exec(sql_read).one()
    db.delete(reserva)
    db.commit()

    sql_read = select(Reserva).where(Reserva.id == id)
    reserva = db.exec(sql_read).first()

    if reserva is None:
        return "Reserva amb id {} eliminada".format(id)







