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
### Tiene la id como clave primaria así como nombre completo, teléfono y cargo como datos.
![create_empleat](./pics_Jose/3-create_empleat.png)

### Revisamos que aparece cómo nuevo empleado por id
![read_empleat](./pics_Jose/5-read_empleat.png)

### Revisamos todos los empleados
![read_empleats](./pics_Jose/2a-read_empleats.png)

### Actualizaremos un empleado por id
![update_empleat](./pics_Jose/4-update_empleat.png)

### Eliminaremos un empleado por id
![delete_empleat](./pics_Jose/6-delete_empleat.png)

## módulo Client

### Creamos un nuevo cliente, introduciendo en los campos la información necesaria.
### Tiene la id como clave primaria así como nombre completo, teléfono como datos.
![create_client](./pics_Jose/7-create_client.png)
 
### Revisamos que aparece el nuevo cliente por id
![read_client](./pics_Jose/8a-read_cliente.png)
![read_client](./pics_Jose/8b-read_cliente.png)

### Revisamos todos los clientes
![read_clients](./pics_Jose/8-read_clients.png)

### Actualizaremos un cliente por id
![update_client](./pics_Jose/9-update_client.png)

### Eliminaremos un cliente por id
![delete_client](./pics_Jose/10_delete_client.png)

## módulo Event

### Creamos un nuevo evento, introduciendo en los campos la información necesaria.
### Tiene la id como clave primaria así como día, hora, mes, año y descripción como datos.
![create_event](./pics_Jose/12-create_event.png)
![create_event](./pics_Jose/12a-create_event.png)
![create_event](./pics_Jose/12b-create_event.png)

### Revisamos que aparece como nuevo evento por id
![read_event](./pics_Jose/15-read_event.png)
![read_event](./pics_Jose/15a-read_event.png)

### Revisamos todos los eventos
![read_events](./pics_Jose/11-read_events.png)
![read_events](./pics_Jose/11a-read_events.png)

### Actualizaremos un evento por id
![update_event](./pics_Jose/13-update_event.png)
![update_event](./pics_Jose/13a-update_event.png)

### Eliminaremos un evento por id
![delete_event](./pics_Jose/14-delete_event.png)
![delete_event](./pics_Jose/14a-delete_event.png)