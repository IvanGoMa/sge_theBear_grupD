from schema.compra_sch import compra_schema, compres_schema
from sqlmodel import Session, select
from models.Compra import Compra

def get_all_compra(db: Session):
    sql_read = select(Compra)
    compras = db.exec(sql_read).all()
    return compres_schema(compras)

def update_compra(id: int, name: str, db: Session):
    sql_select = select(Compra).where(Compra.id == id)
    compra_db = db.exec(sql_select).one_or_none()

    if compra_db is None:
        return {"msg": "Compra not found"}

    compra_db.name = name
    db.add(compra_db)
    db.commit()
    db.refresh(compra_db)
    return {"msg": "Compra updated successfully", "compra": compra_schema(compra_db)}

def delete_compra(id: int, db: Session):
    sql_select = select(Compra).where(Compra.id == id)
    compra_db = db.exec(sql_select).one_or_none()

    if compra_db is None:
        return {"msg": "Compra not found"}

    db.delete(compra_db)
    db.commit()
    return {"msg": "Compra deleted successfully"}
