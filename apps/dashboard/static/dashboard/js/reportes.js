window.renderKpireportesMes = function () {
    const el = document.getElementById("kpi_reporte_1");
    if (!el) return;

    const valor = el.dataset.value || 10;
    el.innerHTML = valor;
};

window.renderKpiCesareareporte = function () {
    const el = document.getElementById("kpi_reporte_2");
    if (!el) return;

    const valor = el.dataset.value || 30;
    el.innerHTML = valor;
};

window.renderKpiComplicaciones = function () {
    const el = document.getElementById("kpi_reporte_3");
    if (!el) return;
    const valor = el.dataset.value || 15;
    el.innerHTML = valor;
};


/* graficos */
window.renderChartTotalreportesPeriodo = function () {
    const div = document.getElementById("chart_reporte_1");
    if (!div) return;

    const meses = JSON.parse(div.dataset.meses || `["Ene","Feb","Mar","Abr","May","Jun","Jul","Ago","Sep","Oct","Nov","Dic"]`);
    const valores = JSON.parse(div.dataset.values || `[10,20,30,50,100]`);

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

window.renderChartTasaCesarea = function () {
    const div = document.getElementById("chart_reporte_2");
    if (!div) return;

    const meses = JSON.parse(div.dataset.meses || `["Ene","Feb","Mar"]`);
    const valores = JSON.parse(div.dataset.values || `[10,20,30]`);

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

window.renderChartTasaComplicaciones = function () {
    const div = document.getElementById("chart_reporte_3");
    if (!div) return;

    const labels = JSON.parse(div.dataset.labels || `["Hemorragia", "Preeclampsia", "Infección", "reporte Prematuro", "Otros"]`);
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




/* tabla */
window.renderTableReporte = function () {
    const div = document.getElementById("tabla_reporte");
    if (!div) return;

    const tabla = JSON.parse(div.dataset.pacientes || '[{"nombre": "Ana Perez", "edad": 28}, {"nombre": "Maria Gomez", "edad": 32}]');

    const tableBody = div.querySelector("tbody");

    tabla.forEach(paciente => {
        const row = document.createElement("tr");
        const cellNombre = document.createElement("td");
        cellNombre.textContent = paciente.nombre;
        row.appendChild(cellNombre);
        const cellEdad = document.createElement("td");
        cellEdad.textContent = paciente.edad;
        row.appendChild(cellEdad);

        tableBody.appendChild(row);
    });
};
