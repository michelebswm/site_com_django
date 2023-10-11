from django.apps import AppConfig

# Importe o arquivo signals.py
from . import ready


class FilmeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'filme'

    def ready(self):
        ready.connect_signals()
