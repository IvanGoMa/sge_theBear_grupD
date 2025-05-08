from sqlmodel import SQLModel, Field

class Jornada(SQLModel, table=True):
    id_empleat: int = Field(foreign_key="empleat.id", primary_key=True)
    dia: int = Field(primary_key=True)
    mes: int = Field( primary_key=True)
    any: int = Field(primary_key=True)
    hora_inici: int = Field(nullable=True) #si és null no treballa
    hora_fi: int = Field(nullable=True) #si és null no treballa