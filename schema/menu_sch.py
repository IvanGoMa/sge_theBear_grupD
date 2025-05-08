def schema(menu) -> dict:
    return {
        "id": menu.id,
        "nom": menu.nom,
        "preu": menu.preu
    }

def schemas(menus) -> list[dict]:
    return [schema(menu) for menu in menus]
