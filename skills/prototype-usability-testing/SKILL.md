---
name: prototype-usability-testing
description: "Planejar e registrar um teste de usabilidade do protótipo antes do handoff técnico. Etapa 5B, opcional, da esteira, entre os Módulos 5 (Prototipação) e 6 (Handoff): roteiro de tarefas derivado da Jornada To-Be, critério de aprovação por tarefa, registro das sessões, achados classificados por severidade e ajustes na especificação de interface. Use quando houver protótipo ou especificação de telas e tempo disponível para testar com usuários antes do desenvolvimento."
---

# Teste de Usabilidade do Protótipo

Etapa 5B — opcional — da Esteira de Produto AI-Enhanced.

| | |
| :--- | :--- |
| **Frameworks** | Teste de usabilidade baseado em tarefas, heurísticas de usabilidade |
| **Entradas** | `contexto.md`, `03-modelagem.md` (Jornada To-Be), `04-feature-frames.md` e `05-prototipacao.md` |
| **Saída** | `05b-teste-usabilidade.md` em `iniciativas/<slug>/` |
| **Skill anterior** | `systemic-ui-interaction-design` |
| **Próxima skill** | `technical-handoff-prompt-engineering` |

## Por que é opcional

A etapa exige recrutamento e sessões com usuários e acrescenta dias ao ciclo. Não cabe na imersão de 2 dias. Quando não executada, a usabilidade passa a ser verificada apenas em produção (Módulo 7), com custo de correção maior, e a decisão é registrada em `aprovacoes.md` como risco aceito.

Critério para recomendar a execução: o fluxo é novo para a Protopersona, envolve tarefa crítica ou irreversível, ou há Feature Frame com Confiança Baixa.

## Regras de execução

1. A skill planeja o teste e registra observações fornecidas pelo usuário. Não simula participantes nem resultados de sessão.
2. O critério de aprovação de cada tarefa é definido antes das sessões.
3. O enunciado da tarefa descreve o objetivo do usuário, sem nomear elementos da interface.
4. Amostras pequenas identificam problemas; não medem preferência nem estimam taxas para a população. Não apresentar percentuais como estatística representativa.
5. Achado que exija mudança em Feature Frame ou em Out of Scope retorna ao Módulo 4; a skill não altera escopo.

## Algoritmo de Execução

### 1. Plano

Objetivo do teste, protótipo e nível de fidelidade, formato (moderado ou não moderado), perfil e quantidade de participantes conforme a Protopersona, duração e responsável. Como referência de prática, 5 participantes por perfil costumam revelar a maior parte dos problemas recorrentes de um fluxo; fluxos com perfis distintos exigem participantes de cada perfil.

### 2. Roteiro de Tarefas

Uma tarefa por estágio crítico da Jornada To-Be. Para cada tarefa: enunciado, estágio, Feature Frame, critério de conclusão (estado observável que indica sucesso) e critério de aprovação (quantos participantes devem concluir sem ajuda).

### 3. Registro das Sessões

Por participante e tarefa: Concluiu / Concluiu com dificuldade / Não concluiu, mais as observações (hesitações, erros, comentários).

### 4. Achados

Consolidar os problemas observados com: tarefa e tela, número de ocorrências, severidade e recomendação.

| Severidade | Definição |
| :--- | :--- |
| Bloqueante | Impede a conclusão da tarefa |
| Alta | Causa erro ou atraso relevante |
| Média | Causa hesitação, sem impedir a conclusão |
| Baixa | Cosmética |

### 5. Efeito na Esteira

- Listar os ajustes em `05-prototipacao.md` (telas e microcopy) e aplicá-los após aprovação do usuário.
- Tarefa reprovada com achado Bloqueante impede o avanço ao Módulo 6 até a correção ou o aceite registrado do risco.
- Achados não corrigidos são registrados em `aprovacoes.md`.

## Padrão de Entrega (Markdown)

Usar o modelo `assets/05b-teste-usabilidade.md`.

- **Plano** e **Roteiro de Tarefas** (entregues antes das sessões).
- **Registro das Sessões**, **Achados** e **Resultado por Tarefa** (após as sessões).
- **Efeito na esteira.**

## Fechamento

Atualizar em `contexto.md` apenas a linha "Teste de usabilidade" da seção "5. Interface" e registrar a decisão da Etapa 5B, com os achados aceitos como risco, em `aprovacoes.md`.
