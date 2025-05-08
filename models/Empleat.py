from sqlmodel import SQLModel, Field

class Empleat(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    nom_complet: str
    telefono: int
    cargo: str