from django.urls import path, include
from .views import Homepage, HomeFilmes, DetalhesFilme


app_name = 'filme'


urlpatterns = [
    path('', Homepage.as_view(), name='homepage'),
    path('filmes/', HomeFilmes.as_view(), name='homefilmes'),
    path('filmes/<int:pk>', DetalhesFilme.as_view(), name='detalhesfilme'),
]
