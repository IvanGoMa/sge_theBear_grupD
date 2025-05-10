document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('empleadoForm');
    const messageDiv = document.getElementById('message');

    form.addEventListener('submit', async (e) => {
        e.preventDefault();

        // Obtenir valors del formulari
        const nomcomplet = document.getElementById('nomcomplet').value.trim();
        const telefono = document.getElementById('telefono').value.trim();
        const cargo = parseInt(document.getElementById('cargo').value);

         try {
            // Enviar dades al servidor amb body JSON
            const response = await fetch('http://localhost:8000/empleats/create/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Accept': 'application/json'
                },
                body: JSON.stringify({
                    nomcomplet: nomcomplet,
                    telefono: telefono,
                    cargo: cargo
                })
            });

            if (response.ok) {
                showMessage('Empleat creat correctament!', 'success');
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