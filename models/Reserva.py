from sqlmodel import SQLModel, Field

class Reserva(SQLModel, table = True):
    id: int = Field(primary_key = True)
    id_client: int = Field(foreign_key="client.id")
    id_mesa: int = Field(foreign_key="mesa.id")
    hora: int
    dia: int
    mes: int
    anyo: int




