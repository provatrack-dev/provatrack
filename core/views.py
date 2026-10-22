from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def login_view(request):
    # Por enquanto só mostra o formulário; autenticar de verdade fica para os próximos itens.
    return render(request, 'login.html')