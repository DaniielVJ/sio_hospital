from django.http import JsonResponse
from django.apps import apps
from django.utils import timezone
from django.db.models import Count, F, DateField, DateTimeField
from django.db.models.functions import ExtractMonth
import calendar



# --- Data endpoints para los gráficos ---
def _find_date_field(model):
    # retorna el nombre del primer campo DateField/DateTimeField válido encontrado
    for f in model._meta.fields:
        if isinstance(f, (DateField, DateTimeField)):
            if f.name not in ('created_by', 'updated_by'):
                return f.name
    return None


def _counts_by_month(model, year):
    date_field = _find_date_field(model)
    labels = [calendar.month_name[i].capitalize() for i in range(1, 13)]
    counts = [0] * 12
    if not date_field:
        return labels, counts

    qs = (model.objects
          .annotate(month=ExtractMonth(F(date_field)))
          .filter(**{f"{date_field}__year": year})
          .values('month')
          .annotate(count=Count('pk'))
          .order_by('month'))

    for item in qs:
        m = int(item.get('month') or 0)
        if 1 <= m <= 12:
            counts[m - 1] = item.get('count', 0)
    return labels, counts


# -- MAIN GRAFICO (PARTOS POR MES EN UN AÑO)
def main_grafico_data(request):
    """
    JSON endpoint para 'MainGrafico' (ej. total partos por mes).
    GET params:
      - year (opcional): año a filtrar (por defecto año actual)
    """
    Gestacion = apps.get_model('pacientes', 'Gestacion')
    year = int(request.GET.get('year') or timezone.now().year)
    labels, data = _counts_by_month(Gestacion, year)
    return JsonResponse({'labels': labels, 'data': data, 'year': year})


#-- PACIENTES POR MES EN LOS ULTIMOS 3 MESES
def grafico2_data(request):
    """
    JSON endpoint para 'Grafico2' (ej. pacientes atendidos por mes).
    GET params:
      - year (opcional): año a filtrar (por defecto año actual)
    """
    Paciente = apps.get_model('pacientes', 'paciente')
    year = int(request.GET.get('year') or timezone.now().year)
    labels, data = _counts_by_month(Paciente, year)
    return JsonResponse({'labels': labels, 'data': data, 'year': year})