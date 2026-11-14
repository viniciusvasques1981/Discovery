---
name: hypothesis-validation-research
description: "Planejar e registrar a validação das hipóteses de maior risco antes que entrem no escopo do produto. Etapa 2B, opcional, da esteira, entre os Módulos 2 (Estratégia) e 3 (Modelagem): seleção de hipóteses por risco e custo, plano de validação com critério de sucesso definido antes da coleta, registro de evidências e reclassificação da Matriz CSD. Use quando houver hipóteses de risco alto na Matriz de Hipóteses e tempo disponível para testá-las antes de definir funcionalidades."
---

# Validação de Hipóteses

Etapa 2B — opcional — da Esteira de Produto AI-Enhanced.

| | |
| :--- | :--- |
| **Frameworks** | Lean UX, Continuous Discovery (testes de suposição) |
| **Entradas** | `contexto.md` e `02-estrategia.md` (Matriz de Hipóteses) |
| **Saída** | `02b-validacao-hipoteses.md` em `iniciativas/<slug>/` |
| **Skill anterior** | `discovery-product-strategy` |
| **Próxima skill** | `behavioral-modeling-feature-framing` |

## Por que é opcional

A etapa depende de coleta com pessoas ou dados reais e acrescenta dias ao ciclo. Não cabe na imersão de 2 dias: ocorre no intervalo entre os dias ou depois dela. Quando não executada, as hipóteses seguem com a situação "não validada", os Feature Frames derivados recebem Confiança Baixa e a decisão é registrada em `contexto.md` como risco aceito.

Critério para recomendar a execução: existe ao menos uma hipótese de risco alto cuja refutação mudaria a Visão de Produto ou o recorte de MVP.

## Regras de execução

1. A skill planeja a validação e registra resultados fornecidos pelo usuário. Não simula entrevistas, respostas de participantes nem dados de uso.
2. O critério de sucesso e o de refutação são definidos antes da coleta e não são alterados depois.
3. Sem resultado informado, a seção Resultado permanece em branco e a hipótese continua "não validada".
4. Declaração de intenção ("eu usaria") tem confiança menor que comportamento observado. Indicar o tipo de evidência em cada resultado.

## Algoritmo de Execução

### 1. Seleção

Ordenar as hipóteses da Matriz de Hipóteses por risco (impacto se falsa) e custo de validação. Selecionar primeiro as de risco alto e custo baixo. Justificar as não selecionadas.

### 2. Plano de Validação

Para cada hipótese selecionada, escolher o método de menor custo capaz de refutá-la:

| Método | Indicado para | Evidência produzida |
| :--- | :--- | :--- |
| Análise de dados existentes | Hipóteses sobre frequência ou volume de um comportamento atual | Comportamento observado |
| Entrevista | Hipóteses sobre a existência e a causa de uma dor | Relato de comportamento passado |
| Protótipo de baixa fidelidade | Hipóteses sobre compreensão de uma solução | Comportamento observado em tarefa |
| Fake door | Hipóteses sobre interesse em uma funcionalidade | Comportamento observado |
| Concierge | Hipóteses sobre o valor da entrega, sem construir o sistema | Comportamento observado |
| Pesquisa quantitativa | Hipóteses sobre a distribuição de uma opinião ou prática | Declaração |

Definir: participantes ou fonte de dados, roteiro ou instrumento, critério de sucesso, critério de refutação, prazo e responsável. Roteiros de entrevista usam perguntas abertas sobre situações passadas, sem apresentar a solução nem induzir a resposta.

### 3. Registro do Resultado

Com os dados fornecidos pelo usuário: amostra obtida, evidência coletada, veredito (Validada / Refutada / Inconclusiva) e confiança. Resultado que não atinge nenhum dos dois critérios é Inconclusivo.

### 4. Efeito na Esteira

- Reclassificar na Matriz CSD as Suposições correspondentes: validada passa a Certeza, com a evidência; refutada é removida ou reformulada.
- Indicar se a Visão de Produto ou os OKRs precisam de revisão.
- Hipóteses inconclusivas ou não testadas seguem com a marca `[não validada]`.

## Padrão de Entrega (Markdown)

Usar o modelo `assets/02b-validacao-hipoteses.md`.

- **Seleção** das hipóteses.
- **Plano de Validação** por hipótese.
- **Resultado**, quando houver dados.
- **Efeito na esteira.**

## Passagem de contexto

Atualizar `iniciativas/<slug>/contexto.md`: situação de cada hipótese, linha da Etapa 2B na tabela de etapas opcionais e, se houve alteração na Matriz CSD ou nos OKRs, o registro de revisões.
