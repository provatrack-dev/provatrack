from django.urls import path

from . import views, views_atletas, views_equipes, views_provas, views_resultados

urlpatterns = [
    # Início e login
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),

    # Atletas
    path('atletas/', views_atletas.atleta_lista, name='atleta_lista'),
    path('atletas/novo/', views_atletas.atleta_form, name='atleta_form'),

    # Equipes
    path('equipes/', views_equipes.equipe_lista, name='equipe_lista'),
    path('equipes/nova/', views_equipes.equipe_form, name='equipe_form'),

    # Provas
    path('provas/', views_provas.prova_lista, name='prova_lista'),
    path('provas/nova/', views_provas.prova_form, name='prova_form'),
    path('provas/<int:pk>/', views_provas.prova_detalhe, name='prova_detalhe'),

    # Resultados e ranking
    path('resultados/', views_resultados.resultado_lista, name='resultado_lista'),
    path('resultados/novo/', views_resultados.resultado_form, name='resultado_form'),
    path('ranking/', views_resultados.ranking_geral, name='ranking_geral'),
]