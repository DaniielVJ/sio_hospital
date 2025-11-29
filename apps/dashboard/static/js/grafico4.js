window.renderChartPresentacion = function () {
    const div = document.getElementById("chart_presentacion");
    if (!div) return;

    const labels = JSON.parse(div.dataset.labels || `["Cefálica","Podálica","Transversa"]`);
    const values = JSON.parse(div.dataset.values || `[150, 10, 5]`);

    const chart = echarts.init(div);

    const option = {
        title: { text: "Presentación Fetal", left: "center" },
        tooltip: { trigger: "item" },
        series: [{
            type: "pie",
            radius: "65%",
            data: labels.map((l, i) => ({ value: values[i], name: l }))
        }]
    };

    chart.setOption(option);
    chart.resize();
};
