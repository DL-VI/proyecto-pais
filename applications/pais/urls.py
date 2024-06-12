from django.urls import path
from .import views

urlpatterns = [
    path('paises/', views.TodosPaises.as_view()),
    path('paises-ciudad/', views.TodosPaises.as_view()),
]
