from django.apps import apps
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import Usuario
import os


@receiver(post_migrate)
def create_superuser(sender, **kwargs):
    if sender.name == 'filme':
        email = os.getenv("EMAIL_ADMIN")
        senha = os.getenv("SENHA_ADMIN")

        usuarios = Usuario.objects.filter(email=email)
        if not usuarios:
            Usuario.objects.create_superuser(
                username=email, email=email, password=senha, is_active=True, is_staff=True, is_superuser=True)
