from schema.users_sch import users_schema
from sqlmodel import  Session, select
from models.User import User

def get_all_users(db:Session):
    sql_read = select(User)
    users = db.exec(sql_read).all()
    return users_schema(users)

def add_new_user(name:str, email:str, db:Session):
    sql_read = select(User)
    users = db.exec(sql_read).all
    return users_schema(users)

def add_new_user(name:str, email:str, db:Session):
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
    return {"msg": "Deleted User succesfully"}


"""def registre():
    users = {
        "user1":{
            "id":1,
            "name":"Roger",
            "surname":"Sobrino",
            "age":49
        },
        "user2": {
            "id": 2,
            "name": "Josep Oriol",
            "surname": "Roca",
            "age": 23
        },
        "user3": {
            "id": 3,
            "name": "Juan Manuel",
            "surname": "Sanchez",
            "age": 40
        }
    }
    return read_sch.schemas(users)"""

