from sqlmodel import SQLModel, Field

class Data(SQLModel, table = True):
    dia: int = Field(primary_key=True)
    hora: int = Field(primary_key=True)