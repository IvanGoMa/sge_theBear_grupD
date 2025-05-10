document.getElementById("menuForm").addEventListener("submit", function(event) {
    event.preventDefault();

    const menu = {
        id: document.getElementById("id").value,
        nombre: document.getElementById("nombre").value,
        descripcion: document.getElementById("descripcion").value,
        precio: document.getElementById("precio").value
    };

    let menus = JSON.parse(localStorage.getItem("menus")) || [];
    menus.push(menu);
    localStorage.setItem("menus", JSON.stringify(menus));

    document.getElementById("message").innerHTML = "<div class='success'>Menú creado exitosamente</div>";
    document.getElementById("menuForm").reset();
});
