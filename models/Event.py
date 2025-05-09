from sqlmodel import SQLModel, Field

class Event(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    dia: int #= Field(foreign_key="data.dia")
    hora: int #= Field(foreign_key="data.hora")
    mes: int
    any: int
    descripcio: str