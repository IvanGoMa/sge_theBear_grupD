from sqlmodel import  Session, select
from models.Client import Client
from schema.clients_sch import clients_schema
from schema.clients_sch import client_schema



def get_all_clients(db:Session):
    sql_read = select(Client)
    clients = db.exec(sql_read).all()
    return clients_schema(clients)

def get_client( id, db:Session):
    sql_read = select(Client).where(Client.id == id)
    clients = db.exec(sql_read).one()
    return client_schema(clients)

def add_new_client(nom_complet:str, telefono:int, db:Session):
    db_client = Client(nom_complet=nom_complet, telefono=telefono)
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return {"msg":"Created client succesfully"}

def update_client(id: int, nom_complet:str, telefono: int, db:Session):
    statement = select(Client).where(Client.id == id)
    results = db.exec(statement)
    client = results.one()
    #return {"User:", user}

    client.nom_complet = nom_complet
    db.add(client)
    db.commit()
    return {"msg":"Updated Client succesfully", "Client":client}

def delete_client(id:int, db:Session):
    statement = select(Client).where(Client.id == id)
    results = db.exec(statement)
    client = results.one()
    #return {"User:", user}

    db.delete(client)
    db.commit()
    return {"msg": "Deleted Client succesfully"}