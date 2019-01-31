from django.contrib import admin
from django.urls import path, include
from . import views

noticias_patterns = ([
    path('', views.noticias, name="noticias"),
    path('add/', views.NoticiasCreate.as_view(), name="add_noticia"),
    path('edit/<int:pk>/', views.EditNoticia.as_view(), name="edit_noticia"),
    path('delete/<int:pk>/', views.DeleteNoticia.as_view(), name="deleteNoticia"),
], 'noticias')