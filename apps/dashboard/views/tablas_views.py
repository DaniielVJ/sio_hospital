from django.http import JsonResponse
from django.contrib.auth.decorators import permission_required
from pacientes.models.paciente import Paciente


@permission_required('pacientes.view_paciente', raise_exception=True)
def ultimos_pacientes_json(request):
    """
    Devuelve JSON con los últimos 10 pacientes (por created_at desc).
    Cada entrada contiene: id, nombre_completo, edad, tipo, comuna.
    """
    qs = (
        Paciente.objects
        .select_related('tipo', 'comuna', 'nacionalidad', 'cesfam')
        .order_by('-created_at')[:10]
    )

    data = []
    for p in qs:
        data.append({
            'id': p.id,
            'nombre_completo': p.obtener_nombre_completo(),
            'edad': p.calcular_edad_paciente(),
            'tipo': str(p.tipo) if p.tipo else None,
            'comuna': str(p.comuna) if p.comuna else None,
        })

    return JsonResponse(data, safe=False)