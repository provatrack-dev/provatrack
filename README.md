# ProvaTrack

Sistema web para gerenciamento de provas de ciclismo e atletismo: atletas, equipes, provas e resultados em um só lugar.

Projeto da disciplina de Desenvolvimento de Sistemas Web, IFRN, Campus Pau dos Ferros.

## Ideia do projeto

Organizar uma prova esportiva costuma envolver planilhas e mensagens soltas: quem está inscrito, de qual equipe, quanto tempo fez e quem ganhou. O ProvaTrack centraliza essas informações em um único sistema, para cadastrar atletas e equipes, criar provas, registrar os resultados e consultar o ranking geral.

## Escopo

**O sistema faz:**
- Cadastro, listagem, edição e exclusão de atletas
- Cadastro, listagem, edição e exclusão de equipes
- Cadastro e listagem de provas, com filtro por modalidade e página de detalhes
- Registro de resultados por prova (posição, tempo e pontos)
- Ranking geral dos atletas por pontos
- Login de usuários

**O sistema não faz (fora do escopo):**
- Inscrição online de atletas pelo público
- Pagamentos e taxas de inscrição
- Cronometragem em tempo real

## Entidades

| Entidade | Descrição | Principais campos |
|---|---|---|
| Equipe | Grupo ao qual os atletas pertencem | nome, sigla, cidade, uf, modalidade |
| Atleta | Participante das provas | nome, data de nascimento, sexo, cidade, modalidade, equipe |
| Prova | Competição de ciclismo ou atletismo | nome, modalidade, data, local, distância, status |
| Resultado | Desempenho de um atleta em uma prova | atleta, prova, posição, tempo, pontos |

Relacionamentos: uma equipe tem vários atletas, e um atleta tem vários resultados. Uma prova gera vários resultados, um por atleta. Detalhes e diagrama em [docs/entidades.md](docs/entidades.md).

## Tecnologias

- Python e Django
- HTML e CSS
- Git e GitHub (issues, board, pull requests)

## Equipe

- Samuel Oliveira
- [NOME COMPLETO DO VITOR]

## Como executar

```bash
git clone https://github.com/provatrack-dev/provatrack.git
cd provatrack
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py runserver
```

Depois acesse http://127.0.0.1:8000/