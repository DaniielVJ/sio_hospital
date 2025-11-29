window.renderMainChart = function () {
    const div = document.getElementById("main_chart");
    if (!div) return;

    const meses = JSON.parse(div.dataset.meses || `["Ene","Feb","Mar"]`);
    const valores = JSON.parse(div.dataset.values || `[10,20,15]`);

    const chart = echarts.init(div);

    const option = {
        title: { text: "Embarazos por Mes", left: "center" },
        tooltip: { trigger: "axis" },
        xAxis: { type: "category", data: meses },
        yAxis: { type: "value" },
        series: [{ type: "bar", data: valores }]
    };

    chart.setOption(option);
    chart.resize();
};
