document.addEventListener('DOMContentLoaded', () => {
    // Seleccionem el mòdul d'usuaris
    const usersModule = document.getElementById('usersModule');
    // Seleccionem el mòdul de reserves
    const reservasModule = document.getElementById('reservasModule');


    // Users
    // Afegim event listener per al clic
    usersModule.addEventListener('click', () => {
        // Redireccionem a la pàgina del formulari
        window.location.href = '/ususaris/index_form.html';
    });

    // Opcional: Afegir efecte al passar el ratolí
    usersModule.addEventListener('mouseenter', () => {
        usersModule.style.borderColor = '#714B67';
    });

    usersModule.addEventListener('mouseleave', () => {
        usersModule.style.borderColor = '#e0e0e0';
    });


    // Reserves
    // Afegim event listener per al clic
    reservesModule.addEventListener('click', () => {
        // Redireccionem a la pàgina del formulari
        window.location.href = './reserva/reserves_form.html';
    });

    // Opcional: Afegir efecte al passar el ratolí
    reservesModule.addEventListener('mouseenter', () => {
        reservesModule.style.borderColor = '#714B67';
    });

    reservesModule.addEventListener('mouseleave', () => {
       reservesModule.style.borderColor = '#e0e0e0';
    });


    // Vendes
    // Afegim event listener per al clic
    ventesModule.addEventListener('click', () => {
        // Redireccionem a la pàgina del formulari
        window.location.href = './venta/ventes_form.html';
    });

    // Opcional: Afegir efecte al passar el ratolí
    ventesModule.addEventListener('mouseenter', () => {
        ventesModule.style.borderColor = '#714B67';
    });

    ventesModule.addEventListener('mouseleave', () => {
       ventesModule.style.borderColor = '#e0e0e0';
    });
});