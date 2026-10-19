from django.shortcuts import render

# Dados de exemplo (iguais aos dos protótipos). Nos próximos itens viram o model Resultado.
PROVAS_OPCOES = ['Corrida Rústica do IFRN', 'Circuito de Pista Alto Oeste', 'Copa Alto Oeste de Ciclismo']

PROVA_SELECIONADA = {
    'modalidade': 'Atletismo', 'data': '20/09/2026', 'local': 'Pau dos Ferros, RN',
    'distancia': '10 km', 'status': 'Encerrada',
}

# Equipe vazia ('') = atleta avulso
RESULTADOS = [
    {'pos': 1, 'iniciais': 'AL', 'nome': 'Ana Beatriz Lima', 'equipe': 'Atletas do Oeste', 'tempo': '00:34:12', 'pontos': 100},
    {'pos': 2, 'iniciais': 'CF', 'nome': 'Camila Ferreira', 'equipe': 'Atletas do Oeste', 'tempo': '00:35:48', 'pontos': 80},
    {'pos': 3, 'iniciais': 'TN', 'nome': 'Thiago Nogueira', 'equipe': 'Corredores do Alto Oeste', 'tempo': '00:36:30', 'pontos': 65},
    {'pos': 4, 'iniciais': 'LD', 'nome': 'Larissa Duarte', 'equipe': 'Sertão Sport', 'tempo': '00:37:05', 'pontos': 55},
    {'pos': 5, 'iniciais': 'JA', 'nome': 'João Pedro Alves', 'equipe': '', 'tempo': '00:38:21', 'pontos': 50},
    {'pos': 6, 'iniciais': 'BC', 'nome': 'Bruno Carvalho', 'equipe': 'Corredores do Alto Oeste', 'tempo': '00:39:44', 'pontos': 45},
    {'pos': 7, 'iniciais': 'PM', 'nome': 'Paula Menezes', 'equipe': 'Sertão Sport', 'tempo': '00:41:10', 'pontos': 40},
    {'pos': 8, 'iniciais': 'RG', 'nome': 'Rafaela Gomes', 'equipe': '', 'tempo': '00:43:27', 'pontos': 35},
]

# modalidade: 'cic' = Ciclismo, 'atl' = Atletismo
RANKING = [
    {'pos': 1, 'iniciais': 'LM', 'nome': 'Lucas Medeiros', 'equipe': 'Serra Pedal', 'modalidade': 'cic', 'modalidade_nome': 'Ciclismo', 'provas': 4, 'pontos': 320},
    {'pos': 2, 'iniciais': 'AL', 'nome': 'Ana Beatriz Lima', 'equipe': 'Atletas do Oeste', 'modalidade': 'atl', 'modalidade_nome': 'Atletismo', 'provas': 4, 'pontos': 295},
    {'pos': 3, 'iniciais': 'RS', 'nome': 'Rafael Souza', 'equipe': 'Serra Pedal', 'modalidade': 'cic', 'modalidade_nome': 'Ciclismo', 'provas': 4, 'pontos': 270},
    {'pos': 4, 'iniciais': 'CF', 'nome': 'Camila Ferreira', 'equipe': 'Atletas do Oeste', 'modalidade': 'atl', 'modalidade_nome': 'Atletismo', 'provas': 3, 'pontos': 240},
    {'pos': 5, 'iniciais': 'MC', 'nome': 'Mariana Costa', 'equipe': 'Pedal Potiguar', 'modalidade': 'cic', 'modalidade_nome': 'Ciclismo', 'provas': 3, 'pontos': 215},
    {'pos': 6, 'iniciais': 'JA', 'nome': 'João Pedro Alves', 'equipe': '', 'modalidade': 'atl', 'modalidade_nome': 'Atletismo', 'provas': 3, 'pontos': 190},
    {'pos': 7, 'iniciais': 'TN', 'nome': 'Thiago Nogueira', 'equipe': 'Corredores do Alto Oeste', 'modalidade': 'atl', 'modalidade_nome': 'Atletismo', 'provas': 2, 'pontos': 170},
    {'pos': 8, 'iniciais': 'LD', 'nome': 'Larissa Duarte', 'equipe': 'Sertão Sport', 'modalidade': 'atl', 'modalidade_nome': 'Atletismo', 'provas': 2, 'pontos': 150},
]


def resultado_lista(request):
    contexto = {
        'provas_opcoes': PROVAS_OPCOES,
        'prova': PROVA_SELECIONADA,
        'resultados': RESULTADOS,
        'participantes': len(RESULTADOS),
        'vencedor': RESULTADOS[0]['nome'],
        'melhor_tempo': RESULTADOS[0]['tempo'],
    }
    return render(request, 'resultados/lista.html', contexto)


def resultado_form(request):
    # Por enquanto só mostra o formulário; salvar de verdade fica para os próximos itens.
    contexto = {
        'provas_opcoes': PROVAS_OPCOES,
        'atletas_opcoes': ['Ana Beatriz Lima', 'Camila Ferreira', 'Lucas Medeiros'],
    }
    return render(request, 'resultados/form.html', contexto)


def ranking_geral(request):
    maior = RANKING[0]['pontos']
    ranking = [dict(item, barra=round(item['pontos'] * 100 / maior)) for item in RANKING]
    # Pódio na ordem do protótipo: 2º, 1º e 3º (o 1º fica no meio e maior)
    podio = [
        {'item': ranking[1], 'cor': '#98a2b3', 'classe': ''},
        {'item': ranking[0], 'cor': '#FF6B35', 'classe': 'primeiro'},
        {'item': ranking[2], 'cor': '#b97a4b', 'classe': ''},
    ]
    contexto = {'ranking': ranking, 'podio': podio, 'total_atletas': 128}
    return render(request, 'resultados/ranking.html', contexto)