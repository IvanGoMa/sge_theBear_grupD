from pydantic_core.core_schema import none_schema
from sqlmodel import Session, select
from models.Compra import Compra
from schema.compra_sch import schema,schemas

def add_compra(id_producte:int,dia:int,cantidad:int,hora:int, db:Session):
    db_compra = Compra(id_producte=id_producte, dia=dia, cantidad = cantidad, hora=hora)
    db.add(db_compra)
    db.commit()
    db.refresh(db_compra)
    return "Compra creada"

def read_compra(id_producte:int,dia:int, db:Session):
    sql_read = select(Compra).where(Compra.id_producte == id_producte).where(Compra.dia == dia)
    compra = db.exec(sql_read).one()
    return schema(compra)

def read_all_compras(db:Session):
    sql_read = select(Compra)
    compras = db.exec(sql_read).all()
    return schemas(compras)

def read_ticket(id_producte:int, db:Session):
    sql_read = select(Compra).where(Compra.id_producte == id_producte)
    ticket = db.exec(sql_read).all()
    return schemas(ticket)

def update_compra(id_producte:int,dia:int,cantidad:int, db:Session):
    sql_read = select(Compra).where(Compra.id_producte == id_producte, Compra.dia == dia)
    compra = db.exec(sql_read).one()
    compra.cantidad = cantidad
    db.add(compra)
    db.commit()
    return "Compra de la reserva {} actualitzada".format(id_producte)

def delete_compra(id_producte:int, dia:int, db:Session):
    sql_read = select(Compra).where(Compra.id_producte == id_producte, Compra.dia == dia)
    compra = db.exec(sql_read).one()
    db.delete(compra)
    db.commit()
    return "Compra eliminada"
