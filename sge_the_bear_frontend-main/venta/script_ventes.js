// URL del endpoint de la API
const API_URL = "http://localhost:8000/get_ventas";

// Función para obtener los datos de los usuarios
async function fetchUsers() {
    try {
        const response = await fetch(API_URL);
        if (!response.ok) {
            throw new Error(`Error en la solicitud: ${response.status}`);
        }
        const ventas = await response.json(); // Convertimos la respuesta a JSON
        displayUsers(ventas); // Mostramos los datos en la tabla
        //console.log(users)
    } catch (error) {
        console.error("Error al obtener los usuarios:", error);
    }
}

// Función para mostrar los usuarios en la tabla
function displayUsers(ventas) {
    const tableBody = document.querySelector("#ventasTable tbody");

    // Limpiamos el contenido actual de la tabla
    tableBody.innerHTML = "";

    // Iteramos sobre la lista de usuarios y creamos las filas de la tabla
    users.forEach(user => {
        const row = document.createElement("tr");

        // Creamos las celdas para cada campo del usuario
        const id_reserva = document.createElement("td");
        id_reserva.textContent = ventas.ventas.id_reserva;
        row.appendChild(id_reserva);

        const id_menu = document.createElement("td");
        id_menu.textContent = ventas.ventas.id_menu;
        row.appendChild(id_menu);

        const cantidad = document.createElement("td");
        cantidad.textContent = ventas.ventas.cantidad;
        row.appendChild(cantidad);


        // Añadimos la fila a la tabla
        tableBody.appendChild(row);
    });
}

// Llamamos a la función para obtener y mostrar los usuarios cuando la página se carga
document.addEventListener("DOMContentLoaded", fetchUsers);