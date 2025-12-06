/* scripts/profile-dropdown.js */

document.addEventListener("DOMContentLoaded", () => {
    const dropdownBtn = document.querySelector(".dropdown-btn");
    const dropdownMenu = document.querySelector(".profile-dropdown");
    const container = document.querySelector(".profile-container");

    // 1. Alternar visibilidad al hacer clic en el botón
    dropdownBtn.addEventListener("click", (e) => {
        e.stopPropagation(); // Evita que el click llegue al document
        dropdownMenu.classList.toggle("active");
        
        // Opcional: Rotar la flechita
        dropdownBtn.classList.toggle("active");
    });

    // 2. Cerrar si se hace clic fuera del contenedor del perfil
    document.addEventListener("click", (e) => {
        if (!container.contains(e.target)) {
            dropdownMenu.classList.remove("active");
            dropdownBtn.classList.remove("active");
        }
    });
});