window.renderKpiRn1 = function () {
    const el = document.getElementById("kpi_rn_1");
    if (!el) return;

    const valor = el.dataset.value || 10;
    el.innerHTML = valor;
};

window.renderKpiRn2 = function () {
    const el = document.getElementById("kpi_rn_2");
    if (!el) return;

    const valor = el.dataset.value || 30;
    el.innerHTML = valor;
};

window.renderKpiRn3= function () {
    const el = document.getElementById("kpi_rn_3");
    if (!el) return;
    const valor = el.dataset.value || 15;
    el.innerHTML = valor;
};


/* graficos */
window.renderChartRn1 = function () {
    const div = document.getElementById("chart_rn_1");
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

window.renderChartRn2 = function () {
    const div = document.getElementById("chart_rn_2");
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

window.renderChartRn3= function () {
    const div = document.getElementById("chart_rn_3");
    if (!div) return;

    const labels = JSON.parse(div.dataset.labels || `["Hemorragia", "Preeclampsia", "Infección",  "Prematuro", "Otros"]`);
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
window.renderTableRn = function () {
    const tbody = document.getElementById("tabla_rn");
    if (!tbody) return;

    let tabla = [];
    try {
        tabla = JSON.parse(tbody.dataset.value || '[{"NombreRN":"Ana Perez","Peso":2800,"EdadGestacional":38,"Reanimacion":"Si"}]');
    } catch (e) {
        console.error('Error parseando tabla_rn dataset:', e);
        tabla = [];
    }

    tbody.innerHTML = '';

    tabla.forEach(rn => {
        const row = document.createElement("tr");

        const cellNombreRN = document.createElement("td");
        cellNombreRN.textContent = rn.NombreRN;
        row.appendChild(cellNombreRN);

        const cellPeso = document.createElement("td");
        cellPeso.textContent = rn.Peso;
        row.appendChild(cellPeso);

        const cellEdadGestacional = document.createElement("td");
        cellEdadGestacional.textContent = rn.EdadGestacional;
        row.appendChild(cellEdadGestacional);

        const cellReanimacion = document.createElement("td");
        cellReanimacion.textContent = rn.Reanimacion;
        row.appendChild(cellReanimacion);

        tbody.appendChild(row);
    });
};
