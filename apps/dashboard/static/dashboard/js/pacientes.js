/* kpi */
window.renderKpiPaciente1 = function () {
    const el = document.getElementById("kpi_paciente_1");
    if (!el) return;

    const valor = el.dataset.value || 0;
    el.innerHTML = valor;
};


window.renderKpiPaciente2 = function () {
    const el = document.getElementById("kpi_paciente_2");
    if (!el) return;

    const valor = el.dataset.value || 0;
    el.innerHTML = valor;
};



window.renderKpiPaciente3 = function () {
    const el = document.getElementById("kpi_paciente_3");
    if (!el) return;

    el.innerHTML = `${el.dataset.value || 0} hrs`;
};

/* graficos */
window.renderChartPaciente1 = function () {
    const div = document.getElementById("chart_paciente_1");
    if (!div) return;

    const meses = JSON.parse(div.dataset.meses || `["Ene","Feb","Mar","Abr","May","Jun","Jul","Ago","Sep","Oct","Nov","Dic"]`);
    const valores = JSON.parse(div.dataset.values || `[180,200,300,260,240,230,150,180,200,220,250,360]`);

    const chart = echarts.init(div);

    const palette = ['#5470C6', '#91CC75', '#EE6666', '#FAC858', '#73C0DE', '#3BA272', '#E062AE'];
    const textColor = 'white';

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

window.renderChartPaciente2 = function () {
    const div = document.getElementById("chart_paciente_2");
    if (!div) return;

    const meses = JSON.parse(div.dataset.meses || `["18-25","26-35","36-45"]`);
    const valores = JSON.parse(div.dataset.values || `[20,30,10]`);

    const chart = echarts.init(div);

    const palette = ['#73C0DE', '#5470C6', '#91CC75', '#EE6666', '#FAC858'];
    const textColor = 'white';

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

window.renderChartPaciente3 = function () {
    const div = document.getElementById("chart_paciente_3");
    if (!div) return;

    const labels = JSON.parse(div.dataset.labels || `["Hemorragia", "Preeclampsia", "Infección", "Parto Prematuro", "Otros"]`);
    const values = JSON.parse(div.dataset.values || `[15, 8, 12, 5, 10]`);

    const chart = echarts.init(div);

    const palette = ['#EE6666', '#5470C6', '#91CC75', '#FAC858', '#73C0DE'];
    const textColor = 'white';

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




/* tabla con maximo 10 pacientes */
window.renderTablePaciente = function () {
    const tbody = document.getElementById("tabla_paciente");
    if (!tbody) return;

    let tabla = [];
    try {
        tabla = JSON.parse(tbody.dataset.value || '[{"nombre":"Ana Perez","edad":28},{"nombre":"Maria Gomez","edad":32}, {"nombre":"Luisa Fernandez","edad":45},{"nombre":"Carmen Rodriguez","edad":36},{"nombre":"Sofia Martinez","edad":29},{"nombre":"Elena Lopez","edad":40},{"nombre":"Marta Sanchez","edad":33}]');
    } catch (e) {
        console.error('Error parseando tabla_pacientes dataset:', e);
        tabla = [];
    }

    // limpiar contenido previo
    tbody.innerHTML = '';

    tabla.forEach(paciente => {
        const row = document.createElement("tr");

        const cellNombre = document.createElement("td");
        cellNombre.textContent = paciente.nombre;
        row.appendChild(cellNombre);
        
        const cellEdad = document.createElement("td");
        cellEdad.textContent = paciente.edad;
        row.appendChild(cellEdad);

        tbody.appendChild(row);
    });
};
