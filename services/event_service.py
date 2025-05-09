from schema.events_sch import events_schema
from schema.events_sch import event_schema
from sqlmodel import  Session, select
from models.Event import Event

def get_all_events(db:Session):
    sql_read = select(Event)
    events = db.exec(sql_read).all()
    return events_schema(events)

def get_event( id, db:Session):
    sql_read = select(Event).where(Event.id == id)
    events = db.exec(sql_read).one()
    return event_schema(events)

def add_new_event(id:int, dia:int, hora:int, mes:int, any:int, descripcio:str, db:Session):
    db_event = Event(id= id, dia=dia, hora=hora, mes=mes, any=any, descripcio=descripcio)
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return {"msg":"Created event succesfully"}

def update_event(id: int, dia:int, hora:int, mes:int, any:int, descripcio:str,db:Session):
    statement = select(Event).where(Event.id == id)
    results = db.exec(statement)
    event = results.one()
    #return {"User:", user}

    event.dia = dia
    event.hora = hora
    event.mes = mes
    event.any = any
    event.descripcio = descripcio
    db.add(event)
    db.commit()
    return {"msg":"Updated Event succesfully", "Event":event}

def delete_event(id:int, db:Session):
    statement = select(Event).where(Event.id == id)
    results = db.exec(statement)
    event = results.one()
    #return {"User:", user}

    db.delete(event)
    db.commit()
    return {"msg": "Deleted Event succesfully"}