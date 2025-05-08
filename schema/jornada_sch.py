def schema(jornada) -> dict:
    return {"id_empleat":jornada.id_empleat, "dia":jornada.dia, "mes":jornada.mes, "any":jornada.any, "hora_inici":jornada.hora_inici, "hora_fi":jornada.hora_fi}

def schemas(jornades) -> list[dict]:
    return [schema(jornada) for jornada in jornades]