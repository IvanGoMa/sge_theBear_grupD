from typing import List
from fastapi import FastAPI, Depends
from services import compra, despeses, menu
from sqlmodel import SQLModel, create_engine, Session, select
from dotenv import load_dotenv
import os

# Cargar variables de entorno
load_dotenv()

app = FastAPI()

# 1. Obtener la URL de la base de datos desde el archivo .env
DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise ValueError("DATABASE_URL no está definida en el archivo .env")

# 2. Crear el motor de la base de datos
engine = create_engine(DATABASE_URL, echo=True)  # echo=True para ver las consultas SQL en consola

# 3. Crear las tablas en la base de datos (si aún no están creadas)
SQLModel.metadata.create_all(engine)

# 4. Función para obtener una sesión de base de datos
def get_db():
    with Session(engine) as db:  # Usar "with" para garantizar que la sesión se cierre correctamente
        yield db

