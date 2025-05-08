def schema(mesa) -> dict:
    return {"id":mesa.id, "capacitat":mesa.capacitat}

def schemas(meses) -> list[dict]:
    return [schema(mesa) for mesa in meses]