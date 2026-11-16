---
name: esteira-orchestration
description: "Orquestração da Esteira de Produto AI-Enhanced. Conduz uma iniciativa do Discovery ao Handoff, define a trilha (pocket, expressa ou completa), identifica o módulo atual, delega ao agente ou à skill do módulo, aciona verificação e revisão independente e registra as aprovações. Use para iniciar uma nova iniciativa, retomar uma existente ou quando não estiver claro qual módulo executar."
---

# Orquestração da Esteira

Skill transversal, executada na conversa principal. Identifica o estágio da iniciativa, aciona o agente ou a skill do módulo e controla o fechamento. Não produz os artefatos dos módulos.

A orquestração é skill, e não agente, porque exige diálogo com o usuário (trilha, etapas opcionais, aprovações) e delegação a agentes.

## Economia de contexto

A conversa principal coordena; o conteúdo fica nos arquivos.

1. Não ler artefatos nem insumos na conversa principal. Para saber o estágio, listar os arquivos da iniciativa e ler apenas `contexto.md`.
2. Ao delegar, passar ao agente o caminho da iniciativa e o módulo. O agente lê as entradas definidas na skill dele.
3. Receber do agente um resumo de até dez linhas e o caminho do artefato. Não pedir o artefato de volta na resposta.
4. Apresentar ao aprovador o resumo, o resultado da verificação e os pontos em aberto. Quem quiser o detalhe abre o arquivo.

## Abertura

1. Criar `iniciativas/<slug>/` com `contexto.md` e `aprovacoes.md` (modelos em `assets/`) e a pasta `00-insumos/` para o material bruto.
2. Definir a trilha e os aprovadores de cada módulo com o usuário. Registrar a trilha em `contexto.md`.

## Trilhas

| Trilha | Composição | Indicação |
| :--- | :--- | :--- |
| **Pocket** | Um único documento, pela skill `pocket-feature-frame`; sem agentes | Ajuste pequeno em produto existente, que passa na triagem de sete critérios |
| **Expressa** | Módulos 1 a 6, sem etapas opcionais | Imersão de 2 dias; prazo fixo; problema já conhecido pelo time |
| **Completa** | Módulos 1 a 6 com as etapas 2B, 3B e 5B | Problema novo, hipóteses de risco alto, fluxo crítico ou irreversível |

Escolha, nesta ordem:

1. Se a demanda é um ajuste em produto existente e aparenta caber em uma única issue, acionar `pocket-feature-frame`. A triagem da própria skill confirma ou devolve para a trilha expressa. Na trilha pocket não se aplicam a delegação nem o fechamento abaixo.
2. Caso contrário, perguntar ao usuário entre expressa e completa.

As etapas opcionais podem ser escolhidas individualmente. Ao chegar ao ponto de cada uma, informar o critério de recomendação e o risco de não executá-la. A decisão é do usuário e é registrada em `aprovacoes.md`, com o motivo. Não tornar obrigatória uma etapa opcional nem omitir a pergunta.

| Etapa opcional | Recomendar quando | Risco de não executar |
| :--- | :--- | :--- |
| 2B — Validação de Hipóteses | Há hipótese de risco alto cuja refutação mudaria a Visão de Produto ou o MVP | Funcionalidades construídas sobre suposição; validação só em produção |
| 3B — Árvore de Oportunidades | Há mais de uma solução plausível por dor, ou stakeholders chegaram com soluções prontas | Primeira solução proposta é adotada sem comparação |
| 5B — Teste de Usabilidade | Fluxo novo para a Protopersona, tarefa crítica ou Feature Frame com Confiança Baixa | Problemas de usabilidade detectados só em produção |

## Delegação

Tabela gerada a partir de `esteira.json`.

<!-- gerado:delegacao -->
| Módulo / Etapa | Agente | Skill | Artefato | Revisão independente | Aprovador padrão |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 — Discovery | `discovery-strategist` | `discovery-product-strategy` | `evidencias.md`, `01-discovery.md` | — | Sponsor |
| 2 — Estratégia | `discovery-strategist` | `discovery-product-strategy` | `02-estrategia.md` | Sim | Sponsor |
| 2B — Validação de Hipóteses (opcional) | `discovery-strategist` | `hypothesis-validation-research` | `02b-validacao-hipoteses.md` | — | Product Manager |
| 3 — Modelagem | `experience-modeler` | `behavioral-modeling-feature-framing` | `03-modelagem.md` | — | Product Manager |
| 3B — Árvore de Oportunidades (opcional) | `experience-modeler` | `behavioral-modeling-feature-framing` | `03b-arvore-oportunidades.md` | — | Product Manager |
| 4 — Feature Frame | `experience-modeler`, `handoff-tech-lead` | `behavioral-modeling-feature-framing`, `technical-feasibility-check` | `04-feature-frames.md` | Sim | Product Manager e Tech Lead |
| 5 — Prototipação | `interface-designer` | `systemic-ui-interaction-design` | `05-prototipacao.md` | — | Product Designer |
| 5B — Teste de Usabilidade (opcional) | `interface-designer` | `prototype-usability-testing` | `05b-teste-usabilidade.md` | — | Product Designer |
| 6 — Handoff | `handoff-tech-lead` | `technical-handoff-prompt-engineering` | `06-handoff.md` | Sim | Tech Lead |
| 7 — Medição | `growth-analyst` | `behavioral-analytics-ux-fixes` | `07-diagnostico-comportamental.md` | — | Product Manager |
| 8 — Experimentação | `growth-analyst` | `behavioral-experimentation-cro` | `08-experimentos.md` | Sim | Product Manager |
<!-- /gerado:delegacao -->

Com subagentes disponíveis, delegar ao agente indicado. Sem subagentes (aplicativos de chat), executar a skill do módulo na própria conversa e fazer a revisão independente em uma conversa nova, somente com os artefatos do bloco.

Skills de apoio, acionáveis em qualquer ponto: `get-more-perspectives` (decisões com mais de uma opção viável) e `match-my-writing-style` (textos de comunicação em nome do usuário).

## Imersão com mais de um produto

Uma imersão pode originar vários produtos. A imersão tem repositório próprio, dono da origem; cada produto segue em seu repositório.

| Etapa | Onde | O que acontece |
| :--- | :--- | :--- |
| Módulos 1 e 2 | Repositório da imersão (tronco) | Evidências e Matriz CSD comuns; Visão e OKRs por produto; `partilha.md` preliminar e ponto de separação |
| Módulo 3 | Tronco, se a separação for no Módulo 4 (padrão) | Protopersona e jornada conjuntas; estágios com produto dono; `partilha.md` fechado |
| Derivação | Do tronco para cada produto | `iniciativa.py derivar <tronco> <produto> <destino>` copia os artefatos herdados e gera a estratégia do produto |
| Módulos 4 a 8 | Repositório de cada produto | Execução normal; `cross-product-alignment` ao fim dos Módulos 4 e 6 |

Condução:

1. Ao fim do Módulo 2, se houver mais de um produto, aplicar as duas perguntas do modelo `assets/partilha.md` e registrar o ponto de separação. Padrão: Módulo 4. Módulo 3 apenas se os produtos não compartilham usuário nem jornada.
2. No ponto de separação, executar `iniciativa.py verificar` no tronco: ele acusa dor ou suposição sem atribuição, produto sem seção de estratégia e estágio sem dono.
3. Derivar cada produto. O destino é a pasta `iniciativas/<produto>/` no clone do repositório do produto, que precisa ter a esteira instalada.
4. Conferir `vizinhos.json` em cada produto: ele aponta para o `interface.md` dos demais.
5. Em cada produto, seguir a trilha a partir do módulo indicado pela derivação. Os artefatos herdados são somente leitura; o script acusa alteração.
6. Mudança na origem (nova evidência, reclassificação da Matriz CSD) é feita no tronco, com aprovação do sponsor, e os produtos são derivados de novo ou registram a diferença.

O material bruto (`00-insumos/`) permanece só no repositório da imersão.

## Fechamento de cada módulo

1. O agente entrega o artefato e atualiza a própria seção de `contexto.md`.
2. Executar `python3 scripts/iniciativa.py verificar iniciativas/<slug>`. Erros retornam ao agente do módulo. Esta etapa não consome contexto relevante e ocorre em todos os módulos.
3. Se o módulo fecha um bloco (coluna "Revisão independente" = Sim), delegar a revisão ao `artifact-reviewer`. Parecer "Reprovado" retorna ao agente do módulo.
4. Apresentar ao aprovador o resumo, o resultado da verificação e, quando houver, o parecer.
5. Com a aprovação, acrescentar uma linha à tabela de Aprovações de `aprovacoes.md`: nome, data, resultado da verificação, parecer e pendências aceitas.

A revisão independente ocorre por bloco, e não por módulo, para não repetir a leitura dos mesmos artefatos. A detecção precoce nos módulos intermediários fica a cargo do script.

## Condições de avanço além da verificação

| Módulo | Condição que depende de julgamento |
| :--- | :--- |
| 1 | Matriz CSD apresentada ao sponsor antes do Módulo 2: classificação errada compromete os módulos seguintes |
| 2 | Decisão sobre a Etapa 2B registrada |
| 3 | Decisão sobre a Etapa 3B registrada |
| 4 | Recorte de MVP confirmado pelo Product Manager após a checagem de viabilidade |
| 5 | Decisão sobre a Etapa 5B registrada |
| 6 | Pendências `[a validar com o time técnico]` apresentadas ao Tech Lead |
| 8 | Critério de decisão do experimento definido antes do início |

Se uma condição não for atendida, apontar o que falta e não avançar. O usuário pode optar por avançar mesmo assim; nesse caso, registrar a pendência em `aprovacoes.md`.

## Regras

- Um módulo por vez.
- No cronograma da imersão de 2 dias, o Módulo 5 é conduzido antes do Módulo 4. Na execução com agentes, manter a ordem 3 → 4 → 5, pois a skill do Módulo 5 depende dos Feature Frames.
- Alteração em artefato já aprovado é registrada em `aprovacoes.md` (data, o que mudou e por quê).
- A aprovação é sempre de uma pessoa. Nenhum agente registra aprovação em nome do usuário.
