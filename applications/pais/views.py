from django.views.generic import ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Pais


class MostrarIdiomasPais(ListView):
    """
    Una vista que muestra los idiomas de un país.

    Esta vista extiende la clase ListView y se utiliza para renderizar la plantilla 'mostrar_idiomas_pais.html'.
    Recupera los idiomas asociados con un país desde el modelo 'Pais' y los pasa a la plantilla
    como el objeto de contexto 'mostrar_idiomas_pais'.

    Atributos:
        template_name (str): El nombre de la plantilla que se va a renderizar.
        context_object_name (str): El nombre del objeto de contexto que se va a pasar a la plantilla.
        model (Model): La clase del modelo que se utilizará para recuperar los datos.
    """
    template_name = 'pais/mostrar_idiomas_pais.html'
    context_object_name = 'mostrar_idiomas_pais'
    model = Pais


class MostrarContinentePais(ListView):
    """
    Una vista que muestra una lista de países basada en el continente seleccionado.

    Atributos:
        template_name (str): El nombre de la plantilla utilizada para renderizar la vista.
        context_object_name (str): El nombre de la variable de contexto que contiene la lista de países.

    Métodos:
        get_queryset(): Devuelve el conjunto de consultas de países filtrados por el continente seleccionado.
    """
    template_name = 'pais/mostrar_paises_continente.html'
    context_object_name = 'mostrar_paises_continente'

    def get_queryset(self):
        return Pais.objects.filter(continente__nombre_continente=self.request.GET.get('continente', ''))


class ActualizarPais(UpdateView):
    """
    Vista para actualizar un objeto Pais.

    Esta vista renderiza la plantilla 'pais/actualizar_pais.html' y permite a los usuarios actualizar
    los campos de un objeto Pais. El atributo fields está configurado como '__all__', lo que significa
    que todos los campos del modelo se mostrarán en el formulario.

    Atributos:
        template_name (str): El nombre de la plantilla que se va a renderizar.
        fields (str): Los campos que se mostrarán en el formulario.
        model (Model): La clase del modelo que se utilizará para actualizar el objeto.
        success_url (str): La URL a la que redirigir después de una actualización exitosa.
    """
    template_name = 'pais/actualizar_pais.html'
    fields = '__all__'
    model = Pais
    success_url = reverse_lazy('mostrar-paises')


class EliminarPais(DeleteView):
    """
    Clase de vista para eliminar un objeto Pais.

    Esta clase hereda de la clase DeleteView proporcionada por Django.
    Es responsable de renderizar la plantilla 'eliminar_pais.html',
    eliminar el objeto Pais especificado de la base de datos y redirigir
    a la URL 'mostrar-paises' después de una eliminación exitosa.

    Atributos:
        template_name (str): El nombre de la plantilla que se va a renderizar.
        model (Model): La clase de modelo que representa el objeto Pais.
        success_url (str): La URL a la que redirigir después de una eliminación exitosa.
    """
    template_name = 'pais/eliminar_pais.html'
    model = Pais
    success_url = reverse_lazy('mostrar-paises')
