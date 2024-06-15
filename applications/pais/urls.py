from django.urls import path
from .import views

app_name = 'pais_app'

urlpatterns = [
    path('mostrar_paises/', views.MostrarContinentePais.as_view(), name='mostrar-paises'),
    path('actualizar_pais/<pk>/', views.ActualizarPais.as_view()),
    path('eliminar_pais/<pk>/', views.EliminarPais.as_view()),
]
