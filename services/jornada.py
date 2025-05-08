from schema.jornada_sch import schema, schemas
from sqlmodel import Session, select
from models.Jornada import Jornada

def get_jornada(id_empleat:int, dia: int, mes: int, any: int, db:Session):
    sql_read = select(Jornada).where(Jornada.id_empleat==id_empleat, Jornada.any==any, Jornada.mes==mes, Jornada.dia==dia)
    jornada = db.exec(sql_read)
    return schema(jornada).one()

def get_jornades(db:Session):
    sql_read = select(Jornada)
    jornades = db.exec(sql_read).all()
    return schemas(jornades)

def add_jornada(id_empleat:int, dia: int, mes: int, any: int, hora_inici: int, hora_fi:int, db:Session):
    db_data = Jornada(id_empleat=id_empleat, dia=dia, mes=mes, any=any, hora_inici=hora_inici, hora_fi=hora_fi)
    db.add(db_data)
    db.commit()
    db.refresh(db_data)
    return {"La jornada s'ha afegir correctament"}

def update_jornada(id_empleat:int, any:int, mes:int, dia:int, hora_inici:int, hora_fi:int, db:Session):
    sql_select = select(Jornada).where( Jornada.id_empleat==id_empleat, Jornada.any==any, Jornada.mes==mes, Jornada.dia==dia)
    jornada_db = db.exec(sql_select).one()

    jornada_db.hora_inici = hora_inici
    jornada_db.hora_fi = hora_fi
    db.add(jornada_db)
    db.commit()
    return{"msg":"S'ha actualitzat la jornada correctament"}

def delete_jornada(id_empleat:int, any:int, mes:int, dia:int, db:Session):
    sql_select = select(Jornada).where(Jornada.id_empleat==id_empleat, Jornada.any==any, Jornada.mes==mes, Jornada.dia==dia)
    user_db = db.exec(sql_select).one()

    db.delete(user_db)
    db.commit()
    return {"msg":"La jornada ha sigut eliminada correctament"}

