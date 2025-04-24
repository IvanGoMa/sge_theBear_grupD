from sqlmodel import SQLModel, Field

class Jornada(SQLModel, table=True):
    id_empleat: int = Field(foreign_key="empleat.id", primary_key=True)
    dia_inici: int = Field(foreign_key="data.dia", primary_key=True)
    hora_inici: int = Field(foreign_key="data.hora", primary_key=True)
    dia_fi: int = Field(foreign_key="data.dia")
    hora_fi: int = Field(foreign_key="hora.dia")