from schema.empleats_sch import empleats_schema
from sqlmodel import  Session, select
from models.Empleat import Empleat

def get_all_empleats(db:Session):
    sql_read = select(Empleat)
    empleats = db.exec(sql_read).all()
    return empleats_schema(empleats)

"""def add_new_user(name:str, email:str, db:Session):  FALTAN MODIFICAR!!!!
    db_user = User(name=name, email=email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return {"msg":"Created user succesfully"}

################
def update_user(id: int, name:str, db:Session):
    statement = select(User).where(User.id == id)
    results = db.exec(statement)
    user = results.one()
    #return {"User:", user}

    user.name = name
    db.add(user)
    db.commit()
    return {"msg":"Updated User succesfully", "User":user}

def delete_user(id:int, db:Session):
    statement = select(User).where(User.id == id)
    results = db.exec(statement)
    user = results.one()
    #return {"User:", user}

    db.delete(user)
    db.commit()
    return {"msg": "Deleted User succesfully"}"""