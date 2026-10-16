from django.shortcuts import render


def atleta_lista(request):
    return render(request, 'em_construcao.html', {'titulo': 'Atletas'})


def atleta_form(request):
    return render(request, 'em_construcao.html', {'titulo': 'Novo atleta'})