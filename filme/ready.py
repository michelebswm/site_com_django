from django.apps import apps
from . import signals


def connect_signals():
    if apps.is_installed('filme'):
        signals.create_superuser(sender=None)
