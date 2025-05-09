document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('reservaForm');
    const messageDiv = document.getElementById('message');

    form.addEventListener('submit', async (e) => {
        e.preventDefault();

        // Obtenir valors del formulari
        const id = parseInt(document.getElementById('id').value);
        const id_client = parseInt(document.getElementById('id_client').value);
        const id_mesa = parseInt(document.getElementById('id_mesa').value);
        const hora = parseInt(document.getElementById('hora').value);
        const dia = parseInt(document.getElementById('dia').value);
        const mes = parseInt(document.getElementById('mes').value);
        const any = parseInt(document.getElementById('any').value);

         try {
            // Enviar dades al servidor amb body JSON
            const response = await fetch('http://localhost:8000/add_reservas/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Accept': 'application/json'
                },
                body: JSON.stringify({
                    id: id,
                    id_client: id_client,
                    id_mesa: id_mesa,
                    hora: hora,
                    dia: dia,
                    mes: mes,
                    any: any
                })
            });

            if (response.ok) {
                showMessage('Reserva creada correctament!', 'success');
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