from sqlmodel import SQLModel, Field

class Jornada(SQLModel, table = True):
    id_cliente: int = Field(foreign_key="")