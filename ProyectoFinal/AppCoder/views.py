from django.shortcuts import render

# Create your views here.
def cursos_view(request):
    return render(request, "AppCoder/cursos.html")
