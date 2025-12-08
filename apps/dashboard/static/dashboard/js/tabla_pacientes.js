window.renderMainChart = function () {
    const div = document.getElementById("tabla_pacientes");
    if (!div) return;

    const tabla = JSON.parse(div.dataset.pacientes || `[]`);

    const tableBody = div.querySelector("tbody");

    tabla.forEach(paciente => {
        const row = document.createElement("tr");
        const cellNombre = document.createElement("td");
        cellNombre.textContent = paciente.nombre;
        row.appendChild(cellNombre);
        const cellEdad = document.createElement("td");
        cellEdad.textContent = paciente.edad;
        row.appendChild(cellEdad);
    
    });

        


}