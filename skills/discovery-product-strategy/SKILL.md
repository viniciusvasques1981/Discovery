---
name: discovery-product-strategy
description: "Processar dados brutos (transcrições, notas de imersão, entrevistas e documentos legados), eliminando ambiguidades e definindo a direção estratégica e os objetivos mensuráveis do produto. Cobre os Módulos 1 (Discovery) e 2 (Estratégia) da esteira: Matriz CSD, dores validadas, Golden Circle, Visão de Produto, Matriz de Hipóteses e OKRs. Use quando houver material bruto de imersão para organizar ou quando for preciso definir o norte estratégico de uma iniciativa."
---

# Discovery e Estratégia de Produto

Módulos 1 e 2 da Esteira de Produto AI-Enhanced.

| | |
| :--- | :--- |
| **Frameworks** | Design Thinking (fase de Empatia), Golden Circle, Lean UX |
| **Entradas** | Transcrições, notas de imersão, entrevistas, documentos legados |
| **Saídas** | `01-discovery.md` e `02-estrategia.md` em `iniciativas/<slug>/` |
| **Próxima skill** | `behavioral-modeling-feature-framing`; antes dela, opcionalmente, `hypothesis-validation-research` (Etapa 2B) |

## Regras de execução

1. Trabalhar somente com o que está nos insumos. Não completar lacunas com conhecimento genérico de mercado.
2. Cada item da Matriz CSD e cada dor deve citar a origem (documento, participante ou trecho).
3. Marcar como `[inferência]` toda conclusão que não esteja literal nos insumos.
4. Se os insumos forem insuficientes para um bloco, registrar a lacuna em Dúvidas em vez de preenchê-lo.
5. Se não houver insumo algum, solicitar o material antes de produzir qualquer saída.

## Algoritmo de Execução

### Módulo 1 — O Mergulho (Discovery)

#### 1. Download do Problema

- **Cenário atual:** como o processo funciona hoje, quem participa e quais sistemas estão envolvidos.
- **Premissas:** condições assumidas como verdadeiras pelos participantes.
- **Limitações técnicas:** restrições de infraestrutura, integração, prazo, orçamento ou conformidade citadas.
- **Dados pessoais e conformidade:** quais dados pessoais a iniciativa trata, quem são os titulares, se há dados sensíveis e quais exigências regulatórias (LGPD), contratuais ou de segurança foram citadas. Resposta ausente nos insumos é registrada como Dúvida. O bloco identifica o tema; não substitui parecer jurídico nem avaliação do encarregado de dados.

#### 2. Triagem CSD (Matriz de Certezas, Suposições e Dúvidas)

- **Certezas:** Fatos comprovados com dados históricos, restrições contratuais/técnicas confirmadas ou diretrizes institucionais validadas.
- **Suposições:** Hipóteses de comportamento, palpites de stakeholders e premissas operacionais que exigem teste em campo. Formular como afirmações falseáveis.
- **Dúvidas:** Lacunas técnicas, indefinições de regras de negócio e limites de infraestrutura. Formular estritamente como perguntas objetivas.

Critério de classificação: se não há evidência documental ou dado, o item não é Certeza. Declaração de stakeholder sem dado de suporte é Suposição.

#### 3. Dores Validadas do Negócio/Operação

Listar cada dor com: descrição, quem sofre, evidência (frequência, custo, tempo ou citação) e impacto no negócio. Dor sem evidência vai para Suposições.

### Módulo 2 — O Propósito (Estratégia)

#### 4. Alinhamento Estratégico (Golden Circle & Lean UX)

- **Por quê (Propósito):** A razão fundamental da iniciativa existir além do retorno financeiro imediato.
- **Como (Diferencial):** O método operacional ou vantagem competitiva.
- **O quê (Entrega):** A solução concreta disponibilizada.

#### 5. Declaração de Visão de Produto

Sintetizar no formato:

> Para **[cliente/usuário alvo]**, cujo **[problema ou necessidade prioritária]**, o **[nome da solução]** é um **[categoria do produto]** que **[benefício principal e diferencial competitivo]**.

#### 6. Matriz de Hipóteses (Lean UX)

Converter as Suposições de maior risco em hipóteses testáveis:

> Acreditamos que **[resultado de negócio]** será alcançado se **[usuário/persona]** obtiver **[benefício]** por meio de **[funcionalidade ou intervenção]**. Saberemos que estamos certos quando **[sinal mensurável]**.

Priorizar por risco (impacto se a hipótese for falsa) e por custo de validação.

As hipóteses de risco alto podem ser testadas antes do Módulo 3 pela Etapa 2B, opcional (`hypothesis-validation-research`). Se a etapa não for executada, as hipóteses seguem com a situação "não validada" e a decisão é registrada em `contexto.md`.

#### 7. Formulação de OKRs

Estruturar 1 Objetivo qualitativo e inspirador acompanhado de 3 Key Results com baseline, meta e janela temporal definida, categorizados pela tipologia de medição correspondente:

| Tipologia | Uso |
| :--- | :--- |
| Evolutivo | Indicador que parte de uma linha de base e deve subir ou descer até a meta |
| Recorrente | Meta que precisa ser atingida a cada período (semana, mês) |
| Cumulativo | Soma de entregas ou volume ao longo da janela |
| Binário | Feito / não feito |
| Faixa | Indicador que deve permanecer entre limites mínimo e máximo |
| Janela Deslizante | Média ou soma dos últimos N dias |
| Percentil | Meta sobre a distribuição (ex.: p95 de tempo de resposta) |
| Razão | Relação entre duas medidas (ex.: conversão, taxa de erro) |
| Instrumentação | KR de criação da medição, quando a linha de base ainda não existe |

Quando a linha de base for desconhecida, não estimar: usar um KR de Instrumentação. Iniciativas com mais de uma frente estratégica podem ter até 3 Objetivos, cada um com seus Key Results.

## Padrão de Entrega (Markdown)

Usar os modelos `assets/01-discovery.md` e `assets/02-estrategia.md`.

**`01-discovery.md`**

- **Download do Problema:** cenário atual, premissas, limitações técnicas e dados pessoais e conformidade.
- **Matriz CSD:** Seções dedicadas para Certezas, Suposições e Dúvidas.
- **Dores Validadas do Negócio/Operação.**

**`02-estrategia.md`**

- **Alinhamento Estratégico:** Golden Circle e Declaração da Visão de Produto.
- **Matriz de Hipóteses.**
- **Matriz de OKRs:** Tabela contendo Objetivo, Key Results, Tipologia de Medição, Linha de Base e Meta.

## Passagem de contexto

Ao concluir, atualizar `iniciativas/<slug>/contexto.md` (modelo em `assets/contexto.md`) com: Por quê, Visão de Produto, dores validadas, OKRs, limitações técnicas, dados pessoais e conformidade, hipóteses com a respectiva situação e Dúvidas ainda abertas. Esse resumo é a entrada obrigatória do Módulo 3.
