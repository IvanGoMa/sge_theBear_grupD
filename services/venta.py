from pydantic_core.core_schema import none_schema
from sqlmodel import Session, select
from models.Venta import Venta
from schema.venta_sch import schema,schemas

def add_venta(id_reserva:int,id_menu:int,cantidad:int, db:Session):
    db_venta = Venta(id_reserva=id_reserva, id_menu=id_menu, cantidad = cantidad)
    db.add(db_venta)
    db.commit()
    db.refresh(db_venta)
    return {"msg":"Venta creada"}

def read_venta(id_reserva:int,id_menu:int, db:Session):
    sql_read = select(Venta).where(Venta.id_reserva == id_reserva).where(Venta.id_menu == id_menu)
    venta = db.exec(sql_read).one()
    return schema(venta)

def read_all_ventas(db:Session):
    sql_read = select(Venta)
    ventas = db.exec(sql_read).all()
    return schemas(ventas)

def read_ticket(id_reserva:int, db:Session):
    sql_read = select(Venta).where(Venta.id_reserva == id_reserva)
    ticket = db.exec(sql_read).all()
    return schemas(ticket)

def update_venta(id_reserva:int,id_menu:int,cantidad:int, db:Session):
    sql_read = select(Venta).where(Venta.id_reserva == id_reserva, Venta.id_menu == id_menu)
    venta = db.exec(sql_read).one()
    venta.cantidad = cantidad
    db.add(venta)
    db.commit()
    return {"msg":"Venta de la reserva {} actualitzada".format(id_reserva)}

def delete_venta(id_reserva:int, id_menu:int, db:Session):
    sql_read = select(Venta).where(Venta.id_reserva == id_reserva, Venta.id_menu == id_menu)
    venta = db.exec(sql_read).one()
    db.delete(venta)
    db.commit()
    return {"msg":"Venta eliminada"}


