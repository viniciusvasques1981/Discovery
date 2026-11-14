---
name: behavioral-modeling-feature-framing
description: "Converter os direcionadores estratégicos em modelos comportamentais de uso e delimitar o escopo funcional por meio da metodologia Feature Framing, prevenindo a expansão descontrolada de escopo (scope creep). Cobre os Módulos 3 (Modelagem) e 4 (Feature Frame) da esteira: Protopersona, Mapa de Empatia, Jornada To-Be, Catálogo de Feature Frames, recorte de MVP e esforço em Fibonacci. Use quando houver estratégia definida e for preciso modelar o usuário ou delimitar escopo de funcionalidades."
---

# Modelagem Comportamental e Feature Framing

Módulos 3 e 4 da Esteira de Produto AI-Enhanced.

| | |
| :--- | :--- |
| **Frameworks** | User Centered Design (UCD), Feature Frame, Lean Inception |
| **Entradas** | `contexto.md`, `01-discovery.md` e `02-estrategia.md` da iniciativa |
| **Saídas** | `03-modelagem.md` e `04-feature-frames.md` em `iniciativas/<slug>/` |
| **Skill anterior** | `discovery-product-strategy` |
| **Próxima skill** | `systemic-ui-interaction-design` |

## Regras de execução

1. Ler `contexto.md` antes de iniciar. Sem dores validadas e Visão de Produto, interromper e solicitar a execução dos Módulos 1 e 2.
2. Toda dor da Protopersona deve corresponder a uma dor validada no Módulo 1. Atributos não sustentados pelos insumos recebem a marca `[inferência]`.
3. Cada Feature Frame deve referenciar o estágio da Jornada To-Be que atende e o Key Result que influencia. Funcionalidade sem esse vínculo não entra no catálogo.
4. O campo Out of Scope é obrigatório e não pode ficar vazio.

## Algoritmo de Execução

### Módulo 3 — O Olhar do Usuário (Modelagem)

#### 1. Modelagem Centrada no Usuário (UCD)

- **Protopersona:** Perfil operacional, responsabilidades no ecossistema, 3 dores centrais no fluxo atual e necessidades imediatas. Incluir motivações e medos (o que a pessoa teme perder ou errar ao adotar a solução).
- **Mapa de Empatia:** O que pensa e sente, vê, ouve, fala e faz; dores e ganhos. Preencher apenas com o que os insumos sustentam.
- **Jornada To-Be:** Mapeamento sequencial contendo: Estágio da Jornada → Ação do Usuário → Fricção Eliminada → Gatilho de Sucesso.

Protopersona é hipótese de perfil, não persona validada por pesquisa. Registrar essa condição na entrega.

### Módulo 4 — Definição (Feature Frame)

#### 2. Engenharia de Escopo via Feature Framing

Para cada funcionalidade proposta, estruturar a matriz de delimitação:

- **Contexto:** Momento exato e gatilho em que a funcionalidade entra em ação.
- **Problema:** A dor específica resolvida naquele ponto da jornada.
- **Solução:** O comportamento funcional e visual executado pelo sistema.
- **Out of Scope (Limites Rígidos):** O que a funcionalidade explicitamente não faz sob nenhuma hipótese neste ciclo.

#### 3. Classificação de Entrega e Recorte de MVP

- **MVP (Sim/Não):** Classificar com base no menor conjunto funcional viável para entrega de valor. Critério: sem a funcionalidade, a Jornada To-Be não se completa de ponta a ponta para a Protopersona principal.
- **Esforço (Fibonacci):** 1, 2, 3, 5, 8 ou 13. A estimativa é relativa e preliminar; deve ser revisada pelo time técnico. Itens estimados em 13 devem ser decompostos.
- **Prioridade:** Ordenar por valor (vínculo com Key Result e dor atendida) em relação ao esforço.

## Padrão de Entrega (Markdown)

Usar os modelos `assets/03-modelagem.md` e `assets/04-feature-frames.md`.

**`03-modelagem.md`**

- **Modelagem Comportamental:** Perfil da Protopersona, Mapa de Empatia e Matriz da Jornada To-Be.

**`04-feature-frames.md`**

- **Catálogo de Feature Frames:** Bloco individual para cada funcionalidade com Contexto, Problema, Solução, Out of Scope e Classificação de MVP.
- **Matriz de priorização:** Funcionalidade, estágio da jornada, Key Result relacionado, MVP, esforço e ordem.
- **Recorte de MVP:** lista final do que entra e do que fica para ciclos seguintes.

## Passagem de contexto

Ao concluir, atualizar `iniciativas/<slug>/contexto.md` com: Protopersona resumida, estágios da Jornada To-Be, lista de Feature Frames do MVP e a consolidação de todos os limites Out of Scope. Os limites Out of Scope devem ser transcritos sem alteração até o Módulo 6.
