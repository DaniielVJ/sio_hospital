document.addEventListener("DOMContentLoaded", () => {

    // TOP KPI
    if (window.renderKpiTotales) renderKpiTotales();
    if (window.renderKpiTasaCesareas) renderKpiTasaCesareas();

    // KPI secundarios
    if (window.renderKpiPartosVaginales) renderKpiPartosVaginales();
    if (window.renderKpiComplicaciones) renderKpiComplicaciones();
    if (window.renderKpiApgar) renderKpiApgar();
    if (window.renderKpiPromedioEstancia) renderKpiPromedioEstancia();

    // Gráfico Principal
    if (window.renderMainChart) renderMainChart();

    // Gráficos Secundarios
    if (window.renderChartGestacion) renderChartGestacion();
    if (window.renderChartComplicaciones) renderChartComplicaciones();
    if (window.renderChartPresentacion) renderChartPresentacion();
    if (window.renderChartApgar) renderChartApgar();
});
