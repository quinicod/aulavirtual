from django.contrib import admin
from aula.models import Seccion, File_seccion
from .models import Perfil
from .models import Nivel
from .models import Curso
from .models import User_asignatura
from .models import Asignatura
from .models import Evento, File_Evento

admin.site.register(Perfil)
admin.site.register(Nivel)
admin.site.register(Curso)
admin.site.register(User_asignatura)
admin.site.register(Asignatura)
admin.site.register(Seccion)
admin.site.register(File_seccion)
admin.site.register(Evento)
admin.site.register(File_Evento)

