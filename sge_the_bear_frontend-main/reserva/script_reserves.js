// URL del endpoint de la API
const API_URL = "http://localhost:8000/get_reservas";

// Función para obtener los datos de los usuarios
async function fetchUsers() {
    try {
        const response = await fetch(API_URL);
        if (!response.ok) {
            throw new Error(`Error en la solicitud: ${response.status}`);
        }
        const reservas = await response.json(); // Convertimos la respuesta a JSON
        displayUsers(reservas); // Mostramos los datos en la tabla
        //console.log(users)
    } catch (error) {
        console.error("Error al obtener los usuarios:", error);
    }
}

// Función para mostrar los usuarios en la tabla
function displayUsers(reservas) {
    const tableBody = document.querySelector("#reservasTable tbody");

    // Limpiamos el contenido actual de la tabla
    tableBody.innerHTML = "";

    // Iteramos sobre la lista de usuarios y creamos las filas de la tabla
    users.forEach(user => {
        const row = document.createElement("tr");

        // Creamos las celdas para cada campo del usuario
        const id = document.createElement("td");
        id.textContent = reservas.reservas.id;
        row.appendChild(id);

        const id_client = document.createElement("td");
        id_client.textContent = reservas.reservas.id_client;
        row.appendChild(id_client);

        const id_mesa = document.createElement("td");
        id_mesa.textContent = reservas.reservas.id_mesa;
        row.appendChild(id_mesa);

        const hora = document.createElement("td");
        hora.textContent = reservas.reservas.hora;
        row.appendChild(hora);

        const dia = document.createElement("td");
        dia.textContent = reservas.reservas.dia;
        row.appendChild(dia);

        const mes = document.createElement("td");
        mes.textContent = reservas.reservas.mes;
        row.appendChild(mes);

        const any = document.createElement("td");
        any.textContent = reservas.reservas.any;
        row.appendChild(any);

        // Añadimos la fila a la tabla
        tableBody.appendChild(row);
    });
}

// Llamamos a la función para obtener y mostrar los usuarios cuando la página se carga
document.addEventListener("DOMContentLoaded", fetchUsers);