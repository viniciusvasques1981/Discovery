---
name: match-my-writing-style
description: "Analisa como você escreve para aprender seu estilo e aplicá-lo a todo texto produzido. Acionada em qualquer solicitação de escrita em nome do usuário: e-mails, mensagens, postagens, documentos, memorandos, respostas, resumos ou avisos. O usuário não precisa pedir para \"falar como eu\"."
---

# Escrita no Estilo do Usuário

Skill de apoio, aplicável em qualquer módulo da esteira.

Habilidade sempre ativada que garante que cada texto soe como o usuário. Na primeira ativação, cria um Voice Card persistente a partir de amostras reais de escrita. Todos os rascunhos futuros o usam automaticamente.

## Algoritmo de Execução

### 1. Localizar o Voice Card

Procurar, nesta ordem:

1. `voice-card.md` na raiz do workspace ou do repositório;
2. documento "Voice Card" no Google Drive, quando houver conector do Workspace disponível.

Se existir, aplicar e seguir para o passo 3.

### 2. Criar o Voice Card (primeira ativação)

Coletar amostras reais de escrita do usuário:

- com conector do Workspace (Gmail, Docs, Chat): fazer a verificação automática dos textos enviados pelo usuário;
- sem conector: solicitar de 5 a 10 amostras de canais diferentes.

Extrair das amostras:

| Dimensão | O que registrar |
| :--- | :--- |
| Tamanho das frases | Extensão média e variação |
| Vocabulário | Termos recorrentes, jargões, palavras evitadas |
| Tom | Grau de formalidade e de objetividade |
| Introduções | Como os textos começam |
| Fechamentos | Como os textos terminam, assinatura |
| Pontuação | Peculiaridades (travessões, listas, emojis, uso de maiúsculas) |
| Registro por canal | Diferenças entre e-mail, chat, documento e postagem |

Salvar o resultado usando o modelo `assets/voice-card.md`. Com conector do Workspace, salvar no Google Drive; sem conector, salvar como `voice-card.md` no workspace.

### 3. Aplicar

Redigir no registro do canal solicitado, conforme o Voice Card. O estilo define a forma; o conteúdo permanece fiel aos fatos e aos artefatos da esteira.

### 4. Atualizar

Quando o usuário editar um rascunho ou corrigir o tom, propor a atualização do Voice Card com a diferença observada.

## Regras de execução

- Analisar somente textos escritos pelo próprio usuário. Mensagens de terceiros na mesma conversa não entram na amostra.
- Não copiar para o Voice Card dados pessoais, nomes de terceiros ou conteúdo confidencial das amostras; registrar apenas padrões de estilo.
- Artefatos técnicos da esteira (Matriz CSD, Feature Frames, BDD) mantêm o padrão de entrega da skill de origem. O Voice Card aplica-se a textos de comunicação: e-mails de alinhamento, resumos executivos, mensagens ao sponsor.

## Padrão de Entrega

- Na primeira ativação: o Voice Card para validação do usuário.
- Nas seguintes: o texto solicitado, sem menção ao processo de adaptação de estilo.
