import * as echarts from "echarts";

document.addEventListener("DOMContentLoaded", () => {

    // -----------------------
    // LEER DATA-* DEL TEMPLATE
    // -----------------------
    const divInfo = document.getElementById("user_info");

    const meses = JSON.parse(divInfo.dataset.meses);
    const embarazos = JSON.parse(divInfo.dataset.embarazos);
    const lista = JSON.parse(divInfo.dataset.lista);

    console.log("Meses:", meses);
    console.log("Embarazos:", embarazos);
    console.log("Lista extra:", lista);

    // -----------------------
    // DATA PARA EL GRÁFICO
    // -----------------------
    const chartDiv = document.getElementById("chart_gestacion");
    const dataChart = JSON.parse(chartDiv.dataset.chart);

    // -----------------------
    // INICIALIZAR ECHARTS
    // -----------------------
    const chart = echarts.init(chartDiv);

    const option = {
        title: {
            text: "Número de Embarazos por Mes",
            left: "center"
        },
        tooltip: { trigger: "axis" },
        xAxis: {
            type: "category",
            data: meses
        },
        yAxis: { type: "value" },
        series: [
            {
                name: "Embarazos",
                type: "bar",
                data: embarazos
            }
        ]
    };

    chart.setOption(option);
    chart.resize();
});
