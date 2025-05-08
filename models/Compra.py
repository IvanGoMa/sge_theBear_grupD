from sqlmodel import SQLModel, Field


class Compra(SQLModel, table=True):
    id_producte: int =  Field(default=None, primary_key=True)
    dia: int =  Field(default=None, primary_key=True)
    hora: str =  Field(default=None, primary_key=True)
    cantitat: int

