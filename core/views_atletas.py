from django.shortcuts import render

# Dados de exemplo (iguais aos do protótipo). No item 5 viram o model Atleta.
ATLETAS = [
    {'id': 1, 'nome': 'Lucas Medeiros', 'iniciais': 'LM', 'sexo': 'Masculino', 'nascimento': '12/03/1998',
     'modalidade': 'ciclismo', 'modalidade_nome': 'Ciclismo', 'cidade': 'Pau dos Ferros', 'equipe': 'Serra Pedal'},
    {'id': 2, 'nome': 'Ana Beatriz Lima', 'iniciais': 'AL', 'sexo': 'Feminino', 'nascimento': '25/07/2001',
     'modalidade': 'atletismo', 'modalidade_nome': 'Atletismo', 'cidade': 'Mossoró', 'equipe': 'Atletas do Oeste'},
    {'id': 3, 'nome': 'Rafael Souza', 'iniciais': 'RS', 'sexo': 'Masculino', 'nascimento': '04/11/1995',
     'modalidade': 'ciclismo', 'modalidade_nome': 'Ciclismo', 'cidade': 'Martins', 'equipe': 'Serra Pedal'},
    {'id': 4, 'nome': 'Camila Ferreira', 'iniciais': 'CF', 'sexo': 'Feminino', 'nascimento': '18/01/2000',
     'modalidade': 'atletismo', 'modalidade_nome': 'Atletismo', 'cidade': 'Alexandria', 'equipe': 'Atletas do Oeste'},
    {'id': 5, 'nome': 'João Pedro Alves', 'iniciais': 'JA', 'sexo': 'Masculino', 'nascimento': '30/09/1999',
     'modalidade': 'atletismo', 'modalidade_nome': 'Atletismo', 'cidade': 'Pau dos Ferros', 'equipe': None},
    {'id': 6, 'nome': 'Mariana Costa', 'iniciais': 'MC', 'sexo': 'Feminino', 'nascimento': '09/05/2002',
     'modalidade': 'ciclismo', 'modalidade_nome': 'Ciclismo', 'cidade': 'Apodi', 'equipe': 'Pedal Potiguar'},
]

# Equipes que aparecem nos selects (vêm do cadastro de Equipes).
EQUIPES_FILTRO = ['Serra Pedal', 'Atletas do Oeste']
EQUIPES_FORM = ['Serra Pedal', 'Atletas do Oeste', 'Pedal Potiguar']


def atleta_lista(request):
    contexto = {
        'atletas': ATLETAS,
        'mostrando': len(ATLETAS),
        'total': 128,  # total de atletas cadastrados, como no protótipo
        'equipes': EQUIPES_FILTRO,
    }
    return render(request, 'atletas/lista.html', contexto)


def atleta_form(request):
    # Por enquanto só mostra o formulário; salvar de verdade fica para os próximos itens.
    return render(request, 'atletas/form.html', {'equipes': EQUIPES_FORM})