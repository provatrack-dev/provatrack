from django.contrib import admin

from .models import Atleta, Equipe


@admin.register(Equipe)
class EquipeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sigla', 'cidade', 'uf', 'modalidade')
    list_filter = ('modalidade',)
    search_fields = ('nome', 'sigla')


@admin.register(Atleta)
class AtletaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sexo', 'modalidade', 'cidade', 'equipe')
    list_filter = ('modalidade', 'sexo', 'equipe')
    search_fields = ('nome', 'cidade')