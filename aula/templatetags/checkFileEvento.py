from django import template
from aula.models import Evento, File_Evento

register = template.Library()

@register.filter(name='checkFileEvento')
def checkFileEvento(user, id_evento): 
    evento = Evento.objects.get(id=int(id_evento)) 
    fileEventos = File_Evento.objects.filter(evento=evento)
    # return True if user in fileEventos else False
    for f in fileEventos:
        if user.id == f.alumno.id:
            return True
    return False