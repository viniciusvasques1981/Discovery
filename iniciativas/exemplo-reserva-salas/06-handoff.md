# Módulo 6 — Handoff Técnico: Reserva de salas (exemplo fictício)

**Entrada:** `contexto.md`, `02-estrategia.md`, `04-feature-frames.md`, `05-prototipacao.md`. A Etapa 5B não foi executada.

> Os blocos entre marcadores `montar:` são preenchidos por `iniciativa.py montar <dir>`. Não escreva dentro deles.

## Backlog Técnico

### ISSUE FF-01 — Consulta de disponibilidade de salas

<!-- montar:por-que -->
**Por quê:** O membro precisa confiar que a sala reservada estará disponível quando chegar. Contribui para KR2 (Proporção das reservas feitas por autoatendimento).
<!-- /montar:por-que -->

<!-- montar:escopo -->
**Escopo:** Grade com as salas da unidade selecionada, por dia e faixa de horário, indicando livre ou ocupado. Abre no dia corrente.
<!-- /montar:escopo -->

**Telas:** T-01

<!-- montar:out-of-scope -->
**Out of Scope** (transcrito do Feature Frame):

- Não exibe quem reservou cada horário.
- Não exibe disponibilidade de mais de uma unidade na mesma tela.
- Não sincroniza com agendas externas.
<!-- /montar:out-of-scope -->

**Critérios de aceite:**

```gherkin
# language: pt
Funcionalidade: Consulta de disponibilidade de salas

  Cenário: [FF-01-C1] Caminho feliz — ver horários livres do dia corrente
    Dado que estou autenticado como membro
    E a unidade "Centro" tem a sala "Sala 1" livre das 14h às 15h de hoje
    Quando acesso a tela de disponibilidade
    Então vejo a grade do dia de hoje para a unidade "Centro"
    E a célula da "Sala 1" às 14h indica "livre"

  Cenário: [FF-01-C2] Exceção — falha ao carregar a disponibilidade
    Dado que estou autenticado como membro
    E o serviço de disponibilidade está indisponível
    Quando acesso a tela de disponibilidade
    Então vejo a mensagem "Não foi possível carregar a disponibilidade. A conexão com o servidor falhou. Tente novamente."
    E vejo o botão "Tentar novamente"

  Cenário: [FF-01-C3] Borda — unidade sem horário livre no dia
    Dado que estou autenticado como membro
    E todas as salas da unidade "Centro" estão ocupadas em todos os horários de hoje
    Quando acesso a tela de disponibilidade
    Então vejo a mensagem de estado vazio com a orientação de escolher outro dia ou outra unidade
    E nenhuma célula é clicável
```

---

### ISSUE FF-02 — Reserva por autoatendimento com bloqueio de conflito

<!-- montar:por-que -->
**Por quê:** O membro precisa confiar que a sala reservada estará disponível quando chegar. Contribui para KR1 (Reduzir os conflitos de reserva registrados por mês), KR2 (Proporção das reservas feitas por autoatendimento).
<!-- /montar:por-que -->

<!-- montar:escopo -->
**Escopo:** O membro confirma sala, data, início e fim. O sistema grava a reserva somente se o intervalo estiver livre; se outro membro reservou antes, informa o conflito e mantém a grade atualizada.
<!-- /montar:escopo -->

**Telas:** T-02, T-03

<!-- montar:out-of-scope -->
**Out of Scope** (transcrito do Feature Frame):

- Não desconta nem verifica créditos de horas do plano.
- Não cobra excedente.
- Não permite reservar em nome de outro membro.
- Não cria reservas recorrentes.
- Não libera fechadura de sala.
<!-- /montar:out-of-scope -->

**Critérios de aceite:**

```gherkin
# language: pt
Funcionalidade: Reserva por autoatendimento

  Cenário: [FF-02-C1] Caminho feliz — reservar um horário livre
    Dado que estou autenticado como membro
    E a "Sala 1" da unidade "Centro" está livre amanhã das 10h às 11h
    Quando confirmo a reserva da "Sala 1" para amanhã das 10h às 11h
    Então vejo a tela de reserva confirmada com unidade, sala, data e horário
    E a reserva é gravada em meu nome
    E a célula da "Sala 1" às 10h de amanhã passa a indicar "ocupado"

  Cenário: [FF-02-C2] Exceção — horário reservado por outro membro durante a confirmação
    Dado que estou na tela de confirmação da "Sala 1" para amanhã das 10h às 11h
    E outro membro reservou a "Sala 1" para amanhã das 10h às 11h
    Quando clico em "Confirmar reserva"
    Então vejo a mensagem "Este horário acabou de ser reservado por outro membro. Escolha outro horário."
    E nenhuma reserva é gravada em meu nome
    E a grade de disponibilidade é exibida atualizada

  Cenário: [FF-02-C3] Borda — duas confirmações simultâneas para o mesmo intervalo
    Dado que dois membros estão na tela de confirmação da "Sala 1" para amanhã das 10h às 11h
    Quando os dois clicam em "Confirmar reserva" no mesmo instante
    Então exatamente uma reserva é gravada para o intervalo
    E o outro membro recebe a mensagem de conflito

  Cenário: [FF-02-C4] Borda — sobreposição parcial de intervalo
    Dado que a "Sala 1" está reservada amanhã das 10h às 11h
    Quando confirmo a reserva da "Sala 1" para amanhã das 10h30 às 11h30
    Então vejo a mensagem de conflito
    E nenhuma reserva é gravada

  Cenário: [FF-02-C5] Borda — clique repetido no botão de confirmação
    Dado que estou na tela de confirmação de um horário livre
    Quando clico duas vezes seguidas em "Confirmar reserva"
    Então o botão fica desabilitado após o primeiro clique
    E exatamente uma reserva é gravada
```

---

### ISSUE FF-03 — Minhas reservas e cancelamento

<!-- montar:por-que -->
**Por quê:** O membro precisa confiar que a sala reservada estará disponível quando chegar. Contribui para KR1 (Reduzir os conflitos de reserva registrados por mês).
<!-- /montar:por-que -->

<!-- montar:escopo -->
**Escopo:** Lista das reservas futuras do membro, com opção de cancelar. O horário cancelado volta a ficar livre na grade.
<!-- /montar:escopo -->

**Telas:** T-04

<!-- montar:out-of-scope -->
**Out of Scope** (transcrito do Feature Frame):

- Não aplica antecedência mínima nem penalidade de cancelamento.
- Não permite editar a reserva; alterar exige cancelar e reservar de novo.
- Não exibe reservas passadas.
<!-- /montar:out-of-scope -->

**Critérios de aceite:**

```gherkin
# language: pt
Funcionalidade: Minhas reservas e cancelamento

  Cenário: [FF-03-C1] Caminho feliz — cancelar uma reserva futura
    Dado que tenho uma reserva da "Sala 1" para amanhã das 10h às 11h
    Quando cancelo essa reserva e confirmo no modal
    Então vejo o aviso "Reserva cancelada"
    E a reserva deixa de aparecer em minhas reservas
    E a célula da "Sala 1" às 10h de amanhã volta a indicar "livre"

  Cenário: [FF-03-C2] Exceção — falha ao cancelar
    Dado que tenho uma reserva futura
    E o serviço de reservas está indisponível
    Quando confirmo o cancelamento
    Então vejo a mensagem "Não foi possível cancelar a reserva. A conexão com o servidor falhou. Tente novamente."
    E a reserva permanece em minhas reservas

  Cenário: [FF-03-C3] Borda — membro sem reservas futuras
    Dado que não tenho reservas futuras
    Quando acesso minhas reservas
    Então vejo a mensagem "Você não tem reservas futuras."
    E vejo o botão "Nova reserva"

  Cenário: [FF-03-C4] Borda — tentativa de cancelar reserva de outro membro
    Dado que existe uma reserva em nome de outro membro
    Quando envio uma requisição de cancelamento dessa reserva
    Então a requisição é recusada
    E a reserva permanece ativa
```

---

## Especificação de Arquitetura

Os insumos informam apenas a stack (E010). Todos os contratos abaixo são proposta.

### APIs e Endpoints

| Método | Caminho | Descrição | Requisição | Resposta | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| GET | `/unidades/{id}/disponibilidade?data=AAAA-MM-DD` | Salas e intervalos ocupados do dia | — | Lista de salas com intervalos ocupados, sem identificação do titular | `[a validar com o time técnico]` |
| POST | `/reservas` | Cria reserva | `salaId`, `inicio`, `fim` | 201 com a reserva; 409 em conflito | `[a validar com o time técnico]` |
| GET | `/reservas/minhas` | Reservas futuras do membro autenticado | — | Lista | `[a validar com o time técnico]` |
| DELETE | `/reservas/{id}` | Cancela reserva do próprio membro | — | 204; 403 se a reserva for de outro membro | `[a validar com o time técnico]` |

### Estrutura de Dados

| Entidade | Campo | Tipo | Nulo | Validação |
| :--- | :--- | :--- | :--- | :--- |
| Sala | `id`, `unidadeId`, `nome` | identificador, identificador, texto | Não | `[a validar com o time técnico]` |
| Reserva | `id`, `salaId`, `membroId` | identificadores | Não | `membroId` = usuário autenticado |
| Reserva | `inicio`, `fim` | data e hora | Não | `fim` > `inicio` |
| Reserva | `canal` | enumeração: `autoatendimento`, `recepcao` | Não | Necessário ao KR2 |
| Reserva | `canceladaEm` | data e hora | Sim | — |

### Regras de Negócio e Concorrência

| Regra | Idempotência | Controle transacional | Restrição de persistência |
| :--- | :--- | :--- | :--- |
| Uma sala não pode ter duas reservas ativas com intervalos sobrepostos | Clique repetido não cria segunda reserva | Verificação e gravação na mesma transação | Restrição no banco que impeça sobreposição por sala (em Postgres, restrição de exclusão sobre intervalo) `[a validar com o time técnico]` |
| Somente o titular cancela a própria reserva | Cancelar duas vezes não gera erro | — | — |

### Infraestrutura e Integrações

- Reuso da autenticação existente por e-mail e senha (E010).
- Carga inicial: reservas futuras da planilha precisam ser importadas antes do lançamento; durante a transição, a recepção registra no sistema com `canal = recepcao`. `[a validar com o time técnico]`
- Sem integração com fechaduras (E017), agenda externa (E016) ou pagamento (E014).

## System Prompt para Coding Assistant

```text
# Contexto do produto
# >>> montar:contexto-produto
Por quê: O membro precisa confiar que a sala reservada estará disponível quando chegar.
Visão: Para membros da Nimbo Coworking, cujo problema é não saber se há sala livre e perder salas já reservadas, a Reserva de Salas é um módulo de autoatendimento do sistema de membros que mostra a disponibilidade das 14 salas e garante que cada horário tenha uma única reserva.
# <<< montar:contexto-produto

# Stack e bibliotecas permitidas
Frontend React; API Node; banco Postgres. Usar as bibliotecas já presentes no projeto.
Não adicionar dependências sem aprovação.

# Regras de interface
Usar os componentes e tokens da biblioteca do sistema; proibido valor fixo de cor, espaçamento
e tipografia. Estado da célula de horário indicado por texto além de cor. Grade navegável por
teclado. Botão "Confirmar reserva" desabilitado e em Loading após o primeiro clique.

# Regras de negócio críticas
1. Uma sala não pode ter duas reservas ativas com intervalos sobrepostos. A garantia deve
   estar no banco, não apenas na interface.
2. Somente o titular cancela a própria reserva.
3. Toda reserva registra o canal: autoatendimento ou recepcao.
4. A consulta de disponibilidade não devolve a identidade de quem reservou.

# Limites de escopo — não implementar
# >>> montar:limites
FF-01 — Consulta de disponibilidade:
- Não exibe quem reservou cada horário.
- Não exibe disponibilidade de mais de uma unidade na mesma tela.
- Não sincroniza com agendas externas.
FF-02 — Reserva por autoatendimento com bloqueio de conflito:
- Não desconta nem verifica créditos de horas do plano.
- Não cobra excedente.
- Não permite reservar em nome de outro membro.
- Não cria reservas recorrentes.
- Não libera fechadura de sala.
FF-03 — Minhas reservas e cancelamento:
- Não aplica antecedência mínima nem penalidade de cancelamento.
- Não permite editar a reserva; alterar exige cancelar e reservar de novo.
- Não exibe reservas passadas.
# <<< montar:limites

# Definição de pronto
Os cenários BDD das issues FF-01, FF-02 e FF-03 devem passar.
```

## Plano de Instrumentação

| Key Result | Evento ou medida | Gatilho | Propriedades | Onde instrumentar | Issue |
| :--- | :--- | :--- | :--- | :--- | :--- |
| KR1 | Conflitos registrados pela recepção | Duas equipes para a mesma sala e horário | unidade, sala, data | Registro manual da recepção (mesma coluna de ocorrências usada na linha de base) | — |
| KR1 | `reserva_conflito_bloqueado` | API devolve conflito na criação | salaId, unidadeId | Backend | FF-02 |
| KR2 | `reserva_criada` | Reserva gravada | canal, salaId, unidadeId, antecedência em horas | Backend | FF-02 |
| KR2 | `disponibilidade_consultada` | Grade carregada | unidadeId, data consultada | Frontend | FF-01 |
| KR1 | `reserva_cancelada` | Cancelamento gravado | salaId, antecedência em horas | Backend | FF-03 |
| KR3 | Não comparecimento por reserva | Início do horário sem presença do membro | unidade, sala, data | Registro manual da recepção por 4 semanas, em planilha própria | — |

**Linha de base**

| Key Result | Linha de base atual | Fonte | Situação |
| :--- | :--- | :--- | :--- |
| KR1 | 41 conflitos em outubro/2026 | Planilha de reservas (E003) | Coletada — um único mês |
| KR2 | 0% | Processo atual (E002) | Coletada |
| KR3 | Inexistente | E008 | A coletar: medição manual começa no lançamento |

O KR3 não tem evento no sistema neste ciclo porque FF-05 ficou fora do MVP. A medição é manual. A propriedade "antecedência em horas" permite testar a hipótese H4 sem custo adicional.

## Dados pessoais e conformidade

| Dado pessoal | Finalidade | Onde é armazenado | Quem acessa | Retenção | Situação |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Nome, e-mail e telefone do membro | Identificar o titular da reserva; já constam do cadastro (E018) | Banco do sistema de membros | Recepção e o próprio membro | Não informada | `[a validar com o responsável por privacidade]` — responsável não identificado (D3) |
| Histórico de reservas por membro | Operação das salas | Banco do sistema de membros | Recepção e o próprio membro | Não informada | `[a validar com o responsável por privacidade]` |

- A consulta de disponibilidade não expõe a identidade de quem reservou (Out of Scope de FF-01).
- Eventos de instrumentação usam identificadores de sala e unidade; não carregam nome, e-mail nem telefone.
- Se for adotada ferramenta de gravação de sessão para o Módulo 7, mascarar os campos de identificação do membro.

## Verificação de rastreabilidade

| Verificação | Resultado | Observação |
| :--- | :--- | :--- |
| Todo Feature Frame do MVP tem uma issue | Conforme | FF-01, FF-02, FF-03 |
| Toda issue tem caminho feliz, exceção e borda | Conforme | — |
| Blocos derivados montados por script (`iniciativa.py montar`) | Conforme | Por quê, Escopo, Out of Scope e limites do System Prompt |
| Por quê e Key Result presentes em cada issue | Conforme | — |
| Todo Key Result tem evento no plano de instrumentação | Conforme com ressalva | KR3 medido manualmente, fora do sistema |
| Todo dado pessoal tem finalidade e responsável | Pendente | Responsável por privacidade não identificado (D3) |
