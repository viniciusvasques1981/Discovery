# Módulo 5 — Prototipação: Reserva de salas (exemplo fictício)

**Entrada:** `contexto.md`, `04-feature-frames.md`
**Design System:** não fornecido — tokens provisórios. O sistema de membros existe (E010), mas sua biblioteca de componentes não consta nos insumos.

## Fluxo de Telas

[T-01 Disponibilidade] → [T-02 Confirmar reserva] → [T-03 Reserva confirmada] → [T-04 Minhas reservas]

T-04 também é acessível pelo menu do sistema de membros.

## Especificação de Telas

### T-01 — Disponibilidade

| | |
| :--- | :--- |
| **Feature Frame** | FF-01 |
| **Estágio da jornada** | J1 |
| **Objetivo** | Mostrar as salas livres da unidade no dia escolhido |
| **Ação primária** | Selecionar um horário livre |
| **Ações secundárias** | Trocar unidade; trocar dia |
| **Entrada / saída** | Entrada pelo menu "Salas"; saída para T-02 |

**Wireframe descritivo:**

1. Cabeçalho: seletor de unidade e seletor de dia (padrão: dia corrente).
2. Grade: linhas = salas da unidade; colunas = faixas de horário. Cada célula indica livre ou ocupado por texto e por cor.
3. Legenda dos estados da célula.

**Estados:**

| Estado | Comportamento |
| :--- | :--- |
| Carregando | Skeleton da grade com as dimensões finais |
| Vazio | "Não há horários livres nesta unidade em [data]. Escolha outro dia ou outra unidade." |
| Erro | "Não foi possível carregar a disponibilidade. A conexão com o servidor falhou. Tente novamente." com botão "Tentar novamente" |
| Sucesso | Grade preenchida |

Célula ocupada não é clicável e não exibe quem reservou (Out of Scope de FF-01).

---

### T-02 — Confirmar reserva

| | |
| :--- | :--- |
| **Feature Frame** | FF-02 |
| **Estágio da jornada** | J2 |
| **Objetivo** | Confirmar sala, data, início e fim |
| **Ação primária** | "Confirmar reserva" |
| **Ações secundárias** | "Voltar" |
| **Entrada / saída** | Entrada por T-01; saída para T-03 ou retorno a T-01 em caso de conflito |

**Wireframe descritivo:**

1. Resumo: unidade, sala, data.
2. Campos: horário de início (preenchido pela célula escolhida) e horário de fim.
3. Botões: "Confirmar reserva" (primário) e "Voltar".

**Estados:**

| Estado | Comportamento |
| :--- | :--- |
| Carregando | Botão primário em Loading e desabilitado após o primeiro clique |
| Vazio | Não se aplica: a tela só abre com um horário selecionado |
| Erro | Conflito: "Este horário acabou de ser reservado por outro membro. Escolha outro horário." com retorno a T-01 atualizada |
| Sucesso | Navega para T-03 |

---

### T-03 — Reserva confirmada

| | |
| :--- | :--- |
| **Feature Frame** | FF-02 |
| **Estágio da jornada** | J2 |
| **Objetivo** | Dar a confirmação imediata da reserva |
| **Ação primária** | "Ver minhas reservas" |
| **Ações secundárias** | "Fazer outra reserva" |
| **Entrada / saída** | Entrada por T-02; saída para T-04 ou T-01 |

**Wireframe descritivo:**

1. Mensagem de confirmação com unidade, sala, data e horário.
2. Botões de continuação.

**Estados:** apenas Sucesso; a tela só é exibida após a gravação da reserva.

---

### T-04 — Minhas reservas

| | |
| :--- | :--- |
| **Feature Frame** | FF-03 |
| **Estágio da jornada** | J3, J4 |
| **Objetivo** | Listar as reservas futuras e permitir o cancelamento |
| **Ação primária** | "Cancelar reserva" |
| **Ações secundárias** | "Nova reserva" |
| **Entrada / saída** | Entrada pelo menu ou por T-03; saída para T-01 |

**Wireframe descritivo:**

1. Lista em ordem cronológica: unidade, sala, data, horário e ação "Cancelar reserva".
2. Modal de confirmação do cancelamento.

**Estados:**

| Estado | Comportamento |
| :--- | :--- |
| Carregando | Skeleton da lista |
| Vazio | "Você não tem reservas futuras." com botão "Nova reserva" |
| Erro | "Não foi possível cancelar a reserva. A conexão com o servidor falhou. Tente novamente." |
| Sucesso | Toast "Reserva cancelada" e item removido da lista |

---

## Matriz de Componentes e Tokens

| Componente | Origem no Design System | Telas | Default | Hover | Active | Focus | Disabled | Loading |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Botão primário | Provisório | T-02, T-03, T-04 | Sim | Sim | Sim | Sim | Sim | Sim |
| Botão secundário | Provisório | T-02, T-03, T-04 | Sim | Sim | Sim | Sim | Sim | Não se aplica |
| Seletor (unidade, dia) | Provisório | T-01 | Sim | Sim | Sim | Sim | Sim | Não se aplica |
| Célula de horário livre | Provisório | T-01 | Sim | Sim | Sim | Sim | Não se aplica | Não se aplica |
| Célula de horário ocupado | Provisório | T-01 | Sim | Não | Não | Não | Sim (estado único) | Não se aplica |
| Modal de confirmação | Provisório | T-04 | Sim | — | — | Foco preso no modal | — | — |
| Toast | Provisório | T-04 | Sim | — | — | — | — | — |

**Tokens (provisórios):**

| Categoria | Token | Valor | Uso |
| :--- | :--- | :--- | :--- |
| Cor | `feedback.success` | a definir | Célula livre, toast |
| Cor | `neutral.disabled` | a definir | Célula ocupada |
| Cor | `feedback.error` | a definir | Mensagens de erro |
| Espaçamento | `space.2` / `space.4` | 8px / 16px | Grade e formulário |

**Lacunas do Design System:** a biblioteca do sistema de membros não foi fornecida; todos os componentes estão como provisórios. A grade de horários provavelmente não tem equivalente `[inferência]`.

## Acessibilidade (WCAG 2.1 AA)

| Requisito | Critério | Telas |
| :--- | :--- | :--- |
| Contraste de texto | ≥ 4.5:1 | Todas |
| Contraste de componentes | ≥ 3:1 entre célula livre e ocupada | T-01 |
| Estado não dependente de cor | Célula informa "livre" ou "ocupado" por texto ou ícone com rótulo | T-01 |
| Área de toque | ≥ 44×44px por célula em telas touch | T-01 |
| Navegação por teclado | Setas percorrem a grade; Enter seleciona; foco visível | T-01 |
| Leitor de tela | Célula anuncia sala, horário e estado | T-01 |
| Feedback visual | < 200ms após o clique em "Confirmar reserva" | T-02 |

## Guia de Microcopy

| Tela | Elemento | Texto |
| :--- | :--- | :--- |
| T-02 | CTA | Confirmar reserva |
| T-02 | Erro de conflito | Este horário acabou de ser reservado por outro membro. Escolha outro horário. |
| T-02 | Erro de validação | O horário de fim deve ser posterior ao de início. Ajuste o horário de fim. |
| T-04 | CTA | Cancelar reserva |
| T-04 | Modal | Cancelar a reserva da [sala] em [data], [horário]? O horário ficará livre para outros membros. |
| T-04 | Empty state | Você não tem reservas futuras. |

## Guia de UI para o Assistente de Código

```text
Stack de interface: React (sistema de membros existente).
Biblioteca do Design System: a confirmar com o time; não criar biblioteca nova.
Componentes permitidos por tela:
  T-01: seletor, grade de horários, legenda.
  T-02: resumo, campos de horário, botão primário, botão secundário.
  T-03: mensagem de confirmação, botões.
  T-04: lista, botão, modal de confirmação, toast.
Tokens obrigatórios: usar os tokens da biblioteca do sistema; proibido valor fixo de cor, espaçamento e tipografia.
Requisitos de acessibilidade: estado da célula por texto além de cor; grade navegável por teclado; botão de confirmação desabilitado e em Loading após o primeiro clique.
```
