from datetime import date

from django.shortcuts import redirect, render

from datetime import datetime
from . import models
from .models import Disfraces, TipoDisfraces, STock

from .forms import disfracesbuscarFormulario, disfracesFormulario

def inicio_view(request):
    return render(request, "AppCoder/inicio.html")


def disfraces_buscar_view(request):
    if request.method == "GET":
        form = disfracesbuscarFormulario()
        return render(
            request,
            "AppCoder/disfraces_buscar.html",
            context={"form": form}
        )
    else:
        formulario = disfracesbuscarFormulario(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            disfraces_filtrados = []
            for nombre in Disfraces.objects.filter(nombre=informacion["nombre"]):
                disfraces_filtrados.append(nombre)

            contexto = {"nombre": disfraces_filtrados}
            return render(request, "AppCoder/disfraces_list.html", contexto)


def disfraces_lista_view(request):
    todos_los_disfraces = []
    for nombre in Disfraces.objects.all():
        todos_los_disfraces.append(nombre)

    contexto = {"nombre": todos_los_disfraces}
    return render(request, "AppCoder/disfraces_list.html", contexto)


def disfraces_view(request):
    if request.method == "GET":
        form = disfracesFormulario()
        return render(request,"AppCoder/disfraces_formulario.html",context={"form": form}
        )
    else:
        formulario = disfracesFormulario(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            modelo = Disfraces(nombre=informacion["nombre"], precio=informacion["precio"])
            modelo.save()

        return redirect("AppCoder:inicio")


