# services/menu.py
from schema.menu_sch import MenuSchema, MenusSchema  # Cambio aquí
from sqlmodel import Session, select
from models.Menu import Menu

# Obtener todos los menús
def get_all_menu(db: Session):
    sql_read = select(Menu)
    menus = db.exec(sql_read).all()
    return MenusSchema(menus=[MenuSchema.from_orm(menu) for menu in menus])  # Modificado

# Actualizar un menú
def update_menu(id: int, nom: str, preu: float, db: Session):
    sql_select = select(Menu).where(Menu.id == id)
    menu_db = db.exec(sql_select).one_or_none()
    if not menu_db:
        return {"error": "Menu not found"}

    menu_db.nom = nom
    menu_db.preu = preu
    db.add(menu_db)
    db.commit()
    db.refresh(menu_db)
    return {"msg": "Menu updated successfully", "menu": MenuSchema.from_orm(menu_db)}  # Modificado

# Eliminar un menú
def delete_menu(id: int, db: Session):
    sql_select = select(Menu).where(Menu.id == id)
    menu_db = db.exec(sql_select).one_or_none()
    if not menu_db:
        return {"error": "Menu not found"}

    db.delete(menu_db)
    db.commit()
    return {"msg": "Menu deleted successfully"}
