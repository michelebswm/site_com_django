from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser


LISTA_CATEGORIAS = (
    ('ANALISES', 'Análises'),
    ('PROGRAMACAO', 'Programação'),
    ('APRESENTACAO', 'Apresentação'),
    ('OUTROS', 'Outros'),
    {'ANIMES', 'Animes'},
    ['FILME_A', 'Filme de Ação'],
)


class Filme(models.Model):
    titulo = models.CharField(max_length=100)
    thumb = models.ImageField(upload_to='thumb_filmes')
    descricao = models.TextField(max_length=1000)
    categoria = models.CharField(
        max_length=15, choices=LISTA_CATEGORIAS)   # Lista de Opções
    visualizacoes = models.IntegerField(default=0)
    # Registrar data e hora que o filme for criado
    data_criacao = models.DateTimeField(default=timezone.now)

    # Formato de string de um objeto dessa classe Filme
    def __str__(self):
        return self.titulo


class Episodio(models.Model):
    # parametos do ForeignKey, "nome_da_tabela", related_name relaciona os episodios ao filme, on_delete se deletar o filme os episodios também sao deletados
    filme = models.ForeignKey(
        "Filme", related_name="episodios", on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    video = models.URLField()

    def __str__(self):
        return self.filme.titulo + ' - ' + self.titulo


class Usuario(AbstractUser):
    filmes_vistos = models.ManyToManyField('Filme')
