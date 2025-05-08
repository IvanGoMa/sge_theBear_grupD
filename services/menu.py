# services/menu.py

from sqlmodel import Session, select
from models.Menu import Menu
from schema.menu_sch import schema, schemas  # Asegúrate de tener estos esquemas creados

def add_menu(id: int, nom: str, preu: float, db: Session):
    db_menu = Menu(id=id, nom=nom, preu=preu)
    db.add(db_menu)
    db.commit()
    db.refresh(db_menu)
    return "Menu creado"

def read_menu(id: int, db: Session):
    sql_read = select(Menu).where(Menu.id == id)
    menu = db.exec(sql_read).one()
    return schema(menu)

def read_all_menus(db: Session):
    sql_read = select(Menu)
    menus = db.exec(sql_read).all()
    return schemas(menus)

def update_menu(id: int, nom: str, preu: float, db: Session):
    sql_read = select(Menu).where(Menu.id == id)
    menu = db.exec(sql_read).one()
    menu.nom = nom
    menu.preu = preu
    db.add(menu)
    db.commit()
    return "Menu {} actualizado".format(id)

def delete_menu(id: int, db: Session):
    sql_read = select(Menu).where(Menu.id == id)
    menu = db.exec(sql_read).one()
    db.delete(menu)
    db.commit()
    return "Menu eliminado"
