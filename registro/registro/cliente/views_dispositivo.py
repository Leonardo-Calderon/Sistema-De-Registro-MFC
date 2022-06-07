from ast import For
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from cliente.forms import FormDispositivo
from cliente.models import DatosPersonales, Dispositivo
# from django.contrib.messages.views import SuccessMessageMixin, Fail
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count

class ListaDispositivo(ListView):
    paginate_by = 5
    model = Dispositivo
    # queryset = Dispositivo.objects.order_by('nombre')

class NuevoDispositivoView(CreateView):
    model = Dispositivo
    # fields = '__all__'
    form_class = FormDispositivo
    success_url = reverse_lazy('categorias_lista')
    extra_context = {'accion':'Nueva'}    

class EditarDispositivoView(UpdateView):
    model = Dispositivo
    # fields = '__all__'
    form_class = FormDispositivo
    extra_context = {'accion':'Modificar'}
    
    success_url = reverse_lazy('dispositivo_lista')
    def form_valid(self, form):
        self.object = self.get_object()
        if DatosPersonales.objects.filter(categoria=self.object):
            messages.error(self.request, 'No se puede editar la categoría')
            pass
        else:
            messages.success(self.request, 'Se edito con éxito la categoría')
        
        success_url = self.get_success_url()
        return HttpResponseRedirect(success_url)  

class EliminarDispositivoView(DeleteView):
    model = Dispositivo
    success_url = reverse_lazy('categorias_lista')
    
    def form_valid(self, form):
        self.object = self.get_object()
        if Dispositivo.objects.filter(categoria=self.object):
            messages.error(self.request, 'No se puede eliminar la categoría; tiene artículos agregados')
            pass
        else:
            self.object.delete()
            messages.success(self.request, 'Se elimino con éxito la categoría')
        
        success_url = self.get_success_url()
        return HttpResponseRedirect(success_url)  
    
class BienvenidaView(LoginRequiredMixin, TemplateView):
    template_name = 'bienvenida.html'
