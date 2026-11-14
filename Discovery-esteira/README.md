# Discovery

Repositório de agentes e skills de Product Discovery e Design Thinking, organizados segundo a **Esteira de Produto AI-Enhanced (Feature Frame)**.

A esteira encadeia oito módulos. Cada módulo recebe o resumo do anterior, de modo que o propósito definido com o sponsor no início esteja presente nos critérios de aceite e no contexto entregue ao assistente de código no final.

## Módulos

| Módulo | Framework | Entrega principal | Skill | Agente |
| :--- | :--- | :--- | :--- | :--- |
| 1 — Discovery | Design Thinking | Matriz CSD e dores validadas | [`discovery-product-strategy`](skills/discovery-product-strategy/SKILL.md) | [`discovery-strategist`](agents/discovery-strategist.md) |
| 2 — Estratégia | Golden Circle, Lean UX | Visão de Produto, hipóteses e OKRs | [`discovery-product-strategy`](skills/discovery-product-strategy/SKILL.md) | [`discovery-strategist`](agents/discovery-strategist.md) |
| 3 — Modelagem | UCD | Protopersona, Mapa de Empatia e Jornada To-Be | [`behavioral-modeling-feature-framing`](skills/behavioral-modeling-feature-framing/SKILL.md) | [`experience-modeler`](agents/experience-modeler.md) |
| 4 — Feature Frame | Feature Frame, Lean Inception | Escopo delimitado e recorte de MVP | [`behavioral-modeling-feature-framing`](skills/behavioral-modeling-feature-framing/SKILL.md) | [`experience-modeler`](agents/experience-modeler.md) |
| 5 — Prototipação | Agile Prototyping | Fluxo de telas, componentes e guia de UI | [`systemic-ui-interaction-design`](skills/systemic-ui-interaction-design/SKILL.md) | [`interface-designer`](agents/interface-designer.md) |
| 6 — Handoff | Agile Handoff | Issues, BDD e System Prompt | [`technical-handoff-prompt-engineering`](skills/technical-handoff-prompt-engineering/SKILL.md) | [`handoff-tech-lead`](agents/handoff-tech-lead.md) |
| 7 — Medição | Heurísticas de usabilidade | Diagnóstico comportamental e correções de UX | [`behavioral-analytics-ux-fixes`](skills/behavioral-analytics-ux-fixes/SKILL.md) | [`growth-analyst`](agents/growth-analyst.md) |
| 8 — Experimentação | Experimentação A/B/n | Plano de experimento com métricas guardiãs | [`behavioral-experimentation-cro`](skills/behavioral-experimentation-cro/SKILL.md) | [`growth-analyst`](agents/growth-analyst.md) |

Os módulos 1 a 6 seguem o [Guia da Esteira](docs/guia-da-esteira.md). Os módulos 7 e 8 estendem o guia com o ciclo pós-entrega e retroalimentam o Módulo 1.

Componentes transversais:

| Componente | Tipo | Função |
| :--- | :--- | :--- |
| [`esteira-orchestrator`](agents/esteira-orchestrator.md) | Agente | Identifica o módulo atual, delega e verifica os portões de saída |
| [`get-more-perspectives`](skills/get-more-perspectives/SKILL.md) | Skill | Painel de 3 a 5 pontos de vista para decisões |
| [`match-my-writing-style`](skills/match-my-writing-style/SKILL.md) | Skill | Aplica o estilo de escrita do usuário a textos de comunicação |

## Estrutura

```text
.
├── AGENTS.md                 instruções gerais (lidas por Copilot, Gemini CLI e Claude Code)
├── CLAUDE.md / GEMINI.md     importam AGENTS.md
├── .claude-plugin/           manifesto de plugin do Claude Code
├── gemini-extension.json     manifesto de extensão do Gemini CLI
├── skills/                   8 skills (SKILL.md + assets/)
├── agents/                   6 agentes
├── templates/                modelos de artefato (fonte única)
├── iniciativas/              artefatos por iniciativa
├── docs/                     guia, mapa da esteira e instalação
└── scripts/                  instalação, sincronização, validação e empacotamento
```

## Uso

1. Instale conforme a plataforma: [docs/instalacao.md](docs/instalacao.md).
2. Crie `iniciativas/<slug>/` e coloque o material bruto em `00-insumos/`.
3. Acione o `esteira-orchestrator`, ou a skill do módulo desejado.
4. Valide o resultado de cada módulo antes de avançar. O arquivo `contexto.md` da iniciativa carrega o resumo para o módulo seguinte.

Exemplo de solicitação inicial:

```text
Inicie a iniciativa "portal-fornecedores" com as transcrições em
iniciativas/portal-fornecedores/00-insumos/ e execute o Módulo 1.
```

## Documentação

| Documento | Conteúdo |
| :--- | :--- |
| [docs/guia-da-esteira.md](docs/guia-da-esteira.md) | Processo de referência, prompts sugeridos e cronograma da imersão de 2 dias |
| [docs/mapa-da-esteira.md](docs/mapa-da-esteira.md) | Relação entre módulos, skills, agentes e artefatos; ajustes de harmonização |
| [docs/instalacao.md](docs/instalacao.md) | Instalação em Claude Code, Gemini CLI, GitHub Copilot e aplicativos de chat |
| [AGENTS.md](AGENTS.md) | Regras gerais seguidas pelos agentes |

## Manutenção

```bash
python3 scripts/esteira.py sync       # copia templates/ para skills/<skill>/assets/
python3 scripts/esteira.py validate   # valida frontmatter, referências e links
python3 scripts/esteira.py package    # gera dist/<skill>.zip para upload
```
