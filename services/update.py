from sqlmodel import Session, select
from models.User import User

async def update_user(identificador:int,name:str, db:Session):
        sql_read = select(User).where(User.id == identificador)
        user = db.exec(sql_read).one()
        print("User:", user)

        user.name = name
        db.add(user)
        db.commit()
        return "Updated successfully"