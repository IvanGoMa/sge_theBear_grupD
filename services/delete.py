from sqlmodel import Session, select
from models.User import User

async def delete_user(identificador:int,db: Session):
    sql_read = select(User).where(User.id == identificador)
    user = db.exec(sql_read).one
    name = user.name

    db.delete(user)
    db.commit()

    sql_read = select(User).where(User.id == identificador)
    user = db.exec(sql_read).first()

    if user is None:
        return "User {} with id {} has been deleted".format(name,identificador)


