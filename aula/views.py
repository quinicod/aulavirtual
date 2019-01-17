from django.shortcuts import render, HttpResponse, get_object_or_404
from aula.models import User_asignatura, Asignatura, Seccion, File_seccion
from django.contrib.auth import authenticate, logout

def index(request):
    return render(request, 'aula/index.html', {})

def asignaturas(request):
    if request.user.is_authenticated:
        usuario=request.user
        asignaturas=User_asignatura.objects.filter(id_user=usuario)

    return render(request, 'aula/asignaturas.html', {'asignaturas':asignaturas})

def asigAula(request, nombre):
    asignatura=Asignatura.objects.get(slug=nombre)
    secciones=Seccion.objects.filter(asignatura=asignatura.id).order_by('created')

    return render(request, 'aula/asigAula.html', {'asignatura':asignatura,'secciones':secciones})