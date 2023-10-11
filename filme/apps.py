from django.apps import AppConfig

# Importe o arquivo signals.py
from . import signals


class FilmeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'filme'
