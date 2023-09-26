from django.shortcuts import render
from .models import Filme
from django.views.generic import TemplateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class Homepage(TemplateView):
    template_name = 'homepage.html'


class HomeFilmes(LoginRequiredMixin, ListView):
    template_name = "homefilmes.html"
    model = Filme


class DetalhesFilme(LoginRequiredMixin, DetailView):
    template_name = "detalhesfilme.html"
    model = Filme

    def get(self, request, *args, **kwargs):
        filme = self.get_object()
        filme.visualizacoes += 1
        filme.save()
        usuario = request.user      # current user
        usuario.filmes_vistos.add(filme)  # .add para adicionar no banco
        # Redireciona o usuário para a url final
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        # Executa primeiro a função da superClass
        context = super(DetalhesFilme, self).get_context_data(**kwargs)
        # Lista dos filmes relacionados de acordo com a categoria
        filmes_relacionados = Filme.objects.filter(
            categoria=self.get_object().categoria)
        context['filmes_relacionados'] = filmes_relacionados
        return context


class PesquisaFilme(LoginRequiredMixin, ListView):
    template_name = "pesquisa.html"
    model = Filme

    # Alterando o object_list

    def get_queryset(self):
        # Quando for feita uma pesquisa quero pegar o termo digitado
        termo_pesquisa = self.request.GET.get(
            'query')  # é o name do input da pesquisa
        if termo_pesquisa:
            object_list = self.model.objects.filter(
                titulo__icontains=termo_pesquisa)
            return object_list
        else:
            return None

# def homepage(request):
#     return render(request, "homepage.html")

#url - view - template
# def homefilmes(request):
#     context = {}
#     lista_filmes = Filme.objects.all()  # pega todos os objetos do banco de dados
#     context['lista_filmes'] = lista_filmes
#     return render(request, "homefilmes.html", context)
