# ProvaTrack

Sistema web para gerenciar provas de ciclismo e atletismo: atletas, equipes, provas, resultados e ranking geral.

Projeto da disciplina de Desenvolvimento de Sistemas Web, IFRN, Campus Pau dos Ferros.

## Sobre o sistema

Organizar uma prova esportiva costuma envolver planilhas e mensagens soltas: quem participa, de qual equipe, quanto tempo fez e quem ganhou. O ProvaTrack reúne tudo em um só lugar: cadastro de atletas e equipes, criação de provas, lançamento de resultados e consulta do ranking geral.

## Documentação

Requisitos, casos de uso, entidades, protótipos e organização do projeto estão no **[Wiki](https://github.com/provatrack-dev/provatrack/wiki)**.

- [Documento de requisitos](docs/requisitos.md)
- [Diagrama de casos de uso](docs/casos-de-uso.md)

## Tecnologias

Python 3.12 ou mais recente, Django, SQLite, HTML e CSS.

## Como executar

Você precisa ter o Python (3.12 ou mais recente) e o Git instalados.

1. Baixe o projeto e entre na pasta:
   ```bash
   git clone https://github.com/provatrack-dev/provatrack.git
   cd provatrack
   ```
2. Crie e ative o ambiente virtual:
   ```bash
   python -m venv venv
   venv\Scripts\activate          # Windows
   source venv/bin/activate       # Linux ou macOS
   ```
3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
4. Crie o banco de dados (SQLite):
   ```bash
   python manage.py migrate
   ```
5. Crie um usuário para entrar no sistema e no Django Admin:
   ```bash
   python manage.py createsuperuser
   ```
6. Carregue os dados de exemplo (equipes, atletas, provas e resultados dos protótipos):

```
python manage.py carregar_dados
```

O comando cadastra 5 equipes, 11 atletas, 6 provas e 8 resultados (os da Corrida Rústica do IFRN) e pode ser rodado mais de uma vez sem duplicar os dados. O passo é opcional, mas ajuda a testar as telas e o Django Admin.

7. Inicie o servidor:

```
python manage.py runserver
```

Depois acesse:

- Sistema: http://127.0.0.1:8000/
- Django Admin (cadastro dos dados): http://127.0.0.1:8000/admin/

## Equipe

- Samuel ([SamuelFCD](https://github.com/SamuelFCD))
- Vitor ([gabrieldntss](https://github.com/gabrieldntss))