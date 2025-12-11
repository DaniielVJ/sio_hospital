window.renderKpiParto1 = function () {
    const el = document.getElementById("kpi_parto_1");
    if (!el) return;

    const valor = el.dataset.value || 10;
    el.innerHTML = valor;
};

window.renderKpiParto2 = function () {
    const el = document.getElementById("kpi_parto_2");
    if (!el) return;

    const valor = el.dataset.value || 30;
    el.innerHTML = valor;
};

window.renderKpiParto3 = function () {
    const el = document.getElementById("kpi_parto_3");
    if (!el) return;
    const valor = el.dataset.value || 15;
    el.innerHTML = valor;
};


/* graficos */
window.renderChartParto1 = function () {
    const div = document.getElementById("chart_parto_1");
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
            type: "scatter",
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

window.renderChartParto2 = function () {
    const div = document.getElementById("chart_parto_2");
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
            type: "line",
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

window.renderChartParto3 = function () {
    const div = document.getElementById("chart_parto_3");
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




/* tabla */
window.renderTableParto = function () {
    const tbody = document.getElementById("tabla_parto");
    if (!tbody) return;

    let tabla = [];
    try { /* recordar poner la comillas al inyectar datos en bruto */
        tabla = JSON.parse(tbody.dataset.value || '[{"Profesional":"Dr. Pudu","NombreRN":"Bebesito bebelin","TipoParto":"Vaginal","Apgar":8},{"Profesional":"Dr mundo","NombreRN":"pudin","TipoParto":"Cesárea","Apgar":9}]');
    } catch (e) {
        console.error('Error parseando tabla_parto dataset:', e);
        tabla = [];
    }

    // limpiar contenido previo
    tbody.innerHTML = '';

    tabla.forEach(parto => {
        const row = document.createElement("tr");

        const cellProfesional = document.createElement("td");
        cellProfesional.textContent = parto.Profesional;
        row.appendChild(cellProfesional);

        const cellNombreRN = document.createElement("td");
        cellNombreRN.textContent = parto.NombreRN;
        row.appendChild(cellNombreRN);

        const cellTipoParto = document.createElement("td");
        cellTipoParto.textContent = parto.TipoParto;
        row.appendChild(cellTipoParto);

        const cellApgar = document.createElement("td");
        cellApgar.textContent = parto.Apgar;
        row.appendChild(cellApgar);

        tbody.appendChild(row);
    });
};
