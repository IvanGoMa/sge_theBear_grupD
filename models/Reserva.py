from sqlmodel import SQLModel, Field

class Reserva(SQLModel, table = True):
    id_client: int = (foreign_key=True)
    id_mesa: int = (foreign_key=True)
    dia: int
    hora: int




