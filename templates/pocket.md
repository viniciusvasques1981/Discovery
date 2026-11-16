# Ajuste Pocket: [título]

| | |
| :--- | :--- |
| **Identificador** | AJ-[NN] |
| **Data** | AAAA-MM-DD |
| **Solicitante** | |
| **Iniciativa relacionada** | `iniciativas/[slug]/` ou "nenhuma" |
| **Aprovador** | [nome e papel] — [data] |

## 0. Triagem

Todas as respostas devem ser "Sim". Um "Não" encaminha o ajuste para a trilha expressa.

| Critério | Sim / Não |
| :--- | :--- |
| Altera um único ponto de um fluxo existente (um estágio da jornada) | |
| Cabe em uma única issue, com esforço até 5 em Fibonacci | |
| Não cria nem altera coleta, uso ou exposição de dados pessoais | |
| Não exige integração nova nem mudança de modelo de dados ou de contrato de API | |
| É reversível sem migração de dados | |
| Não altera a Visão de Produto, os OKRs nem um limite Out of Scope vigente | |
| O problema tem ao menos uma evidência (item 1) | |

## 1. Problema e evidência

- **O que acontece hoje:**
- **Quem é afetado:**
- **Evidência** (ao menos uma):

| Tipo | Descrição | Fonte |
| :--- | :--- | :--- |
| Dado de uso / Gravação de sessão / Chamado de suporte / Relato de usuário / Achado de teste | | |

- **O que é suposição:** [causa presumida ou efeito esperado ainda não comprovado]

## 2. Resultado esperado

| | |
| :--- | :--- |
| **Métrica** | |
| **Valor atual** | [número com fonte, ou `[pendente de dados]`] |
| **Direção esperada** | Aumentar / Diminuir / Eliminar |
| **Key Result relacionado** | KR_ da iniciativa, ou "nenhum" |

## 3. Feature Frame

| | |
| :--- | :--- |
| **Contexto** | Momento exato e gatilho em que o ajuste entra em ação. |
| **Problema** | A dor específica resolvida. |
| **Solução** | O comportamento funcional e visual após o ajuste. |
| **Esforço (Fibonacci)** | 1 / 2 / 3 / 5 |

**Out of Scope (Limites Rígidos):**

- Não [limite verificável].

## 4. Interface

Somente o que muda.

| Tela / elemento | Antes | Depois |
| :--- | :--- | :--- |
| | | |

- **Estados afetados** (carregando, vazio, erro, sucesso):
- **Microcopy:**
- **Acessibilidade** (contraste, foco, área de toque, leitor de tela): [o que precisa ser conferido neste ajuste, ou "sem impacto"]

## 5. Handoff

### ISSUE AJ-[NN] — [título]

**Por quê:** [problema e evidência em uma frase] — [métrica esperada].

**Escopo:** [solução do Feature Frame]

**Out of Scope** (transcrito do item 3):

- Não [limite].

**Critérios de aceite:**

```gherkin
# language: pt
Funcionalidade: [nome]

  Cenário: [AJ-NN-C1] Caminho feliz — [objetivo]
    Dado que [estado inicial]
    Quando [ação]
    Então [resultado observável]

  Cenário: [AJ-NN-C2] Exceção ou borda — [objetivo]
    Dado que [estado inicial]
    Quando [ação]
    Então [resultado observável]

  Cenário: [AJ-NN-C3] Não regressão — [comportamento que deve permanecer]
    Dado que [estado inicial]
    Quando [ação]
    Então [resultado observável]
```

## 6. Verificação pós-entrega

| | |
| :--- | :--- |
| **O que conferir** | [a métrica do item 2] |
| **Onde** | [ferramenta ou relatório] |
| **Quando** | [prazo após a publicação] |
| **Resultado** | [preencher após a conferência] |

## Autoverificação

| Verificação | Resultado |
| :--- | :--- |
| Triagem com todas as respostas "Sim" | |
| Evidência citada com fonte | |
| Nenhum número estimado; valores ausentes marcados `[pendente de dados]` | |
| Out of Scope idêntico nos itens 3 e 5 | |
| Ajuste não contraria Out of Scope vigente da iniciativa | |
| Cenário de não regressão presente | |
