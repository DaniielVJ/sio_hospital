window.renderChartApgar = function () {
    const div = document.getElementById("chart_apgar");
    if (!div) return;

    const apgar = JSON.parse(div.dataset.values || `[8,9,7,8]`);
    const labels = apgar.map((_, i) => `RN ${i + 1}`);

    const chart = echarts.init(div);

    const option = {
        title: { text: "APGAR de Recién Nacidos", left: "center" },
        tooltip: { trigger: "axis" },
        xAxis: { type: "category", data: labels },
        yAxis: { min: 0, max: 10 },
        series: [{ type: "line", data: apgar }]
    };

    chart.setOption(option);
    chart.resize();
};
