from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from aula.models import User_asignatura, Asignatura, Seccion, File_seccion, Perfil
from django.contrib.auth import authenticate, logout
from foro.models import Post, Respuesta
from foro.forms import nuevoPostForm, nuevaRespuestaForm, nuevaSeccion, anyadirMaterial, MaterialForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import UpdateView

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
    foros=Post.objects.filter(id_asignatura=asignatura.id).order_by('created')
    nuevoPost=nuevoPostForm()
    nuevaRespuesta=nuevaRespuestaForm()
    user=request.user
    perfil=Perfil.objects.get(id_user=user)
    form_class=nuevaSeccion()
    formaterial=anyadirMaterial()
    materialForm=MaterialForm()
    return render(request, 'aula/asigAula.html', {'asignatura':asignatura,'secciones':secciones,'foros':foros,'formPost':nuevoPost,'nuevaRespuesta':nuevaRespuesta,'perfil':perfil,'nuevaSeccion':form_class,'formaterial':formaterial,'materialForm':materialForm})

def anyadirSeccion(request, id):
    if request.method == 'POST':
        anyadirSeccion=nuevaSeccion(data=request.POST)
        if anyadirSeccion.is_valid():
            titulo=request.POST.get('titulo','')
            asignatura=Asignatura.objects.get(id=id)
            seccion=Seccion(titulo=titulo, asignatura=asignatura)
            seccion.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def addMaterial(request, id):
    if request.method == 'POST':
        material=anyadirMaterial(request.POST, request.FILES)
        if material.is_valid():
            file=request.FILES.get('file')
            descripcion=request.POST.get('descripcion')
            seccion=Seccion.objects.get(id=id)
            # asignatura=seccion.asignatura
            file_seccion=File_seccion(file=file, descripcion=descripcion,id_seccion=seccion)
            file_seccion.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            # return redirect(reverse('asigAula', args={'nombre':asignatura.slug}))

def borrarMaterial(request, id):
    seccion=Seccion.objects.get(id=id)
    seccion.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def editarMaterial(request, id):
    pass

class updateSeccion(UpdateView):
    model = Seccion
    form_class = MaterialForm
    template_name = 'aula/asigAula.html'

