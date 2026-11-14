# Esteira de Produto AI-Enhanced — instruções para agentes

Este repositório contém agentes e skills que executam uma esteira de produto do Discovery ao Handoff técnico, com ciclo de medição e experimentação pós-entrega. O processo de referência está em `docs/guia-da-esteira.md`.

## Estrutura

| Caminho | Conteúdo |
| :--- | :--- |
| `skills/<nome>/SKILL.md` | Método de cada módulo: algoritmo de execução e padrão de entrega |
| `skills/<nome>/assets/` | Modelos de artefato usados pela skill (cópia de `templates/`) |
| `agents/<nome>.md` | Papéis: entradas, conduta e critério de conclusão |
| `templates/` | Fonte única dos modelos de artefato |
| `iniciativas/<slug>/` | Artefatos produzidos para cada iniciativa |
| `docs/` | Guia do processo, mapa da esteira e instalação |

## Módulos

| Módulo | Skill | Agente | Artefato |
| :--- | :--- | :--- | :--- |
| 1 — Discovery | `discovery-product-strategy` | `discovery-strategist` | `01-discovery.md` |
| 2 — Estratégia | `discovery-product-strategy` | `discovery-strategist` | `02-estrategia.md` |
| 3 — Modelagem | `behavioral-modeling-feature-framing` | `experience-modeler` | `03-modelagem.md` |
| 4 — Feature Frame | `behavioral-modeling-feature-framing` | `experience-modeler` | `04-feature-frames.md` |
| 5 — Prototipação | `systemic-ui-interaction-design` | `interface-designer` | `05-prototipacao.md` |
| 6 — Handoff | `technical-handoff-prompt-engineering` | `handoff-tech-lead` | `06-handoff.md` |
| 7 — Medição | `behavioral-analytics-ux-fixes` | `growth-analyst` | `07-diagnostico-comportamental.md` |
| 8 — Experimentação | `behavioral-experimentation-cro` | `growth-analyst` | `08-experimentos.md` |

Coordenação: `esteira-orchestrator`. Apoio em qualquer módulo: `get-more-perspectives` e `match-my-writing-style`.

## Regras gerais

1. **Regra de Ouro.** Nenhum módulo começa sem ler `iniciativas/<slug>/contexto.md`. Todo módulo termina atualizando esse arquivo.
2. **Rastreabilidade.** O Por quê definido no Módulo 2 deve constar em cada issue do Módulo 6. Cada Feature Frame aponta para um estágio da Jornada To-Be e um Key Result.
3. **Out of Scope imutável.** Os limites definidos no Módulo 4 são transcritos literalmente até o Módulo 6.
4. **Fato e inferência.** Conteúdo não sustentado pelos insumos recebe a marca `[inferência]`. Dados ausentes não são estimados: registrar como Dúvida, `[pendente de dados]` ou `[a validar com o time técnico]`.
5. **Um módulo por vez.** Apresentar o resultado e aguardar validação do usuário antes de avançar.
6. **Idioma.** Artefatos em português do Brasil. Sintaxe Gherkin com `# language: pt`.
7. **Formato.** Markdown, seguindo o modelo em `assets/` da skill.

## Estrutura de uma iniciativa

```text
iniciativas/<slug>/
├── 00-insumos/                      material bruto (transcrições, notas, documentos)
├── contexto.md                      resumo acumulado
├── 01-discovery.md
├── 02-estrategia.md
├── 03-modelagem.md
├── 04-feature-frames.md
├── 05-prototipacao.md
├── 06-handoff.md
├── 07-diagnostico-comportamental.md
└── 08-experimentos.md
```

Insumos de imersão podem conter dados confidenciais. Não versionar `00-insumos/` em repositório público.

## Manutenção do repositório

- Editar modelos somente em `templates/` e executar `python3 scripts/esteira.py sync`.
- Executar `python3 scripts/esteira.py validate` antes de cada commit.
- Ao criar uma skill: pasta em `skills/` com `SKILL.md` (`name` igual ao nome da pasta, `description` com o que faz e quando usar), entrada em `SKILL_TEMPLATES` de `scripts/esteira.py` e linha nas tabelas deste arquivo e de `docs/mapa-da-esteira.md`.
