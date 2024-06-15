from django.urls import path
from .import views

app_name = 'pais_app'

urlpatterns = [
    path('mostrar_paises/', views.MostrarContinentePais.as_view(), name='mostrar-paises'),
    path('actualizar_pais/<pk>/', views.ActualizarPais.as_view()),
    path('eliminar_pais/<pk>/', views.EliminarPais.as_view()),
]

"""
Patrones de URL para la aplicación 'pais_app'.

Este módulo define los patrones de URL para las vistas en la aplicación 'pais_app'.
La lista urlpatterns contiene instancias de la función path(), que mapea un patrón de URL a una vista.

- 'mostrar_paises/' mapea a la vista MostrarContinentePais.
- 'actualizar_pais/<pk>/' mapea a la vista ActualizarPais.
- 'eliminar_pais/<pk>/' mapea a la vista EliminarPais.

El parámetro 'name' se utiliza para proporcionar un nombre único a cada patrón de URL, que puede ser utilizado para revertir la URL en las plantillas.

Nota: La variable 'app_name' se utiliza para especificar el espacio de nombres de la aplicación.
"""
