from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from noticias.models import Noticia
from django.core.paginator import Paginator
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from noticias.forms import NoticiasForm

def noticias(request):
    noticias=Noticia.objects.all()
    paginator = Paginator(noticias, 4)

    page = request.GET.get('page')
    noticias = paginator.get_page(page)
    return render(request, 'noticias/index.html', {'noticias':noticias})

class NoticiasCreate(CreateView):
    model = Noticia
    form_class = NoticiasForm
    template_name = 'noticias/addNoticias.html'
    success_url = reverse_lazy('noticias:noticias')

class EditNoticia(UpdateView):
    model = Noticia
    form_class = NoticiasForm
    template_name = 'noticias/editNoticia.html'
    success_url = reverse_lazy('noticias:noticias')

class DeleteNoticia(DeleteView):
    model = Noticia
    template_name = 'noticias/confirmdeletenoticia.html'
    success_url = reverse_lazy('noticias:noticias')