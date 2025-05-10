from pydantic_core.core_schema import none_schema
from sqlmodel import Session, select
from models.Despesa import Despesa
from schema.despeses_sch import schema,schemas

def add_despeses(id_empleat:int,dia:int,cantidad:int,hora:int,descripcion:str,db:Session):
    db_despeses = Despesa(id_empleat=id_empleat, dia=dia, cantidad = cantidad, hora=hora, descripcion=descripcion)
    db.add(db_despeses)
    db.commit()
    db.refresh(db_despeses)
    return "Despesa creada"

def read_despeses(id_empleat:int,dia:int, db:Session):
    sql_read = select(Despesa).where(Despesa.id_empleat == id_empleat).where(Despesa.dia == dia)
    despeses = db.exec(sql_read).one()
    return schema(despeses)

def read_all_despesess(db:Session):
    sql_read = select(Despesa)
    despesess = db.exec(sql_read).all()
    return schemas(despesess)

def read_ticket(id_empleat:int, db:Session):
    sql_read = select(Despesa).where(Despesa.id_empleat == id_empleat)
    ticket = db.exec(sql_read).all()
    return schemas(ticket)

def update_despeses(id_empleat:int,dia:int,cantidad:int, db:Session):
    sql_read = select(Despesa).where(Despesa.id_empleat == id_empleat, Despesa.dia == dia)
    despeses = db.exec(sql_read).one()
    despeses.cantitat = cantidad
    db.add(despeses)
    db.commit()
    return "Despesa de la reserva {} actualitzada".format(id_empleat)

def delete_despeses(id_empleat:int, dia:int, db:Session):
    sql_read = select(Despesa).where(Despesa.id_empleat == id_empleat, Despesa.dia == dia)
    despeses = db.exec(sql_read).one()
    db.delete(despeses)
    db.commit()
    return "Despesa eliminada"
