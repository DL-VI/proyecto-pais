from django.views.generic import ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Pais


class MostrarIdiomasPais(ListView):
    template_name = 'pais/mostrar_idiomas_pais.html'
    context_object_name = 'mostrar_idiomas_pais'
    model = Pais


class MostrarContinentePais(ListView):
    template_name = 'pais/mostrar_paises_continente.html'
    context_object_name = 'mostrar_paises_continente'

    def get_queryset(self):
        return Pais.objects.filter(continente__nombre_continente=self.request.GET.get('continente', ''))


class ActualizarPais(UpdateView):
    template_name = 'pais/actualizar_pais.html'
    fields = '__all__'
    model = Pais
    success_url = reverse_lazy('mostrar-paises')


class EliminarPais(DeleteView):
    template_name = 'pais/eliminar_pais.html'
    model = Pais
    success_url = reverse_lazy('mostrar-paises')
