# Revisões Independentes: Reserva de salas (exemplo fictício)

Registro das revisões do agente `artifact-reviewer`. Para brevidade, o exemplo detalha três revisões; as demais constam apenas pelo parecer na tabela de Aprovações de `contexto.md`.

## Revisão de `01-discovery.md` — 2026-11-03

**Comparado com:** `00-insumos/transcricao-imersao.md`

### Parecer

Aprovado

### Apontamentos

| # | Tipo | Local no artefato | Apontamento | Evidência | Severidade | Situação |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| — | — | — | Nenhum apontamento Bloqueante ou Relevante | — | — | — |

### Itens conferidos sem apontamento

| Verificação | Resultado |
| :--- | :--- |
| Números (3 unidades, 14 salas, 612 reservas, 41 conflitos) idênticos aos da transcrição | Conforme (L01, L03) |
| Estimativas sem registro (2 horas por dia, 20% de não comparecimento) classificadas como Suposição | Conforme (L07, L08 → S3, S2) |
| Percentual de 6,7% marcado como inferência e restrito a um mês | Conforme |
| Não comparecimento fora das dores validadas | Conforme |
| Dúvidas em forma de pergunta | Conforme |
| Nenhuma solução proposta no Módulo 1 | Conforme |

### Limites desta revisão

C1, C4 e C5 são declarações de participantes sem documento de suporte. Foram aceitas como Certeza por tratarem de fatos estruturais informados por quem responde por eles; a decisão cabe ao aprovador.

## Revisão de `02-estrategia.md` — 2026-11-03

**Comparado com:** `00-insumos/transcricao-imersao.md`, `01-discovery.md`

### Parecer

Aprovado com ressalvas

### Apontamentos

| # | Tipo | Local no artefato | Apontamento | Evidência | Severidade | Situação |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| R-00 | Classificação incorreta | Matriz de OKRs, KR1 | A linha de base usa um único mês; o artefato declara a limitação, mas a meta de zero é avaliada contra uma referência sem variação conhecida | L03 cita apenas outubro | Menor | Aceito pelo aprovador |

### Itens conferidos sem apontamento

| Verificação | Resultado |
| :--- | :--- |
| Visão de Produto no formato padrão | Conforme |
| Hipóteses derivadas de Suposições existentes (S1, S2, S4, S5) | Conforme |
| Meta de 70% do KR2 presente nos insumos | Conforme (L09) |
| KR3 como Instrumentação, sem linha de base estimada | Conforme |

### Limites desta revisão

O "Como" do Golden Circle está marcado como inferência; a adequação estratégica não é objeto desta revisão.

## Revisão de `06-handoff.md` — 2026-11-04

**Comparado com:** `04-feature-frames.md`, `05-prototipacao.md`, `02-estrategia.md`, `contexto.md`

### Parecer

Reprovado na primeira revisão; Aprovado após a correção de R-01.

### Apontamentos

| # | Tipo | Local no artefato | Apontamento | Evidência | Severidade | Situação |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| R-01 | Rastreabilidade quebrada | Plano de Instrumentação | O KR3 não tinha evento nem medida. FF-05, que registraria o comparecimento, está fora do MVP | `02-estrategia.md` define o KR3; `04-feature-frames.md` classifica FF-05 como "MVP: Não" | Bloqueante | Corrigido: incluída a medida manual pela recepção por 4 semanas |
| R-02 | Campo obrigatório ausente | Dados pessoais e conformidade | Retenção não informada e responsável não identificado | D3 em `01-discovery.md` | Relevante | Aceito pelo aprovador; marcado como a validar |

### Itens conferidos sem apontamento

| Verificação | Resultado |
| :--- | :--- |
| Uma issue por Feature Frame do MVP | Conforme (FF-01, FF-02, FF-03) |
| Out of Scope idêntico ao do Módulo 4 nas issues e no System Prompt | Conforme, nos três Feature Frames |
| Caminho feliz, exceção e borda em cada issue | Conforme |
| Por quê e Key Result em cada issue | Conforme |
| Contratos de API marcados como a validar | Conforme |
| Mensagens dos cenários idênticas ao Guia de Microcopy | Conforme |

### Limites desta revisão

A adequação técnica dos contratos propostos e da restrição de banco não foi avaliada: depende do esquema atual, não fornecido.
