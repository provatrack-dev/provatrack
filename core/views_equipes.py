from django.shortcuts import render


def equipe_lista(request):
    return render(request, 'em_construcao.html', {'titulo': 'Equipes'})


def equipe_form(request):
    return render(request, 'em_construcao.html', {'titulo': 'Nova equipe'})