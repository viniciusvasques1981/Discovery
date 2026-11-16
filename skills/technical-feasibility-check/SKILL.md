---
name: technical-feasibility-check
description: "Avaliar a viabilidade técnica de um catálogo de Feature Frames antes do recorte de MVP: esforço revisado em Fibonacci, dependências e restrições, risco técnico e parecer por funcionalidade. Parte do Módulo 4 da esteira. Use quando houver Feature Frames propostos e for preciso saber o que é viável no ciclo, ou quando o esforço estimado por produto precisar de revisão técnica."
---

# Checagem de Viabilidade Técnica

Etapa do Módulo 4 da Esteira de Produto AI-Enhanced, executada pelo Tech Lead (pessoa do time ou agente `handoff-tech-lead`).

| | |
| :--- | :--- |
| **Entradas** | `04-feature-frames.md` e a seção "1–2. Por quê" de `contexto.md` (restrições); informações de stack e arquitetura, quando disponíveis |
| **Saída** | Seção "Checagem de viabilidade técnica" de `04-feature-frames.md` |

## Regras de execução

1. Não alterar Contexto, Problema, Solução nem Out of Scope dos Feature Frames. A checagem só preenche a própria seção.
2. Sem informação de stack e arquitetura, o parecer é preliminar: declarar essa condição e listar o que precisa ser confirmado pelo time técnico.
3. Não inventar restrições. Dependência não citada nas entradas é apresentada como pergunta ao time.

## Algoritmo de Execução

Para cada Feature Frame:

1. **Esforço revisado:** 1, 2, 3, 5, 8 ou 13, com o motivo quando diferir do proposto. Item em 13 deve ser decomposto.
2. **Dependências e restrições:** integrações, dados, infraestrutura e conformidade.
3. **Risco técnico:** Alto, Médio ou Baixo.
4. **Parecer:** Viável / Viável com ressalva / Inviável neste ciclo.

Feature Frame com parecer "Inviável neste ciclo" sai do MVP. Registrar o responsável pela checagem e a data.

## Fechamento

Acrescentar as ressalvas, em uma linha, à seção "3–4. Usuário e escopo" de `contexto.md`.
