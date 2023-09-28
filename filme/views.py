from django.shortcuts import render, redirect
from .models import Filme
from django.views.generic import TemplateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class Homepage(TemplateView):
    template_name = 'homepage.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            # Redireciona para o app_name filme url name homefilmes
            return redirect('filme:homefilmes')
        else:
            # Redireciona para a url final da view neste caso a homepage
            return super().get(request, *args, **kwargs)


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


class EditarPerfil(LoginRequiredMixin, TemplateView):
    template_name = 'editarperfil.html'


class CriarConta(TemplateView):
    template_name = 'criarconta.html'
