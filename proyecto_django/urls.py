from django.contrib import admin
from django.urls import path, include, re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('', include('applications.continente.urls')),
    re_path('', include('applications.pais.urls')),
    re_path('', include('applications.idioma.urls')),
]
