from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def login_view(request):
    # Provisória: o Vitor troca por login.html na issue da tela de login
    return render(request, 'em_construcao.html', {'titulo': 'Entrar'})