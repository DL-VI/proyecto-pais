from django.views.generic import ListView
from .models import Continente


class ListarContinente(ListView):
    template_name = 'continente/continente.html'
    context_object_name = 'continentes'
    model = Continente
