from sqlmodel import SQLModel, Field

class Data(SQLModel, table = True):
    any: int = Field(primary_key=True)
    mes: int = Field(primary_key=True)
    dia: int = Field(primary_key=True)
    hora: int = Field(primary_key=True)