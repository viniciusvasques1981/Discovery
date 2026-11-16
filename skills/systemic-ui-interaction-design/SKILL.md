---
name: systemic-ui-interaction-design
description: "Traduzir os Feature Frames em especificações técnicas de interface, arquitetura de informação, mapeamento de Design System e diretrizes de microcopy. Cobre o Módulo 5 (Prototipação) da esteira: fluxo de telas, wireframes descritivos, componentes e tokens, acessibilidade WCAG 2.1 AA e guia de UI para assistentes de código. Use quando os Feature Frames estiverem definidos e for preciso especificar telas, componentes ou microcopy."
---

# Design Sistêmico de UI e Interação

Módulo 5 da Esteira de Produto AI-Enhanced.

| | |
| :--- | :--- |
| **Framework** | Agile Prototyping |
| **Entradas** | `contexto.md`, `04-feature-frames.md` e o Design System da empresa (documentação, tokens ou biblioteca de componentes). Não ler outros artefatos. Leituras de wireframe e de protótipo da Etapa 0 citadas nos Feature Frames servem de referência, nunca de especificação; estilos e componentes lidos de um protótipo só são tratados como Design System com confirmação do usuário |
| **Saída** | `05-prototipacao.md` em `iniciativas/<slug>/` |
| **Skill anterior** | `behavioral-modeling-feature-framing` |
| **Próxima skill** | `technical-handoff-prompt-engineering`; antes dela, opcionalmente, `prototype-usability-testing` (Etapa 5B) |

## Regras de execução

1. Especificar somente telas e componentes necessários aos Feature Frames classificados como MVP. Nenhuma tela pode implementar algo listado em Out of Scope.
2. Se o Design System da empresa for fornecido, mapear para os componentes e tokens existentes e sinalizar lacunas. Não criar componente novo quando houver equivalente.
3. Se o Design System não for fornecido, declarar essa condição e propor tokens genéricos identificados como provisórios.
4. Cada tela deve indicar o Feature Frame e o estágio da Jornada To-Be que atende.

## Algoritmo de Execução

### 1. Fluxo de Telas e Arquitetura de Informação

- Listar as telas do fluxo, a ordem de navegação e os pontos de entrada e saída.
- Para cada tela: objetivo, hierarquia de informação, ações primária e secundárias, estados (carregando, vazio, erro, sucesso).
- Descrever o wireframe em texto estruturado (regiões, ordem de leitura e prioridade visual).

### 2. Mapeamento de Design System e Tokens

- Especificar componentes base reutilizáveis (botões, inputs, cards, modais, drawers, toasts, badges).
- Definir Tokens de Design: Cores (semânticas, neutras e de feedback), Tipografia (hierarquia de leitura) e Espaçamento/Grid (escala de 4px/8px).
- Documentar os estados de interação de cada componente: Default, Hover, Active, Focus, Disabled e Loading.

### 3. Usabilidade e Acessibilidade (HIG / WCAG 2.1 AA)

- Validar contraste mínimo (4.5:1 para texto normal, 3:1 para componentes visuais).
- Assegurar área mínima de toque (44×44px em interfaces móveis/touch).
- Projetar navegação por teclado e conformidade com leitores de tela (rótulos ARIA, estados de foco explícitos).
- Respeitar o tempo de resposta percebida do sistema (< 200ms para feedback visual imediato).

### 4. Guia de Microcopy e UX Writing

- **CTAs:** Verbo de ação objetivo no infinitivo ou imperativo direto.
- **Mensagens de Erro Construtivas:** Compostas obrigatoriamente por: O que aconteceu + Por que aconteceu + Como resolver.
- **Empty States e Skeletons:** Instrução de navegação para saída de estados vazios e transições de carregamento sem salto de layout (CLS zero).

### 5. Guia de UI para o Assistente de Código

Consolidar em um bloco único, pronto para ser anexado ao handoff:

- Stack de interface (ex.: React) e biblioteca do Design System a utilizar.
- Componentes permitidos por tela e respectivas propriedades relevantes.
- Tokens obrigatórios e proibição de valores fixos (cores, espaçamentos e tipografia fora dos tokens).
- Requisitos de acessibilidade verificáveis.

## Padrão de Entrega (Markdown)

Usar o modelo `assets/05-prototipacao.md`.

- **Especificação de Telas:** Lista detalhada por tela ou fluxo com regras de layout e navegação.
- **Matriz de Componentes e Tokens:** Relação de elementos de UI e seus respectivos estados.
- **Guia de Microcopy:** Tabela com rótulos de botões, mensagens de erro contextuais e tratamentos de empty state.
- **Guia de UI para o Assistente de Código.**

## Fechamento

1. Executar `python3 scripts/iniciativa.py verificar iniciativas/<slug>` e corrigir os erros apontados.
2. Atualizar apenas a seção "5. Interface" de `contexto.md`, em linhas curtas: telas, lacunas do Design System e a decisão sobre a Etapa 5B.

Antes do handoff, a especificação pode ser testada com usuários pela Etapa 5B, opcional (`prototype-usability-testing`). Se não for executada, a usabilidade passa a ser verificada apenas em produção, no Módulo 7.
