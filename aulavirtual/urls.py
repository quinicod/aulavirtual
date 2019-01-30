"""aulavirtual URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import RedirectView

urlpatterns = [
    # path('', include(core.urls)),
    path('jet/' , include ('jet.urls')),
    path('admin/', admin.site.urls),
    path('', include('django.contrib.auth.urls')),
    path('', include('registration.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('aula/', include('aula.urls')),
    path('noticias/', include('noticias.urls')),
    path('foro/', include('foro.urls')),
    path('', RedirectView.as_view(url='noticias')), # redirige a la ruta de nombre aula de aula/urls.py
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
