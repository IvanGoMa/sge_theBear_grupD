from sqlmodel import SQLModel, Field

class Venta(SQLModel, table = True):
    id: