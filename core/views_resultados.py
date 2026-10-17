from django.shortcuts import render


def resultado_lista(request):
    return render(request, 'em_construcao.html', {'titulo': 'Resultados'})


def resultado_form(request):
    return render(request, 'em_construcao.html', {'titulo': 'Novo resultado'})


def ranking_geral(request):
    return render(request, 'em_construcao.html', {'titulo': 'Ranking geral'})