from schema.empleats_sch import empleats_schema
from sqlmodel import  Session, select
from models.Empleat import Empleat

def get_all_empleats(db:Session):
    sql_read = select(Empleat)
    empleats = db.exec(sql_read).all()
    return empleats_schema(empleats)

def add_new_empleat(nom_complet:str, telefono:int, cargo:str, db:Session):
    db_empleat = Empleat(nom_complet=nom_complet, telefono=telefono, cargo=cargo)
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