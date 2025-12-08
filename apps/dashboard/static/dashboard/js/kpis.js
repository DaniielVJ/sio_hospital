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

window.fetchKpis = function (endpoint) {
    // permite configurar desde plantilla: window.KPIS_API_URL = '...';
    const url = endpoint || window.KPIS_API_URL || '/dashboard/api/kpis/';
    fetch(url, { credentials: 'same-origin' })
        .then(res => {
            if (!res.ok) throw new Error('Network response was not ok');
            return res.json();
        })
        .then(data => {
            const map = {
                kpi1: data.pc_mes,
                kpi2: data.p_diario,
                kpi3: data.activos,
                kpi4: data.complicaciones,
                kpi5: data.apgar,
                kpi6: data.promedio_estancia,
                kpi7: data.pc_semana
            };

            Object.keys(map).forEach(id => {
                const el = document.getElementById(id);
                if (!el) return;
                el.dataset.value = map[id] ?? 0;
            });

            // llamar renderers si existen
            window.renderKpiTotales && window.renderKpiTotales();
            window.renderKpiTasaCesareas && window.renderKpiTasaCesareas();
            window.renderKpiPartosVaginales && window.renderKpiPartosVaginales();
            window.renderKpiComplicaciones && window.renderKpiComplicaciones();
            window.renderKpiApgar && window.renderKpiApgar();
            window.renderKpiPromedioEstancia && window.renderKpiPromedioEstancia();
        })
        .catch(err => {
            console.error('Error cargando KPIs:', err);
        });
};

window.addEventListener('DOMContentLoaded', function () {
    window.fetchKpis();
});
