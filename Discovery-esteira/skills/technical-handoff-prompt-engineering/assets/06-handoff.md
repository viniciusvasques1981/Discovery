# Módulo 6 — Handoff Técnico: [iniciativa]

**Entrada:** `contexto.md`, `04-feature-frames.md`, `05-prototipacao.md`

## Backlog Técnico

### ISSUE FF-01 — [título]

**Por quê:** [propósito da iniciativa] — contribui para [KR_].

**Escopo:** [solução do Feature Frame]

**Telas:** T-_

**Out of Scope** (transcrito do Feature Frame):

- Não [limite].

**Critérios de aceite:**

```gherkin
# language: pt
Funcionalidade: [nome]

  Cenário: [FF-01-C1] Caminho feliz — [objetivo]
    Dado que [estado inicial]
    Quando [ação]
    Então [resultado observável]
    E [validação de persistência ou interface]

  Cenário: [FF-01-C2] Exceção — [objetivo]
    Dado que [estado inicial]
    Quando [ação]
    Então [resultado observável]

  Cenário: [FF-01-C3] Borda — [objetivo]
    Dado que [estado inicial]
    Quando [ação]
    Então [resultado observável]
```

---

## Especificação de Arquitetura

### APIs e Endpoints

| Método | Caminho | Descrição | Requisição | Resposta | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| | | | | | confirmado / `[a validar com o time técnico]` |

### Estrutura de Dados

| Entidade | Campo | Tipo | Nulo | Validação |
| :--- | :--- | :--- | :--- | :--- |
| | | | | |

### Regras de Negócio e Concorrência

| Regra | Idempotência | Controle transacional | Restrição de persistência |
| :--- | :--- | :--- | :--- |
| | | | |

### Infraestrutura e Integrações

## System Prompt para Coding Assistant

```text
# Contexto do produto
[Por quê e Visão de Produto]

# Stack e bibliotecas permitidas
[lista]. Não adicionar dependências fora desta lista sem aprovação.

# Regras de interface
[Guia de UI do Módulo 5]

# Regras de negócio críticas
[lista]

# Limites de escopo — não implementar
[Out of Scope consolidado, transcrito literalmente]

# Definição de pronto
Os cenários BDD de cada issue devem passar.
```

## Métricas a instrumentar

| Key Result | Evento ou medida | Onde instrumentar |
| :--- | :--- | :--- |
| | | |

## Verificação de rastreabilidade

| Verificação | Resultado | Observação |
| :--- | :--- | :--- |
| Todo Feature Frame do MVP tem uma issue | | |
| Toda issue tem caminho feliz, exceção e borda | | |
| Out of Scope idêntico em Feature Frame, issue e System Prompt | | |
| Por quê e Key Result presentes em cada issue | | |
