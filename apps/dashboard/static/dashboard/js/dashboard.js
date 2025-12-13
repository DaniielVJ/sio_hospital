document.addEventListener("DOMContentLoaded", () => {

    /* Pacientes */
    if (window.renderKpiPaciente1) renderKpiPaciente1();
    if (window.renderKpiPaciente2) renderKpiPaciente2();
    if (window.renderKpiPaciente3) renderKpiPaciente3();

    if (window.renderChartPaciente1) renderChartPaciente1();
    if (window.renderChartPaciente2) renderChartPaciente2();
    if (window.renderChartPaciente3) renderChartPaciente3();

    if (window.renderTablePaciente) renderTablePaciente();

    /* Partos */
    if (window.renderKpiParto1) renderKpiParto1();
    if (window.renderKpiParto2) renderKpiParto2();
    if (window.renderKpiParto3) renderKpiParto3();

    if (window.renderChartParto1) renderChartParto1();
    if (window.renderChartParto2) renderChartParto2();
    if (window.renderChartParto3) renderChartParto3();

    if (window.renderTableParto) renderTableParto();

    /* Recien Nacidos */
    if (window.renderKpiRn1) renderKpiRn1();
    if (window.renderKpiRn2) renderKpiRn2();
    if (window.renderKpiRn3) renderKpiRn3();

    if (window.renderChartRn1) renderChartRn1();
    if (window.renderChartRn2) renderChartRn2();
    if (window.renderChartRn3) renderChartRn3();

    if (window.renderTableRn) renderTableRn();

    /* Reportes */
    if (window.renderKpiReporte1) renderKpiReporte1();
    if (window.renderKpiReporte2) renderKpiReporte2();
    if (window.renderKpiReporte3) renderKpiReporte3();

    if (window.renderChartReporte1) renderChartReporte1();
    if (window.renderChartReporte2) renderChartReporte2();
    if (window.renderChartReporte3) renderChartReporte3();

    if (window.renderTableReporte) renderTableReporte();

    /* Profesionales */
    if (window.renderKpiProfesional1) renderKpiProfesional1();
    if (window.renderKpiProfesional2) renderKpiProfesional2();
    if (window.renderKpiProfesional3) renderKpiProfesional3();

    if (window.renderChartProfesional1) renderChartProfesional1();
    if (window.renderChartProfesional2) renderChartProfesional2();
    if (window.renderChartProfesional3) renderChartProfesional3();

    if (window.renderTableProfesional) renderTableProfesional();

    /* Re-renderizar charts de pacientes cuando cambie el tema (clase 'dark' en body) */
    (function observeThemeChangeForPacienteCharts() {
        if (!document.body) return;
        const observer = new MutationObserver((mutations) => {
            if (mutations.some(m => m.attributeName === 'class')) {
                if (window.renderChartPaciente1) try { window.renderChartPaciente1(); } catch (e) {}
                if (window.renderChartPaciente2) try { window.renderChartPaciente2(); } catch (e) {}
                if (window.renderChartPaciente3) try { window.renderChartPaciente3(); } catch (e) {}
            }
        });
        observer.observe(document.body, { attributes: true, attributeFilter: ['class'] });
    })();

});
