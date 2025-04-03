from sqlmodel import SQLModel, Field

class Event(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    date: int
    id_client: int = Field(foreign_key="client.id")  # Relación con Client
    id_employee: int = Field(foreign_key="employee.id")  # Relación con Employee
    description: str