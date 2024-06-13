from django.views.generic import ListView
from .models import Pais


class idomasPaises(ListView):
    template_name = 'pais/pais.html'
    context_object_name = 'paises'
    model = Pais
