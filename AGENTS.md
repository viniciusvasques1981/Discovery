# Esteira de Produto AI-Enhanced — instruções para agentes

Este repositório contém agentes e skills que executam uma esteira de produto do Discovery ao Handoff técnico, com ciclo de medição e experimentação pós-entrega. O processo de referência está em `docs/guia-da-esteira.md`.

## Estrutura

| Caminho | Conteúdo |
| :--- | :--- |
| `skills/<nome>/SKILL.md` | Método de cada módulo: algoritmo de execução e padrão de entrega |
| `skills/<nome>/assets/` | Modelos de artefato usados pela skill (cópia de `templates/`) |
| `agents/<nome>.md` | Papéis executados em contexto separado: entradas, conduta e critério de conclusão |
| `templates/` | Fonte única dos modelos de artefato |
| `iniciativas/<slug>/` | Artefatos produzidos para cada iniciativa |
| `iniciativas/exemplo-reserva-salas/` | Iniciativa fictícia completa, usada como referência e caso de regressão |
| `scripts/` | Manutenção do repositório e automações (issues, Clarity) |
| `docs/` | Guia do processo, mapa da esteira e instalação |

## Módulos e etapas

| Módulo / Etapa | Skill | Agente | Artefato |
| :--- | :--- | :--- | :--- |
| 1 — Discovery | `discovery-product-strategy` | `discovery-strategist` | `01-discovery.md` |
| 2 — Estratégia | `discovery-product-strategy` | `discovery-strategist` | `02-estrategia.md` |
| 2B — Validação de Hipóteses (opcional) | `hypothesis-validation-research` | `discovery-strategist` | `02b-validacao-hipoteses.md` |
| 3 — Modelagem | `behavioral-modeling-feature-framing` | `experience-modeler` | `03-modelagem.md` |
| 3B — Árvore de Oportunidades (opcional) | `behavioral-modeling-feature-framing` | `experience-modeler` | `03b-arvore-oportunidades.md` |
| 4 — Feature Frame | `behavioral-modeling-feature-framing` | `experience-modeler`, com checagem de viabilidade pelo `handoff-tech-lead` | `04-feature-frames.md` |
| 5 — Prototipação | `systemic-ui-interaction-design` | `interface-designer` | `05-prototipacao.md` |
| 5B — Teste de Usabilidade (opcional) | `prototype-usability-testing` | `interface-designer` | `05b-teste-usabilidade.md` |
| 6 — Handoff | `technical-handoff-prompt-engineering` | `handoff-tech-lead` | `06-handoff.md` |
| 7 — Medição | `behavioral-analytics-ux-fixes` | `growth-analyst` | `07-diagnostico-comportamental.md` |
| 8 — Experimentação | `behavioral-experimentation-cro` | `growth-analyst` | `08-experimentos.md` |
| Revisão independente | `artifact-evidence-review` | `artifact-reviewer` | `revisoes.md` |

Coordenação: skill `esteira-orchestration`, executada na conversa principal. Apoio em qualquer módulo: `get-more-perspectives` e `match-my-writing-style`.

## Trilhas

- **Expressa:** Módulos 1 a 6, sem etapas opcionais. Compatível com a imersão de 2 dias.
- **Completa:** inclui as etapas 2B, 3B e 5B, que dependem de coleta com pessoas ou dados e acrescentam dias ao ciclo.

Etapa opcional não executada é registrada em `contexto.md` como risco aceito, com quem decidiu e o motivo. Nunca tornar obrigatória uma etapa opcional nem omitir a pergunta ao usuário.

## Regras gerais

1. **Regra de Ouro.** Nenhum módulo começa sem ler `iniciativas/<slug>/contexto.md`. Todo módulo termina atualizando esse arquivo.
2. **Rastreabilidade.** O Por quê definido no Módulo 2 deve constar em cada issue do Módulo 6. Cada Feature Frame aponta para um estágio da Jornada To-Be e um Key Result. Todo Key Result tem evento no Plano de Instrumentação.
3. **Out of Scope imutável.** Os limites definidos no Módulo 4 são transcritos literalmente até o Módulo 6.
4. **Fato e inferência.** Conteúdo não sustentado pelos insumos recebe a marca `[inferência]`. Dados ausentes não são estimados: registrar como Dúvida, `[pendente de dados]`, `[não validada]` ou `[a validar com o time técnico]`.
5. **Nada simulado.** Entrevistas, sessões de teste, dados de uso e resultados de experimento são sempre informados pelo usuário. Agentes planejam e registram; não inventam participantes nem respostas.
6. **Um módulo por vez.** Ao fim de cada módulo: revisão independente, apresentação do resultado e aprovação de uma pessoa antes de avançar.
7. **Aprovação humana.** Nenhum agente registra aprovação em nome do usuário. O parecer do `artifact-reviewer` não substitui a aprovação.
8. **Viabilidade antes do MVP.** O recorte de MVP só é fechado após a checagem de viabilidade técnica.
9. **Dados pessoais.** Identificados no Módulo 1 e detalhados no Módulo 6. O conteúdo organiza a informação para o responsável por privacidade; não constitui parecer jurídico.
10. **Idioma.** Artefatos em português do Brasil. Sintaxe Gherkin com `# language: pt`.
11. **Formato.** Markdown, seguindo o modelo em `assets/` da skill.

## Estrutura de uma iniciativa

```text
iniciativas/<slug>/
├── 00-insumos/                      material bruto (transcrições, notas, documentos)
├── contexto.md                      resumo acumulado, aprovações e etapas opcionais
├── revisoes.md                      pareceres da revisão independente
├── 01-discovery.md
├── 02-estrategia.md
├── 02b-validacao-hipoteses.md       opcional
├── 03-modelagem.md
├── 03b-arvore-oportunidades.md      opcional
├── 04-feature-frames.md
├── 05-prototipacao.md
├── 05b-teste-usabilidade.md         opcional
├── 06-handoff.md
├── 07-diagnostico-comportamental.md
└── 08-experimentos.md
```

Insumos de imersão podem conter dados confidenciais. Não versionar `00-insumos/` em repositório público; a única exceção é a iniciativa de exemplo, que é fictícia.

## Manutenção do repositório

- Editar modelos somente em `templates/` e executar `python3 scripts/esteira.py sync`.
- Executar `python3 scripts/esteira.py validate` antes de cada commit.
- Ao alterar uma skill, reexecutar o módulo correspondente sobre `iniciativas/exemplo-reserva-salas/00-insumos/` e comparar com o artefato do exemplo.
- Ao criar uma skill: pasta em `skills/` com `SKILL.md` (`name` igual ao nome da pasta, `description` com o que faz e quando usar), entrada em `SKILL_TEMPLATES` de `scripts/esteira.py` e linha nas tabelas deste arquivo e de `docs/mapa-da-esteira.md`.
- Critério para escolher entre skill e agente: `docs/mapa-da-esteira.md`, seção "Skill ou agente".
