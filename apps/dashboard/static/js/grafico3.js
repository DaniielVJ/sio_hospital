window.renderChartComplicaciones = function () {
    const div = document.getElementById("chart_complicaciones");
    if (!div) return;

    const labels = JSON.parse(div.dataset.labels || `["Hemorragia", "Preeclampsia"]`);
    const values = JSON.parse(div.dataset.values || `[15, 8]`);

    const chart = echarts.init(div);

    const option = {
        title: { text: "Complicaciones más Frecuentes", left: "center" },
        tooltip: { trigger: "axis" },
        xAxis: { type: "category", data: labels },
        yAxis: { type: "value" },
        series: [{ type: "bar", data: values }]
    };

    chart.setOption(option);
    chart.resize();
};
