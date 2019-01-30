from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class Noticia(models.Model):
    titulo=models.CharField(max_length=100, verbose_name="Titulo")
    contenido = RichTextField(verbose_name="Contenido", null=True)
    imagen=models.ImageField(upload_to='noticias', null=True, blank=True, verbose_name='Imagen')
    created=models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated=models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name="Noticia"
        verbose_name_plural="Noticias"
        ordering=["-created"]
    
    def __str__(self):
        return self.titulo