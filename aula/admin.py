from django.contrib import admin
from aula.models import Calendario, Seccion, File_seccion
from .models import Perfil
from .models import Nivel
from .models import Curso
from .models import User_asignatura
from .models import Asignatura

admin.site.register(Calendario)
admin.site.register(Perfil)
admin.site.register(Nivel)
admin.site.register(Curso)
admin.site.register(User_asignatura)
admin.site.register(Asignatura)
admin.site.register(Seccion)
admin.site.register(File_seccion)

