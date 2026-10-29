Código-fonte deste documento versionado em [`docs/requisitos.md`](https://github.com/provatrack-dev/provatrack/blob/main/docs/requisitos.md).

# Documento de requisitos do ProvaTrack

Estrutura baseada no documento de requisitos e no documento de visão vistos na disciplina de Engenharia de Software (Prof. Ciro Moura).

## 1. Introdução

### 1.1 Finalidade
Descrever o que o ProvaTrack deve fazer (requisitos funcionais) e as restrições sob as quais deve funcionar (requisitos não funcionais).

### 1.2 Escopo
O ProvaTrack é um sistema web para gerenciar provas de ciclismo e atletismo: equipes, atletas, provas, resultados e ranking geral.

**Fora do escopo:** inscrição online de atletas pelo público, pagamentos e taxas de inscrição, cronometragem em tempo real.

### 1.3 Definições

| Termo | Significado |
|---|---|
| Organizador | Pessoa que organiza as provas e tem login para cadastrar e alterar dados |
| Visitante | Pessoa sem login, que apenas consulta as informações |
| Atleta avulso | Atleta que não pertence a nenhuma equipe |
| Ranking geral | Classificação dos atletas pela soma dos pontos de todas as provas |

### 1.4 Referências
- Proposta de Projeto de Desenvolvimento de Sistemas Web (IFRN)
- [[Entidades]] · [[Layout base]] · [[Protótipos|Prototipos]]
- [[Casos de uso]]

## 2. Posicionamento

### 2.1 Descrição do problema
Organizar uma prova esportiva costuma envolver planilhas e mensagens soltas: quem participa, de qual equipe, quanto tempo fez e quem ganhou. As informações ficam espalhadas, difíceis de consultar e sujeitas a erro.

### 2.2 Envolvidos e usuários

| Perfil | Interesse no sistema |
|---|---|
| Organizador | Cadastrar atletas, equipes, provas e resultados com rapidez e sem erro |
| Visitante (atletas, equipes e público) | Consultar provas, resultados e ranking |
| Equipe de desenvolvimento (Samuel e Vitor) | Entregar o sistema conforme a proposta da disciplina |
| Professor | Avaliar o sistema, o repositório e o quadro de tarefas |

## 3. Requisitos funcionais

Prioridade: **Alta** = essencial para o sistema funcionar; **Média** = importante, mas o sistema funciona sem ela.

| ID | Requisito | Ator | Prioridade |
|---|---|---|---|
| RF01 | O sistema deve permitir que o Organizador entre com usuário e senha e saia do sistema. | Organizador | Alta |
| RF02 | O sistema deve permitir cadastrar, listar, editar e excluir atletas. | Organizador | Alta |
| RF03 | O sistema deve permitir cadastrar, listar, editar e excluir equipes. | Organizador | Alta |
| RF04 | O sistema deve permitir cadastrar, listar, editar e excluir provas. | Organizador | Alta |
| RF05 | O sistema deve permitir lançar, editar e excluir o resultado de um atleta em uma prova (posição, tempo e pontos). | Organizador | Alta |
| RF06 | O sistema deve listar os atletas e permitir filtrar por modalidade e por equipe. | Visitante, Organizador | Média |
| RF07 | O sistema deve listar as equipes. | Visitante, Organizador | Média |
| RF08 | O sistema deve listar as provas e permitir filtrar por modalidade e por status. | Visitante, Organizador | Alta |
| RF09 | O sistema deve exibir os detalhes de uma prova (nome, modalidade, data, local, distância, status e descrição). | Visitante, Organizador | Alta |
| RF10 | O sistema deve exibir a classificação final de cada prova (posição, atleta, equipe, tempo e pontos). | Visitante, Organizador | Alta |
| RF11 | O sistema deve exibir o ranking geral, somando os pontos de cada atleta em todas as provas, e permitir filtrar por modalidade. | Visitante, Organizador | Alta |
| RF12 | O sistema deve exibir mensagem de confirmação após cadastrar, editar ou excluir um registro. | Organizador | Média |

## 4. Regras de negócio

| ID | Regra |
|---|---|
| RN01 | Um atleta só pode ter **um** resultado por prova. |
| RN02 | O atleta pode não ter equipe (atleta avulso). |
| RN03 | Ao excluir uma equipe, os atletas dela continuam cadastrados, como avulsos. |
| RN04 | Atleta ou prova que já tenha resultado lançado não pode ser excluído. |
| RN05 | O ranking geral ordena os atletas pela soma de pontos, do maior para o menor. |
| RN06 | Só o Organizador logado pode cadastrar, editar ou excluir dados. As contas são criadas pelo administrador no Django Admin (não há cadastro pelo público). |

## 5. Requisitos não funcionais

Escritos de forma mensurável, para poderem ser testados.

| ID | Categoria | Requisito |
|---|---|---|
| RNF01 | Desempenho | Cada tela deve carregar em até 3 segundos, com até 500 registros cadastrados. |
| RNF02 | Segurança | As senhas devem ser armazenadas com hash (sistema de usuários do Django). |
| RNF03 | Segurança | Todo formulário que envia dados deve usar método POST com token CSRF. |
| RNF04 | Segurança | As telas de cadastro, edição e exclusão devem exigir login (RN06). |
| RNF05 | Usabilidade | Qualquer tela do menu deve ser acessada em no máximo 2 cliques a partir do início. |
| RNF06 | Usabilidade | Todas as telas devem seguir os protótipos e o layout base (paleta, fonte Inter, navbar e rodapé). |
| RNF07 | Compatibilidade | O sistema deve funcionar nas versões atuais do Chrome e do Firefox. |
| RNF08 | Persistência | Os dados devem ficar gravados em banco de dados (SQLite) e não podem ser perdidos ao reiniciar o servidor. |
| RNF09 | Tecnologia | O sistema deve ser feito em Python com Django, HTML e CSS. |
| RNF10 | Manutenção | O código deve ficar versionado no GitHub, com README explicando como instalar e executar. |
| RNF11 | Idioma | Toda a interface deve estar em português do Brasil. |

## 6. Restrições
- Projeto feito em dupla, com prazo parcial em 30/10/2026 e final em 03/12/2026.
- Uso de GitHub Projects (Kanban) para organizar as tarefas.
