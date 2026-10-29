from django.contrib import admin

from .models import Atleta, Equipe, Prova, Resultado


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


@admin.register(Prova)
class ProvaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'modalidade', 'data', 'local', 'distancia_km', 'status')
    list_filter = ('modalidade', 'status')
    search_fields = ('nome', 'local')


@admin.register(Resultado)
class ResultadoAdmin(admin.ModelAdmin):
    list_display = ('prova', 'posicao', 'atleta', 'tempo', 'pontos')
    list_filter = ('prova',)
    search_fields = ('atleta__nome', 'prova__nome')