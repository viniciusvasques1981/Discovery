# Discovery

Repositório de agentes e skills de Product Discovery e Design Thinking, organizados segundo a **Esteira de Produto AI-Enhanced (Feature Frame)**.

A esteira encadeia oito módulos e três etapas opcionais. Cada módulo recebe o resumo do anterior, de modo que o propósito definido com o sponsor no início esteja presente nos critérios de aceite e no contexto entregue ao assistente de código no final.

## Módulos

Tabela gerada a partir de `esteira.json`.

<!-- gerado:modulos-readme -->
| Módulo / Etapa | Framework | Entrega principal | Skill | Agente | Artefato |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 — Discovery | Design Thinking (Empatia) | Base de evidências, Matriz CSD e dores validadas | [`discovery-product-strategy`](skills/discovery-product-strategy/SKILL.md) | [`discovery-strategist`](agents/discovery-strategist.md) | `evidencias.md`, `01-discovery.md` |
| 2 — Estratégia | Golden Circle, Lean UX | Visão de Produto, hipóteses e OKRs | [`discovery-product-strategy`](skills/discovery-product-strategy/SKILL.md) | [`discovery-strategist`](agents/discovery-strategist.md) | `02-estrategia.md` |
| 2B — Validação de Hipóteses (opcional) | Lean UX | Plano e resultado de validação | [`hypothesis-validation-research`](skills/hypothesis-validation-research/SKILL.md) | [`discovery-strategist`](agents/discovery-strategist.md) | `02b-validacao-hipoteses.md` |
| 3 — Modelagem | UCD | Protopersona, Mapa de Empatia e Jornada To-Be | [`behavioral-modeling-feature-framing`](skills/behavioral-modeling-feature-framing/SKILL.md) | [`experience-modeler`](agents/experience-modeler.md) | `03-modelagem.md` |
| 3B — Árvore de Oportunidades (opcional) | Opportunity Solution Tree | Oportunidades e soluções comparadas | [`behavioral-modeling-feature-framing`](skills/behavioral-modeling-feature-framing/SKILL.md) | [`experience-modeler`](agents/experience-modeler.md) | `03b-arvore-oportunidades.md` |
| 4 — Feature Frame | Feature Frame, Lean Inception | Escopo delimitado, viabilidade técnica e recorte de MVP | [`behavioral-modeling-feature-framing`](skills/behavioral-modeling-feature-framing/SKILL.md), [`technical-feasibility-check`](skills/technical-feasibility-check/SKILL.md) | [`experience-modeler`](agents/experience-modeler.md), [`handoff-tech-lead`](agents/handoff-tech-lead.md) | `04-feature-frames.md` |
| 5 — Prototipação | Agile Prototyping | Fluxo de telas, componentes e guia de UI | [`systemic-ui-interaction-design`](skills/systemic-ui-interaction-design/SKILL.md) | [`interface-designer`](agents/interface-designer.md) | `05-prototipacao.md` |
| 5B — Teste de Usabilidade (opcional) | Teste baseado em tarefas | Roteiro, achados e ajustes | [`prototype-usability-testing`](skills/prototype-usability-testing/SKILL.md) | [`interface-designer`](agents/interface-designer.md) | `05b-teste-usabilidade.md` |
| 6 — Handoff | Agile Handoff | Issues, BDD, plano de instrumentação e System Prompt | [`technical-handoff-prompt-engineering`](skills/technical-handoff-prompt-engineering/SKILL.md) | [`handoff-tech-lead`](agents/handoff-tech-lead.md) | `06-handoff.md` |
| 7 — Medição | Heurísticas de usabilidade | Diagnóstico comportamental e correções de UX | [`behavioral-analytics-ux-fixes`](skills/behavioral-analytics-ux-fixes/SKILL.md) | [`growth-analyst`](agents/growth-analyst.md) | `07-diagnostico-comportamental.md` |
| 8 — Experimentação | Experimentação A/B/n | Plano de experimento com métricas guardiãs | [`behavioral-experimentation-cro`](skills/behavioral-experimentation-cro/SKILL.md) | [`growth-analyst`](agents/growth-analyst.md) | `08-experimentos.md` |
<!-- /gerado:modulos-readme -->

Os módulos 1 a 6 seguem o [Guia da Esteira](docs/guia-da-esteira.md). Os módulos 7 e 8 e as etapas opcionais estendem o guia.

Componentes transversais:

<!-- gerado:transversais-readme -->
| Componente | Tipo | Função | Skill | Agente |
| :--- | :--- | :--- | :--- | :--- |
| Revisão independente | Skill + agente | Confere a origem das afirmações ao fim de cada bloco (módulos 2, 4, 6 e 8) | [`artifact-evidence-review`](skills/artifact-evidence-review/SKILL.md) | [`artifact-reviewer`](agents/artifact-reviewer.md) |
| Ajuste pequeno (trilha pocket) | Skill | Ajuste pequeno em um único documento curto | [`pocket-feature-frame`](skills/pocket-feature-frame/SKILL.md) | — |
| Orquestração | Skill | Define a trilha, delega cada módulo, aciona verificação e revisão e registra as aprovações | [`esteira-orchestration`](skills/esteira-orchestration/SKILL.md) | — |
| Painel de perspectivas | Skill | Painel de 3 a 5 pontos de vista para decisões | [`get-more-perspectives`](skills/get-more-perspectives/SKILL.md) | — |
| Estilo de escrita | Skill | Aplica o estilo de escrita do usuário a textos de comunicação | [`match-my-writing-style`](skills/match-my-writing-style/SKILL.md) | — |
<!-- /gerado:transversais-readme -->

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
├── esteira.json              fonte única: módulos, skills, agentes, modelos e scripts
├── AGENTS.md                 regras de execução (lidas por Copilot, Gemini CLI e Claude Code)
├── CLAUDE.md / GEMINI.md     importam AGENTS.md
├── .claude-plugin/           manifesto de plugin do Claude Code
├── gemini-extension.json     manifesto de extensão do Gemini CLI
├── skills/                   skills (SKILL.md + assets/ + scripts/)
├── agents/                   agentes
├── templates/                modelos de artefato (fonte única)
├── scripts/                  manutenção do repositório e operações de iniciativa
├── iniciativas/              artefatos por iniciativa; inclui um exemplo fictício completo
└── docs/                     guia, mapa da esteira, instalação, manutenção e página de apresentação
```

## Uso

1. Instale conforme a plataforma: [docs/instalacao.md](docs/instalacao.md).
2. Crie `iniciativas/<slug>/` e coloque o material bruto em `00-insumos/`.
3. Acione a skill `esteira-orchestration`, ou a skill do módulo desejado.
4. Ao fim de cada módulo, um script confere o artefato e uma pessoa aprova. Ao fim dos módulos 2, 4, 6 e 8, um agente revisor independente confere a sustentação das afirmações. O arquivo `contexto.md` carrega as decisões para o módulo seguinte.

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
| [docs/manutencao.md](docs/manutencao.md) | Fonte única, comandos e rotinas de manutenção |
| [AGENTS.md](AGENTS.md) | Regras gerais seguidas pelos agentes |

## Uso de tokens

O desenho evita que o modelo releia ou copie o que um script pode fazer:

- o material bruto é lido uma vez; os módulos seguintes usam a base de evidências, com referência de linha;
- Out of Scope e Por quê são copiados para o handoff por script;
- conferências mecânicas são feitas por script, e a revisão por agente ocorre por bloco;
- `contexto.md` guarda decisões e ponteiros, sem tabelas copiadas.

Detalhes em [docs/mapa-da-esteira.md](docs/mapa-da-esteira.md).

## Manutenção

```bash
python3 scripts/esteira.py sync       # gera tabelas e copia modelos e scripts para as skills
python3 scripts/esteira.py validate   # valida registro, referências, cópias e links
python3 scripts/esteira.py package    # gera dist/<skill>.zip para upload
```

Rotinas e detalhes em [docs/manutencao.md](docs/manutencao.md).
