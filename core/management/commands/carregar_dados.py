from datetime import datetime, timedelta

from django.core.management.base import BaseCommand
from django.db import transaction

from core.models import Atleta, Equipe, Prova, Resultado

# Dados de exemplo iguais aos dos protótipos (docs/prototipos/).

# (nome, sigla, cidade, uf, modalidade)
EQUIPES = [
    ('Serra Pedal', 'SPE', 'Pau dos Ferros', 'RN', 'ciclismo'),
    ('Atletas do Oeste', 'ADO', 'Mossoró', 'RN', 'atletismo'),
    ('Pedal Potiguar', 'PPO', 'Apodi', 'RN', 'ciclismo'),
    ('Corredores do Alto Oeste', 'CAO', 'Alexandria', 'RN', 'atletismo'),
    ('Sertão Sport', 'SSP', 'Caicó', 'RN', 'ambas'),
]

# (nome, nascimento, sexo, cidade, modalidade, equipe)
# Os 6 primeiros vêm da lista de atletas. Os 5 últimos só aparecem nos resultados e no
# ranking; para eles o protótipo não traz nascimento nem cidade, e o sexo foi deduzido do nome.
ATLETAS = [
    ('Lucas Medeiros', '12/03/1998', 'M', 'Pau dos Ferros', 'ciclismo', 'Serra Pedal'),
    ('Ana Beatriz Lima', '25/07/2001', 'F', 'Mossoró', 'atletismo', 'Atletas do Oeste'),
    ('Rafael Souza', '04/11/1995', 'M', 'Martins', 'ciclismo', 'Serra Pedal'),
    ('Camila Ferreira', '18/01/2000', 'F', 'Alexandria', 'atletismo', 'Atletas do Oeste'),
    ('João Pedro Alves', '30/09/1999', 'M', 'Pau dos Ferros', 'atletismo', None),
    ('Mariana Costa', '09/05/2002', 'F', 'Apodi', 'ciclismo', 'Pedal Potiguar'),
    ('Thiago Nogueira', None, 'M', '', 'atletismo', 'Corredores do Alto Oeste'),
    ('Larissa Duarte', None, 'F', '', 'atletismo', 'Sertão Sport'),
    ('Bruno Carvalho', None, 'M', '', 'atletismo', 'Corredores do Alto Oeste'),
    ('Paula Menezes', None, 'F', '', 'atletismo', 'Sertão Sport'),
    ('Rafaela Gomes', None, 'F', '', 'atletismo', None),
]

# (nome, modalidade, data, local, distancia_km, status, descricao)
PROVAS = [
    ('Volta Ciclística do Seridó', 'ciclismo', '15/11/2026', 'Caicó, RN', '80', 'aberta',
     'Prova de estrada com largada na praça central de Caicó e percurso pelo Seridó potiguar. '
     'Categorias elite, feminino e master.'),
    ('Meia Maratona de Pau dos Ferros', 'atletismo', '22/11/2026', 'Pau dos Ferros, RN', '21.1', 'aberta',
     'Corrida de rua de 21,1 km pelas principais avenidas de Pau dos Ferros.'),
    ('Desafio MTB Serra de Martins', 'ciclismo', '06/12/2026', 'Martins, RN', '45', 'aberta',
     'Prova de mountain bike com subidas e trilhas pela Serra de Martins.'),
    ('Copa Alto Oeste de Ciclismo', 'ciclismo', '12/10/2026', 'Mossoró, RN', '60', 'andamento',
     'Copa de ciclismo de estrada disputada em etapas na região do Alto Oeste.'),
    ('Corrida Rústica do IFRN', 'atletismo', '20/09/2026', 'Pau dos Ferros, RN', '10', 'encerrada',
     'Corrida rústica de 10 km promovida pelo IFRN, com percurso misto de asfalto e terra.'),
    ('Circuito de Pista Alto Oeste', 'atletismo', '30/08/2026', 'Apodi, RN', '5', 'encerrada',
     'Circuito de provas de pista com largadas de 5 km em Apodi.'),
]

# Resultados da Corrida Rústica do IFRN (tela "Resultados por prova"): (atleta, posição, tempo, pontos)
PROVA_RESULTADOS = 'Corrida Rústica do IFRN'
RESULTADOS = [
    ('Ana Beatriz Lima', 1, '00:34:12', 100),
    ('Camila Ferreira', 2, '00:35:48', 80),
    ('Thiago Nogueira', 3, '00:36:30', 65),
    ('Larissa Duarte', 4, '00:37:05', 55),
    ('João Pedro Alves', 5, '00:38:21', 50),
    ('Bruno Carvalho', 6, '00:39:44', 45),
    ('Paula Menezes', 7, '00:41:10', 40),
    ('Rafaela Gomes', 8, '00:43:27', 35),
]


def data_br(texto):
    return datetime.strptime(texto, '%d/%m/%Y').date() if texto else None


def duracao(texto):
    horas, minutos, segundos = (int(parte) for parte in texto.split(':'))
    return timedelta(hours=horas, minutes=minutos, seconds=segundos)


class Command(BaseCommand):
    help = 'Carrega os dados de exemplo dos protótipos (equipes, atletas, provas e resultados).'

    @transaction.atomic
    def handle(self, *args, **options):
        # update_or_create: pode rodar mais de uma vez sem duplicar os dados.
        equipes = {}
        for nome, sigla, cidade, uf, modalidade in EQUIPES:
            equipes[nome], _ = Equipe.objects.update_or_create(
                nome=nome,
                defaults={'sigla': sigla, 'cidade': cidade, 'uf': uf, 'modalidade': modalidade},
            )

        atletas = {}
        for nome, nascimento, sexo, cidade, modalidade, equipe in ATLETAS:
            atletas[nome], _ = Atleta.objects.update_or_create(
                nome=nome,
                defaults={
                    'data_nascimento': data_br(nascimento),
                    'sexo': sexo,
                    'cidade': cidade,
                    'modalidade': modalidade,
                    'equipe': equipes[equipe] if equipe else None,
                },
            )

        provas = {}
        for nome, modalidade, data, local, distancia, status, descricao in PROVAS:
            provas[nome], _ = Prova.objects.update_or_create(
                nome=nome,
                defaults={
                    'modalidade': modalidade,
                    'data': data_br(data),
                    'local': local,
                    'distancia_km': distancia,
                    'status': status,
                    'descricao': descricao,
                },
            )

        for atleta, posicao, tempo, pontos in RESULTADOS:
            Resultado.objects.update_or_create(
                atleta=atletas[atleta],
                prova=provas[PROVA_RESULTADOS],
                defaults={'posicao': posicao, 'tempo': duracao(tempo), 'pontos': pontos},
            )

        self.stdout.write(self.style.SUCCESS(
            f'Dados carregados: {Equipe.objects.count()} equipes, {Atleta.objects.count()} atletas, '
            f'{Prova.objects.count()} provas e {Resultado.objects.count()} resultados.'
        ))