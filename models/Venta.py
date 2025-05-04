from sqlmodel import SQLModel, Field

class Venta(SQLModel, table = True):
    id_reserva: int = Field(primary_key=True) #foreign_key="reserva.id")
    id_menu: int = Field(primary_key=True) # foreign_key="menu.id")
    cantidad: int
