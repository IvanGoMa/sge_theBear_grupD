from sqlmodel import SQLMODEL,Field

class user(SQLMODEL, table=True):
    id:int = Field(default=None, primary_key=True)
    name: str
    email: str