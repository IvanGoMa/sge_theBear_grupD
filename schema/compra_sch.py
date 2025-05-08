def schema(compra) -> dict:
    return {
        "id_producte": compra.id_producte,
        "dia": compra.dia,
        "hora": compra.hora,
        "cantitat": compra.cantitat
    }

def schemas(compras) -> list[dict]:
    return [schema(compra) for compra in compras]
