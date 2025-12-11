document.addEventListener("DOMContentLoaded", () => {
    const togglePassword = document.querySelector('#togglePassword');
    const passwordInput = document.querySelector('#password');
    const eyeIcon = document.querySelector('.eye-icon');

    // Verificamos que los elementos existan para evitar errores
    if (togglePassword && passwordInput) {
        
        togglePassword.addEventListener('click', function () {
            
            // Verificamos el tipo actual del input
            const type = passwordInput.getAttribute('type') === 'password' ? 'text' : 'password';
            
            // Lo cambiamos
            passwordInput.setAttribute('type', type);

            // (Opcional) Efecto visual al estar activa la contraseña visible
            // Esto añade una clase 'active' al ícono si quieres estilizarlo diferente en CSS
            if (type === 'text') {
                eyeIcon.style.opacity = "1"; // Ojo totalmente visible
                eyeIcon.style.color = "var(--primary)"; // Si fuera SVG inline, se pondría rojo
            } else {
                eyeIcon.style.opacity = "0.5"; // Vuelve a estar gris/tenue
                eyeIcon.style.color = ""; 
            }
        });
    }
});