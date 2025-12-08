window.renderKpiTotales = function () {
    const el = document.getElementById("kpi_total_partos");
    if (!el) return;

    const valor = el.dataset.value || 0;
    el.innerHTML = valor;
};

window.renderKpiTasaCesareas = function () {
    const el = document.getElementById("kpi_tasa_cesareas");
    if (!el) return;

    const valor = el.dataset.value || 0;
    el.innerHTML = valor;
};

window.renderKpiPartosVaginales = function () {
    const el = document.getElementById("kpi_partos_vaginales");
    if (!el) return;

    const valor = el.dataset.value || 0;
    el.innerHTML = valor;
};

window.renderKpiComplicaciones = function () {
    const el = document.getElementById("kpi_complicaciones");
    if (!el) return;

    const valor = el.dataset.value || 0;
    el.innerHTML = valor;
};

window.renderKpiApgar = function () {
    const el = document.getElementById("kpi_apgar");
    if (!el) return;

    const valor = el.dataset.value || 0;
    el.innerHTML = valor;
};

window.renderKpiPromedioEstancia = function () {
    const el = document.getElementById("kpi_estancia");
    if (!el) return;

    el.innerHTML = `${el.dataset.value || 0} hrs`;
};
