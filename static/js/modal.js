/* =========================================
   LÓGICA UNIVERSAL DE MODALES (AJAX)
   ========================================= */

document.addEventListener('DOMContentLoaded', function() {
    
    // Referencias al DOM (Asumiendo que el esqueleto existe en el HTML)
    const modalOverlay = document.getElementById('modalUniversal');
    const modalContent = document.getElementById('contenidoModal');
    const closeModalBtns = document.querySelectorAll('.btn-close-modal');

    // Función Global: Abrir Modal
    // Se puede llamar desde cualquier onclick="abrirModal('/ruta/')"
    window.abrirModal = function(url) {
        if (!modalOverlay || !modalContent) {
            console.error("Error: No se encontró el esqueleto del modal en el HTML.");
            return;
        }

        // 1. Mostrar Modal y Spinner
        modalOverlay.classList.add('active');
        modalContent.innerHTML = `
            <div style="display:flex; flex-direction:column; align-items:center; justify-content:center; padding:3rem;">
                <div class="loader-spinner" style="border: 4px solid #f3f3f3; border-top: 4px solid #3498db; border-radius: 50%; width: 40px; height: 40px; animation: spin 1s linear infinite;"></div>
                <p style="margin-top:1rem; color:#666;">Cargando información...</p>
            </div>
            <style>@keyframes spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }</style>
        `;

        // 2. Fetch AJAX a Django
        fetch(url)
            .then(response => {
                if (!response.ok) throw new Error('Error en la red');
                return response.text();
            })
            .then(html => {
                // 3. Inyectar HTML recibido
                modalContent.innerHTML = html;
            })
            .catch(error => {
                console.error('Error:', error);
                modalContent.innerHTML = `
                    <div style="text-align:center; padding: 2rem; color: #e74c3c;">
                        <h3>⚠️ Error al cargar</h3>
                        <p>No se pudo obtener la información. Intente nuevamente.</p>
                    </div>
                `;
            });
    };

    // Función Global: Cerrar Modal
    window.cerrarModal = function() {
        if (modalOverlay) {
            modalOverlay.classList.remove('active');
            // Limpiamos el contenido después de la animación (300ms)
            setTimeout(() => {
                modalContent.innerHTML = '';
            }, 300);
        }
    };

    // Event Listeners para cerrar
    closeModalBtns.forEach(btn => {
        btn.addEventListener('click', cerrarModal);
    });

    // Cerrar al hacer click fuera (en el overlay oscuro)
    if (modalOverlay) {
        modalOverlay.addEventListener('click', function(e) {
            if (e.target === modalOverlay) {
                cerrarModal();
            }
        });
    }
});