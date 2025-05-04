def schema(reserva) -> dict:
    return {"id":reserva.id,"id_client":reserva.id_client,"id_mesa":reserva.id_mesa,"hora":reserva.hora,"dia":reserva.dia,"mes":reserva.mes,"any":reserva.any}

def schemas(reservas) -> list[dict]:
    return [schema(reserva) for reserva in reservas]
