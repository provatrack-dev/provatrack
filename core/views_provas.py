from django.shortcuts import render


def prova_lista(request):
    return render(request, 'em_construcao.html', {'titulo': 'Provas'})


def prova_form(request):
    return render(request, 'em_construcao.html', {'titulo': 'Nova prova'})


def prova_detalhe(request, pk):
    return render(request, 'em_construcao.html', {'titulo': 'Detalhes da prova'})