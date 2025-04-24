from sqlmodel import SQLModel, Field

class Mesa(SQLModel, table = True):
    id: int = Field(primary_key=True)
    capacitat: int