from django.views.generic import TemplateView, ListView, View, DetailView
from django.http import Http404


from core.mixins import AdminTiRequiredMixin
from .config import Gestacion, Paciente, Parto, RecienNacido

class MenuInicioAuditoriaView(TemplateView):
    template_name = "auditoria/inicio_auditoria.html"



class ListarHistoricoPaciente(AdminTiRequiredMixin, ListView):
    model = Paciente
    template_name = "auditoria/historicos_pacientes.html"
    context_object_name = "historicos"
    paginate_by = 20

    def get_queryset(self):
        qs = Paciente.history.all().select_related('history_user')

        query_params = self.request.GET.copy()
        if 'page' in query_params:
            query_params.pop('page')

        self.query_string = query_params.urlencode()

        self.username = self.request.GET.get('username', "")
        self.start_date = self.request.GET.get('start_date', "")
        self.end_date = self.request.GET.get('end_date', "")
        self.tipo = self.request.GET.get('tipo', "")

        if self.username:
            qs = qs.filter(history_user__username=self.username)

        if self.start_date:
            qs = qs.filter(history_date__date__gte=self.start_date)
            # IMPORTANTE USAR el lookup __date para que compare la fecha simplemente si el campo es datetimefield si no pasara nuestra fecha a un datetime 
            # con 00:00 horas y evaluara que sea mayor e igual pero no solo de la fecha si no tmb por su hora 00:00

        if self.end_date:
            qs = qs.filter(history_date__date__lte=self.end_date)
        
        if self.tipo:
            qs = qs.filter(history_type=self.tipo)

        return qs.order_by('-history_date')


    def get_context_data(self, **kwargs):
        context_data =  super().get_context_data(**kwargs)
        context_data['username'] = self.username
        context_data['start_date'] = self.start_date
        context_data['end_date'] = self.end_date
        context_data['query_string'] = self.query_string
        context_data['tipo'] = self.tipo
        return context_data
    

class ListarHistoricoGestaciones(AdminTiRequiredMixin, ListView):
    model = Gestacion
    template_name = "auditoria/historicos_gestaciones.html"
    context_object_name = "historicos"
    paginate_by = 20

    def get_queryset(self):
        qs = Gestacion.history.all().select_related('history_user')

        query_params = self.request.GET.copy()
        if 'page' in query_params:
            query_params.pop('page')

        self.query_string = query_params.urlencode()

        self.username = self.request.GET.get('username', "")
        self.start_date = self.request.GET.get('start_date', "")
        self.end_date = self.request.GET.get('end_date', "")
        self.tipo = self.request.GET.get('tipo', "")

        if self.username:
            qs = qs.filter(history_user__username=self.username)

        if self.start_date:
            qs = qs.filter(history_date__date__gte=self.start_date)
            # IMPORTANTE USAR el lookup __date para que compare la fecha simplemente si el campo es datetimefield si no pasara nuestra fecha a un datetime 
            # con 00:00 horas y evaluara que sea mayor e igual pero no solo de la fecha si no tmb por su hora 00:00

        if self.end_date:
            qs = qs.filter(history_date__date__lte=self.end_date)
        
        if self.tipo:
            qs = qs.filter(history_type=self.tipo)

        return qs.order_by('-history_date')


    def get_context_data(self, **kwargs):
        context_data =  super().get_context_data(**kwargs)
        context_data['username'] = self.username
        context_data['start_date'] = self.start_date
        context_data['end_date'] = self.end_date
        context_data['query_string'] = self.query_string
        context_data['tipo'] = self.tipo
        return context_data
    


class ListarHistoricoPartos(AdminTiRequiredMixin, ListView):
    model = Parto
    template_name = "auditoria/historicos_partos.html"
    context_object_name = "historicos"
    paginate_by = 20

    def get_queryset(self):
        qs = Parto.history.all().select_related('history_user')

        query_params = self.request.GET.copy()
        if 'page' in query_params:
            query_params.pop('page')

        self.query_string = query_params.urlencode()

        self.username = self.request.GET.get('username', "")
        self.start_date = self.request.GET.get('start_date', "")
        self.end_date = self.request.GET.get('end_date', "")
        self.tipo = self.request.GET.get('tipo', "")

        if self.username:
            qs = qs.filter(history_user__username=self.username)

        if self.start_date:
            qs = qs.filter(history_date__date__gte=self.start_date)
            # IMPORTANTE USAR el lookup __date para que compare la fecha simplemente si el campo es datetimefield si no pasara nuestra fecha a un datetime 
            # con 00:00 horas y evaluara que sea mayor e igual pero no solo de la fecha si no tmb por su hora 00:00

        if self.end_date:
            qs = qs.filter(history_date__date__lte=self.end_date)
        
        if self.tipo:
            qs = qs.filter(history_type=self.tipo)

        return qs.order_by('-history_date')


    def get_context_data(self, **kwargs):
        context_data =  super().get_context_data(**kwargs)
        context_data['username'] = self.username
        context_data['start_date'] = self.start_date
        context_data['end_date'] = self.end_date
        context_data['query_string'] = self.query_string
        context_data['tipo'] = self.tipo
        return context_data
    
class ListarHistoricoRecienNacidos(AdminTiRequiredMixin, ListView):
    model = RecienNacido
    template_name = "auditoria/historicos_gestaciones.html"
    context_object_name = "historicos"
    paginate_by = 20

    def get_queryset(self):
        qs = RecienNacido.history.all().select_related('history_user')

        query_params = self.request.GET.copy()
        if 'page' in query_params:
            query_params.pop('page')

        self.query_string = query_params.urlencode()

        self.username = self.request.GET.get('username', "")
        self.start_date = self.request.GET.get('start_date', "")
        self.end_date = self.request.GET.get('end_date', "")
        self.tipo = self.request.GET.get('tipo', "")

        if self.username:
            qs = qs.filter(history_user__username=self.username)

        if self.start_date:
            qs = qs.filter(history_date__date__gte=self.start_date)
            # IMPORTANTE USAR el lookup __date para que compare la fecha simplemente si el campo es datetimefield si no pasara nuestra fecha a un datetime 
            # con 00:00 horas y evaluara que sea mayor e igual pero no solo de la fecha si no tmb por su hora 00:00

        if self.end_date:
            qs = qs.filter(history_date__date__lte=self.end_date)
        
        if self.tipo:
            qs = qs.filter(history_type=self.tipo)

        return qs.order_by('-history_date')


    def get_context_data(self, **kwargs):
        context_data =  super().get_context_data(**kwargs)
        context_data['username'] = self.username
        context_data['start_date'] = self.start_date
        context_data['end_date'] = self.end_date
        context_data['query_string'] = self.query_string
        context_data['tipo'] = self.tipo
        return context_data
    




class HistoricoCreacionPacienteView(AdminTiRequiredMixin, View):
    template_name = ""



class CargarInfoHistoricoPacienteView(DetailView):
    model = Paciente.history.model
    template_name = ""
    context_object_name = "historico"

    def dispatch(self, request, id_paciente=None, tipo=None, pk_history=None, *args, **kwargs):

        if tipo and tipo == "creacion":
            self.template_name = "auditoria/detalles_auditoria_creacion.html"
        elif tipo and tipo == "actualizacion":
            self.template_name = "auditoria/detalles_auditoria_actualizacion.html"
        elif tipo and tipo == "eliminacion":
            self.template_name = "auditoria/detalles_auditoria_eliminacion.html"
        else:
            raise Http404()

        return super().dispatch(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        context_data =  super().get_context_data(**kwargs)  
        context_data['model_record'] = self.object.instance._meta.model_name
        context_data['instancia'] = self.obtener_datos_instancia(self.object)

        return context_data


    def obtener_datos_instancia(self, instancia):
        datos = []
        # _meta.fields te da la definición de cada columna
        for field in instancia._meta.fields:
            # Ignoramos el ID si queremos
            if field.name == 'history_id':
                continue


            nombre_campo = field.verbose_name  # "Fecha de Nacimiento"
            valor = getattr(instancia, field.name) # "1990-05-20"
            
            datos.append({
                'label': nombre_campo,
                'value': valor
            })
        return datos