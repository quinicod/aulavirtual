from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from aula.models import User_asignatura, Asignatura, Seccion, File_seccion, Perfil, Evento, File_Evento
from django.contrib.auth import authenticate, logout
from foro.models import Post, Respuesta
from foro.forms import nuevoPostForm, nuevaRespuestaForm
from .forms import nuevaSeccion, anyadirMaterial, MaterialForm, EventoForm
from aula.forms import Contacto
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import UpdateView
from django.core.mail import send_mail, BadHeaderError
from django.core.serializers import serialize


def asignaturas(request):
    if request.user.is_authenticated:
        usuario=request.user
        asignaturas=User_asignatura.objects.filter(id_user=usuario)

    return render(request, 'aula/asignaturas.html', {'asignaturas':asignaturas})

def asigAula(request, nombre):
    asignatura=Asignatura.objects.get(slug=nombre)
    secciones=Seccion.objects.filter(asignatura=asignatura.id).order_by('created')
    foros=Post.objects.filter(id_asignatura=asignatura.id).order_by('created')
    eventos=Evento.objects.filter(asignatura=asignatura).order_by('created')
    nuevoPost=nuevoPostForm()
    nuevaRespuesta=nuevaRespuestaForm()
    user=request.user
    perfil=Perfil.objects.get(id_user=user)
    form_class=nuevaSeccion()
    formaterial=anyadirMaterial()
    materialForm=MaterialForm()
    eventoForm=EventoForm()
    # json eventos
    event = [{"pk": e.pk, "fecha": e.fecha_inicio} for e in eventos]
    # Comprobar si el alumno ha entregado tareas
    return render(request, 'aula/asigAula.html', {'asignatura':asignatura,'secciones':secciones,
    'foros':foros,'formPost':nuevoPost,'nuevaRespuesta':nuevaRespuesta,'perfil':perfil,
    'nuevaSeccion':form_class,'formaterial':formaterial,'materialForm':materialForm, 'eventos':eventos,'json_eventos':event,
    'eventoForm':eventoForm})

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

class editarMaterial(UpdateView):
    model=File_seccion
    form_class=MaterialForm
    template_name='aula/asigAula.html'

class updateSeccion(UpdateView): 
    model = Seccion
    form_class = MaterialForm
    template_name = 'aula/asigAula.html'

def enviarEmail(request):
    usuario = request.POST.get('name','')
    subject = request.POST.get('asunto', '')
    message = request.POST.get('mensaje', '')
    from_email = request.POST.get('email', '')
    if subject and message and from_email:
        try:
            # email al admin con la consulta del usuario
            message= message+" \nConsulta de: "+usuario
            send_mail(subject, message,'joaquinguzmangarciaplata@gmail.com', ['joaquinguzmangarciaplata@gmail.com'])
            # email de confirmacion de envio al usuario
            mensaje_confimacion='Su consulta se ha enviado correctamente al administrador de la pagina.'
            send_mail(subject, mensaje_confimacion,'joaquinguzmangarciaplata@gmail.com', [from_email])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return redirect(reverse('contacta')+"?ok")
    else:
        # In reality we'd use a form class
        # to get proper validation errors.
        return HttpResponse('Make sure all fields are entered and valid.')

def entregaEvento(request, id):
    if request.method == 'POST':
        entrega=EventoForm(request.POST, request.FILES)
        if entrega.is_valid():
            file=request.FILES.get('file')
            alumno=request.user
            evento=Evento.objects.get(id=id)
            file_evento=File_Evento(file=file, alumno=alumno, evento=evento)
            file_evento.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


