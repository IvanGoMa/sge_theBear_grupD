// URL del endpoint de la API
const API_URL = "http://localhost:8000/get_all_clients";

// Función para obtener los datos de los usuarios
async function fetchUsers() {
    try {
        const response = await fetch(API_URL);
        if (!response.ok) {
            throw new Error(`Error en la solicitud: ${response.status}`);
        }
        const clients = await response.json(); // Convertimos la respuesta a JSON
        displayUsers(clients); // Mostramos los datos en la tabla
        //console.log(users)
    } catch (error) {
        console.error("Error al obtener los clientes:", error);
    }
}

// Función para mostrar los clientes en la tabla
function displayUsers(clients) {
    const tableBody = document.querySelector("#clientsTable tbody");

    // Limpiamos el contenido actual de la tabla
    tableBody.innerHTML = "";

    // Iteramos sobre la lista de clientes y creamos las filas de la tabla
    users.forEach(cliente => {
        const row = document.createElement("tr");

        // Creamos las celdas para cada campo del cliente
        const idCell = document.createElement("td");
        idCell.textContent = cliente.cliente.id;
        row.appendChild(idCell);

        const nomcompletCell = document.createElement("td");
        nomcompletCell.textContent = cliente.cliente.nomcomplet;
        row.appendChild(nomcompletCell);

        const telefonoCell = document.createElement("td");
        telefonoCell.textContent = cliente.cliente.telefono;
        row.appendChild(telefonoCell);

        // Añadimos la fila a la tabla
        tableBody.appendChild(row);
    });
}

// Llamamos a la función para obtener y mostrar los usuarios cuando la página se carga
document.addEventListener("DOMContentLoaded", fetchUsers);