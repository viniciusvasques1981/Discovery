# Instalação e uso por plataforma

O conteúdo canônico está em `skills/` e `agents/`. Os formatos seguem o padrão aberto de Agent Skills (`SKILL.md` com frontmatter `name` e `description`) e de agentes em Markdown com frontmatter, lidos por Claude Code, Gemini CLI e GitHub Copilot.

> Os comandos abaixo seguem a documentação pública de cada ferramenta consultada em novembro de 2026. Não foram executados nas três plataformas durante a montagem deste repositório; valide a instalação no seu ambiente.

## Resumo

| Plataforma | Forma de instalação | Skills | Agentes | Instruções gerais |
| :--- | :--- | :--- | :--- | :--- |
| Claude Code | Plugin (`.claude-plugin/plugin.json`) ou cópia para `.claude/` | `skills/` | `agents/` | `CLAUDE.md` → `AGENTS.md` |
| Gemini CLI | Extensão (`gemini-extension.json`) ou cópia para `.gemini/` | `skills/` | `agents/` (recurso em preview) | `GEMINI.md` → `AGENTS.md` |
| GitHub Copilot | Cópia para `.github/` | `.github/skills/` | `.github/agents/*.agent.md` | `AGENTS.md` |
| Gemini (app) / Claude (app) | Upload do `.zip` de cada skill | `dist/*.zip` | Colar o conteúdo do agente como instrução | — |

## Claude Code

Como plugin, a partir de um clone local:

```bash
git clone https://github.com/viniciusvasques1981/Discovery.git
claude --plugin-dir ./Discovery
```

Como arquivos de projeto:

```bash
./Discovery/scripts/install.sh claude /caminho/do/projeto
```

Uso: as skills são ativadas pela descrição ou por nome (`/discovery-product-strategy`). Os agentes ficam disponíveis para delegação; para iniciar pela coordenação, peça o agente `esteira-orchestrator`.

## Gemini CLI

Como extensão:

```bash
gemini extensions install https://github.com/viniciusvasques1981/Discovery
```

Para desenvolvimento local, com alterações refletidas sem reinstalar:

```bash
gemini extensions link ./Discovery
```

Como arquivos de projeto:

```bash
./Discovery/scripts/install.sh gemini /caminho/do/projeto
```

Subagentes em extensões do Gemini CLI são um recurso em preview. Se os agentes não forem carregados, use as skills diretamente; o encadeamento entre módulos está descrito em `AGENTS.md`.

## GitHub Copilot

```bash
./Discovery/scripts/install.sh copilot /caminho/do/projeto
```

O script copia as skills para `.github/skills/` e os agentes para `.github/agents/` com a extensão `.agent.md`. O Copilot também lê `AGENTS.md` na raiz do projeto; copie-o se quiser as regras gerais da esteira.

## Aplicativos de chat (Gemini, Claude)

Gere um `.zip` por skill:

```bash
python3 scripts/esteira.py package
```

Os arquivos são gravados em `dist/`. Cada `.zip` contém a pasta da skill com `SKILL.md` e `assets/`, pronto para upload na área de skills do aplicativo.

Em ferramentas sem suporte a skills (por exemplo, um Gem ou um Project com instruções personalizadas), cole o conteúdo do `SKILL.md` do módulo como instrução e anexe o modelo correspondente de `templates/`. A passagem de contexto é manual: ao iniciar um módulo, cole o `contexto.md` atualizado, conforme a Regra de Ouro do guia.

## Manutenção

| Comando | Função |
| :--- | :--- |
| `python3 scripts/esteira.py sync` | Copia `templates/` para `skills/<skill>/assets/` |
| `python3 scripts/esteira.py validate` | Valida frontmatter, referências entre skills e agentes, sincronização de modelos e links |
| `python3 scripts/esteira.py package` | Gera `dist/<skill>.zip` |

`templates/` é a fonte única dos modelos. Após editar um modelo, execute `sync`. A validação roda em cada push e pull request (`.github/workflows/validate.yml`).
