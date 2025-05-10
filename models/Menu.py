# models/Menu.py
from sqlmodel import SQLModel, Field

class Menu(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    nom: str
    preu: float
