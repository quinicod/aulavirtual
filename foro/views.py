from django.shortcuts import render
from foro.forms import nuevoPostForm, nuevaRespuestaForm
from django.http import HttpResponseRedirect
from .models import Post, Respuesta
from aula.models import Asignatura, Perfil

def nuevoPost(request):
    nuevoPost=nuevoPostForm()

    if request.method=='POST':
        nuevoPost=nuevoPostForm(data=request.POST)
        if nuevoPost.is_valid():
            usuario=request.user
            perfil=Perfil.objects.get(id_user=usuario)
            descripcion=request.POST.get('descripcion','')
            id_asignatura=request.POST.get('id_asignatura')
            asignatura=Asignatura.objects.get(id=id_asignatura)
            post = Post(titulo=descripcion, usuario=perfil, id_asignatura=asignatura)
            post.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def nuevaRespuesta(request):
    nuevaRespuesta=nuevaRespuestaForm()

    if request.method=='POST':
        nuevaRespuesta=nuevaRespuestaForm(data=request.POST)
        if nuevaRespuesta.is_valid():
            usuario=request.user
            perfil=Perfil.objects.get(id_user=usuario)
            respuesta=request.POST.get('respuesta','')
            post=request.POST.get('post')
            post=Post.objects.get(id=post)
            respuesta = Respuesta(respuesta=respuesta, usuario=perfil, post=post)
            respuesta.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def borrarRespuesta(request, id):
    respuesta=Respuesta.objects.get(id=id)
    respuesta.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def borrarPost(request, id):
    post=Post.objects.get(id=id)
    post.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
