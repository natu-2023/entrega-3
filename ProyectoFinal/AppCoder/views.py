from datetime import date

from django.shortcuts import redirect, render

from datetime import datetime
from . import models
from .models import Disfraces, TipoDisfraces
from .forms import disfracesbuscarformulario, disfracesFormulario, tipodisfracesFormulario

def inicio_view(request):
    return render(request, "AppCoder/inicio.html")


############       Disfraces   ##################

def disfraces_buscar_view(request):
    mensaje_error = None
    disfraz = None
    nombre = None
    
    if request.method == 'GET':
        form = disfracesbuscarformulario(request.GET)
                
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            print(nombre)
            try:
                disfraz = Disfraces.objects.get(nombre__icontains=nombre)
            except Disfraces.DoesNotExist:
                mensaje_error = f"No se encontró ningún disfraz con el nombre '{nombre}'."
    else:
        form = disfracesbuscarformulario()

    return render(request, "AppCoder/disfraces_buscar.html", {'form': form, 'disfraz': disfraz, 'mensaje_error': mensaje_error})  
    

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

######################Tipo de Disfraces y stock  ####################

   
def tipo_disfraces_lista_view(request):
    todos_los_tipos_disfraces = []
    for clase in TipoDisfraces.objects.all():
        todos_los_tipos_disfraces.append(clase)

    contexto = {"clase": todos_los_tipos_disfraces}
    return render(request, "AppCoder/tipo_disfraces_list.html", contexto)


def tipo_disfraces_view(request):
    if request.method == "GET":
        form = tipodisfracesFormulario()
        return render(request,"AppCoder/tipo_disfraces_formulario.html",context={"form": form}
        )
    else:
        formulario = tipodisfracesFormulario(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            modelo = TipoDisfraces(clase=informacion["clase"], talle=informacion["talle"], cantidad=informacion["cantidad"])
            modelo.save()

        return redirect("AppCoder:inicio")