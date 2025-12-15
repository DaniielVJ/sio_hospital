from django.views import View
from django.http import FileResponse
from django.shortcuts import get_object_or_404
from django.db.models import Q

from apps.partos.models import Parto, ViaNacimiento
from apps.recien_nacidos.models import ComplicacionPostParto, RecienNacido


from core.mixins import SupervisorRequiredMixin
from ..utils import crear_tabla_cesarea_buffer,crear_tabla_caracteristicas_parto_buffer, crear_tabla_d1_buffer, crear_tabla_d2_buffer, crear_tabla_esterilizaciones_buffer, crear_tabla_eutocico_distocico_buffer, crear_tabla_hepatitis_b_buffer, crear_tabla_modelo_atencion_buffer, crear_tabla_profilaxis_gonorrea_buffer



class GenerarReporteCesarea(SupervisorRequiredMixin, View):
    def get(self, *args, **kwargs):
        
        cesarea_electiva = ViaNacimiento.objects.get(tipo="CES.ELECTIVA")
        cesarea_electiva_total = Parto.objects.filter(via_nacimiento=cesarea_electiva).count()
        
        buffer_pdf = crear_tabla_cesarea_buffer(cesarea_electiva_total)
        return FileResponse(buffer_pdf, as_attachment=True, filename="tabla_cesarea.pdf")

#=====================================================================================    

class GenerarReporteCaracteristicasParto(SupervisorRequiredMixin, View):
    def get(self , *args, **kwargs):
        # Aqui se cuentan todos los partos que hayan sido o dado a luz a un recien nacido con un peso mayor o igual a 2500gramos y que 
        # hayan recibido lactancia antes de los 60 minutos.
        qs = Parto.objects.filter(rns__peso__gte=2500, rns__lactante_60=True).distinct()
        eutocico = get_object_or_404(ViaNacimiento, pk=3, tipo="EUTOCICO")
        distocico = get_object_or_404(ViaNacimiento, pk=4, tipo="DISTOCICO")
        ces_electiva = get_object_or_404(ViaNacimiento, pk=1, tipo="CES.ELECTIVA")
        ces_urgencia = get_object_or_404(ViaNacimiento, pk=2, tipo="CES. URGENCIA")

        start_date = self.request.GET.get('start_date')
        end_date = self.request.GET.get('end_date')
        
        if start_date:
            qs = qs.filter(hora_inicio__date__gte=start_date)
        
        if end_date:
            qs = qs.filter(hora_inicio__date__lte=end_date)


        total_partos = qs.count()
        vaginal = qs.filter(via_nacimiento=eutocico).count()
        instrumental = qs.filter(via_nacimiento=distocico).count()
        ces_electiva_total = qs.filter(via_nacimiento=ces_electiva).count()
        ces_urgencia_total = qs.filter(via_nacimiento=ces_urgencia).count()


        buffer_pdf = crear_tabla_caracteristicas_parto_buffer(
            total_partos,
            vaginal,
            instrumental,
            ces_electiva_total,
            ces_urgencia_total)
        return FileResponse(buffer_pdf, as_attachment=True, filename="tabla_caracteristicas_parto(REM A 24).pdf")
    

#====================================================================================

class GenerarReporteD1(SupervisorRequiredMixin, View):
    def get(self, *args, **kwargs):
        anomalia_congenita_object = get_object_or_404(ComplicacionPostParto, Q(nombre="Malformación congénita") & Q(pk=6))
        qs = RecienNacido.objects.all()

        start_date = self.request.GET.get('start_date')
        end_date = self.request.GET.get('end_date')
        
        if start_date:
            qs = qs.filter(fecha_hora__date__gte=start_date)
        

        if end_date:
            qs = qs.filter(fecha_hora__date__lte=end_date)


        rn_con_anomalia_congenita = RecienNacido.objects.filter(complicaciones_postparto=anomalia_congenita_object).count()
        qs = qs.filter(~Q(destino="fallece"))
        total_rn = qs.count()
        rn_menor_500 = qs.filter(peso__lt=500).count()
        rn_500_999 = qs.filter(peso__gte=500, peso__lte=999).count()
        rn_1000_1499 = qs.filter(peso__gte=1000, peso__lte=1499).count()
        rn_1500_1999 = qs.filter(peso__gte=1500, peso__lte=1999).count()
        rn_2000_2499 = qs.filter(peso__gte=2000, peso__lte=2499).count()
        rn_2500_2999 = qs.filter(peso__gte=2500, peso__lte=2999).count()
        rn_3000_3999 = qs.filter(peso__gte=3000, peso__lte=3999).count()
        rn_4000 = qs.filter(peso__gte=4000).count()

        print(total_rn, rn_menor_500, rn_500_999, rn_1000_1499, rn_1500_1999, rn_2000_2499, rn_2500_2999, rn_3000_3999, rn_4000)
        
        buffer_pdf = crear_tabla_d1_buffer(total_rn, rn_menor_500, rn_500_999, rn_1000_1499, rn_1500_1999, rn_2000_2499, rn_2500_2999, rn_3000_3999, rn_4000, rn_con_anomalia_congenita, start_date, end_date)
        return FileResponse(buffer_pdf, as_attachment=True, filename="tabla_d1(REM A 24).pdf")
    

    
#====================================================================================

class GenerarReporteD2(SupervisorRequiredMixin, View):
    def get(self, *args, **kwargs):
        
        pass
        
        buffer_pdf = crear_tabla_d2_buffer()
        return FileResponse(buffer_pdf, as_attachment=True, filename="tabla_d2(REM A 24).pdf"    )



#====================================================================================

class GenerarReporteEsterilizacionesQuirurgicas(SupervisorRequiredMixin, View):
    def get(self, *args, **kwargs):
        
        pass
    
        buffer_pdf = crear_tabla_esterilizaciones_buffer()
        return FileResponse(buffer_pdf, as_attachment=True, filename="tabla_esterilizaciones_quirurgicas.pdf")
    

#====================================================================================

class GenerarReporteEutocicoDistocico(SupervisorRequiredMixin, View):
    def get(slef, *args, **kwargs):
        
        pass

        buffer_pdf = crear_tabla_eutocico_distocico_buffer()
        return FileResponse(buffer_pdf, as_attachment=True, filename="tabla_eutocico_distocico(REM A 21.pdf")
    


# =====================================================================================

class GenerarReporteHepatitisB(SupervisorRequiredMixin, View):
    def get(self, *args , **kwargs):
        
        pass

        
        buffer_pdf = crear_tabla_hepatitis_b_buffer()
        return FileResponse(buffer_pdf, as_attachment=True, filename="tabla_hepatitis_b(REM A 11).pdf")
    

# ====================================================================================

class GenerarReporteModeloAtencion( SupervisorRequiredMixin, View):
    def get(self, *args, **kwargs):
        
        pass

        
        buffer_pdf = crear_tabla_modelo_atencion_buffer()
        return FileResponse(buffer_pdf, as_attachment=True, filename="tabla_modelo_atencion.pdf")
    

# =====================================================================================


class GenerarReporteProfilaxisGonorrea(SupervisorRequiredMixin, View):
    def get(self, *args, **kwargs):
        
        pass

        
        buffer_pdf = crear_tabla_profilaxis_gonorrea_buffer()
        return FileResponse(buffer_pdf, as_attachment=True, filename="tabla_profilaxis_gonorrea(REM A 11).pdf")