from django.views import View
from django.http import FileResponse
from apps.partos.models import Parto, ViaNacimiento

from ..utils import crear_tabla_cesarea_buffer,crear_tabla_caracteristicas_parto_buffer, crear_tabla_d1_buffer, crear_tabla_d2_buffer, crear_tabla_esterilizaciones_buffer, crear_tabla_eutocico_distocico_buffer, crear_tabla_hepatitis_b_buffer, crear_tabla_modelo_atencion_buffer, crear_tabla_profilaxis_gonorrea_buffer



class GenerarReporteCesarea(View):
    def get(self, *args, **kwargs):
        
        cesarea_electiva = ViaNacimiento.objects.get(tipo="CES.ELECTIVA")
        cesarea_electiva_total = Parto.objects.filter(via_nacimiento=cesarea_electiva).count()
        
        buffer_pdf = crear_tabla_cesarea_buffer(cesarea_electiva_total)
        return FileResponse(buffer_pdf, as_attachment=True, filename="tabla_cesarea.pdf")

#=====================================================================================    

class GenerarReporteCaracteristicasParto(View):
    def get(self , *args, **kwargs):
        
        pass

        

        buffer_pdf = crear_tabla_caracteristicas_parto_buffer(
            total_partos=122,
            vaginal=65,
            instrumental=0,
            cesarea_electiva=26,
            cesarea_urgencia=31)
        return FileResponse(buffer_pdf, as_attachment=True, filename="tabla_caracteristicas_parto(REM A 24).pdf")
    

#====================================================================================

class GenerarReporteD1(View):
    def get(self, *args, **kwargs):
        
        pass
        
        buffer_pdf = crear_tabla_d1_buffer()
        return FileResponse(buffer_pdf, as_attachment=True, filename="tabla_d1(REM A 24).pdf")
    

    
#====================================================================================

class GenerarReporteD2(View):
    def get(self, *args, **kwargs):
        
        pass
        
        buffer_pdf = crear_tabla_d2_buffer()
        return FileResponse(buffer_pdf, as_attachment=True, filename="tabla_d2(REM A 24).pdf"    )



#====================================================================================

class GenerarReporteEsterilizacionesQuirurgicas(View):
    def get(self, *args, **kwargs):
        
        pass
    
        buffer_pdf = crear_tabla_esterilizaciones_buffer()
        return FileResponse(buffer_pdf, as_attachment=True, filename="tabla_esterilizaciones_quirurgicas.pdf")
    

#====================================================================================

class GenerarReporteEutocicoDistocico(View):
    def get(slef, *args, **kwargs):
        
        pass

        buffer_pdf = crear_tabla_eutocico_distocico_buffer()
        return FileResponse(buffer_pdf, as_attachment=True, filename="tabla_eutocico_distocico(REM A 21.pdf")
    


# =====================================================================================

class GenerarReporteHepatitisB(View):
    def get(self, *args , **kwargs):
        
        pass

        
        buffer_pdf = crear_tabla_hepatitis_b_buffer()
        return FileResponse(buffer_pdf, as_attachment=True, filename="tabla_hepatitis_b(REM A 11).pdf")
    

# ====================================================================================

class GenerarReporteModeloAtencion(View):
    def get(self, *args, **kwargs):
        
        pass

        
        buffer_pdf = crear_tabla_modelo_atencion_buffer()
        return FileResponse(buffer_pdf, as_attachment=True, filename="tabla_modelo_atencion.pdf")
    

# =====================================================================================


class GenerarReporteProfilaxisGonorrea(View):
    def get(self, *args, **kwargs):
        
        pass

        
        buffer_pdf = crear_tabla_profilaxis_gonorrea_buffer()
        return FileResponse(buffer_pdf, as_attachment=True, filename="tabla_profilaxis_gonorrea(REM A 11).pdf")