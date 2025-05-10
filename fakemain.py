from fastapi import FastAPI, Depends
from sqlmodel import Session, SQLModel, create_engine
from services import compra, despeses, menu
from dotenv import load_dotenv
from fastapi.staticfiles import StaticFiles
import os

# Crear la instància de FastAPI
app = FastAPI()

# Montar la carpeta "menu" per servir HTML, JS, CSS, etc.
app.mount("/menu", StaticFiles(directory="sge_the_bear_frontend-main/menu"), name="menu")

# Cargar variables de entorno
load_dotenv()

# Obtener la URL de la base de datos desde el archivo .env
DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise ValueError("DATABASE_URL no está definida en el archivo .env")

# Crear el motor de la base de datos
engine = create_engine(DATABASE_URL, echo=True)

# Crear las tablas si no existen
SQLModel.metadata.create_all(engine)

# Dependency para obtener la sesión
def get_db():
    with Session(engine) as db:
        yield db


# Endpoints para Compra

@app.post("/compra/")
def create_compra_view(id_producte: int, dia: int, hora: int, cantidad: int, db: Session = Depends(get_db)):
    return compra.add_compra(id_producte=id_producte, dia=dia, hora=hora, cantidad=cantidad, db=db)


@app.get("/compra/")
def get_compra_view(id_producte: int, dia: int = 1, db: Session = Depends(get_db)):
    return compra.read_compra(id_producte, dia, db)


@app.get("/compres/")
def get_all_compras_view(db: Session = Depends(get_db)):
    return compra.read_all_compras(db=db)


@app.get("/compra/")
def get_ticket_view(id_producte: int, db: Session = Depends(get_db)):
    return compra.read_ticket(id_producte=id_producte, db=db)


@app.put("/compra/")
def update_compra_view(id_producte: int, dia: int, cantidad: int, db: Session = Depends(get_db)):
    return compra.update_compra(id_producte=id_producte, dia=dia, cantidad=cantidad, db=db)


@app.delete("/compra/")
def delete_compra_view(id_producte: int, dia: int, db: Session = Depends(get_db)):
    return compra.delete_compra(id_producte=id_producte, dia=dia, db=db)


@app.post("/despesa/")
def create_despesa_view(id_empleat: int, dia: int, hora: int, cantidad: int, descripcion: str, db: Session = Depends(get_db)):
    return despeses.add_despeses(id_empleat=id_empleat, dia=dia, hora=hora, cantidad=cantidad, descripcion=descripcion, db=db)


@app.get("/despesa/")
def get_despesa_view(id_empleat: int, dia: int, db: Session = Depends(get_db)):
    return despeses.read_despeses(id_empleat=id_empleat, dia=dia, db=db)


@app.put("/despesa/")
def update_despesa_view(id_empleat: int, dia: int, cantidad: int, db: Session = Depends(get_db)):
    return despeses.update_despeses(id_empleat=id_empleat, dia=dia, cantidad=cantidad, db=db)


@app.delete("/despesa/")
def delete_despesa_view(id_empleat: int, dia: int, db: Session = Depends(get_db)):
    return despeses.delete_despeses(id_empleat=id_empleat, dia=dia, db=db)


@app.post("/menu/")
def create_menu_view(id: int, nom: str, preu: float, db: Session = Depends(get_db)):
    return menu.add_menu(id=id, nom=nom, preu=preu, db=db)

@app.get("/menu/{id}")
def get_menu_view(id: int, db: Session = Depends(get_db)):
    return menu.read_menu(id=id, db=db)

@app.get("/menu/")
def get_all_menus_view(db: Session = Depends(get_db)):
    return menu.read_all_menus(db=db)

@app.put("/menu/{id}")
def update_menu_view(id: int, nom: str, preu: float, db: Session = Depends(get_db)):
    return menu.update_menu(id=id, nom=nom, preu=preu, db=db)

@app.delete("/menu/{id}")
def delete_menu_view(id: int, db: Session = Depends(get_db)):
    return menu.delete_menu(id=id, db=db)



