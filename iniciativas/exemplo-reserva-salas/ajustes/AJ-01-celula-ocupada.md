# Ajuste Pocket: Célula de horário ocupado sem aparência de botão (exemplo fictício)

| | |
| :--- | :--- |
| **Identificador** | AJ-01 |
| **Data** | 2027-02-15 |
| **Solicitante** | Helena (Diretora de Operações) |
| **Iniciativa relacionada** | `iniciativas/exemplo-reserva-salas/` |
| **Aprovador** | Helena, Product Manager — 2027-02-15 |

## 0. Triagem

| Critério | Sim / Não |
| :--- | :--- |
| Altera um único ponto de um fluxo existente (um estágio da jornada) | Sim — J1, tela T-01 |
| Cabe em uma única issue, com esforço até 5 em Fibonacci | Sim — esforço 2 |
| Não cria nem altera coleta, uso ou exposição de dados pessoais | Sim |
| Não exige integração nova nem mudança de modelo de dados ou de contrato de API | Sim — alteração apenas de interface |
| É reversível sem migração de dados | Sim |
| Não altera a Visão de Produto, os OKRs nem um limite Out of Scope vigente | Sim — mantém "Não exibe quem reservou cada horário" (FF-01) |
| O problema tem ao menos uma evidência (item 1) | Sim |

## 1. Problema e evidência

- **O que acontece hoje:** membros clicam em células de horário ocupado na grade de disponibilidade e nada acontece.
- **Quem é afetado:** membros que consultam a disponibilidade.
- **Evidência:**

| Tipo | Descrição | Fonte |
| :--- | :--- | :--- |
| Dado de uso | Dead click em 388 de 1.840 sessões (21,1%) em `/disponibilidade`, de 09 a 11/02/2027 | `00-insumos/telemetria-pos-lancamento.md` |
| Gravação de sessão | Em 9 de 12 gravações com dead click, o clique ocorreu sobre célula ocupada | `00-insumos/telemetria-pos-lancamento.md` |

- **O que é suposição:** que a causa seja a aparência interativa da célula (achado A1 de `07-diagnostico-comportamental.md`); que a redução de dead clicks melhore a conclusão de reservas.

## 2. Resultado esperado

| | |
| :--- | :--- |
| **Métrica** | Proporção de sessões com dead click em `/disponibilidade` |
| **Valor atual** | 21,1% (388 de 1.840 sessões, 09 a 11/02/2027) |
| **Direção esperada** | Diminuir |
| **Key Result relacionado** | KR2, de forma indireta |

## 3. Feature Frame

| | |
| :--- | :--- |
| **Contexto** | O membro visualiza a grade de disponibilidade (T-01) com horários ocupados. |
| **Problema** | A célula ocupada é percebida como clicável e não responde. |
| **Solução** | A célula ocupada perde os sinais de interatividade (cursor de ponteiro e efeito de hover) e exibe o rótulo "Ocupado". |
| **Esforço (Fibonacci)** | 2 |

**Out of Scope (Limites Rígidos):**

- Não exibe quem reservou o horário.
- Não torna a célula ocupada clicável nem abre detalhe da reserva.
- Não altera a célula de horário livre.
- Não inclui o destaque do próximo horário livre (tratado no experimento EXP-01).

## 4. Interface

| Tela / elemento | Antes | Depois |
| :--- | :--- | :--- |
| T-01 — célula ocupada | Cursor de ponteiro e hover iguais aos da célula livre; estado indicado por cor | Cursor padrão, sem hover; rótulo "Ocupado" visível |

- **Estados afetados:** apenas Sucesso (grade preenchida).
- **Microcopy:** "Ocupado".
- **Acessibilidade:** conferir contraste do rótulo (≥ 4.5:1); a célula ocupada sai da ordem de foco por teclado e continua anunciada pelo leitor de tela como "[sala], [horário], ocupado".

## 5. Handoff

### ISSUE AJ-01 — Remover aparência interativa da célula de horário ocupado

**Por quê:** 21,1% das sessões em `/disponibilidade` têm clique sem resposta, na maioria sobre células ocupadas — reduzir a proporção de sessões com dead click.

**Escopo:** A célula ocupada perde os sinais de interatividade (cursor de ponteiro e efeito de hover) e exibe o rótulo "Ocupado".

**Out of Scope** (transcrito do item 3):

- Não exibe quem reservou o horário.
- Não torna a célula ocupada clicável nem abre detalhe da reserva.
- Não altera a célula de horário livre.
- Não inclui o destaque do próximo horário livre (tratado no experimento EXP-01).

**Critérios de aceite:**

```gherkin
# language: pt
Funcionalidade: Célula de horário ocupado na grade de disponibilidade

  Cenário: [AJ-01-C1] Caminho feliz — célula ocupada não sugere interação
    Dado que a "Sala 1" está reservada hoje das 14h às 15h
    Quando visualizo a grade de disponibilidade de hoje
    Então a célula da "Sala 1" às 14h exibe o rótulo "Ocupado"
    E o cursor sobre essa célula é o padrão
    E a célula não apresenta efeito de hover

  Cenário: [AJ-01-C2] Borda — navegação por teclado ignora células ocupadas
    Dado que a "Sala 1" está reservada hoje das 14h às 15h e livre das 15h às 16h
    Quando percorro a grade pelo teclado
    Então o foco não para na célula das 14h
    E o leitor de tela anuncia a célula das 14h como "Sala 1, 14h, ocupado"

  Cenário: [AJ-01-C3] Não regressão — célula livre continua selecionável
    Dado que a "Sala 1" está livre hoje das 15h às 16h
    Quando clico na célula da "Sala 1" às 15h
    Então sou levado à tela de confirmação da reserva
```

## 6. Verificação pós-entrega

| | |
| :--- | :--- |
| **O que conferir** | Proporção de sessões com dead click em `/disponibilidade` |
| **Onde** | Ferramenta de sessão, via `scripts/clarity_resumo.py` |
| **Quando** | 3 dias após a publicação (janela máxima da exportação) |
| **Resultado** | A preencher |

## Autoverificação

| Verificação | Resultado |
| :--- | :--- |
| Triagem com todas as respostas "Sim" | Conforme |
| Evidência citada com fonte | Conforme |
| Nenhum número estimado; valores ausentes marcados `[pendente de dados]` | Conforme |
| Out of Scope idêntico nos itens 3 e 5 | Conforme |
| Ajuste não contraria Out of Scope vigente da iniciativa | Conforme |
| Cenário de não regressão presente | Conforme |

**Fora deste ajuste:** estado Loading do botão "Confirmar reserva" (achado A2) — é outro ponto do fluxo e deve ter documento próprio.
