---
name: discovery-product-strategy
description: "Processar dados brutos (transcrições, notas de imersão, entrevistas e documentos legados), eliminando ambiguidades e definindo a direção estratégica e os objetivos mensuráveis do produto. Cobre os Módulos 1 (Discovery) e 2 (Estratégia) da esteira: Base de Evidências, Matriz CSD, dores validadas, Golden Circle, Visão de Produto, Matriz de Hipóteses e OKRs. Use quando houver material bruto de imersão para organizar ou quando for preciso definir o norte estratégico de uma iniciativa."
---

# Discovery e Estratégia de Produto

Módulos 1 e 2 da Esteira de Produto AI-Enhanced.

| | |
| :--- | :--- |
| **Frameworks** | Design Thinking (fase de Empatia), Golden Circle, Lean UX |
| **Entradas** | Módulo 1: `00-insumos/`. Módulo 2: `evidencias.md` e `01-discovery.md` |
| **Saídas** | `evidencias.md`, `01-discovery.md` e `02-estrategia.md` em `iniciativas/<slug>/` |
| **Próxima skill** | `behavioral-modeling-feature-framing`; antes dela, opcionalmente, `hypothesis-validation-research` (Etapa 2B) |

## Regras de execução

1. Trabalhar somente com o que está nos insumos. Não completar lacunas com conhecimento genérico de mercado.
2. O material bruto é lido uma única vez, no passo 1. Do passo 2 em diante, a fonte é `evidencias.md`.
3. Cada item da Matriz CSD e cada dor cita os identificadores de evidência (E001, E002) que o sustentam.
4. Marcar como `[inferência]` toda conclusão que não esteja literal nas evidências.
5. Se as evidências forem insuficientes para um bloco, registrar a lacuna em Dúvidas em vez de preenchê-lo.
6. Se não houver insumo algum, solicitar o material antes de produzir qualquer saída.

## Algoritmo de Execução

### Módulo 1 — O Mergulho (Discovery)

#### 1. Base de Evidências

1. Numerar os insumos: `python3 scripts/iniciativa.py numerar iniciativas/<slug>`. O script grava cada documento em `00-insumos/numerados/` com um identificador por linha (`D1:L0012`) e um índice com o tamanho de cada documento.
2. Ler os documentos numerados **um por vez**. A cada documento, acrescentar as evidências extraídas a `evidencias.md` antes de abrir o seguinte. Não carregar todos os documentos de uma vez.
3. Cada evidência é uma afirmação fiel ao insumo, em uma frase, sem interpretação, com: identificador (E001…), tipo (Dado, Declaração, Relato, Restrição, Decisão, Pedido), fonte (quem disse ou qual documento) e referência de linha. Trechos contíguos usam faixa: `D1:L0012-L0015`.
4. Registrar tudo que possa sustentar uma certeza, suposição, dúvida, dor, restrição ou pedido. Conversa sem conteúdo (saudações, logística da reunião) não vira evidência.

Sem execução de scripts: citar documento e trecho de forma manual (`D1`, mais as primeiras palavras do trecho) e manter as demais regras.

#### 2. Download do Problema

- **Cenário atual:** como o processo funciona hoje, quem participa e quais sistemas estão envolvidos.
- **Premissas:** condições assumidas como verdadeiras pelos participantes.
- **Limitações técnicas:** restrições de infraestrutura, integração, prazo, orçamento ou conformidade citadas.
- **Dados pessoais e conformidade:** quais dados pessoais a iniciativa trata, quem são os titulares, se há dados sensíveis e quais exigências regulatórias (LGPD), contratuais ou de segurança foram citadas. Resposta ausente é registrada como Dúvida. O bloco identifica o tema; não substitui parecer jurídico nem avaliação do encarregado de dados.

#### 3. Triagem CSD (Matriz de Certezas, Suposições e Dúvidas)

- **Certezas:** Fatos comprovados com dados históricos, restrições contratuais/técnicas confirmadas ou diretrizes institucionais validadas.
- **Suposições:** Hipóteses de comportamento, palpites de stakeholders e premissas operacionais que exigem teste em campo. Formular como afirmações falseáveis.
- **Dúvidas:** Lacunas técnicas, indefinições de regras de negócio e limites de infraestrutura. Formular estritamente como perguntas objetivas.

Critério de classificação: evidência do tipo Dado, Restrição ou Decisão pode sustentar Certeza. Evidência do tipo Declaração, Relato isolado ou Pedido sustenta Suposição.

#### 4. Dores Validadas do Negócio/Operação

Listar cada dor com: descrição, quem sofre, evidência (frequência, custo, tempo ou citação) e impacto no negócio. Dor sem evidência vai para Suposições.

### Módulo 2 — O Propósito (Estratégia)

#### 5. Alinhamento Estratégico (Golden Circle & Lean UX)

- **Por quê (Propósito):** A razão fundamental da iniciativa existir além do retorno financeiro imediato. Escrever em uma frase: ela é copiada por script para cada issue do handoff.
- **Como (Diferencial):** O método operacional ou vantagem competitiva.
- **O quê (Entrega):** A solução concreta disponibilizada.

#### 6. Declaração de Visão de Produto

Sintetizar no formato:

> Para **[cliente/usuário alvo]**, cujo **[problema ou necessidade prioritária]**, o **[nome da solução]** é um **[categoria do produto]** que **[benefício principal e diferencial competitivo]**.

#### 7. Matriz de Hipóteses (Lean UX)

Converter as Suposições de maior risco em hipóteses testáveis:

> Acreditamos que **[resultado de negócio]** será alcançado se **[usuário/persona]** obtiver **[benefício]** por meio de **[funcionalidade ou intervenção]**. Saberemos que estamos certos quando **[sinal mensurável]**.

Priorizar por risco (impacto se a hipótese for falsa) e por custo de validação. As hipóteses de risco alto podem ser testadas antes do Módulo 3 pela Etapa 2B, opcional. Se a etapa não for executada, as hipóteses seguem com a situação "não validada".

#### 8. Formulação de OKRs

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

Quando a linha de base for desconhecida, não estimar: usar um KR de Instrumentação. Iniciativas com mais de uma frente estratégica podem ter até 3 Objetivos. Na tabela de OKRs, a primeira coluna de cada linha começa por `KR1 — `, `KR2 — `: o script de montagem do handoff lê esse formato.

## Imersão com mais de um produto

Quando as evidências apontam para mais de um produto, o Módulo 2 muda em três pontos:

1. **Estratégia por produto.** Usar o modelo `assets/02-estrategia-varios-produtos.md`: propósito comum e Matriz de Hipóteses primeiro; depois, uma seção por produto, com o título no formato do modelo,, com Golden Circle, Visão de Produto e OKRs próprios. Não há limite de produtos. Os Key Results são numerados dentro de cada produto (KR1, KR2…).
2. **Mapa de partilha preliminar.** Criar `partilha.md` (modelo `assets/partilha.md`) com a lista de produtos e a atribuição de cada dor e suposição do Módulo 1: Exclusivo, Compartilhado ou Sem dono. Dor sem dono é apontada ao sponsor.
3. **Ponto de separação.** Responder, com evidência, às duas perguntas do modelo. O padrão é o Módulo 4: Protopersona e Jornada To-Be são feitas em conjunto e cada estágio recebe um produto dono. Usar o Módulo 3 somente quando os produtos não compartilham usuário nem jornada.

A iniciativa da imersão é o tronco: fica no repositório da imersão e não segue além do ponto de separação. Cada produto continua no próprio repositório, a partir de `iniciativa.py derivar`.

## Padrão de Entrega (Markdown)

Modelos em `assets/evidencias.md`, `assets/01-discovery.md` e `assets/02-estrategia.md`.

- **`evidencias.md`:** tabela de evidências com identificador, tipo, fonte e referência de linha.
- **`01-discovery.md`:** Download do Problema, Matriz CSD e Dores Validadas do Negócio/Operação.
- **`02-estrategia.md`:** Alinhamento Estratégico, Declaração da Visão de Produto, Matriz de Hipóteses e Matriz de OKRs (Objetivo, Key Results, Tipologia de Medição, Linha de Base e Meta).

## Fechamento

1. Executar `python3 scripts/iniciativa.py verificar iniciativas/<slug>` e corrigir os erros apontados.
2. Atualizar apenas a seção "1–2. Por quê" de `contexto.md` (modelo em `assets/contexto.md`), em linhas curtas, e a tabela de Dúvidas abertas. Não copiar tabelas dos artefatos.
