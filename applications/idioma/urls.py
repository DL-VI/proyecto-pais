from django.urls import path
from .import views

urlpatterns = [
    path('idiomas/', views.Idiomas.as_view()),
]
