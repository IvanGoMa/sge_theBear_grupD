from sqlmodel import SQLModel, Field

class Client(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    nom_complet: str
    telefono: int