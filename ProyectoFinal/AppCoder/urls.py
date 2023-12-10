from django.contrib import admin
from django.urls import path
from .views import inicio_view, disfraces_buscar_view, disfraces_view, disfraces_lista_view

urlpatterns = [
    path("inicio/", inicio_view),
    path("disfraces/", disfraces_view),
    path("disfraces_buscar/", disfraces_buscar_view),
    path("disfraces_todos/", disfraces_lista_view),
]