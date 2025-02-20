from schema import read_sch

def registre():
    users = {
        "users":{
            "id": 1,
            "name":"Roger",
            "surname":"Sobrino",
            "age": 49
        },
        "users2": {
            "id": 2,
            "name": "Josep Oriol",
            "surname": "Roca",
            "age": 23
        }
        "users3": {
            "id": 3,
            "name": "Juan Manuel",
            "surname": "Sanchez",
            "age": 48
        }
    }
    return read_sch.schemas(users)