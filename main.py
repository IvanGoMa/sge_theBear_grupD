from fastapi import FastAPI, Depends, HTTPException
from sqlmodel import SQLModel, create_engine, Session, Field, select
from dotenv import load_dotenv
import os

# Cargar variables de entorno
load_dotenv()

# Obtener la URL de la base de datos desde .env
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("Error: La variable de entorno DATABASE_URL no está definida")

# Configurar conexión a PostgreSQL
engine = create_engine(DATABASE_URL)

# Crear la base de datos si no existe
SQLModel.metadata.create_all(engine)

app = FastAPI()


def get_db():
    db = Session(engine)
    try:
        yield db
    finally:
        db.close()


class User(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    email: str


@app.get("/users/")
def read_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users


@app.post("/users/")
def create_user(name: str, email: str, db: Session = Depends(get_db)):
    db_user = User(name=name, email=email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@app.put("/update_user/{id}", response_model=dict)
async def update_user_endpoint(id: int, name: str, db: Session = Depends(get_db)):
    return update_user(id, name, db)

@app.delete("/user/delete/{id}", response_model=dict)
async def delete_user_endpoint(id: int, db: Session = Depends(get_db)):
    return delete_user(id, db)


