window.renderKpiProfesional1 = function () {
    const el = document.getElementById("kpi_profesional_1");
    if (!el) return;

    const valor = el.dataset.value || 10;
    el.innerHTML = valor;
};

window.renderKpiProfesional2 = function () {
    const el = document.getElementById("kpi_profesional_2");
    if (!el) return;

    const valor = el.dataset.value || 30;
    el.innerHTML = valor;
};

window.renderKpiProfesional3 = function () {
    const el = document.getElementById("kpi_profesional_3");
    if (!el) return;
    const valor = el.dataset.value || 15;
    el.innerHTML = valor;
};
/* helper para color segun tema */
function getChartTextColor() {
    return document.body.classList.contains('dark') ? '#ffffff' : '#000000';
}


/* graficos */
window.renderChartProfesional1 = function () {
    const div = document.getElementById("chart_profesional_1");
    if (!div) return;

    const meses = JSON.parse(div.dataset.meses || `["Ene","Feb","Mar","Abr","May","Jun","Jul","Ago","Sep","Oct","Nov","Dic"]`);
    const valores = JSON.parse(div.dataset.values || `[10,20,30,50,100]`);

    const chart = echarts.init(div);

    const palette = ['#5470C6', '#91CC75', '#EE6666', '#FAC858', '#73C0DE', '#3BA272', '#E062AE'];
    const textColor = getChartTextColor();

    const option = {
        textStyle: { color: textColor },
        tooltip: { 
            trigger: "axis",
            textStyle: { color: textColor }
        },
        xAxis: { type: "category", data: meses, axisLabel: { color: textColor } },
        yAxis: { type: "value", axisLabel: { color: textColor } },
        series: [{
            type: "bar",
            data: valores,
            itemStyle: {
                color: function(params) {
                    return palette[params.dataIndex % palette.length];
                }
            },
            label: {
                show: true,
                position: 'top',
                color: textColor
            }
        }],
        legend: { textStyle: { color: textColor } },
        color: palette
    };

    chart.setOption(option);
    chart.resize();
};

window.renderChartProfesional2 = function () {
    const div = document.getElementById("chart_profesional_2");
    if (!div) return;

    const meses = JSON.parse(div.dataset.meses || `["Ene","Feb","Mar"]`);
    const valores = JSON.parse(div.dataset.values || `[10,20,30]`);

    const chart = echarts.init(div);

    const palette = ['#73C0DE', '#5470C6', '#91CC75', '#EE6666', '#FAC858'];
    const textColor = getChartTextColor();

    const option = {
        textStyle: { color: textColor },
        tooltip: { trigger: "axis", textStyle: { color: textColor } },
        xAxis: { type: "category", data: meses, axisLabel: { color: textColor } },
        yAxis: { type: "value", axisLabel: { color: textColor } },
        series: [{
            type: "bar",
            data: valores,
            itemStyle: {
                color: function(params) {
                    return palette[params.dataIndex % palette.length];
                }
            },
            label: {
                show: true,
                position: 'top',
                color: textColor
            }
        }],
        legend: { textStyle: { color: textColor } },
        color: palette
    };

    chart.setOption(option);
    chart.resize();
};

window.renderChartProfesional3 = function () {
    const div = document.getElementById("chart_profesional_3");
    if (!div) return;

    const labels = JSON.parse(div.dataset.labels || `["Hemorragia", "Preeclampsia", "Infección", "profesional Prematuro", "Otros"]`);
    const values = JSON.parse(div.dataset.values || `[15, 8, 12, 5, 10]`);

    const chart = echarts.init(div);

    const palette = ['#EE6666', '#5470C6', '#91CC75', '#FAC858', '#73C0DE'];
    const textColor = getChartTextColor();

    const pieData = labels.map((name, i) => ({ value: values[i] || 0, name }));

    const option = {
        textStyle: { color: textColor },
        tooltip: { trigger: 'item', textStyle: { color: textColor } },
        legend: { orient: 'vertical', left: 'left', textStyle: { color: textColor } },
        color: palette,
        series: [
          {
            name: 'Complicaciones',
            type: 'pie',
            radius: '50%',
            data: pieData,
            emphasis: {
              itemStyle: {
                shadowBlur: 10,
                shadowOffsetX: 0,
                shadowColor: 'rgba(0, 0, 0, 0.5)'
              }
            },
            label: {
              formatter: '{b}: {c} ({d}%)',
              color: textColor
            }
          }
        ]
    };
    chart.setOption(option);
    chart.resize();
};




/* tabla */
window.renderTableProfesional = function () {
    const tbody = document.getElementById("tabla_profesional");
    if (!tbody) return;

    let tabla = [];
    try {
        tabla = JSON.parse(tbody.dataset.value || '[{"Nombre":"Dr. Juan","Area":"Pabellon","Especialidad":"Matron","Apgar":5}]');
    } catch (e) {
        console.error('Error parseando tabla_profesional dataset:', e);
        tabla = [];
    }

    tbody.innerHTML = '';

    tabla.forEach(profesional => {
        const row = document.createElement("tr");

        const cellNombre = document.createElement("td");
        cellNombre.textContent = profesional.Nombre;
        row.appendChild(cellNombre);

        const cellArea = document.createElement("td");
        cellArea.textContent = profesional.Area;
        row.appendChild(cellArea);

        const cellEspecialidad = document.createElement("td");
        cellEspecialidad.textContent = profesional.Especialidad;
        row.appendChild(cellEspecialidad);

        const cellApgar = document.createElement("td");
        cellApgar.textContent = profesional.Apgar;
        row.appendChild(cellApgar);

        tbody.appendChild(row);
    });
};
