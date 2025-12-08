from django.views.generic import TemplateView
from django.http import JsonResponse
from django.shortcuts import render
from django.utils import timezone
from django.db.models import Avg
from datetime import timedelta
from apps.pacientes.models import Paciente
from core.mixins import MatronaSupervisorRequiredMixin


class KpisJsonView(MatronaSupervisorRequiredMixin, TemplateView):
    """Entrega KPIs como fragmento HTML para htmx; JSON como fallback."""

    def get(self, request, *args, **kwargs):
        now = timezone.localtime()
        today = now.date()
        year, month = today.year, today.month

        field_names = {f.name for f in Paciente._meta.fields}

        pc_mes = Paciente.objects.filter(created_at__year=year, created_at__month=month).count()
        p_diario = Paciente.objects.filter(created_at__date=today).count()

        if 'activo' in field_names:
            activos = Paciente.objects.filter(activo=True).count()
        else:
            activos = Paciente.objects.count()

        complicaciones = 0
        if 'complicacion' in field_names:
            complicaciones = Paciente.objects.filter(complicacion=True).count()

        apgar_avg = 0
        if 'apgar' in field_names:
            apgar_avg = Paciente.objects.aggregate(avg=Avg('apgar'))['avg'] or 0

        promedio_estancia = 0
        if 'estancia_horas' in field_names:
            promedio_estancia = Paciente.objects.aggregate(avg=Avg('estancia_horas'))['avg'] or 0
        elif 'promedio_estancia' in field_names:
            promedio_estancia = Paciente.objects.aggregate(avg=Avg('promedio_estancia'))['avg'] or 0

        week_start = today - timedelta(days=today.weekday())
        week_end = week_start + timedelta(days=6)
        pc_semana = Paciente.objects.filter(created_at__date__range=(week_start, week_end)).count()

        context = {
            "pc_mes": pc_mes,
            "p_diario": p_diario,
            "activos": activos,
            "complicaciones": complicaciones,
            "apgar": round(apgar_avg, 2) if isinstance(apgar_avg, (int, float)) else apgar_avg,
            "promedio_estancia": round(promedio_estancia, 2) if isinstance(promedio_estancia, (int, float)) else promedio_estancia,
            "pc_semana": pc_semana,
        }

        # Si la petición proviene de htmx devolvemos el fragmento HTML
        if request.headers.get('HX-Request') or request.headers.get('Hx-Request'):
            return render(request, 'componentes/kpi1.html', context)

        # Fallback: JSON (mantener compatibilidad)
        return JsonResponse(context)