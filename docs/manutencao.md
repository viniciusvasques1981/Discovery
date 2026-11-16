# Manutenção do repositório

Este arquivo reúne o que só interessa a quem altera o repositório. As regras de execução da esteira estão em [AGENTS.md](../AGENTS.md).

## Fonte única

`esteira.json` descreve módulos, etapas opcionais, componentes transversais, os modelos e scripts de cada skill e o nível de modelo de cada agente. A partir dele, `esteira.py sync` gera:

| Destino | Conteúdo gerado |
| :--- | :--- |
| `AGENTS.md` | Tabela de módulos, skills, agentes e artefatos |
| `README.md` | Tabela de módulos e tabela de componentes transversais, com links |
| `docs/mapa-da-esteira.md` | As mesmas tabelas, com links relativos a `docs/` |
| `skills/esteira-orchestration/SKILL.md` | Tabela de delegação, com revisão e aprovador por módulo |
| `skills/<skill>/assets/` | Cópia dos modelos de `templates/` usados pela skill |
| `skills/<skill>/scripts/` | Cópia dos scripts de `scripts/` usados pela skill |

As tabelas ficam entre marcadores `<!-- gerado:nome -->` e `<!-- /gerado:nome -->`. Não edite o conteúdo entre eles: altere `esteira.json` e execute o `sync`.

## Comandos

| Comando | Função |
| :--- | :--- |
| `python3 scripts/esteira.py sync` | Gera as tabelas e copia modelos e scripts para as skills |
| `python3 scripts/esteira.py validate` | Valida registro, frontmatter, referências, cópias, tabelas e links |
| `python3 scripts/esteira.py package` | Gera `dist/<skill>.zip` para upload em aplicativos de chat |
| `python3 scripts/esteira.py install <plataforma> <dir>` | Copia skills e agentes para um projeto |
| `python3 scripts/iniciativa.py verificar iniciativas/exemplo-reserva-salas` | Confere a iniciativa de exemplo |

A validação e a verificação do exemplo rodam em cada push e pull request (`.github/workflows/validate.yml`).

## O que a validação detecta

- Skill ou agente presente em pasta e ausente de `esteira.json`, e o inverso. Um agente removido do registro e esquecido em `agents/` é apontado como órfão.
- Tabela gerada desatualizada em qualquer um dos quatro arquivos.
- Cópia de modelo ou de script diferente da fonte.
- Referência, em skill ou agente, a skill ou agente inexistente.
- `model:` fixado no arquivo canônico de um agente.
- Contagem de skills e agentes em `docs/index.html` diferente da real.
- Link relativo quebrado em qualquer Markdown.

## Rotinas

**Alterar um modelo de artefato.** Edite em `templates/` e execute `sync`. Se mudar rótulos lidos pelos scripts (títulos `### FF-01 — nome`, `### ISSUE FF-01 — título`, linhas `| **Solução** |`, `| **MVP** |`, colunas da Matriz de priorização, linhas `| KR1 — ...`), ajuste `scripts/iniciativa.py`.

**Criar uma skill.** Crie `skills/<nome>/SKILL.md` com `name` igual ao nome da pasta e `description` dizendo o que faz e quando usar. Registre a skill em `esteira.json`, em `skills` (modelos e scripts) e em um módulo ou componente transversal. Execute `sync` e `validate`.

**Criar ou remover um agente.** Crie ou apague o arquivo em `agents/` e ajuste `esteira.json` em `modulos`/`transversais` e em `modelos.papeis`.

**Alterar uma skill.** Reexecute o módulo correspondente sobre `iniciativas/exemplo-reserva-salas/00-insumos/` e compare com o artefato do exemplo.

**Alterar a página `docs/index.html`.** Ela não é gerada. A validação confere apenas as contagens de skills e agentes.

## Skill ou agente

Critério em [mapa-da-esteira.md](mapa-da-esteira.md), seção "Skill ou agente".

## Nível de modelo por agente

Os arquivos em `agents/` não fixam modelo, porque cada plataforma usa nomes diferentes. O nível de cada agente (`leve`, `padrao`, `avancado`) fica em `esteira.json > modelos.papeis`, e o nome do modelo por plataforma em `modelos.plataformas`. O comando `install` grava `model:` no agente copiado quando há nome definido para a plataforma; valor vazio mantém o modelo da sessão.
