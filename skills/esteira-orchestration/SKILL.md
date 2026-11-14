---
name: esteira-orchestration
description: "Orquestração da Esteira de Produto AI-Enhanced. Conduz uma iniciativa do Discovery ao Handoff, define a trilha (pocket, expressa ou completa), identifica o módulo atual, delega ao agente ou à skill do módulo, aciona a revisão independente e registra as aprovações. Use para iniciar uma nova iniciativa, retomar uma existente ou quando não estiver claro qual módulo executar."
---

# Orquestração da Esteira

Skill transversal. Coordena a execução da Esteira de Produto AI-Enhanced a partir da conversa principal: identifica o estágio da iniciativa, aciona o agente ou a skill do módulo e verifica a continuidade do contexto. Não produz os artefatos dos módulos.

## Por que é uma skill, e não um agente

A orquestração exige diálogo com o usuário (escolha da trilha, decisão sobre etapas opcionais, aprovações) e delegação a agentes. Ambos pertencem à conversa principal: um subagente executa uma tarefa e devolve o resultado, sem conduzir aprovações, e a capacidade de um subagente acionar outros varia conforme a ferramenta e a versão.

## Modo de delegação

| Ambiente | Como executar cada módulo | Como fazer a revisão independente |
| :--- | :--- | :--- |
| Com subagentes (Claude Code, Gemini CLI, Copilot) | Delegar ao agente indicado no mapa de delegação | Delegar ao `artifact-reviewer`, passando apenas o artefato e as fontes |
| Sem subagentes (aplicativos de chat) | Executar a skill do módulo na própria conversa | Abrir uma conversa nova, somente com o artefato e os insumos, e executar `artifact-evidence-review` |

## Responsabilidades

1. **Abrir a iniciativa:** criar `iniciativas/<slug>/` com `contexto.md` (a partir do modelo `assets/contexto.md`) e a pasta `00-insumos/` para o material bruto.
2. **Definir a trilha** com o usuário e registrá-la em `contexto.md`.
3. **Diagnosticar o estágio:** verificar quais artefatos numerados já existem e qual é o próximo módulo.
4. **Delegar:** acionar o agente do módulo com as entradas corretas.
5. **Acionar a revisão independente** (`artifact-reviewer`) ao fim de cada módulo.
6. **Verificar o portão de saída** e registrar a aprovação humana antes de avançar.
7. **Manter a Regra de Ouro:** nenhum módulo começa sem o resumo do anterior em `contexto.md`.

## Trilhas

| Trilha | Composição | Indicação |
| :--- | :--- | :--- |
| **Pocket** | Um único documento, pela skill `pocket-feature-frame`; sem agentes | Ajuste pequeno em produto existente, que passa na triagem de sete critérios |
| **Expressa** | Módulos 1 a 6, sem etapas opcionais | Imersão de 2 dias; prazo fixo; problema já conhecido pelo time |
| **Completa** | Módulos 1 a 6 com as etapas 2B, 3B e 5B | Problema novo, hipóteses de risco alto, fluxo crítico ou irreversível |

Escolha da trilha, nesta ordem:

1. Se a demanda é um ajuste em produto existente e aparenta caber em uma única issue, acionar `pocket-feature-frame`. A triagem da própria skill confirma ou encaminha de volta para a trilha expressa.
2. Caso contrário, perguntar ao usuário entre expressa e completa.

Um ajuste pocket escalonado durante a execução entra na trilha expressa com o documento parcial como insumo. Na trilha pocket não se aplicam o mapa de delegação, a sequência de fechamento por módulo nem os portões abaixo: a skill tem autoverificação e aprovação única próprias.

As etapas opcionais podem ser escolhidas individualmente. Ao chegar ao ponto de cada etapa opcional, informar o critério de recomendação e o risco de não executá-la; a decisão é do usuário e é registrada na tabela "Etapas opcionais" de `contexto.md`, com o motivo.

| Etapa opcional | Ponto | Recomendar quando | Risco de não executar |
| :--- | :--- | :--- | :--- |
| 2B — Validação de Hipóteses | Entre os Módulos 2 e 3 | Há hipótese de risco alto cuja refutação mudaria a Visão de Produto ou o MVP | Funcionalidades construídas sobre suposição; validação só em produção |
| 3B — Árvore de Oportunidades | Entre os Módulos 3 e 4 | Há mais de uma solução plausível por dor, ou stakeholders chegaram com soluções prontas | Primeira solução proposta é adotada sem comparação |
| 5B — Teste de Usabilidade | Entre os Módulos 5 e 6 | Fluxo novo para a Protopersona, tarefa crítica ou Feature Frame com Confiança Baixa | Problemas de usabilidade detectados só em produção |

Não tornar obrigatória uma etapa opcional nem omitir a pergunta. Etapa pulada não bloqueia o avanço.

## Mapa de delegação

| Módulo / Etapa | Agente | Skill | Artefato |
| :--- | :--- | :--- | :--- |
| 1 — Discovery | `discovery-strategist` | `discovery-product-strategy` | `01-discovery.md` |
| 2 — Estratégia | `discovery-strategist` | `discovery-product-strategy` | `02-estrategia.md` |
| 2B — Validação de Hipóteses (opcional) | `discovery-strategist` | `hypothesis-validation-research` | `02b-validacao-hipoteses.md` |
| 3 — Modelagem | `experience-modeler` | `behavioral-modeling-feature-framing` | `03-modelagem.md` |
| 3B — Árvore de Oportunidades (opcional) | `experience-modeler` | `behavioral-modeling-feature-framing` | `03b-arvore-oportunidades.md` |
| 4 — Feature Frame | `experience-modeler`, com checagem de viabilidade pelo `handoff-tech-lead` | `behavioral-modeling-feature-framing` | `04-feature-frames.md` |
| 5 — Prototipação | `interface-designer` | `systemic-ui-interaction-design` | `05-prototipacao.md` |
| 5B — Teste de Usabilidade (opcional) | `interface-designer` | `prototype-usability-testing` | `05b-teste-usabilidade.md` |
| 6 — Handoff | `handoff-tech-lead` | `technical-handoff-prompt-engineering` | `06-handoff.md` |
| 7 — Medição | `growth-analyst` | `behavioral-analytics-ux-fixes` | `07-diagnostico-comportamental.md` |
| 8 — Experimentação | `growth-analyst` | `behavioral-experimentation-cro` | `08-experimentos.md` |
| Revisão independente | `artifact-reviewer` | `artifact-evidence-review` | `revisoes.md` |

Skills de apoio, acionáveis em qualquer ponto: `get-more-perspectives` (decisões com mais de uma opção viável) e `match-my-writing-style` (textos de comunicação em nome do usuário).

## Sequência de fechamento de cada módulo

1. O agente do módulo entrega o artefato e atualiza `contexto.md`.
2. O `artifact-reviewer` revisa o artefato em contexto separado e grava o parecer em `revisoes.md`.
3. Apontamentos Bloqueantes retornam ao agente do módulo para correção.
4. A conversa principal apresenta ao usuário o resumo do módulo, o parecer e os apontamentos restantes.
5. O aprovador indicado em `contexto.md` aprova ou devolve. Registrar nome, data e pendências aceitas na tabela de Aprovações.

## Portões de saída

| Módulo | Condição para avançar | Aprovador padrão |
| :--- | :--- | :--- |
| 1 | Matriz CSD com origem de cada item; ao menos uma dor com evidência; bloco de dados pessoais preenchido ou convertido em Dúvidas | Sponsor |
| 2 | Visão de Produto no formato padrão; OKRs com linha de base ou KR de Instrumentação; decisão sobre a Etapa 2B registrada | Sponsor |
| 3 | Protopersona vinculada a dores validadas; Jornada To-Be completa; decisão sobre a Etapa 3B registrada | Product Manager |
| 4 | Todo Feature Frame com Out of Scope; checagem de viabilidade técnica preenchida; recorte de MVP definido | Product Manager e Tech Lead |
| 5 | Toda tela vinculada a um Feature Frame do MVP; lacunas de Design System listadas; decisão sobre a Etapa 5B registrada | Product Designer |
| 6 | Verificação de rastreabilidade aprovada; todo Key Result com evento no Plano de Instrumentação; dados pessoais com finalidade e responsável | Tech Lead |
| 7 | Achados com volume de sessões e nível de evidência | Product Manager |
| 8 | Hipótese, métricas guardiãs e critério de decisão definidos antes do início | Product Manager |

Os papéis de aprovador são um padrão; ajustar à estrutura do time na abertura da iniciativa. Em todos os módulos, parecer "Reprovado" do `artifact-reviewer` impede o avanço até a correção ou o aceite registrado pelo aprovador.

Se o portão não for atendido, apontar o que falta e não avançar. O usuário pode optar por avançar mesmo assim; nesse caso, registrar a pendência em `contexto.md`.

## Regras

- Um módulo por vez. Após cada módulo, apresentar o resumo e aguardar a aprovação antes de seguir.
- No cronograma da imersão de 2 dias, o Módulo 5 é conduzido antes do Módulo 4. Na execução com agentes, manter a ordem lógica 3 → 4 → 5, pois a skill do Módulo 5 depende dos Feature Frames.
- Não alterar artefatos de módulos anteriores sem registrar a revisão em `contexto.md` (data, o que mudou e por quê).
- Ao retomar uma iniciativa, ler `contexto.md` integralmente antes de qualquer ação.
- A aprovação é sempre de uma pessoa. Nenhum agente registra aprovação em nome do usuário.
