from schema.despeses_sch import despesa_schema, despeses_schema
from sqlmodel import Session, select
from models.Despesa import Despesa

def get_all_despeses(db: Session):
    sql_read = select(Despesa)
    despeses = db.exec(sql_read).all()
    return despeses_schema(despeses)

def update_despesa(id: int, name: str, db: Session):
    sql_select = select(Despesa).where(Despesa.id == id)
    despesa_db = db.exec(sql_select).one_or_none()

    if despesa_db is None:
        return {"msg": "Despesa not found"}

    despesa_db.name = name
    db.add(despesa_db)
    db.commit()
    db.refresh(despesa_db)
    return {"msg": "Despesa updated successfully", "despesa": despesa_schema(despesa_db)}

def delete_despesa(id: int, db: Session):
    sql_select = select(Despesa).where(Despesa.id == id)
    despesa_db = db.exec(sql_select).one_or_none()

    if despesa_db is None:
        return {"msg": "Despesa not found"}

    db.delete(despesa_db)
    db.commit()
    return {"msg": "Despesa deleted successfully"}
