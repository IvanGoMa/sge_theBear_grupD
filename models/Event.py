from sqlmodel import SQLModel, Field

class Event(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    dia: int = Field(foreign_key="data.dia")
    hora: int = Field(foreign_key="data.hora")
    id_client: int = Field(foreign_key="client.id")  # Relación con Client
    id_empleat: int = Field(foreign_key="empleat.id")  # Relación con Empleat
    descripcio: str