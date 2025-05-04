def schema(venta) -> dict:
    return {"id_reserva":venta.id_reserva,"id_menu":venta.id_menu, "cantidad":venta.cantidad}

def schemas(ventas) -> list[dict]:
    return [schema(venta) for venta in ventas]
