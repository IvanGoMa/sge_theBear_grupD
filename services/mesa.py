from schema.mesa_sch import schema, schemas
from sqlmodel import Session, select
from models.Mesa import Mesa


def get_mesa(id:id, db: Session):
    sql_read = select(Mesa).where(Mesa.id==id)
    mesa = db.exec(sql_read)
    return schema(mesa).one()


def get_meses(db: Session):
    sql_read = select(Mesa)
    meses = db.exec(sql_read).all()
    return schemas(meses)


def add_jornada(id:int, capacitat:int, db: Session):
    db_data = Mesa(id=id, capacitat=capacitat)
    db.add(db_data)
    db.commit()
    db.refresh(db_data)
    return {"La mesa s'ha afegir correctament"}


def update_mesa(id: int, capacitat:int, db: Session):
    sql_select = select(Mesa).where(Mesa.id==id)
    mesa_db = db.exec(sql_select).one()

    mesa_db.capacitat = capacitat
    db.add(mesa_db)
    db.commit()
    return {"msg": "S'ha actualitzat la mesa correctament"}


def delete_mesa(id: int, db: Session):
    sql_select = select(Mesa).where(Mesa.id == id)
    mesa_db = db.exec(sql_select).one()

    db.delete(mesa_db)
    db.commit()
    return {"msg": "La mesa ha sigut eliminada correctament"}