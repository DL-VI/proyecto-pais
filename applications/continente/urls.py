from django.urls import path
from .import views


urlpatterns = [
    path('continentes/', views.ListarContinente.as_view()),
]
