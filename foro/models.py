from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
from aula.models import Asignatura, Perfil

class Post(models.Model):
    titulo=models.CharField(max_length=80, null=False, verbose_name="Titulo")
    usuario=models.ForeignKey(Perfil, on_delete=models.DO_NOTHING, verbose_name="Usuario")
    id_asignatura=models.ForeignKey(Asignatura, on_delete=models.CASCADE, verbose_name="id_Asignatura")
    created=models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated=models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")
    class Meta:
        verbose_name="Post"
        verbose_name_plural="Posts"
        ordering=["-created"]
    def __str__(self):
        return self.titulo

class Respuesta(models.Model):
    respuesta=models.CharField(max_length=200, verbose_name="Respuesta")
    usuario=models.ForeignKey(Perfil, on_delete=models.DO_NOTHING, verbose_name="Usuario")
    post=models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name="Post")
    created=models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated=models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")
    class Meta:
        verbose_name="Respuesta"
        verbose_name_plural="Respuestas"
        ordering=["-created"]
    def __str__(self):
        return self.respuesta