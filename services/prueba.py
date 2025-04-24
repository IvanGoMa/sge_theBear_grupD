from schema.prueba_sch import pruebas_schema
from sqlmodel import Session, select
from models.Prueba import Prueba
from datetime import datetime

def get_all_pruebas(db:Session):
    sql_read = select(Prueba)
    pruebas = db.exec(sql_read).all()
    return pruebas_schema(pruebas)

async def add_new_prueba(data:datetime, db:Session):
    db_prueba = Prueba(data=data)
    db.add(db_prueba)
    db.commit()
    db.refresh(db_prueba)
    return {"msg":"Created prueba successfully"}

async def update_prueba(data:datetime, db: Session):
    sql_read = select(Prueba).where(Prueba.data == data)
    prueba = db.exec(sql_read).one()
    print("Prueba:", prueba)

    prueba.data = data
    db.add(prueba)
    db.commit()
    return "Updated successfully"

async def delete_prueba(data:datetime,db: Session):
    sql_read = select(Prueba).where(Prueba.data == data)
    prueba = db.exec(sql_read).one
    data = prueba.data

    db.delete(prueba)
    db.commit()

    sql_read = select(Prueba).where(Prueba.data == data)
    prueba = db.exec(sql_read).first()

    if prueba is None:
        return "Prueba {} has been deleted".format(data)