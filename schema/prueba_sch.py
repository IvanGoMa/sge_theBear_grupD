def prueba_schema(prueba) -> dict:
    response = {"prueba":prueba}
    return response


def pruebas_schema(pruebas) -> list[dict]:
    response = [prueba_schema(prueba) for prueba in pruebas]
    return response