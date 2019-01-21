from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('nuevoPost/', views.nuevoPost, name="nuevoPost"),
    path('nuevaRespuesta/', views.nuevaRespuesta, name="nuevaRespuesta"),
    path('borrarRespuesta/<int:id>', views.borrarRespuesta, name="borrarRespuesta"),
    path('borrarPost/<int:id>', views.borrarPost, name="borrarPost")
    
]