from django.http import Http404
from django.shortcuts import render

# Dados de exemplo (iguais aos do protótipo). No item 5 viram o model Prova.
PROVAS = [
    {
        'id': 1, 'nome': 'Volta Ciclística do Seridó', 'modalidade': 'ciclismo', 'modalidade_nome': 'Ciclismo',
        'data': '15/11/2026', 'local': 'Caicó, RN', 'distancia': '80 km',
        'status': 'aberta', 'status_nome': 'Inscrições abertas', 'inscritos': 12,
        'descricao': 'Prova de estrada com largada na praça central de Caicó e percurso pelo Seridó potiguar. '
                     'Categorias elite, feminino e master.',
    },
    {
        'id': 2, 'nome': 'Meia Maratona de Pau dos Ferros', 'modalidade': 'atletismo', 'modalidade_nome': 'Atletismo',
        'data': '22/11/2026', 'local': 'Pau dos Ferros, RN', 'distancia': '21,1 km',
        'status': 'aberta', 'status_nome': 'Inscrições abertas', 'inscritos': 48,
        'descricao': 'Corrida de rua de 21,1 km pelas principais avenidas de Pau dos Ferros.',
    },
    {
        'id': 3, 'nome': 'Desafio MTB Serra de Martins', 'modalidade': 'ciclismo', 'modalidade_nome': 'Ciclismo',
        'data': '06/12/2026', 'local': 'Martins, RN', 'distancia': '45 km',
        'status': 'aberta', 'status_nome': 'Inscrições abertas', 'inscritos': 30,
        'descricao': 'Prova de mountain bike com subidas e trilhas pela Serra de Martins.',
    },
    {
        'id': 4, 'nome': 'Copa Alto Oeste de Ciclismo', 'modalidade': 'ciclismo', 'modalidade_nome': 'Ciclismo',
        'data': '12/10/2026', 'local': 'Mossoró, RN', 'distancia': '60 km',
        'status': 'andamento', 'status_nome': 'Em andamento', 'inscritos': 25,
        'descricao': 'Copa de ciclismo de estrada disputada em etapas na região do Alto Oeste.',
    },
    {
        'id': 5, 'nome': 'Corrida Rústica do IFRN', 'modalidade': 'atletismo', 'modalidade_nome': 'Atletismo',
        'data': '20/09/2026', 'local': 'Pau dos Ferros, RN', 'distancia': '10 km',
        'status': 'encerrada', 'status_nome': 'Encerrada', 'inscritos': 60,
        'descricao': 'Corrida rústica de 10 km promovida pelo IFRN, com percurso misto de asfalto e terra.',
    },
    {
        'id': 6, 'nome': 'Circuito de Pista Alto Oeste', 'modalidade': 'atletismo', 'modalidade_nome': 'Atletismo',
        'data': '30/08/2026', 'local': 'Apodi, RN', 'distancia': '5 km',
        'status': 'encerrada', 'status_nome': 'Encerrada', 'inscritos': 18,
        'descricao': 'Circuito de provas de pista com largadas de 5 km em Apodi.',
    },
]


def prova_lista(request):
    contexto = {
        'provas': PROVAS,
        'total': len(PROVAS),
        'abertas': len([p for p in PROVAS if p['status'] == 'aberta']),
        'andamento': len([p for p in PROVAS if p['status'] == 'andamento']),
        'ciclismo': len([p for p in PROVAS if p['modalidade'] == 'ciclismo']),
        'atletismo': len([p for p in PROVAS if p['modalidade'] == 'atletismo']),
    }
    return render(request, 'provas/lista.html', contexto)


def prova_detalhe(request, pk):
    for prova in PROVAS:
        if prova['id'] == pk:
            return render(request, 'provas/detalhe.html', {'prova': prova})
    raise Http404('Prova não encontrada')


def prova_form(request):
    # Por enquanto só mostra o formulário; salvar de verdade fica para os próximos itens.
    return render(request, 'provas/form.html')