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



## Modulo Compra


### Creamos una nueva compra, con lo siguientes parametros id, nombre y precio

![Captura de pantalla 2025-05-10 201050](https://github.com/user-attachments/assets/746a2ea7-c1ba-4d19-929d-26fcbfaf884c)
![Captura de pantalla 2025-05-10 201115](https://github.com/user-attachments/assets/1bc2066a-8f77-4028-9c89-8226ee3aabbb)


## Devuelve las compras por id
![Captura de pantalla 2025-05-10 201131](https://github.com/user-attachments/assets/3d33c159-94e1-434a-8988-ef5bf48a8cda)
![Captura de pantalla 2025-05-10 201150](https://github.com/user-attachments/assets/c450ee99-df9a-430b-adca-7a6717a12ad6)


## Actualizamos una compra existent
![Captura de pantalla 2025-05-10 201206](https://github.com/user-attachments/assets/aa180043-3c6c-4aa3-8175-5da6fb926567)
![Captura de pantalla 2025-05-10 201227](https://github.com/user-attachments/assets/ddf93920-8714-4c4d-a33f-54e45a9c9dcf)ç

## Eliminamos una compra existente para la cual necesitmos un id del producto y el dia.

![Captura de pantalla 2025-05-10 201246](https://github.com/user-attachments/assets/f79b9562-5ca9-4ea9-ae17-b32211f8e0c8)
![Captura de pantalla 2025-05-10 201258](https://github.com/user-attachments/assets/9f211596-6648-43e0-b9e9-76c0220eccaf)


## Este get es diferente al otro este lo que hace es devolvernos todas las compras que esten almacenadas en la base de datos
![Captura de pantalla 2025-05-10 201131](https://github.com/user-attachments/assets/e4b27049-a1c0-4629-b198-b251e1739f7c)
![Captura de pantalla 2025-05-10 201150](https://github.com/user-attachments/assets/729219e9-67d0-4a2c-a408-3fa1954e44a1)


## MODULO DE GASTOS


## Creamos un nuevo gasto 

![Captura de pantalla 2025-05-10 201348](https://github.com/user-attachments/assets/c68bad0d-be77-45a4-b710-9dcb3255d369)

![Captura de pantalla 2025-05-10 201401](https://github.com/user-attachments/assets/58211796-03ba-43c6-bbbf-eb4e82de535c)

## Ahora obtendremos los gastos de un empleado especifico en un dia

![Captura de pantalla 2025-05-10 201417](https://github.com/user-attachments/assets/91a60ca5-f2bb-4f15-a579-1a1ffe9aa15a)
![Captura de pantalla 2025-05-10 201432](https://github.com/user-attachments/assets/4ed9a4a7-712f-40d7-95da-29b7370c4474)



## Actulaizamos un gasto exisitente 
![Captura de pantalla 2025-05-10 201456](https://github.com/user-attachments/assets/86c015af-da37-4b78-a356-fc3b64d88191)

![Captura de pantalla 2025-05-10 201509](https://github.com/user-attachments/assets/a1f52e57-c1b9-4869-b227-636ac506b388)

## Borramos un gasto especifico

![image](https://github.com/user-attachments/assets/e61642d0-0cba-49cf-bd3a-53bd0323ddff)


## MODULO MENU


## Creamos un nuevo menu 

![image](https://github.com/user-attachments/assets/50e85bc9-9b57-4b15-a9da-7d3dba6c3156)
![image](https://github.com/user-attachments/assets/187b3aa1-7885-4bf2-94a0-00b88bf6a8df)

## Nos muestra un menu en especifico 
![image](https://github.com/user-attachments/assets/30f6f744-c45d-4977-86ae-a58653d8a0a2)
![image](https://github.com/user-attachments/assets/6e2ea2d2-bdad-4c55-871f-2a168e1c324c)


## En cambio aqui nos muestra todos los menus 
![image](https://github.com/user-attachments/assets/b1ec8fe8-04dd-4061-a0ef-2501267f0e52)
![image](https://github.com/user-attachments/assets/784c87a0-1d91-4713-8d4e-7753302e6e54)


## Actualizar unn menu especifico
![image](https://github.com/user-attachments/assets/06ef70a2-6f9c-4251-bdb4-ed200f283e01)
![image](https://github.com/user-attachments/assets/3f727a17-18f9-4180-a211-9246ce6c7f44)


## Eliminar un menu especifico
![image](https://github.com/user-attachments/assets/4d8fae21-bb13-4896-a8b8-53527808c3de)
![image](https://github.com/user-attachments/assets/3a750d23-1d10-4c3f-981c-7a8b2b5a3799)







