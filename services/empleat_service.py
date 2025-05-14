from sqlmodel import  Session, select
from models.Empleat import Empleat
from schema.empleats_sch import empleats_schema
from schema.empleats_sch import empleat_schema


def get_all_empleats(db:Session):
    sql_read = select(Empleat)
    empleats = db.exec(sql_read).all()
    return empleats_schema(empleats)

def get_empleat( id, db:Session):
    sql_read = select(Empleat).where(Empleat.id == id)
    empleats = db.exec(sql_read).one()
    return empleat_schema(empleats)

def add_new_empleat(id:int, nom_complet:str, telefono:int, cargo:str, db:Session):
    db_empleat = Empleat(id=id, nom_complet=nom_complet, telefono=telefono, cargo=cargo)
    db.add(db_empleat)
    db.commit()
    db.refresh(db_empleat)
    return {"msg":"Created empleat succesfully"}

def update_empleat(id: int, nom_complet:str, telefono:int, cargo:str, db:Session):
    statement = select(Empleat).where(Empleat.id == id)
    results = db.exec(statement)
    empleat = results.one()
    #return {"Empleat:", empleat}

    empleat.nom_complet = nom_complet
    empleat.telefono = telefono
    empleat.cargo = cargo
    db.add(empleat)
    db.commit()
    return {"msg":"Updated Empleat succesfully", "Empleat":empleat}

def delete_empleat(id:int, db:Session):
    statement = select(Empleat).where(Empleat.id == id)
    results = db.exec(statement)
    empleat = results.one()
    #return {"Empleat:", empleat}

    db.delete(empleat)
    db.commit()
    return {"msg": "Deleted Empleat succesfully"}