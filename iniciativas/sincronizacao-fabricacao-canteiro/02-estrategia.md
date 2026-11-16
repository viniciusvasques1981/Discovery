# Módulo 1 — Discovery: sincronizacao-fabricacao-canteiro

**Entrada:** `evidencias.md`. A coluna Origem cita identificadores de evidência (E001, E002).

## Download do Problema

### Cenário atual

O processo de planejamento de fabricação e execução do canteiro ainda funciona em frentes separadas. O cronograma de produção e de montagem não está sincronizado em uma única visão, e a comunicação depende, em grande parte, de planilhas, reuniões e acompanhamento manual. Isso cria um gap entre a liberação de formas/gabaritos e a disponibilidade real da obra para a execução.

### Premissas

- A transformação de projeto para execução depende de informações compartilhadas entre fábrica, logística e obra.
- As mudanças de projeto são inevitáveis e têm impacto direto no cronograma de montagem.
- As equipes de montagem e produção têm conhecimento operacional suficiente para identificar os pontos de ruptura, mas não há um rastreio centralizado.
- A solução deve considerar dados em planilhas e ERP, sem depender de uma migração total imediatamente.

### Limitações técnicas

- Bases de dados e planilhas operacionais são heterogêneas e não estão totalmente integradas.
- Dados de campo têm menor confiabilidade e frequência de atualização do que dados da fábrica.
- O escopo do produto precisa respeitar um MVP com ingestão seletiva e priorização de fontes de verdade.

### Dados pessoais e conformidade

| Pergunta | Resposta | Origem |
| :--- | :--- | :--- |
| A iniciativa trata dados pessoais? Quais? | Em princípio, não há menção a dados pessoais de pessoas físicas. A estrutura é operacional e de controle de produção. | E006, E007 |
| Há dados pessoais sensíveis ou de crianças e adolescentes? | Não foi identificado nas evidências. | — |
| Quem são os titulares? | Não identificado nos insumos. | — |
| Há exigência regulatória, contratual ou de segurança citada? | Não há menção explícita a LGPD ou demais exigências, mas dados do ERP e de operação devem seguir governança interna. | E007 |
| Quem responde por privacidade e segurança na organização? | Não identificado. | — |

Resposta não encontrada nos insumos é registrada como Dúvida. Este bloco identifica o tema; não substitui parecer jurídico nem avaliação do encarregado de dados.

## Matriz CSD

### Certezas

| # | Certeza | Evidência | Origem |
| :--- | :--- | :--- | :--- |
| C1 | O planejamento de produção e a execução no canteiro ainda operam com baixa sincronização, em ambientes distintos. | E001, E009, E016 | E001, E009, E016 |
| C2 | Alterações de projeto afetam cronograma de frentes e exigem acompanhamento manual. | E002, E003 | E002, E003 |
| C3 | A variedade de formas e gabaritos customizados aumenta custo de setup e necessidade de estoque. | E004 | E004 |
| C4 | Falta de componentes provoca paradas intermitentes, ociosidade e turnover. | E005 | E005 |
| C5 | Dados da operação continuam em planilhas e bases heterogêneas, com integração incompleta. | E006, E007, E008 | E006, E007, E008 |

### Suposições

| # | Suposição (afirmação falseável) | Como validar | Origem |
| :--- | :--- | :--- | :--- |
| S1 | Uma visão unificada de fábrica x canteiro reduzirá o tempo de resposta a alterações de projeto. | medir redução no tempo de handoff e retrabalho | E002, E003, E010 |
| S2 | O sequenciamento de formas e o balanceamento de equipes terão impacto direto em produtividade e turnover. | comparar cronograma e ocupação de equipes | E012, E018 |
| S3 | O rastreio de componentes e materiais reduz paradas intermitentes e desperdício. | monitorar pendências e indisponibilidade por componente | E005, E017 |

### Dúvidas

| # | Dúvida (pergunta objetiva) | Quem pode responder | Origem |
| :--- | :--- | :--- | :--- |
| D1 | Qual é a frequência real de atualização dos dados de campo e quem é responsável pela manutenção? | gestor de operações | E008, E019 |
| D2 | Existe uma base única de referência para formas, gabaritos e componentes? | diretor industrial | E004, E014 |
| D3 | Há governança interna para dados operacionais e integração com ERP? | área de TI / processos | E007 |

## Dores Validadas do Negócio/Operação

| # | Dor | Quem sofre | Evidência | Impacto no negócio |
| :--- | :--- | :--- | :--- | :--- |
| P1 | Falta de sincronização entre planejamento e execução | gestores de operação e obra | E001, E009, E016 | atraso, retrabalho e perda de previsibilidade |
| P2 | Alteração de projeto sem visibilidade real para o canteiro | coordenação de obra e direção industrial | E002, E003 | impacto no cronograma e na entrega |
| P3 | Ociosidade e turnover por ausência de componentes e ferramental | equipes especializadas e gestão de produção | E005, E017 | queda de produtividade e custo de mão de obra |
| P4 | Setup e estoque de formas e gabaritos desbalanceados | operação fabril e logística | E004 | custo, espaço e baixa eficiência |

## Dúvidas prioritárias

As 3 dúvidas cuja resposta mais alteraria a estratégia:

1. Qual a qualidade e frequência real dos dados de campo disponíveis para alimentar o produto?
2. Há uma convenção única para materiais, formas e gabaritos ou o processo ainda é heterogêneo?
3. Quais integrações com ERP e planilhas devem entrar no MVP versus ficar fora do escopo?

