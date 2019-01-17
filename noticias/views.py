from django.shortcuts import render, get_object_or_404
from noticias.models import Noticia
from django.core.paginator import Paginator

def noticias(request):
    noticias=Noticia.objects.all()
    paginator = Paginator(noticias, 2) # Show 25 contacts per page

    page = request.GET.get('page')
    noticias = paginator.get_page(page)
    return render(request, 'noticias/index.html', {'noticias':noticias})
