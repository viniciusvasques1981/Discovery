---
name: pocket-feature-frame
description: "Versão pocket da Esteira de Produto AI-Enhanced, para ajustes pequenos em produto existente: correção de usabilidade, mudança de microcopy, novo estado de tela, campo ou regra simples. Produz um único documento curto com triagem, problema e evidência, resultado esperado, Feature Frame, mudança de interface, uma issue com BDD e verificação pós-entrega. Use quando a demanda couber em uma única issue; se a triagem falhar, encaminha para a trilha expressa."
---

# Pocket Feature Frame

Trilha pocket da Esteira de Produto AI-Enhanced. Condensa os Módulos 1 a 7 em um único artefato, para demandas em que o processo completo custaria mais do que o ajuste.

| | |
| :--- | :--- |
| **Entradas** | A descrição do ajuste e ao menos uma evidência do problema; `contexto.md` da iniciativa relacionada, se existir |
| **Saída** | Um arquivo `AJ-NN-<slug>.md` em `iniciativas/<slug>/ajustes/` ou, sem iniciativa relacionada, em `ajustes/` |
| **Agentes** | Nenhum. A skill é executada na conversa principal |
| **Aprovação** | Uma pessoa, uma vez, ao final |

## O que a trilha pocket preserva e o que dispensa

| Elemento da esteira | Na trilha pocket |
| :--- | :--- |
| Separação entre fato e suposição | Preservada: evidência obrigatória e suposição declarada |
| Out of Scope | Preservado, transcrito literalmente na issue |
| BDD | Preservado, com mínimo de três cenários |
| Medição | Preservada: uma métrica e uma verificação pós-entrega |
| Matriz CSD completa, Golden Circle, OKRs | Dispensados; o ajuste se vincula a um Key Result existente, se houver |
| Protopersona, Mapa de Empatia, Jornada To-Be | Dispensados; usa-se o que já existe na iniciativa |
| Catálogo e priorização de Feature Frames | Dispensados: há um único Feature Frame |
| Especificação completa de telas e Design System | Reduzida ao que muda |
| Contratos de arquitetura e System Prompt | Dispensados: ajuste que os exija não é pocket |
| Revisão independente por agente | Substituída pela autoverificação ao final do documento |
| Aprovação por módulo | Substituída por uma aprovação única |

## Regras de execução

1. Executar a triagem antes de qualquer outro item. Um único "Não" interrompe a skill e encaminha a demanda para `esteira-orchestration`, na trilha expressa.
2. Sem evidência, não há ajuste pocket. Pedido sem dado, gravação, chamado, relato ou achado de teste volta ao solicitante com a pergunta: "o que mostra que isso é um problema?".
3. Não estimar números. Valor atual ausente recebe `[pendente de dados]`.
4. Havendo iniciativa relacionada, ler `contexto.md`. O ajuste não pode contrariar um Out of Scope vigente; se contrariar, é mudança de escopo e segue para a trilha expressa.
5. Não propor melhorias além do pedido. Ideias adjacentes são listadas ao final como "fora deste ajuste", sem entrar no escopo.
6. O documento deve ser curto: cada item cabe em um parágrafo ou em uma tabela pequena. Item que exija mais do que isso é sinal de que a demanda não é pocket.

## Algoritmo de Execução

### 0. Triagem

Aplicar os sete critérios:

| Critério | Por que desqualifica |
| :--- | :--- |
| Altera um único ponto de um fluxo existente | Mais de um ponto exige rever a jornada (Módulo 3) |
| Cabe em uma única issue, com esforço até 5 | Acima disso há decomposição e priorização (Módulo 4) |
| Não cria nem altera coleta, uso ou exposição de dados pessoais | Exige a análise de conformidade (Módulos 1 e 6) |
| Não exige integração nova nem mudança de modelo de dados ou de contrato de API | Exige especificação de arquitetura (Módulo 6) |
| É reversível sem migração de dados | Mudança irreversível exige aprovação de sponsor e Tech Lead |
| Não altera a Visão de Produto, os OKRs nem um Out of Scope vigente | É decisão estratégica ou de escopo (Módulos 2 e 4) |
| O problema tem ao menos uma evidência | Sem evidência, é hipótese a validar (Etapa 2B) |

Em caso de dúvida em qualquer critério, responder "Não".

### 1. Problema e evidência

Descrever o que acontece hoje e quem é afetado. Registrar a evidência com tipo e fonte. Separar o que é suposição: normalmente a causa presumida e o efeito esperado do ajuste.

### 2. Resultado esperado

Uma métrica, o valor atual com fonte e a direção esperada. Vincular a um Key Result da iniciativa, se houver. Não criar OKR novo.

### 3. Feature Frame

Contexto, Problema, Solução, esforço e Out of Scope, com os mesmos critérios da skill `behavioral-modeling-feature-framing`: limites verificáveis, nunca vazios.

### 4. Interface

Tabela "antes e depois" apenas dos elementos alterados, estados afetados e microcopy. Mensagens de erro seguem a regra: o que aconteceu + por que aconteceu + como resolver. Indicar o que precisa ser conferido em acessibilidade (contraste 4.5:1 para texto e 3:1 para componentes, foco visível, área de toque de 44×44px, rótulos para leitor de tela) ou declarar "sem impacto".

### 5. Handoff

Uma issue no padrão `### ISSUE AJ-NN — título`, compatível com `scripts/criar_issues.py`, contendo Por quê, Escopo, Out of Scope transcrito e ao menos três cenários em Gherkin:

1. caminho feliz;
2. exceção ou borda;
3. não regressão: o comportamento vizinho que deve permanecer igual.

### 6. Verificação pós-entrega

O que conferir, onde e quando. O resultado é preenchido depois da publicação; se a métrica não se mover, o ajuste retorna como insumo do Módulo 7 ou de um experimento (Módulo 8).

### 7. Autoverificação e aprovação

Preencher a tabela de autoverificação do modelo. Apresentar o documento ao aprovador e registrar nome, papel e data. A skill não registra aprovação em nome do usuário.

## Gatilhos de escalonamento durante a execução

Interromper e encaminhar para a trilha expressa se, ao detalhar o ajuste, surgir qualquer um destes sinais:

- a solução passou a exigir segunda issue ou segunda tela nova;
- o esforço foi revisto para 8 ou mais;
- apareceu dado pessoal, integração ou mudança de modelo de dados;
- a evidência aponta para um problema maior do que o ajuste resolve;
- o solicitante acrescentou requisitos durante a conversa.

Ao escalonar, o documento pocket parcial é mantido como insumo da iniciativa.

## Padrão de Entrega (Markdown)

Usar o modelo `assets/pocket.md`. Nome do arquivo: `AJ-NN-<slug>.md`, com numeração sequencial na pasta de ajustes.

## Fechamento

Havendo iniciativa relacionada, acrescentar uma linha a "Alterações em artefatos já aprovados" de `aprovacoes.md`: data, identificador do ajuste, o que mudou e a evidência. Após a verificação pós-entrega, registrar o resultado no próprio documento do ajuste.
