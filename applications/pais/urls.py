from django.urls import path
from .import views

urlpatterns = [
    path('paises/', views.idomasPaises.as_view()),
]
