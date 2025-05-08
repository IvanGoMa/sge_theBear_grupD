
def producte_schema(producte) -> dict:
    return {
        "id": producte.id,
        "desc": producte.desc,
        "preu": producte.preu
    }

def productes_schema(productes) -> list[dict]:
    return [producte_schema(producte) for producte in productes]

# schema/menu_sch.py
from pydantic import BaseModel
from typing import List

# Esquema para un solo menú
class MenuSchema(BaseModel):
    id: int
    nom: str
    preu: float

    class Config:
        orm_mode = True  # Esto permite trabajar con SQLAlchemy/SQLModel

# Esquema para una lista de menús
class MenusSchema(BaseModel):
    menus: List[MenuSchema]  # Usamos una lista de MenuSchema

    class Config:
        orm_mode = True
