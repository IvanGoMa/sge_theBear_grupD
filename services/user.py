from schema.users_sch import users_schema
from sqlmodel import  Session, select
from models.User import User

def get_all_users(db:Session):
    sql_read = select(User)
    users = db.exec(sql_read).all()
    return users_schema(users)

def add_new_user(name:str, email:str, db:Session):
    db_user = User(name=name, email=email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return {"Created user succesfully"}

################
def update_user(name:str, db:Session):
    statement = select(User).where(User.id == "2")
    results = db.exec(statement)
    user = results.one()
    return {"User:", user}

    User.name = "Kim"
    db.add(User)
    db.commit()
    return {"Updated User succesfully"}

def delete_user(name:str, db:Session):
    statement = select(User).where(User.id == "2")
    results = db.exec(statement)
    user = results.one()
    return {"User:", user}

    db.delete(User)
    db.commit()
    return {"Deleted User succesfully"}


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

