---
name: technical-handoff-prompt-engineering
description: "Consolidar os Feature Frames e especificações de UI em artefatos de engenharia de software prontos para desenvolvimento, testes de aceitação e contextualização de assistentes de código de IA (Cursor, GitHub Copilot, Claude Code, Gemini CLI). Cobre o Módulo 6 (Handoff Técnico) da esteira: issues estruturadas, cenários BDD/Gherkin, contratos de arquitetura e System Prompt para assistente de código. Use quando escopo e interface estiverem especificados e for preciso preparar a entrega para o time técnico."
---

# Handoff Técnico e Engenharia de Prompt

Módulo 6 da Esteira de Produto AI-Enhanced.

| | |
| :--- | :--- |
| **Framework** | Agile Handoff |
| **Entradas** | `contexto.md`, `04-feature-frames.md` e `05-prototipacao.md` da iniciativa |
| **Saída** | `06-handoff.md` em `iniciativas/<slug>/` |
| **Skill anterior** | `systemic-ui-interaction-design` |
| **Próxima skill** | `behavioral-analytics-ux-fixes` (após a entrega em produção) |

## Regras de execução

1. Cada issue corresponde a um Feature Frame do MVP e mantém o identificador dele.
2. Os limites Out of Scope são transcritos literalmente do Feature Frame para a issue e para o System Prompt. Não resumir nem reinterpretar.
3. Contratos de API, modelos de dados e infraestrutura não informados nos insumos são apresentados como proposta, com a marca `[a validar com o time técnico]`.
4. Cada issue deve conter o Por quê da iniciativa (propósito e Key Result relacionado), conforme `contexto.md`.

## Algoritmo de Execução

### 1. Especificação de Aceite em BDD / Gherkin

Elaborar cenários funcionais cobrindo caminho feliz (happy path), cenários de exceção e condições de borda usando a sintaxe estrita:

```gherkin
Cenário: [Identificador e Objetivo do Teste]
  Dado que [condição ou estado inicial do sistema]
  E [contexto complementar, se aplicável]
  Quando [ação disparada pelo usuário ou evento de mensageria]
  Então [resultado ou mutação de estado observável]
  E [validação de persistência ou interface]
```

Usar `# language: pt` no início de arquivos `.feature`. Cada cenário valida um único comportamento observável.

### 2. Contexto Técnico e Contratos de Arquitetura

- **APIs e Endpoints:** Métodos HTTP, caminhos relativos, cabeçalhos, parâmetros e payloads de requisição/resposta.
- **Estrutura de Dados:** Tipagens, restrições de nulabilidade e validações de esquema.
- **Regras de Negócio e Concorrência:** Idempotência, controle transacional e restrições de persistência.
- **Infraestrutura e Integrações:** Sistemas envolvidos, dependências externas e requisitos não funcionais citados no Discovery.

### 3. Metaprompting para LLMs de Código

Sintetizar o contexto do projeto em um System Prompt com regras restritivas, isolando bibliotecas permitidas, proibindo dependências arbitrárias e transcrevendo os limites de Out of Scope herdados do Feature Frame.

Estrutura mínima do System Prompt:

1. Contexto do produto (Por quê e Visão de Produto).
2. Stack e bibliotecas permitidas.
3. Regras de interface (Guia de UI do Módulo 5).
4. Regras de negócio críticas.
5. Limites de escopo (Out of Scope consolidado).
6. Definição de pronto (cenários BDD que devem passar).

## Padrão de Entrega (Markdown)

Usar o modelo `assets/06-handoff.md`.

- **Backlog Técnico / Issues Estruturadas:** Título, escopo e cenários formais em BDD/Gherkin.
- **Especificação de Arquitetura:** Contratos de integração, modelos de dados e restrições de negócio.
- **System Prompt para Coding Assistant:** Bloco de instruções de contexto pronto para compor o arquivo `.cursorrules`, `.github/copilot-instructions.md`, `AGENTS.md`, prompt de sistema ou contexto de workspace.

## Verificação de rastreabilidade

Antes de concluir, conferir e registrar o resultado na entrega:

| Verificação | Critério |
| :--- | :--- |
| Feature Frame → Issue | Todo Feature Frame do MVP tem uma issue |
| Issue → BDD | Toda issue tem caminho feliz, exceção e borda |
| Out of Scope | Limites idênticos em Feature Frame, issue e System Prompt |
| Por quê | Propósito e Key Result presentes em cada issue |

## Passagem de contexto

Ao concluir, atualizar `iniciativas/<slug>/contexto.md` com: lista de issues, métricas a instrumentar em produção (derivadas dos OKRs) e pendências marcadas como `[a validar com o time técnico]`.
