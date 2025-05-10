// URL del endpoint de la API
const API_URL = "http://localhost:8000/get_all_events";

// Función para obtener los datos de los eventos
async function fetchUsers() {
    try {
        const response = await fetch(API_URL);
        if (!response.ok) {
            throw new Error(`Error en la solicitud: ${response.status}`);
        }
        const events = await response.json(); // Convertimos la respuesta a JSON
        displayUsers(events); // Mostramos los datos en la tabla
        //console.log(users)
    } catch (error) {
        console.error("Error al obtener los eventos:", error);
    }
}

// Función para mostrar los eventos en la tabla
function displayUsers(events) {
    const tableBody = document.querySelector("#eventsTable tbody");

    // Limpiamos el contenido actual de la tabla
    tableBody.innerHTML = "";

    // Iteramos sobre la lista de eventos y creamos las filas de la tabla
    users.forEach(event => {
        const row = document.createElement("tr");

        // Creamos las celdas para cada campo del evento
        const idCell = document.createElement("td");
        idCell.textContent = event.event.id;
        row.appendChild(idCell);

        const diaCell = document.createElement("td");
        diaCell.textContent = event.event.dia;
        row.appendChild(diaCell);

        const horaCell = document.createElement("td");
        horaCell.textContent = event.event.hora;
        row.appendChild(horaCell);

        const mesCell = document.createElement("td");
        mesCell.textContent = event.event.mes;
        row.appendChild(mesCell);

        const anyoCell = document.createElement("td");
        anyoCell.textContent = event.event.anyo;
        row.appendChild(anyoCell);

        const descripcioCell = document.createElement("td");
        descripcioCell.textContent = empleado.empleado.descripcio;
        row.appendChild(descripcioCell);

        // Añadimos la fila a la tabla
        tableBody.appendChild(row);
    });
}

// Llamamos a la función para obtener y mostrar los usuarios cuando la página se carga
document.addEventListener("DOMContentLoaded", fetchUsers);