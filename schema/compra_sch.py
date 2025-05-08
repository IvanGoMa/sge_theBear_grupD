def compra_schema(compra) -> dict:
    return {
        "id_producte": compra.id_producte,
        "dia": compra.dia,
        "hora": compra.hora,
        "cantitat": compra.cantitat
    }

def compres_schema(compres) -> list[dict]:
    return [compra_schema(compra) for compra in compres]
