from django.shortcuts import render
from .models import Filme
from django.views.generic import TemplateView, ListView, DetailView

# Create your views here.


class Homepage(TemplateView):
    template_name = 'homepage.html'


class HomeFilmes(ListView):
    template_name = "homefilmes.html"
    model = Filme


class DetalhesFilme(DetailView):
    template_name = "detalhesfilme.html"
    model = Filme

    def get_context_data(self, **kwargs):
        # Executa primeiro a função da superClass
        context = super(DetalhesFilme, self).get_context_data(**kwargs)
        # Lista dos filmes relacionados de acordo com a categoria
        filmes_relacionados = Filme.objects.filter(
            categoria=self.get_object().categoria)
        context['filmes_relacionados'] = filmes_relacionados
        return context

# def homepage(request):
#     return render(request, "homepage.html")

#url - view - template
# def homefilmes(request):
#     context = {}
#     lista_filmes = Filme.objects.all()  # pega todos os objetos do banco de dados
#     context['lista_filmes'] = lista_filmes
#     return render(request, "homefilmes.html", context)
