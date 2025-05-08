from schema.events_sch import events_schema
from sqlmodel import  Session, select
from models.Event import Event

def get_all_events(db:Session):
    sql_read = select(Event)
    events = db.exec(sql_read).all()
    return events_schema(events)

def add_new_event(dia:int, hora:int, db:Session):
    db_event = Event(dia=dia, hora=hora)
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return {"msg":"Created event succesfully"}

def update_event(id: int, dia:int, hora:int, db:Session):
    statement = select(Event).where(Event.id == id)
    results = db.exec(statement)
    event = results.one()
    #return {"User:", user}

    event.hora = hora
    event.dia = dia
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