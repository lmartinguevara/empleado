from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView, CreateView, TemplateView, UpdateView,DeleteView
from .models import Empleado
from .forms import RegistroForm
# Create your views here.


class InicioView(TemplateView):
    template_name = "inicio.html"


class ListAllEmpleados(ListView):
    
    paginate_by = 4
    template_name = "persona/list_all.html"

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword",'')
        lista = Empleado.objects.filter(
            first_name__icontains = palabra_clave
        )        
        return lista

class ListEmpleadosAdmin(ListView):
    
    paginate_by = 10
    template_name = "persona/list_empleados.html"
    ordering = 'first_name'
    context_object_name = 'empleados'
    model = Empleado    
   
    
class ListByAreaEmpleados(ListView):
    template_name = "persona/list_by_area.html"
    context_object_name = 'empleados'
    
    def get_queryset(self):
        area = self.kwargs['shorname']
        lista = Empleado.objects.filter(
            departamento__shor_name = area 
        )
        
        return lista


class ListEmpleadosByKword(ListView):
    template_name = "persona/list_by_kword.html"
    context_object_name = 'empleados'

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword",'')
        lista = Empleado.objects.filter(
            first_name = palabra_clave
        )        
        return lista


class ListHabilidadesEmpleado(ListView):
    template_name = "persona/habilidades.html"
    context_object_name = 'habilidades'
    
    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", 1 )
        empleado  = Empleado.objects.get(id = palabra_clave)
        return empleado.habilidades.all()




class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = "persona/detail_empleado.html"

    
    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        context['titulo'] = 'Empleado del mes'
        return context
    

class EmpleadoCreateView(CreateView):
    model = Empleado
    template_name = "persona/add.html"
    form_class = RegistroForm
    success_url = reverse_lazy('persona_app:empleados_admin')

    def form_valid(self,form):
        empleado = form.save(commit = False)
        empleado.full_name = empleado.first_name + ' ' + empleado.last_name
        empleado.save()
        return super(EmpleadoCreateView,self).form_valid(form)


class SuccessView(TemplateView):
    template_name = "persona/success.html"



class EmpleadoUpdateView(UpdateView):
    model = Empleado
    template_name = "persona/update.html"
    fields = ('__all__')
    success_url = reverse_lazy('persona_app:empleados_admin')

    #def post(self, request, *args, **kwargs):
        #self.object = self.get_object()
        #return super().post(request, *args, **kwargs)


class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = "persona/delete.html"
    success_url = reverse_lazy('persona_app:empleados_admin')