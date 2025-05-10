// URL del endpoint de la API
const API_URL = "http://localhost:8000/get_all_empleats";

// Función para obtener los datos de los usuarios
async function fetchUsers() {
    try {
        const response = await fetch(API_URL);
        if (!response.ok) {
            throw new Error(`Error en la solicitud: ${response.status}`);
        }
        const empleats = await response.json(); // Convertimos la respuesta a JSON
        displayUsers(empleats); // Mostramos los datos en la tabla
        //console.log(users)
    } catch (error) {
        console.error("Error al obtener los empleados:", error);
    }
}

// Función para mostrar los empleados en la tabla
function displayUsers(empleats) {
    const tableBody = document.querySelector("#empleatsTable tbody");

    // Limpiamos el contenido actual de la tabla
    tableBody.innerHTML = "";

    // Iteramos sobre la lista de empleados y creamos las filas de la tabla
    users.forEach(empleat => {
        const row = document.createElement("tr");

        // Creamos las celdas para cada campo del empleado
        const idCell = document.createElement("td");
        idCell.textContent = empleat.empleat.id;
        row.appendChild(idCell);

        const nomcompletCell = document.createElement("td");
        nomcompletCell.textContent = empleat.empleat.nomcomplet;
        row.appendChild(nomcompletCell);

        const telefonoCell = document.createElement("td");
        telefonoCell.textContent = empleat.empleat.telefono;
        row.appendChild(telefonoCell);

        const cargoCell = document.createElement("td");
        cargoCell.textContent = empleat.empleat.cargo;
        row.appendChild(cargoCell);

        // Añadimos la fila a la tabla
        tableBody.appendChild(row);
    });
}

// Llamamos a la función para obtener y mostrar los usuarios cuando la página se carga
document.addEventListener("DOMContentLoaded", fetchUsers);