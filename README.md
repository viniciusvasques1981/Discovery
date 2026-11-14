# Discovery

Repositório de agentes e skills de Product Discovery e Design Thinking, organizados segundo a **Esteira de Produto AI-Enhanced (Feature Frame)**.

A esteira encadeia oito módulos e três etapas opcionais. Cada módulo recebe o resumo do anterior, de modo que o propósito definido com o sponsor no início esteja presente nos critérios de aceite e no contexto entregue ao assistente de código no final.

## Módulos

| Módulo / Etapa | Framework | Entrega principal | Skill | Agente |
| :--- | :--- | :--- | :--- | :--- |
| 1 — Discovery | Design Thinking | Matriz CSD, dores validadas, dados pessoais | [`discovery-product-strategy`](skills/discovery-product-strategy/SKILL.md) | [`discovery-strategist`](agents/discovery-strategist.md) |
| 2 — Estratégia | Golden Circle, Lean UX | Visão de Produto, hipóteses e OKRs | [`discovery-product-strategy`](skills/discovery-product-strategy/SKILL.md) | [`discovery-strategist`](agents/discovery-strategist.md) |
| 2B — Validação de Hipóteses *(opcional)* | Lean UX | Plano e resultado de validação | [`hypothesis-validation-research`](skills/hypothesis-validation-research/SKILL.md) | [`discovery-strategist`](agents/discovery-strategist.md) |
| 3 — Modelagem | UCD | Protopersona, Mapa de Empatia e Jornada To-Be | [`behavioral-modeling-feature-framing`](skills/behavioral-modeling-feature-framing/SKILL.md) | [`experience-modeler`](agents/experience-modeler.md) |
| 3B — Árvore de Oportunidades *(opcional)* | Opportunity Solution Tree | Oportunidades e soluções comparadas | [`behavioral-modeling-feature-framing`](skills/behavioral-modeling-feature-framing/SKILL.md) | [`experience-modeler`](agents/experience-modeler.md) |
| 4 — Feature Frame | Feature Frame, Lean Inception | Escopo delimitado, viabilidade técnica e recorte de MVP | [`behavioral-modeling-feature-framing`](skills/behavioral-modeling-feature-framing/SKILL.md) | [`experience-modeler`](agents/experience-modeler.md) |
| 5 — Prototipação | Agile Prototyping | Fluxo de telas, componentes e guia de UI | [`systemic-ui-interaction-design`](skills/systemic-ui-interaction-design/SKILL.md) | [`interface-designer`](agents/interface-designer.md) |
| 5B — Teste de Usabilidade *(opcional)* | Teste baseado em tarefas | Roteiro, achados e ajustes | [`prototype-usability-testing`](skills/prototype-usability-testing/SKILL.md) | [`interface-designer`](agents/interface-designer.md) |
| 6 — Handoff | Agile Handoff | Issues, BDD, plano de instrumentação e System Prompt | [`technical-handoff-prompt-engineering`](skills/technical-handoff-prompt-engineering/SKILL.md) | [`handoff-tech-lead`](agents/handoff-tech-lead.md) |
| 7 — Medição | Heurísticas de usabilidade | Diagnóstico comportamental e correções de UX | [`behavioral-analytics-ux-fixes`](skills/behavioral-analytics-ux-fixes/SKILL.md) | [`growth-analyst`](agents/growth-analyst.md) |
| 8 — Experimentação | Experimentação A/B/n | Plano de experimento com métricas guardiãs | [`behavioral-experimentation-cro`](skills/behavioral-experimentation-cro/SKILL.md) | [`growth-analyst`](agents/growth-analyst.md) |

Os módulos 1 a 6 seguem o [Guia da Esteira](docs/guia-da-esteira.md). Os módulos 7 e 8 e as etapas opcionais estendem o guia.

Componentes transversais:

| Componente | Tipo | Função |
| :--- | :--- | :--- |
| [`esteira-orchestration`](skills/esteira-orchestration/SKILL.md) | Skill | Define a trilha, delega cada módulo, aciona a revisão e registra as aprovações |
| [`artifact-evidence-review`](skills/artifact-evidence-review/SKILL.md) + [`artifact-reviewer`](agents/artifact-reviewer.md) | Skill + agente | Revisão independente: confronta cada artefato com os insumos |
| [`get-more-perspectives`](skills/get-more-perspectives/SKILL.md) | Skill | Painel de 3 a 5 pontos de vista para decisões |
| [`match-my-writing-style`](skills/match-my-writing-style/SKILL.md) | Skill | Aplica o estilo de escrita do usuário a textos de comunicação |

## Trilhas

| Trilha | Composição | Indicação |
| :--- | :--- | :--- |
| **Pocket** | Um documento curto ([`pocket-feature-frame`](skills/pocket-feature-frame/SKILL.md)) | Ajuste pequeno em produto existente, que caiba em uma única issue |
| **Expressa** | Módulos 1 a 6 | Imersão de 2 dias; prazo fixo |
| **Completa** | Módulos 1 a 6 com as etapas 2B, 3B e 5B | Problema novo, hipóteses de risco alto, fluxo crítico |

A trilha pocket tem uma triagem de sete critérios; um "Não" encaminha a demanda para a trilha expressa. As etapas opcionais dependem de coleta com pessoas e acrescentam dias ao ciclo. Quando não executadas, o risco aceito fica registrado em `contexto.md`.

## Estrutura

```text
.
├── AGENTS.md                 instruções gerais (lidas por Copilot, Gemini CLI e Claude Code)
├── CLAUDE.md / GEMINI.md     importam AGENTS.md
├── .claude-plugin/           manifesto de plugin do Claude Code
├── gemini-extension.json     manifesto de extensão do Gemini CLI
├── skills/                   13 skills (SKILL.md + assets/)
├── agents/                   6 agentes
├── templates/                modelos de artefato (fonte única)
├── iniciativas/              artefatos por iniciativa; inclui um exemplo fictício completo
├── docs/                     guia, mapa da esteira e instalação
└── scripts/                  instalação, validação, empacotamento, issues e Clarity
```

## Uso

1. Instale conforme a plataforma: [docs/instalacao.md](docs/instalacao.md).
2. Crie `iniciativas/<slug>/` e coloque o material bruto em `00-insumos/`.
3. Acione a skill `esteira-orchestration`, ou a skill do módulo desejado.
4. Ao fim de cada módulo, o artefato passa pela revisão independente e pela aprovação de uma pessoa. O arquivo `contexto.md` carrega o resumo para o módulo seguinte.

Exemplo de solicitação inicial:

```text
Inicie a iniciativa "portal-fornecedores" com as transcrições em
iniciativas/portal-fornecedores/00-insumos/, na trilha expressa, e execute o Módulo 1.
```

Para um ajuste pequeno:

```text
Use a trilha pocket: os usuários clicam nos horários ocupados da grade e nada acontece.
Evidência: 21% das sessões com dead click nessa tela, segundo o Clarity.
```

Referência de preenchimento: [iniciativas/exemplo-reserva-salas](iniciativas/exemplo-reserva-salas/README.md).

## Documentação

| Documento | Conteúdo |
| :--- | :--- |
| [docs/guia-da-esteira.md](docs/guia-da-esteira.md) | Processo de referência, prompts sugeridos e cronograma da imersão de 2 dias |
| [docs/mapa-da-esteira.md](docs/mapa-da-esteira.md) | Módulos, skills, agentes e artefatos; critério skill ou agente; extensões ao guia |
| [docs/instalacao.md](docs/instalacao.md) | Instalação em Claude Code, Gemini CLI, GitHub Copilot e aplicativos de chat; automações |
| [AGENTS.md](AGENTS.md) | Regras gerais seguidas pelos agentes |

## Manutenção

```bash
python3 scripts/esteira.py sync       # copia templates/ para skills/<skill>/assets/
python3 scripts/esteira.py validate   # valida frontmatter, referências e links
python3 scripts/esteira.py package    # gera dist/<skill>.zip para upload
```
