window.renderMainChart = function () {
    const div = document.getElementById("chart_main");
    if (!div) return;

    const meses = JSON.parse(div.dataset.meses || `["Ene","Feb","Mar","Abr","May","Jun","Jul","Ago","Sep","Oct","Nov","Dic"]`);
    const valores = JSON.parse(div.dataset.values || `[10,20,15]`);

    const chart = echarts.init(div);

    const option = {
        title: { text: "Cantidad de embarazos durante el año", left: "center" },
        tooltip: { trigger: "axis" },
        xAxis: { type: "category", data: meses },
        yAxis: { type: "value" },
        series: [{ type: "bar", data: valores }]
    };

    chart.setOption(option);
    chart.resize();
};
