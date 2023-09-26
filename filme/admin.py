from django.contrib import admin
from .models import Filme, Episodio, Usuario
from django.contrib.auth.admin import UserAdmin

# Os campos do UserAdmin são tuplas, desta forma transformei em lista python para incluir o novo campo
# de filmes vistos.
campos = list(UserAdmin.fieldsets)
campos.append(
    ("Histórico", {'fields': ('filmes_vistos',)})
)

UserAdmin.fieldsets = tuple(campos)

# Register your models here.
admin.site.register(Filme)
admin.site.register(Episodio)
admin.site.register(Usuario, UserAdmin)
