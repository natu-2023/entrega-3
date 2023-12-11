from django.contrib import admin
from django.urls import path
from .views import inicio_view, disfraces_buscar_view, disfraces_view, disfraces_lista_view, tipo_disfraces_lista_view, tipo_disfraces_view

app_name = 'AppCoder'

urlpatterns = [
    path("inicio/", inicio_view, name='inicio'),
    path("disfraces/", disfraces_view, name='disfraces'),
    path('disfraces_buscar/', disfraces_buscar_view, name='disfraces_buscar'),
    path("disfraces_todos/", disfraces_lista_view, name='disfraces_todos'),
    path("tipo_disfraces/", tipo_disfraces_view, name='tipo_disfraces'),
    path("tipo_disfraces_todos/", tipo_disfraces_lista_view, name='tipo_disfraces_todos'),
]

