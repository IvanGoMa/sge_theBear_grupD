from sqlmodel import SQLModel, Field
from datetime import datetime

class Prueba(SQLModel, table = True):
    data: datetime = Field(primary_key = True)

