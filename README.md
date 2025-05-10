# sge_theBear_grupD
projecte the bear sge grup D
##
Model Entitat-Relació
![ModelER.jpeg](ModelER.jpeg)

## Model Relacional
![img.png](img.png)

Cambios:  
Productos se cambia a menú, que tiene: id, primer, segon, postre, preu  
Gasto (no tiene relación): id, descripcio, preu  
Jornada: id_empleat, dia, mes, any, hora_inici, hora_final  
Reserva: id  
Evento: Se quita id empleado y cliente  
Compra (no tiene relación): id, hora, dia, mes, any, producto (string), cantidad, provedor (string), precio  


## Endpoints Reserva
La clau primària de les reserves és l'id, i també tenen l'id del client que reserva, la taula que reserven i l'hora i la data.
### Llegir totes les reserves
![16_read_reservas.png](pics_Jose/16_read_reservas.png)
![17_read_reservas_2.png](pics_Jose/17_read_reservas_2.png)

### Llegir una reserva per id
![18_read_reserva.png](pics_Jose/18_read_reserva.png)

### Crear una reserva introduint tots els camps
![19_add_reserva.png](pics_Jose/19_add_reserva.png)
![20_add_reserva_2.png](pics_Jose/20_add_reserva_2.png)

### Modificar una reserva per id
![21_update_reserva.png](pics_Jose/21_update_reserva.png)
![22_update_reserva_2.png](pics_Jose/22_update_reserva_2.png)

### Esborrar una reserva
![23_delete_reserva.png](pics_Jose/23_delete_reserva.png)


## Endpoints Venda
Una venda té com a clau primària les claus foranes id reserva e id menú. Té com a atribut la quantitat de menús que es venen.

### Llegir totes les vendes
![24_read_ventas.png](pics_Jose/24_read_ventas.png)
![25_read_ventas.png](pics_Jose/25_read_ventas.png)

### Llegir una venda per l'id de la reserva i del menú
![26_read_venta.png](pics_Jose/26_read_venta.png)

### Llegir totes les vendes d'una taula
![27_read_ticket.png](pics_Jose/27_read_ticket.png)

Hem definit una venda com la quantitat d'un menú que es ven en una reserva. Aquest endpoint serveix per poder generar un tiquet,
 ja que ens ensenya tots els menús que s'han venut a una reserva.
### Afegir venda
![28_add_venta.png](pics_Jose/28_add_venta.png)

### Modificar venda
![29_update_ventas.png](pics_Jose/29_update_ventas.png)
![30_update_ventas_2.png](pics_Jose/30_update_ventas_2.png)

### Esborrar venda
![31_delete_ventas.png](pics_Jose/31_delete_ventas.png)


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

## módulo Event

### Creamos un nuevo evento, introduciendo en los campos la información necesaria.
![create_event](./pics_Jose/12-create_event.png)
![create_event](./pics_Jose/12a-create_event.png)
![create_event](./pics_Jose/12b-create_event.png)

### Revisamos que aparece como nuevo evento
![read_event](./pics_Jose/15-read_event.png)
![read_event](./pics_Jose/15a-read_event.png)

### Revisamos todos los eventos
![read_events](./pics_Jose/11-read_events.png)
![read_events](./pics_Jose/11a-read_events.png)

### Actualizaremos un evento
![update_event](./pics_Jose/13-update_event.png)
![update_event](./pics_Jose/13a-update_event.png)

### Eliminaremos un evento
![delete_event](./pics_Jose/14-delete_event.png)
![delete_event](./pics_Jose/14a-delete_event.png)



## Modulo Compra


### Creamos una nueva compra, con lo siguientes parametros id, nombre y precio

![Captura de pantalla 2025-05-10 201050](https://github.com/user-attachments/assets/746a2ea7-c1ba-4d19-929d-26fcbfaf884c)
![Captura de pantalla 2025-05-10 201115](https://github.com/user-attachments/assets/1bc2066a-8f77-4028-9c89-8226ee3aabbb)


## Devuelve todas las compras, es perfecto para obtener una lista de todas las compras realizadas
![Captura de pantalla 2025-05-10 201131](https://github.com/user-attachments/assets/3d33c159-94e1-434a-8988-ef5bf48a8cda)
![Captura de pantalla 2025-05-10 201150](https://github.com/user-attachments/assets/c450ee99-df9a-430b-adca-7a6717a12ad6)


## Consulta una compra por su id








