window.addEventListener("load", function() {
    let menus = JSON.parse(localStorage.getItem("menus")) || [];
    let tableBody = document.querySelector("#menuTable tbody");

    menus.forEach(menu => {
        let row = document.createElement("tr");

        row.innerHTML = `
            <td>${menu.id}</td>
            <td>${menu.nombre}</td>
            <td>${menu.descripcion}</td>
            <td>${menu.precio}</td>
        `;

        tableBody.appendChild(row);
    });
});
