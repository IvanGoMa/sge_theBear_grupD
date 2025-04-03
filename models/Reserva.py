from sqlmodel import SQLModel, Field

class Reserva(SQLModel, table = True):
    id: int = Field(default=None, primary_key=True)
    date: date
    time: time
    id_table:int = (foreign_key=True)
    id_client: int = (foreign_key=True)


