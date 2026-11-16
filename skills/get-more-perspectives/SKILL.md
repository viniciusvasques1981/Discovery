---
name: get-more-perspectives
description: "Veja de 3 a 5 pontos de vista diferentes antes de tomar uma decisão. Reúne um painel consultivo virtual de especialistas para opinar sobre qualquer decisão, estratégia ou dilema. Use quando o usuário quiser várias perspectivas sobre uma decisão importante, estiver indeciso entre opções ou disser \"o que os especialistas acham\"."
---

# Painel de Perspectivas

Skill de apoio, aplicável em qualquer módulo da esteira.

Reúne um painel consultivo virtual de especialistas, cada um com uma experiência e perspectiva distintas, para opinar sobre qualquer decisão, estratégia ou dilema. Cada consultor dá a própria opinião de forma independente, e a habilidade sintetiza uma recomendação em forma de painel.

## Painel padrão

| Consultor | Foco | Pergunta central |
| :--- | :--- | :--- |
| Operador | Execução | O que é necessário para isso funcionar na prática? |
| Cético | Risco | O que pode dar errado e qual premissa é mais frágil? |
| Visionário | Oportunidade | Qual é o ganho máximo possível e o que o destrava? |
| Defensor do cliente | Impacto no usuário | Como isso altera a experiência de quem usa? |
| Financeiro | Números | Qual é o custo, o retorno e o prazo de retorno? |

O painel pode ser reduzido a 3 consultores ou ter perfis substituídos conforme a decisão (ex.: Jurídico, Tech Lead, Operações de campo).

## Algoritmo de Execução

1. **Enquadrar a decisão:** reescrever em uma frase a decisão a ser tomada, as opções em análise e as restrições conhecidas. Se a decisão ou as opções não estiverem claras, pedir esclarecimento antes de montar o painel.
2. **Pareceres independentes:** cada consultor emite parecer sem referência aos demais, contendo posição, justificativa, principal risco e condição que o faria mudar de posição. Onde houver subagentes, gerar cada parecer em um subagente separado, que recebe apenas a decisão enquadrada e o perfil do consultor; os pareceres são reunidos na conversa principal. Sem subagentes, redigir cada parecer por completo antes de iniciar o seguinte.
3. **Mapa de convergência:** apontar onde os pareceres concordam, onde divergem e o motivo da divergência (premissa diferente, horizonte de tempo diferente ou critério diferente).
4. **Síntese:** recomendação do painel, condições para a recomendação valer e a informação ausente que mais alteraria o resultado.

## Regras de execução

- Os pareceres são simulações de pontos de vista, não opiniões de especialistas reais. Registrar essa condição na entrega.
- Pareceres gerados em uma única conversa tendem a convergir, porque cada um é escrito com os anteriores à vista. Quando a execução não for por subagentes, registrar essa limitação na entrega.
- Não forçar consenso. Divergência não resolvida deve ser apresentada como tal.
- Números usados pelos consultores devem vir do contexto fornecido. Quando ausentes, o consultor indica qual dado precisaria para sustentar a posição.

## Uso na esteira

| Módulo | Aplicação |
| :--- | :--- |
| 2 — Estratégia | Avaliar a Visão de Produto e a ambição dos OKRs |
| 4 — Feature Frame | Decidir o recorte de MVP e os limites Out of Scope |
| 8 — Experimentação | Decidir entre implementar, descartar ou iterar após o resultado |

## Padrão de Entrega (Markdown)

- **Decisão enquadrada:** decisão, opções e restrições.
- **Pareceres:** um bloco por consultor.
- **Mapa de convergência e divergência.**
- **Recomendação do painel:** recomendação, condições e lacunas de informação.
