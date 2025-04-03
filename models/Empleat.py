from sqlmodel import SQLModel, Field

class Empleat(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    fullName: str
    phone: int
    position: str   #cargo
