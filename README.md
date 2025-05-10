# sge_theBear_grupD
projecte the bear sge grup D

![img.png](img.png)

Cambios: 
Productos se cambia a menú, que tiene: id, primer, segon, postre, preu
Gasto (no tiene relación): id, descripcio, preu
Jornada: id_empleat, dia, mes, any, hora_inici, hora_final
Reserva: id
Evento: Se quita id empleado y cliente
Compra (no tiene relación): id, hora, dia, mes, any, producto (string), cantidad, provedor (string), precio

## módulos Empleat, Client y Event

![vista general](./pics_Jose/1.png)

## módulo Empleat

### Creamos un nuevo empleado, introduciendo en los campos la información necesaria.
![create_empleat](./pics_Jose/3-create_empleat.png)

### Revisamos que aparece cómo nuevo empleado
![read_empleat](./pics_Jose/5-read_empleat.png)

### Revisamos todos los empleados
![read_empleats](./pics_Jose/2a-read_empleats.png)

### Actualizaremos un empleado
![update_empleat](./pics_Jose/4-update_empleat.png)

### Eliminaremos un empleado
![delete_empleat](./pics_Jose/6-delete_empleat.png)

## módulo Client

### Creamos un nuevo cliente, introduciendo en los campos la información necesaria.
![create_client](./pics_Jose/7-create_client.png)

### Revisamos todos los clientes
![read_clients](./pics_Jose/8-read_clients.png)

### Actualizaremos un cliente
![update_client](./pics_Jose/9-update_client.png)

### Eliminaremos un cliente
![delete_client](./pics_Jose/10_delete_client.png)