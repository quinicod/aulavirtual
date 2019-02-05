from django.contrib import admin
from django.urls import path, include
from . import views, views_bc
from aula.views_bc import Contacta

urlpatterns = [
    path('', views.asignaturas, name="asignaturas"),
    path('asignaturas/<nombre>', views.asigAula, name="asigAula"),
    path('asignaturas/nuevaSeccion/<int:id>', views.anyadirSeccion, name="nuevaSeccion"),
    path('asignaturas/anyadirMaterial/<int:id>', views.addMaterial, name="anyadirMaterial"),
    path('asignaturas/borrarMaterial/<int:id>', views.borrarMaterial, name="borrarMaterial"),
    path('asignaturas/editarMaterial/<int:id>', views.editarMaterial.as_view(), name="editarMaterial"),
    path('contactanos', views_bc.Contacta.as_view(), name="contacta"),
    path('contactanos/enviarEmail', views.enviarEmail, name="enviarEmail"),
    path('asignaturas/entregaEvento/<int:id>', views.entregaEvento, name="entregaEvento"),

    
]