document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('eventForm');
    const messageDiv = document.getElementById('message');

    form.addEventListener('submit', async (e) => {
        e.preventDefault();

        // Obtenir valors del formulari
        const dia = document.getElementById('dia').value.trim();
        const hora = document.getElementById('hora').value.trim();
        const mes = document.getElementById('mes').value.trim();
        const anyo = document.getElementById('anyo').value.trim();
        const descripcio = document.getElementById('descripcio').value.trim();

         try {
            // Enviar dades al servidor amb body JSON
            const response = await fetch('http://localhost:8000/events/create/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Accept': 'application/json'
                },
                body: JSON.stringify({
                    dia: dia,
                    hora: hora,
                    mes: mes,
                    anyo: anyo,
                    descripcio: descripcio,
                })
            });

            if (response.ok) {
                showMessage('Event creat correctament!', 'success');
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