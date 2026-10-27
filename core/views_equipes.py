from django.shortcuts import render

# Dados de exemplo (iguais aos do protótipo). No item 5 viram o model Equipe.
EQUIPES = [
    {'id': 1, 'nome': 'Serra Pedal', 'sigla': 'SPE', 'cidade': 'Pau dos Ferros/RN',
     'modalidade': 'ciclismo', 'modalidade_nome': 'Ciclismo', 'atletas': 18},
    {'id': 2, 'nome': 'Atletas do Oeste', 'sigla': 'ADO', 'cidade': 'Mossoró/RN',
     'modalidade': 'atletismo', 'modalidade_nome': 'Atletismo', 'atletas': 24},
    {'id': 3, 'nome': 'Pedal Potiguar', 'sigla': 'PPO', 'cidade': 'Apodi/RN',
     'modalidade': 'ciclismo', 'modalidade_nome': 'Ciclismo', 'atletas': 12},
    {'id': 4, 'nome': 'Corredores do Alto Oeste', 'sigla': 'CAO', 'cidade': 'Alexandria/RN',
     'modalidade': 'atletismo', 'modalidade_nome': 'Atletismo', 'atletas': 15},
    {'id': 5, 'nome': 'Sertão Sport', 'sigla': 'SSP', 'cidade': 'Caicó/RN',
     'modalidade': 'ambas', 'modalidade_nome': 'Ambas', 'atletas': 21},
]


def equipe_lista(request):
    contexto = {
        'equipes': EQUIPES,
        'mostrando': len(EQUIPES),
        'total': 12,  # total de equipes cadastradas, como no protótipo
    }
    return render(request, 'equipes/lista.html', contexto)


def equipe_form(request):
    # Por enquanto só mostra o formulário; salvar de verdade fica para os próximos itens.
    return render(request, 'equipes/form.html')