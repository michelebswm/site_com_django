from django.urls import path, include
from .views import Homepage, HomeFilmes, DetalhesFilme, PesquisaFilme, EditarPerfil, CriarConta, CustomLoginView
from django.contrib.auth import views as auth_view


app_name = 'filme'


urlpatterns = [
    path('', Homepage.as_view(), name='homepage'),
    path('filmes/', HomeFilmes.as_view(), name='homefilmes'),
    path('filmes/<int:pk>', DetalhesFilme.as_view(), name='detalhesfilme'),
    path('pesquisa/', PesquisaFilme.as_view(), name='pesquisafilme'),
    path('login/', CustomLoginView.as_view(
        template_name='login.html'), name='login'),
    path('logout/', auth_view.LogoutView.as_view(
        template_name='logout.html'), name='logout'),
    path('editarperfil/', EditarPerfil.as_view(), name='editarperfil'),
    path('criarconta/', CriarConta.as_view(), name='criarconta'),
]
