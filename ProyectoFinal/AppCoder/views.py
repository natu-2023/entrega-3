from datetime import date

from django.shortcuts import redirect, render

from datetime import datetime

from . import models

from .models import Disfraces

from .forms import disfracesbuscarFormulario, disfracesfiltrados, disfracesFormulario

# Create your views here.
def inicio_view(request):
    return render(request, "AppCoder/inicio.html")
######################



def disfraces_buscar_view(request):
    if request.method == "GET":
        form = disfracesFormulario()
        return render(
            request,
            "AppCoder/disfraz_formulario_busqueda.html",
            context={"form": form}
        )
    else:
        formulario = disfracesbuscarFormulario(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            disfraces_filtrados = []
            for Disfraces in Disfraces.objects.filter(disfraz=informacion["disfraces"]):
                disfraces_filtrados.append(Disfraces)

            contexto = {"disfraces": disfracesfiltrados}
            return render(request, "AppCoder/disfraces_list.html", contexto)


#def cursos_todos_view(request):
#    todos_los_cursos = []
#    for curso in Curso.objects.all():
#        todos_los_cursos.append(curso)

#   contexto = {"cursos": todos_los_cursos}
#    return render(request, "AppCoder/cursos_list.html", contexto)


def disfraces_view(request):
    if request.method == "GET":
        print("+" * 90) #  Imprimimos esto para ver por consola
        print("+" * 90) #  Imprimimos esto para ver por consola
        form = disfracesFormulario()
        return render(
            request,
            "AppCoder/disfraces_formulario_avanzado.html",
            context={"form": form}
        )
    else:
        formulario = disfracesFormulario(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            modelo = Disfraces(disfraz=informacion["disfraces"], precio=informacion["precio"])
            modelo.save()

        return redirect("AppCoder:inicio")


#def profesores_view(xx):
#    nombre = "Mariano Manuel"
#    apellido = "Barracovich"
#    ahora = datetime.now()
#    diccionario = {
#        'nombre': nombre,
#        'apellido': apellido,
#        "nacionalidad": "argentino",
#        "hora": ahora,
#        "ciudades_preferidas": ["Buenos Aires", "Lima", "San Pablo", "Trieste"]
#    }  # Para enviar al contexto
#    return render(xx, "AppCoder/padre.html", diccionario)
