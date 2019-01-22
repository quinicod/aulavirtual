from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('asignaturas/', views.asignaturas, name="asignaturas"),
    path('asignaturas/<nombre>', views.asigAula, name="asigAula"),
    path('asignaturas/nuevaSeccion/<int:id>', views.anyadirSeccion, name="nuevaSeccion"),
    
]