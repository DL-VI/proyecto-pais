from django.shortcuts import render
from django.views.generic import ListView
from .models import Idioma


class Idiomas(ListView):
    template_name = 'idioma/idioma.html'
    context_object_name = 'idiomas'
    model = Idioma
