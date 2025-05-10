def schema(despesa) -> dict:
    return {
        "id_empleat": despesa.id_empleat,
        "dia": despesa.dia,
        "hora": despesa.hora,
        "cantitat": despesa.cantitat,
        "description": despesa.description
    }

def schemas(despeses) -> list[dict]:
    return [schema(despesa) for despesa in despeses]

