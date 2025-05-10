from sqlmodel import SQLModel, Field


class Despesa(SQLModel, table=True):
    id_empleat: int = Field(default=None, primary_key=True)
    dia: int = Field(default=None, primary_key=True)
    hora: int = Field(default=None, primary_key=True)
    cantitat: int
    description: str