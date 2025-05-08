def despesa_schema(despesa) -> dict:
    return {
        "id_empleat": despesa.id_empleat,
        "dia": despesa.dia,
        "hora": despesa.hora,
        "cantitat": despesa.cantitat,
        "description": despesa.description
    }

def despeses_schema(despeses) -> list[dict]:
    return [despesa_schema(despesa) for despesa in despeses]
