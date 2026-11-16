---
name: technical-handoff-prompt-engineering
description: "Consolidar os Feature Frames e especificações de UI em artefatos de engenharia de software prontos para desenvolvimento, testes de aceitação e contextualização de assistentes de código de IA (Cursor, GitHub Copilot, Claude Code, Gemini CLI). Cobre o Módulo 6 (Handoff Técnico) da esteira: issues estruturadas, cenários BDD/Gherkin, contratos de arquitetura, plano de instrumentação, conformidade de dados pessoais e System Prompt para assistente de código. Use quando escopo e interface estiverem especificados e for preciso preparar a entrega para o time técnico."
---

# Handoff Técnico e Engenharia de Prompt

Módulo 6 da Esteira de Produto AI-Enhanced.

| | |
| :--- | :--- |
| **Framework** | Agile Handoff |
| **Entradas** | `contexto.md`, `02-estrategia.md` (OKRs), `04-feature-frames.md` e `05-prototipacao.md`; `05b-teste-usabilidade.md`, se existir |
| **Saída** | `06-handoff.md` em `iniciativas/<slug>/` |
| **Skill anterior** | `systemic-ui-interaction-design` |
| **Próxima skill** | `behavioral-analytics-ux-fixes` (após a entrega em produção) |

## Regras de execução

1. Cada issue corresponde a um Feature Frame do MVP e mantém o identificador dele.
2. Não transcrever Out of Scope, Escopo nem o Por quê. Esses blocos ficam entre marcadores `montar:` e são preenchidos por script a partir dos Feature Frames e da estratégia. Escrever apenas o que é novo: título, telas, cenários BDD, contratos, instrumentação e as regras do System Prompt.
3. Contratos de API, modelos de dados e infraestrutura não informados nos insumos são apresentados como proposta, com a marca `[a validar com o time técnico]`.
4. Todo Key Result deve ter ao menos um evento ou medida no Plano de Instrumentação.
5. O título de cada issue segue o padrão `### ISSUE FF-NN — título`, exigido pelo script `scripts/criar_issues.py`.

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

### 3. Plano de Instrumentação

Entregável obrigatório. Derivar dos OKRs do Módulo 2:

- **Eventos e medidas:** para cada Key Result, o evento que permite calculá-lo, o gatilho, as propriedades e o ponto de instrumentação (frontend, backend ou ferramenta analítica). Vincular cada evento à issue que o implementa.
- **Linha de base:** valor atual de cada Key Result e fonte. Quando não existir, registrar "a coletar antes do lançamento" e criar a issue de instrumentação correspondente.
- **Telemetria comportamental:** indicar se haverá ferramenta de sessão (ex.: Microsoft Clarity), necessária ao Módulo 7.

### 4. Dados Pessoais e Conformidade

Para cada dado pessoal identificado no Módulo 1: finalidade, local de armazenamento, quem acessa e retenção. Informação não confirmada recebe a marca `[a validar com o responsável por privacidade]`. Eventos de instrumentação não devem carregar dados pessoais sem necessidade; ferramentas de gravação de sessão exigem mascaramento de campos sensíveis. Esta seção organiza a informação para o responsável; não constitui parecer jurídico.

### 5. Metaprompting para LLMs de Código

Sintetizar o contexto do projeto em um System Prompt com regras restritivas, isolando bibliotecas permitidas, proibindo dependências arbitrárias e transcrevendo os limites de Out of Scope herdados do Feature Frame.

Estrutura mínima do System Prompt:

1. Contexto do produto — bloco `montar:contexto-produto`, preenchido por script.
2. Stack e bibliotecas permitidas.
3. Regras de interface (Guia de UI do Módulo 5).
4. Regras de negócio críticas.
5. Limites de escopo — bloco `montar:limites`, preenchido por script.
6. Definição de pronto (cenários BDD que devem passar).

### 6. Montagem

Depois de escrever o arquivo com os marcadores vazios, executar:

```bash
python3 scripts/iniciativa.py montar iniciativas/<slug>
```

O script copia para cada issue o Por quê (propósito e Key Results do Feature Frame), o Escopo (Solução do Feature Frame) e o Out of Scope, e preenche os dois blocos do System Prompt. Pode ser executado de novo sempre que um Feature Frame mudar.

Sem execução de scripts: preencher os blocos manualmente, transcrevendo o Out of Scope sem alteração, e conferir a igualdade item a item.

## Padrão de Entrega (Markdown)

Usar o modelo `assets/06-handoff.md`.

- **Backlog Técnico / Issues Estruturadas:** Título, escopo e cenários formais em BDD/Gherkin.
- **Especificação de Arquitetura:** Contratos de integração, modelos de dados e restrições de negócio.
- **Plano de Instrumentação:** eventos por Key Result e linha de base.
- **Dados Pessoais e Conformidade.**
- **System Prompt para Coding Assistant:** Bloco de instruções de contexto pronto para compor o arquivo `.cursorrules`, `.github/copilot-instructions.md`, `AGENTS.md`, prompt de sistema ou contexto de workspace.

## Criação das issues no GitHub

O script `scripts/criar_issues.py` lê `06-handoff.md` e cria uma issue por bloco `### ISSUE`. Por padrão apenas exibe o que seria criado; a criação exige a opção `--criar` e a CLI `gh` autenticada. Executar somente mediante solicitação do usuário.

```bash
python3 scripts/criar_issues.py iniciativas/<slug>/06-handoff.md --repo dono/repositorio
python3 scripts/criar_issues.py iniciativas/<slug>/06-handoff.md --repo dono/repositorio --criar
```

## Fechamento

1. Executar `python3 scripts/iniciativa.py verificar iniciativas/<slug>`. O script confere: uma issue por Feature Frame do MVP, mínimo de três cenários por issue, blocos derivados atualizados e um evento para cada Key Result. Corrigir os erros e registrar o resultado na tabela "Verificação de rastreabilidade" do artefato.
2. Em produto derivado de imersão com vários produtos (existe `origem.json`), executar a skill `cross-product-alignment`: eventos, contratos e entidades passam a constar na interface lida pelos vizinhos.
3. Atualizar apenas a seção "6. Handoff" de `contexto.md`, em linhas curtas: issues, eventos de instrumentação, linhas de base pendentes e pendências técnicas.
