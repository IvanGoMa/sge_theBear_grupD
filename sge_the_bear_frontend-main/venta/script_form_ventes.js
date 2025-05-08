document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('ventaForm');
    const messageDiv = document.getElementById('message');

    form.addEventListener('submit', async (e) => {
        e.preventDefault();

        // Obtenir valors del formulari
        const id_reserva = parseInt(document.getElementById('id_reserva').value);
        const id_menu = parseInt(document.getElementById('id_menu').value);
        const cantidad = parseInt(document.getElementById('cantidad').value);

         try {
            // Enviar dades al servidor amb body JSON
            const response = await fetch('http://localhost:8000/add_ventas/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Accept': 'application/json'
                },
                body: JSON.stringify({
                    id_reserva: id_reserva,
                    id_menu: id_menu,
                    cantidad: cantidad
                })
            });

            if (response.ok) {
                showMessage('Venta creada correctament!', 'success');
                form.reset(); // Netejar el formulari
            } else {
                showMessage(`Error: ${data.detail || 'Error desconegut'}`, 'error');
            }
        } catch (error) {
            showMessage(`Error de connexió: ${error.message}`, 'error');
        }
    });

    function showMessage(text, type) {
        messageDiv.textContent = text;
        messageDiv.className = 'message ' + type;
    }
});