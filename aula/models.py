from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
from django.template import defaultfilters

class Calendario(models.Model):
    ref=models.CharField(max_length=100, verbose_name="Referencia")
    created=models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated=models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name="Calendario"
        verbose_name_plural="Calendarios"
        ordering=["-created"]
    
    def __str__(self):
        return self.ref

class Perfil(models.Model):
    id_user=models.OneToOneField(User, verbose_name="Id usuario", on_delete=models.CASCADE)
    tipo=models.CharField(max_length=3, verbose_name="Tipo")
    id_calendario=models.OneToOneField(Calendario, verbose_name="Id Calendario", on_delete=models.CASCADE)
    created=models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated=models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name="Perfil"
        verbose_name_plural="Perfiles"
        ordering=["-created"]

    def __str__(self):
        return str(self.id_user)

class Nivel(models.Model):
    nombre=models.CharField(max_length=50, verbose_name="Nombre")
    created=models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated=models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name="Nivel"
        verbose_name_plural="Niveles"
        ordering=["-created"]

    def __str__(self):
        return self.nombre

class Curso(models.Model):
    nombre=models.CharField(max_length=100, verbose_name="Nombre")
    siglas=models.CharField(max_length=10, verbose_name="Siglas")
    id_nivel=models.ForeignKey(Nivel, verbose_name="Id_nivel", on_delete=models.CASCADE)
    id_calendario=models.OneToOneField(Calendario, verbose_name="Id Calendario", on_delete=models.CASCADE)
    created=models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated=models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name="Curso"
        verbose_name_plural="Cursos"
        ordering=["-created"]

    def __str__(self):
        return self.nombre

# class Calendario_curso(models.Model):
#     id_curso=models.OneToOneField(Curso, verbose_name="Id Curso", on_delete=models.CASCADE)
#     id_calendario=models.OneToOneField(Calendario, verbose_name="Id Calendario", on_delete=models.CASCADE)
#     created=models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
#     updated=models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

#     class Meta:
#         verbose_name="Calendario_curso"
#         verbose_name_plural="Calendario_cursos"
#         ordering=["-created"]

#     def __str__(self):
#         return str(self.id_calendario)



class Asignatura(models.Model):
    nombre=models.CharField(max_length=100, verbose_name="Nombre")
    slug = models.SlugField(max_length=100, blank=True)
    imagen=models.ImageField(upload_to='aula/asignaturas', null=True, blank=True, verbose_name='Imagen')
    id_curso=models.ForeignKey(Curso, verbose_name="Id_Curso", on_delete=models.CASCADE)
    alumnos=models.ManyToManyField(User, through='User_asignatura')
    created=models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated=models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    def save(self, *args, **kwargs):
      self.slug = defaultfilters.slugify(self.nombre)
      super(Asignatura, self).save(*args, **kwargs)

    class Meta:
        verbose_name="Asignatura"
        verbose_name_plural="Asignaturas"
        ordering=["-created"]

    def __str__(self):
        return self.nombre

class Seccion(models.Model):
    titulo=models.CharField(max_length=100, verbose_name="Titulo")
    asignatura=models.ForeignKey(Asignatura, verbose_name="Asignatura", on_delete=models.CASCADE)
    created=models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated=models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name="Sección"
        verbose_name_plural="Secciones"
        ordering=["-created"]

    def __str__(self):
        return self.Titulo

class File_seccion(models.Model):
    id_seccion=models.ForeignKey(Seccion, verbose_name="Seccion", on_delete=models.CASCADE)
    file=models.FileField(upload_to="aula/files")
    descripcion=models.TextField(max_length=500, verbose_name="Descripción", null=True, blank=True)
    created=models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated=models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name="File_seccion"
        verbose_name_plural="File_seccion"
        ordering=["-created"]

    def __str__(self):
        return str(self.id_seccion)+" "+self.descripcion

class User_asignatura(models.Model):
    id_user=models.ForeignKey(User, verbose_name="Id usuario", on_delete=models.CASCADE)
    id_asignatura=models.ForeignKey(Asignatura, verbose_name="Id asignatura", on_delete=models.CASCADE)
    created=models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated=models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name="User_asignatura"
        verbose_name_plural="User_asignaturas"
        ordering=["-created"]

    def __str__(self):
        return (str(self.id_user)+" "+str(self.id_asignatura))