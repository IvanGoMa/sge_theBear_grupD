from sqlmodel import SQLModel, Field
from datetime import datetime

class Reserva(SQLModel, table = True):
    id: int = Field(primary_key = True)
    id_client: int = Field(foreign_key="client.id")
    id_mesa: int = Field(foreign_key="mesa.id")
    data: datetime = Field(foreign_key = "data.data")




