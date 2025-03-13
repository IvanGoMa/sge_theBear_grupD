from sqlalchemy import table
from sqlmodel import SQLModel, Field

class User(SQLModel, table=TRUE):
    id: int = Field(default=None, primary_key=True)
    name: str
    email: str
