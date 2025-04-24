from pandas.plotting import table
from sqlmodel import SQLModel, Field

class Jornada(SQLModel, table=True):
    id_empleat: int = Field(foreign_key="empleat.id", primary_key=True)
    dia: int  = Field(foreign_key="data.dia", primary_key=True)
    mes: int = Field(foreign_key="data.mes", primary_key=True)
    any: int = Field(foreign_key="data.any", primary_key=True)
    hora_inici: int = Field(foreign_key="data.dia", primary_key=True)
    hora_fi: int = Field(foreign_key="hora.dia")