from django.urls import path
from .import views

urlpatterns = [
    path('paises/', views.TodosPaises.as_view()),
]
