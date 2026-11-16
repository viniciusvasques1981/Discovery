# Módulo 6 — Handoff Técnico: sincronizacao-fabricacao-canteiro

**Entrada:** `contexto.md`, `04-feature-frames.md`, `05-prototipacao.md`  
**Status:** handoff técnico fictício, com pontos de validação de arquitetura e instrumentação.

> Os blocos marcados com `montar:` são preenchidos por script em execução real; neste exercício fictício, eles foram transcritos para manter o contexto do produto e do escopo.

## Backlog Técnico

### ISSUE FF-01 — Painel de sincronização fábrica x canteiro

**Por quê:**
- O problema central é a baixa sincronização entre planejamento fabril e execução no canteiro.
- Os OKRs do produto priorizam previsibilidade operacional, redução de atrasos e melhoria do controle de impactos.

**Escopo:**
- Centralizar status de cronograma, produção e obra em um painel operacional.
- Exibir sincronização por frente de trabalho e por status de liberação.
- Apresentar origem dos dados e a última atualização conhecida.

**Telas:** T-01, T-02, T-03

**Out of Scope:**
- automação completa de replanejamento
- previsão avançada de demanda
- integração profunda com todas as fontes operacionais de um único passo
- dashboard executivo com regras de negócio não definidas pela operação

**Critérios de aceite:**

```gherkin
# language: pt
Funcionalidade: painel de sincronização fábrica x canteiro

  Cenário: [FF-01-C1] Visão geral da sincronização
    Dado que o gestor abre o painel de sincronização
    Quando a tela carrega dados de produção e obra
    Então o sistema exibe o status por frente, a última atualização e os desvios identificados
    E mostra a origem dos dados e o estado do carregamento

  Cenário: [FF-01-C2] Tela sem fonte configurada
    Dado que o contexto selecionado não possui fonte conectada
    Quando o painel tenta carregar indicadores
    Então o sistema mostra mensagem de ausência de dados e orienta o usuário a configurar a fonte
    E não exibe indicadores com valores inventados

  Cenário: [FF-01-C3] Falha de sincronização
    Dado que uma fonte de dados falha ou fica desatualizada
    Quando o painel processa a leitura
    Então o sistema sinaliza a falha, identifica a fonte e mantém o histórico mais recente como desatualizado
    E não informa ao usuário que os dados estão em dia
```

---

### ISSUE FF-02 — Impacto de alterações de projeto

**Por quê:**
- Alterações de projeto geram atraso e retrabalho quando não chegam em tempo real ao canteiro.
- O produto precisa apoiar a decisão com impacto de cronograma, materiais e equipes.

**Escopo:**
- Registrar alterações com contexto de projeto, frente e impacto esperável.
- Exibir o impacto em cronograma, materiais e equipes afetadas.
- Indicar a necessidade de revisão de sequência e despacho.

**Telas:** T-02, T-09

**Out of Scope:**
- cálculo de otimização automatizada de sequência
- decisões de escopo sem registro formal
- remoção automática de pendências não aprovadas

**Critérios de aceite:**

```gherkin
# language: pt
Funcionalidade: impacto de alterações de projeto

  Cenário: [FF-02-C1] Alteração registrada com impacto calculado
    Dado que existe uma alteração de projeto validada
    Quando o sistema processa o evento de alteração
    Então o painel mostra os impactos em cronograma, materiais e frentes afetadas
    E identifica a data do impacto calculado e a origem da alteração

  Cenário: [FF-02-C2] Alteração sem fonte confiável
    Dado que a alteração chegou sem identificador ou sem dados mínimos
    Quando o sistema tenta associar o impacto
    Então o sistema registra o evento como incompleto e solicita revisão manual
    E não calcula impacto definitivo sem a validação mínima

  Cenário: [FF-02-C3] Alerta de frente afetada
    Dado que uma frente de trabalho é afetada por uma alteração
    Quando o impacto é calculado
    Então o sistema marca a frente em alerta e apresenta a lista de itens críticos afetados
    E mantém o histórico da alteração para rastreabilidade
```

---

### ISSUE FF-03 — Status de componentes e ferramental

**Por quê:**
- A indisponibilidade de materiais, formas e gabaritos gera paradas intermitentes, ociosidade e turnover.
- O rastreio precisa ser simples, confiável e ligado ao uso real por frente.

**Escopo:**
- Exibir disponibilidade por material, forma e ferramental em cada frente.
- Apresentar status de indisponibilidade, atraso e histórico de movimentação.
- Assumir que a ação depende de identificação consistente de materiais e fontes.

**Telas:** T-03, T-06, T-09

**Out of Scope:**
- otimização automática de estoque
- previsão de demanda de materiais por ciclo de produção
- rastreio de embarque logístico completo

**Critérios de aceite:**

```gherkin
# language: pt
Funcionalidade: status de componentes e ferramental

  Cenário: [FF-03-C1] Material indisponível em frente
    Dado que um material, forma ou gabarito está sem disponibilidade para a frente atual
    Quando o painel consulta o status
    Então o sistema mostra o alerta e o impacto esperado sobre a execução
    E destaca a frente afetada e o item indisponível

  Cenário: [FF-03-C2] Status sem dado confiável
    Dado que a fonte de material está indisponível ou sem padronização de código
    Quando o sistema consulta o item
    Então o sistema retorna status “indisponível para validação” e não classifica a disponibilidade como positiva
    E orienta o usuário para revisão de dados

  Cenário: [FF-03-C3] Rastreabilidade por frente
    Dado que a frente recebe atualização de disponibilidade
    Quando o sistema registra o evento
    Então o histórico do item e da frente é atualizado para rastreio operacional
    E o painel reflete a mudança de forma transparente
```

---

## Especificação de Arquitetura

### APIs e Endpoints

| Método | Caminho | Descrição | Requisição | Resposta | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| GET | `/api/v1/projetos/{id}/status` | devolve status por frente e indicadores do painel | contexto do projeto | JSON com status, fontes e última sincronização | `[a validar com o time técnico]` |
| GET | `/api/v1/frentes/{id}/impactos` | listas alterações e impactos calculados | id da frente | JSON com impactos, materiais e equipes afetadas | `[a validar com o time técnico]` |
| GET | `/api/v1/materiais/{id}/status` | retorna disponibilidade e registros de indisponibilidade | material ou forma/gabarito | JSON de status e histórico | `[a validar com o time técnico]` |
| POST | `/api/v1/alteracoes` | cria alteração de projeto com contexto mínimo | payload de alteração | confirmação do registro e id | `[a validar com o time técnico]` |
| POST | `/api/v1/importacoes/planilhas` | upload de XLSX para validação inicial de dados operacionais | arquivo + metadados | id da importação + status de processamento | `[a validar com o time técnico]` |

### Estrutura de Dados

| Entidade | Campo | Tipo | Nulo | Validação |
| :--- | :--- | :--- | :--- | :--- |
| Projeto | id | string | Não | obrigatório |
| Projeto | nome | string | Não | obrigatório |
| Projeto | status | enum | Sim | produção / obra / bloqueado |
| FrenteTrabalho | id | string | Não | obrigatório |
| FrenteTrabalho | projetoId | string | Não | FK para Projeto |
| FrenteTrabalho | status | enum | Não | planejada / em_execucao / bloqueada |
| AlteracaoProjeto | id | string | Não | obrigatório |
| AlteracaoProjeto | projetoId | string | Não | FK |
| AlteracaoProjeto | frenteId | string | Sim | FK opcional |
| AlteracaoProjeto | impacto | object | Não | cronograma, material, equipe |
| Material | id | string | Não | obrigatório |
| Material | codigo | string | Não | padronização mínima |
| Material | status | enum | Não | disponivel / indisponivel / em_validacao |

### Regras de Negócio e Concorrência

| Regra | Idempotência | Controle transacional | Restrição de persistência |
| :--- | :--- | :--- | :--- |
| Alteração do mesmo projeto com mesmo identificador deve ser idempotente | Sim | transação por registro | evitar duplicidade de alteração |
| Impacto em cronograma deve depender de frente e projeto válidos | Sim | validar antes de guardar | não gerar impacto sem contexto |
| Material indisponível deve manter rastreio histórico | Sim | evento + atualização de status | manter histórico para auditoria |
| Importação manual de planilha deve validar formato e campos mínimos | Sim | etapa de validação antes do cálculo | reprocessamento em lote controlado |

### Infraestrutura e Integrações

- Integração inicial com ERP e planilhas XLSX.
- Fonte primária de dados operacionais: SQL/ERP e planilhas de apontamento.
- Regras de qualidade: campos mínimos, padronização de códigos e data/hora de atualização.
- Padrão de sincronização e consistência: guardar a última atualização por fonte e nunca substituir um dado válido por um valor desconhecido sem explicação.
- Dependências de arquitetura e segurança: validação de autenticação, autorização e retenção de dados ainda precisam de confirmação técnica.

---

## System Prompt para Coding Assistant

```text
# Contexto do produto
O produto é um sistema de sincronização operacional entre fábrica e canteiro, com foco em visibilidade do cronograma, impacto de alterações, rastreio de componentes e redução de ociosidade por indisponibilidade de materiais e formas.

# Stack e bibliotecas permitidas
[lista a validar com o time técnico]. Não adicionar dependências fora desta lista sem aprovação.

# Regras de interface
- seguir o guia de UI do módulo 5
- priorizar leitura rápida no dashboard
- manter status de dados e fontes explícitos
- não inventar métricas sem linha de base e instrumentação definidas

# Regras de negócio críticas
- uma alteração de projeto só pode gerar impacto quando houver projeto, frente e contexto mínimos válidos
- status de material/forma deve distinguir disponível, indisponível e em validação
- dados de origem e última atualização devem ser exibidos
- telas de dashboard não podem mostrar indicadores sem fonte e sem status claro

# Limites de escopo
- não implementar otimização avançada de agenda, previsão de demanda ou automação completa de logística
- não assumir que o app operacional está no MVP sem decisão formal de escopo
- não criar integrações que não estejam explicitamente aprovadas

# Definição de pronto
Os cenários BDD de cada issue devem passar e o sistema deve manter rastreio de eventos e dados de origem.
```

---

## Plano de Instrumentação

Entregável obrigatório. Cada Key Result precisa de ao menos um evento ou medida que permita calculá-lo.

| Key Result | Evento ou medida | Gatilho | Propriedades | Onde instrumentar | Issue |
| :--- | :--- | :--- | :--- | :--- | :--- |
| KR1: tempo médio de resposta a alterações de projeto | `alteracao_projeto_registrada` | alteração de projeto validada | projetoId, frenteId, tipoAlteracao, tempoResposta | Frontend/Backend | FF-02 |
| KR1: tempo médio de resposta a alterações de projeto | `impacto_cronograma_calculado` | cálculo de impacto da alteração | projetoId, frenteId, impactoPrevisto, critico | Backend | FF-02 |
| KR2: taxa de atrasos por frente de trabalho | `frente_execucao_atualizada` | atualização operacional da frente | frenteId, projetoId, status, data | Frontend/Backend | FF-01 |
| KR3: paradas por indisponibilidade | `material_indisponivel_alerta` | material/forma sem disponibilidade | materialId, codigo, frenteId, origem, severidade | Frontend/Backend | FF-03 |
| KR3: paradas por indisponibilidade | `status_material_atualizado` | mudança de status do item | materialId, statusAnterior, statusNovo, frenteId | Backend | FF-03 |

**Linha de base**

| Key Result | Linha de base atual | Fonte | Situação |
| :--- | :--- | :--- | :--- |
| KR1 | a coletar antes do lançamento | registros históricos de alteração e cronograma | Coletar antes do lançamento |
| KR2 | a coletar antes do lançamento | cronograma por frente e indicadores da obra | Coletar antes do lançamento |
| KR3 | a coletar antes do lançamento | registros de indisponibilidade e paradas | Coletar antes do lançamento |

Linha de base não disponível deve ser coletada antes do lançamento. Sem ela, o Key Result não pode ser avaliado após a entrega.

## Dados pessoais e conformidade

| Dado pessoal | Finalidade | Onde é armazenado | Quem acessa | Retenção | Situação |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Nenhum dado pessoal identificado nos insumos | operação e acompanhamento de produção | não aplicável | não aplicável | não aplicável | confirmado |
| Registros fotográficos (se aprovados no futuro) | evidência de execução / conformidade | a definir | a definir | a definir | `[a validar com o responsável por privacidade]` |

Eventos de instrumentação não devem carregar dados pessoais em propriedades sem necessidade. Ferramentas de gravação de sessão exigem mascaramento de campos sensíveis, caso sejam habilitadas.

## Verificação de rastreabilidade

| Verificação | Resultado | Observação |
| :--- | :--- | :--- |
| Todo Feature Frame do MVP tem uma issue | Sim | FF-01, FF-02, FF-03 |
| Toda issue tem caminho feliz, exceção e borda | Sim | 3 cenários por issue |
| Blocos derivados montados por script (`iniciativa.py montar`) | Não executado neste exercício | script a ser executado em ambiente da esteira |
| Por quê e Key Result presentes em cada issue | Sim | transcrição manual conforme contexto |
| Todo Key Result tem evento no plano de instrumentação | Sim | eventos listados no plano |
| Todo dado pessoal tem finalidade e responsável | Sim | sem dados pessoais identificados |

