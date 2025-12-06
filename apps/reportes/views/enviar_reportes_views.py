from django.views import View
from django.http import FileResponse
from apps.partos.models import Parto, ViaNacimiento

from ..utils import crear_tabla_cesarea_buffer



class GenerarReporteCesarea(View):
    def get(self, *args, **kwargs):
        
        cesarea_electiva = ViaNacimiento.objects.get(tipo="CES.ELECTIVA")
        cesarea_electiva_total = Parto.objects.filter(via_nacimiento=cesarea_electiva).count()
        
        buffer_pdf = crear_tabla_cesarea_buffer(cesarea_electiva_total)
        return FileResponse(buffer_pdf, as_attachment=True, filename="tabla_cesarea.pdf")