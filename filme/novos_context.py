from .models import Filme


def lista_filmes_recentes(request):
    # Lista de todos os filmes ordenados em ordem de data_criacao decrescente colocando -data_criacao
    lista_filmes = Filme.objects.all().order_by(
        '-data_criacao')[0:10]  # Pegando os 10 primeiros
    return {"lista_filmes_recentes": lista_filmes}


def lista_filmes_emalta(request):
    lista_filmes = Filme.objects.all().order_by('-visualizacoes')[0:10]
    return {"lista_filmes_emalta": lista_filmes}
