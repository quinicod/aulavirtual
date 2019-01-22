from django.views.generic.edit import CreateView
from .models import Seccion

class PageCreateView(CreateView):
    model=Seccion
    fields=['titulo']