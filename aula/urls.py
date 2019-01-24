from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('asignaturas/', views.asignaturas, name="asignaturas"),
    path('asignaturas/<nombre>', views.asigAula, name="asigAula"),
    path('asignaturas/nuevaSeccion/<int:id>', views.anyadirSeccion, name="nuevaSeccion"),
    path('asignaturas/anyadirMaterial/<int:id>', views.addMaterial, name="anyadirMaterial"),
    path('asignaturas/borrarMaterial/<int:id>', views.borrarMaterial, name="borrarMaterial"),
    path('asignaturas/editarMaterial/<int:id>', views.editarMaterial, name="editarMaterial"),
    
]