from schema.users_sch import users_schema
from sqlmodel import Session, select
from models.User import User

def get_all_users(db:Session):
    sql_read = select(User)
    users = db.exec(sql_read).all()
    return users_schema(users)

def update_user(id: int, name: str, db: Session):
    sql_select = select(User).where(User.id == id)
    user_db = db.exec(sql_select).one_or_none()  # ✅ Evita errores si el usuario no existe

    user_db.name = name
    db.add(user_db)
    db.commit()
    db.refresh(user_db)  # ✅ Refrescar el objeto después de la actualización
    return {"msg": "User updated successfully", "user": user_db}

def delete_user(id: int, db: Session):
    sql_select = select(User).where(User.id == id)
    user_db = db.exec(sql_select).one_or_none()  # ✅ Evita errores si el usuario no existe

    db.delete(user_db)
    db.commit()
    return {"msg": "User deleted successfully"}
