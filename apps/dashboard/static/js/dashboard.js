document.addEventListener("DOMContentLoaded", () => {


    const divInfo = document.getElementById("user_info");
    const chartDiv = document.getElementById("chart_gestacion");

    // Datos ficticios por defecto
    const Meses = ["Ene", "Feb", "Mar", "Abr", "May", "Jun"];
    const Embarazos = [5, 8, 6, 7, 4, 9];

    const meses = divInfo ? (divInfo.dataset.meses, Meses) : Meses;
    const embarazos = divInfo ? (divInfo.dataset.embarazos, Embarazos) : Embarazos;

    console.log("Meses:", meses);
    console.log("Embarazos:", embarazos);

    // Inicializar ECharts
    const chart = echarts.init(chartDiv);

    const option = {
        title: { text: "Número de Embarazos por Mes", left: "center" },
        tooltip: { trigger: "axis" },
        xAxis: { type: "category", data: meses },
        yAxis: { type: "value" },
        series: [{ name: "Embarazos", type: "bar", data: embarazos }]
    };

    chart.setOption(option);
    chart.resize();
});
