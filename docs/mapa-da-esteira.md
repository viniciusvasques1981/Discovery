# Mapa da Esteira

Relação entre os módulos do [Guia da Esteira](guia-da-esteira.md), as skills, os agentes e os artefatos deste repositório.

## Fluxo

```mermaid
flowchart LR
    I[00-insumos] --> M1[1 Discovery]
    M1 --> M2[2 Estratégia]
    M2 --> M3[3 Modelagem]
    M2 -.-> V2[2B Validação de Hipóteses]
    V2 -.-> M3
    M3 --> M4[4 Feature Frame]
    M3 -.-> O3[3B Árvore de Oportunidades]
    O3 -.-> M4
    M4 --> M5[5 Prototipação]
    M5 --> M6[6 Handoff]
    M5 -.-> T5[5B Teste de Usabilidade]
    T5 -.-> M6
    M6 --> P((Produção))
    P --> M7[7 Medição]
    M7 --> M8[8 Experimentação]
    M8 -. revisão da Matriz CSD e dos OKRs .-> M1
```

Linhas tracejadas indicam etapas opcionais e retroalimentação. `contexto.md` é lido e atualizado em todos os módulos; a verificação por script ocorre ao fim de cada um e a revisão independente, ao fim dos módulos 2, 4, 6 e 8.

## Módulos, skills e agentes

Tabela gerada a partir de `esteira.json`.

<!-- gerado:modulos-mapa -->
| Módulo / Etapa | Framework | Entrega principal | Skill | Agente | Artefato |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 — Discovery | Design Thinking (Empatia) | Base de evidências, Matriz CSD e dores validadas | [`discovery-product-strategy`](../skills/discovery-product-strategy/SKILL.md) | [`discovery-strategist`](../agents/discovery-strategist.md) | `evidencias.md`, `01-discovery.md` |
| 2 — Estratégia | Golden Circle, Lean UX | Visão de Produto, hipóteses e OKRs | [`discovery-product-strategy`](../skills/discovery-product-strategy/SKILL.md) | [`discovery-strategist`](../agents/discovery-strategist.md) | `02-estrategia.md` |
| 2B — Validação de Hipóteses (opcional) | Lean UX | Plano e resultado de validação | [`hypothesis-validation-research`](../skills/hypothesis-validation-research/SKILL.md) | [`discovery-strategist`](../agents/discovery-strategist.md) | `02b-validacao-hipoteses.md` |
| 3 — Modelagem | UCD | Protopersona, Mapa de Empatia e Jornada To-Be | [`behavioral-modeling-feature-framing`](../skills/behavioral-modeling-feature-framing/SKILL.md) | [`experience-modeler`](../agents/experience-modeler.md) | `03-modelagem.md` |
| 3B — Árvore de Oportunidades (opcional) | Opportunity Solution Tree | Oportunidades e soluções comparadas | [`behavioral-modeling-feature-framing`](../skills/behavioral-modeling-feature-framing/SKILL.md) | [`experience-modeler`](../agents/experience-modeler.md) | `03b-arvore-oportunidades.md` |
| 4 — Feature Frame | Feature Frame, Lean Inception | Escopo delimitado, viabilidade técnica e recorte de MVP | [`behavioral-modeling-feature-framing`](../skills/behavioral-modeling-feature-framing/SKILL.md), [`technical-feasibility-check`](../skills/technical-feasibility-check/SKILL.md) | [`experience-modeler`](../agents/experience-modeler.md), [`handoff-tech-lead`](../agents/handoff-tech-lead.md) | `04-feature-frames.md` |
| 5 — Prototipação | Agile Prototyping | Fluxo de telas, componentes e guia de UI | [`systemic-ui-interaction-design`](../skills/systemic-ui-interaction-design/SKILL.md) | [`interface-designer`](../agents/interface-designer.md) | `05-prototipacao.md` |
| 5B — Teste de Usabilidade (opcional) | Teste baseado em tarefas | Roteiro, achados e ajustes | [`prototype-usability-testing`](../skills/prototype-usability-testing/SKILL.md) | [`interface-designer`](../agents/interface-designer.md) | `05b-teste-usabilidade.md` |
| 6 — Handoff | Agile Handoff | Issues, BDD, plano de instrumentação e System Prompt | [`technical-handoff-prompt-engineering`](../skills/technical-handoff-prompt-engineering/SKILL.md) | [`handoff-tech-lead`](../agents/handoff-tech-lead.md) | `06-handoff.md` |
| 7 — Medição | Heurísticas de usabilidade | Diagnóstico comportamental e correções de UX | [`behavioral-analytics-ux-fixes`](../skills/behavioral-analytics-ux-fixes/SKILL.md) | [`growth-analyst`](../agents/growth-analyst.md) | `07-diagnostico-comportamental.md` |
| 8 — Experimentação | Experimentação A/B/n | Plano de experimento com métricas guardiãs | [`behavioral-experimentation-cro`](../skills/behavioral-experimentation-cro/SKILL.md) | [`growth-analyst`](../agents/growth-analyst.md) | `08-experimentos.md` |
<!-- /gerado:modulos-mapa -->

Componentes transversais:

<!-- gerado:transversais-mapa -->
| Componente | Tipo | Função | Skill | Agente |
| :--- | :--- | :--- | :--- | :--- |
| Revisão independente | Skill + agente | Confere a origem das afirmações ao fim de cada bloco (módulos 2, 4, 6 e 8) | [`artifact-evidence-review`](../skills/artifact-evidence-review/SKILL.md) | [`artifact-reviewer`](../agents/artifact-reviewer.md) |
| Ajuste pequeno (trilha pocket) | Skill | Ajuste pequeno em um único documento curto | [`pocket-feature-frame`](../skills/pocket-feature-frame/SKILL.md) | — |
| Orquestração | Skill | Define a trilha, delega cada módulo, aciona verificação e revisão e registra as aprovações | [`esteira-orchestration`](../skills/esteira-orchestration/SKILL.md) | — |
| Alinhamento entre produtos | Skill | Em imersões com mais de um produto: publica a interface do produto, lê a dos vizinhos e trata dependências e sobreposições | [`cross-product-alignment`](../skills/cross-product-alignment/SKILL.md) | — |
| Painel de perspectivas | Skill | Painel de 3 a 5 pontos de vista para decisões | [`get-more-perspectives`](../skills/get-more-perspectives/SKILL.md) | — |
| Estilo de escrita | Skill | Aplica o estilo de escrita do usuário a textos de comunicação | [`match-my-writing-style`](../skills/match-my-writing-style/SKILL.md) | — |
<!-- /gerado:transversais-mapa -->

## Trilha pocket

Para ajustes pequenos em produto existente. Condensa os Módulos 1 a 7 em um único documento curto, produzido por uma única skill, sem agentes.

| Bloco do documento | Módulo de origem | O que resta |
| :--- | :--- | :--- |
| 0. Triagem | — | Sete critérios de entrada; um "Não" encaminha para a trilha expressa |
| 1. Problema e evidência | 1 — Discovery | Uma evidência obrigatória; suposição declarada |
| 2. Resultado esperado | 2 — Estratégia | Uma métrica, vinculada a Key Result existente |
| 3. Feature Frame | 4 — Feature Frame | Um único frame, com Out of Scope |
| 4. Interface | 5 — Prototipação | Somente o que muda: antes e depois |
| 5. Handoff | 6 — Handoff | Uma issue com três cenários BDD, incluindo não regressão |
| 6. Verificação pós-entrega | 7 — Medição | O que conferir, onde e quando |

O Módulo 3 não tem bloco próprio: a trilha pocket usa a modelagem já existente na iniciativa. Critérios de triagem (todos devem ser atendidos): um único ponto do fluxo; uma única issue com esforço até 5; sem dados pessoais novos; sem integração nem mudança de modelo de dados; reversível; sem alteração de Visão, OKRs ou Out of Scope vigente; ao menos uma evidência.

## Imersão com mais de um produto

```mermaid
flowchart LR
    subgraph Imersao[Repositório da imersão: tronco]
        M1[1 Discovery] --> M2[2 Estratégia por produto]
        M2 --> M3[3 Modelagem conjunta]
        M3 --> PT[partilha.md fechado]
    end
    PT -- derivar --> A4
    PT -- derivar --> B4
    subgraph ProdutoA[Repositório do produto A]
        A4[4 Feature Frame] --> A5[5] --> A6[6 Handoff] --> A7[7 e 8]
    end
    subgraph ProdutoB[Repositório do produto B]
        B4[4 Feature Frame] --> B5[5] --> B6[6 Handoff] --> B7[7 e 8]
    end
    A6 <-. interface.md .-> B6
    A7 -. reclassificação de suposições .-> M1
    B7 -. reclassificação de suposições .-> M1
```

| Peça | Arquivo ou comando | Função |
| :--- | :--- | :--- |
| Tronco | Iniciativa no repositório da imersão | Dono das evidências, da Matriz CSD e da estratégia; guarda o material bruto |
| Estratégia por produto | `02-estrategia.md`, com uma seção por produto | Visão e OKRs de cada produto; propósito e hipóteses comuns |
| Mapa de partilha | `partilha.md` | Produtos, ponto de separação, dono de cada dor, suposição e estágio, pontos de integração previstos |
| Derivação | `iniciativa.py derivar <tronco> <produto> <destino>` | Cria a instância do produto com os artefatos herdados e a estratégia no formato padrão |
| Origem | `origem.json` | Registra de onde a instância veio e a assinatura dos artefatos herdados |
| Interface | `interface.md`, por `iniciativa.py publicar` | Resumo do produto para os vizinhos: Feature Frames, Out of Scope, eventos, contratos, entidades, reclassificações |
| Vizinhança | `iniciativa.py vizinhos <dir>` | Lê as interfaces dos vizinhos, mostra o que mudou e cruza os dois lados |
| Dependência declarada | Linhas "Depende de" e "Fornece para" do Feature Frame | Liga funcionalidades de produtos diferentes |

**Ponto de separação.** O padrão é a entrada do Módulo 4: a fronteira entre produtos é uma decisão de escopo, e a jornada conjunta já mostra onde o usuário passa de um produto para o outro, que são os pontos de integração. A entrada do Módulo 3 é usada quando os produtos não compartilham usuário nem jornada. Depois do Módulo 4 não há separação: MVP e viabilidade dependem de cada time.

**O que o cruzamento acusa.** Dependência de funcionalidade inexistente, removida ou fora do MVP do vizinho; dois produtos com funcionalidade no MVP para a mesma dor; evento ou entidade parecida com nomes diferentes; suposição do tronco reclassificada pelo outro produto; produtos derivados de versões diferentes do tronco.

**Limites.** A conexão é eventual: cada produto vê o vizinho no estado da última leitura. A leitura exige acesso ao `interface.md` do outro repositório. O cruzamento é par a par; com muitos produtos da mesma imersão, um índice central passa a ser necessário. O script compara identificadores e nomes; conflito de significado (um produto pressupõe algo que o outro declarou fora de escopo com outras palavras) depende de leitura.

## Trilhas e impacto no prazo

| Etapa | Obrigatória | Impacto no prazo | Motivo |
| :--- | :--- | :--- | :--- |
| Módulos 1 a 6 | Sim | Base da imersão de 2 dias | — |
| Checagem de viabilidade técnica (Módulo 4) | Sim | Baixo | Feita por agente na mesma sessão; confirmação do time no Módulo 6 |
| Pontuação de valor e confiança (Módulo 4) | Sim | Baixo | Três campos por Feature Frame |
| Plano de instrumentação e dados pessoais (Módulos 1 e 6) | Sim | Baixo | Seções adicionais em artefatos existentes |
| Verificação por script e registro de aprovação | Sim | Baixo | Script a cada módulo; aprovação já era necessária |
| Revisão independente por bloco | Sim | Baixo | Agente ao fim dos módulos 2, 4, 6 e 8 |
| 2B — Validação de Hipóteses | Não | Dias | Exige coleta com pessoas ou dados |
| 3B — Árvore de Oportunidades | Não | Horas | Exige gerar e comparar soluções alternativas |
| 5B — Teste de Usabilidade | Não | Dias | Exige recrutamento e sessões |

As estimativas de impacto são qualitativas; não foram medidas em execuções reais.

## Skill ou agente

| | Skill | Agente |
| :--- | :--- | :--- |
| **Define** | O método: algoritmo de execução e padrão de entrega | O papel: quem executa, com quais entradas, conduta e critério de conclusão |
| **Onde roda** | No contexto da conversa em andamento | Em contexto separado, devolvendo o resultado |
| **Ativação** | Automática, pela descrição, ou por nome | Delegação a partir da conversa principal ou seleção pelo usuário |

Critérios usados neste repositório para decidir a forma de cada componente:

| Critério | Indica |
| :--- | :--- |
| Precisa dialogar com o usuário durante a execução (escolhas, aprovações) | Skill |
| Precisa acionar outros agentes | Skill, na conversa principal |
| Precisa ser independente de quem produziu o trabalho | Agente |
| Processa insumo volumoso que não deve ocupar a conversa principal | Agente |
| É um método reutilizável fora da esteira | Skill |
| Apenas encapsula uma skill, sem contexto próprio a preservar | Skill; o agente é redundante |

Aplicação:

| Componente | Forma | Justificativa |
| :--- | :--- | :--- |
| Orquestração | Skill | Dialoga com o usuário e delega a agentes. Era agente na primeira versão; foi convertida |
| Trilha pocket | Skill | Insumo pequeno e diálogo direto com o solicitante; um contexto separado só acrescentaria custo |
| Revisão de artefatos | Skill + agente | O método é a skill; a independência exige o contexto separado do agente |
| `discovery-strategist`, `growth-analyst` | Agente | Processam transcrições e telemetria volumosas |
| `handoff-tech-lead` | Agente | Atua em dois módulos, e a checagem de viabilidade se beneficia de visão separada da de produto |
| Checagem de viabilidade | Skill própria | Era uma seção da skill de handoff; separada para que o Módulo 4 não carregue o método do Módulo 6 |
| `experience-modeler`, `interface-designer` | Agente | Caso mais fraco: insumos pequenos e validações frequentes com o usuário. Mantidos por uniformidade e porque, no Copilot, agentes funcionam como modos selecionáveis. Podem ser dispensados usando as skills diretamente |
| `get-more-perspectives` | Skill | Método reutilizável; os pareceres são gerados em subagentes separados quando disponíveis, para preservar a independência |
| `match-my-writing-style` | Skill | Instrução permanente de estilo; não há tarefa a delegar |

## Passagem de contexto (Regra de Ouro)

O guia determina que cada módulo receba o resumo do anterior. Neste repositório a regra é implementada por arquivo:

1. Cada iniciativa tem uma pasta `iniciativas/<slug>/`.
2. O Módulo 1 numera os insumos e extrai a base de evidências (`evidencias.md`). O material bruto não é relido depois.
3. Cada módulo grava um artefato numerado e atualiza apenas a própria seção de `contexto.md`.
4. `iniciativa.py verificar` confere o artefato. Ao fim de cada bloco, o `artifact-reviewer` confere a sustentação das afirmações.
5. Uma pessoa aprova; nome e data vão para `aprovacoes.md`.
6. O módulo seguinte lê `contexto.md` e as entradas listadas na skill dele.

O Out of Scope é escrito uma vez, no Feature Frame. `iniciativa.py montar` o copia para cada issue e para o System Prompt, o que torna a igualdade uma propriedade do processo, e não algo a conferir.

## Uso de tokens

Medidas adotadas para reduzir leitura e escrita repetidas:

| Medida | O que evita |
| :--- | :--- |
| Base de evidências com referência de linha | Releitura do material bruto pelos módulos 2 a 6 e pelo revisor |
| Leitura dos insumos um documento por vez | Carregar toda a imersão em um único contexto |
| Montagem por script (`iniciativa.py montar`) | Geração repetida de Out of Scope, Escopo e Por quê em cada issue e no System Prompt |
| Verificação por script (`iniciativa.py verificar`) | Uso do modelo para conferir campos, cálculos, cobertura e vínculos |
| Revisão independente por bloco | Uma revisão por módulo, com releitura dos mesmos artefatos |
| `contexto.md` como índice; aprovações em arquivo separado | Leitura de tabelas de registro e de cópias de artefatos em todo módulo |
| Entradas explícitas por skill | Leitura de artefatos que o módulo não usa |
| Skill de viabilidade separada | Carregar o método do Módulo 6 durante o Módulo 4 |
| Resposta do agente em até dez linhas | Conteúdo dos artefatos trafegando pela conversa principal |
| Nível de modelo por agente (`esteira.json`) | Uso do modelo mais caro em tarefas de formato fixo |
| `AGENTS.md` só com regras de execução | Carregar instruções de manutenção em toda sessão |

Os níveis de modelo valem para agentes. Skills rodam no modelo da conversa: para a trilha pocket e para a orquestração, um modelo menor tende a ser suficiente, a critério do usuário.

## Extensões em relação ao guia

Acréscimos às skills originais, para cobrir o que o guia pede:

| Skill | Acréscimo | Origem no guia |
| :--- | :--- | :--- |
| `discovery-product-strategy` | Download do Problema (cenário atual, premissas, limitações técnicas) | Módulo 1, prompt sugerido |
| `discovery-product-strategy` | Matriz de Hipóteses no formato Lean UX | Módulo 2, resultado |
| `behavioral-modeling-feature-framing` | Motivações e medos na Protopersona; Mapa de Empatia | Módulo 3, prompt sugerido |
| `behavioral-modeling-feature-framing` | Esforço em Fibonacci e matriz de priorização | Módulo 4, prompt sugerido |
| `systemic-ui-interaction-design` | Fluxo de telas, wireframe descritivo e Guia de UI para assistente de código | Módulo 5, prompt sugerido |
| `technical-handoff-prompt-engineering` | Infraestrutura e integrações; verificação de rastreabilidade | Módulo 6, prompt sugerido |
| `match-my-writing-style` | Alternativa sem conector do Workspace (`voice-card.md` local) | Necessário fora do Gemini |

Acréscimos que não constam no guia:

| Acréscimo | Onde | Obrigatório |
| :--- | :--- | :--- |
| Módulos 7 (Medição) e 8 (Experimentação) | Skills de analytics e experimentação | Pós-entrega |
| Etapa 2B — Validação de Hipóteses | `hypothesis-validation-research` | Não |
| Etapa 3B — Árvore de Oportunidades | `behavioral-modeling-feature-framing` | Não |
| Etapa 5B — Teste de Usabilidade | `prototype-usability-testing` | Não |
| Checagem de viabilidade técnica antes do MVP | Módulo 4 | Sim |
| Valor, Confiança e índice de prioridade | Módulo 4 | Sim |
| Plano de Instrumentação com linha de base | Módulo 6 | Sim |
| Dados pessoais e conformidade | Módulos 1 e 6 | Sim |
| Revisão independente por bloco | `artifact-evidence-review` | Sim |
| Base de evidências, montagem e verificação por script | `scripts/iniciativa.py` | Sim |
| Fonte única da tabela de módulos | `esteira.json` | — |
| Aprovador por módulo | `contexto.md` | Sim |
| Criação de issues e resumo do Clarity por script | `scripts/` | Não |
| Iniciativa de exemplo | `iniciativas/exemplo-reserva-salas/` | — |
| Trilha pocket para ajustes pequenos | `pocket-feature-frame` | Alternativa às demais trilhas |
| Vários produtos por imersão: partilha, derivação, interface e vizinhança | `cross-product-alignment`, `scripts/iniciativa.py` | Quando a imersão origina mais de um produto |

Pontos em que guia e skills divergem e a decisão adotada:

| Tema | Guia | Skill original | Decisão |
| :--- | :--- | :--- | :--- |
| OKRs | "Proponha 3 OKRs" | 1 Objetivo com 3 Key Results | Padrão de 1 Objetivo com 3 KRs; até 3 Objetivos quando houver mais de uma frente estratégica |
| Ordem dos Módulos 4 e 5 | No cronograma de 2 dias, o Módulo 5 ocorre antes do Módulo 4 | A skill de UI recebe Feature Frames como entrada | Execução com agentes segue 3 → 4 → 5; o cronograma presencial permanece como no guia |
| Assistente de código | Copilot | Cursor e GitHub Copilot | System Prompt neutro, aplicável a qualquer assistente |
