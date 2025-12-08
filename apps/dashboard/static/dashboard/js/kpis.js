window.renderKpiTotales = function () {
    const el = document.getElementById("kpi1");
    if (!el) return;

    const valor = el.dataset.value || 0;
    el.innerHTML = valor;
};

window.renderKpiTasaCesareas = function () {
    const el = document.getElementById("kpi2");
    if (!el) return;

    const valor = el.dataset.value || 0;
    el.innerHTML = valor;
};

window.renderKpiPartosVaginales = function () {
    const el = document.getElementById("kpi3");
    if (!el) return;

    const valor = el.dataset.value || 0;
    el.innerHTML = valor;
};

window.renderKpiComplicaciones = function () {
    const el = document.getElementById("kpi4");
    if (!el) return;

    const valor = el.dataset.value || 0;
    el.innerHTML = valor;
};

window.renderKpiApgar = function () {
    const el = document.getElementById("kpi5");
    if (!el) return;

    const valor = el.dataset.value || 0;
    el.innerHTML = valor;
};

window.renderKpiPromedioEstancia = function () {
    const el = document.getElementById("kpi6");
    if (!el) return;

    el.innerHTML = `${el.dataset.value || 0} hrs`;
};
