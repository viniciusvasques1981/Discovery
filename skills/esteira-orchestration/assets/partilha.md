# Mapa de Partilha: [imersão]

> Usado quando uma imersão origina mais de um produto. Vive no repositório da imersão (o tronco) e define o que cada produto herda. É iniciado no Módulo 2 e fechado no ponto de separação. Os identificadores de produto vão entre crases.

**Ponto de separação:** Módulo 4

Padrão: Módulo 4, com Protopersona e Jornada To-Be feitas em conjunto. Usar Módulo 3 somente quando as duas respostas forem "não": os produtos atendem a mesma pessoa em algum momento? A saída de um é entrada da jornada do outro?

| Pergunta | Resposta | Evidência |
| :--- | :--- | :--- |
| Os produtos atendem a mesma pessoa, em algum momento? | Sim / Não | |
| A saída de um produto é a entrada da jornada do outro? | Sim / Não | |

## Produtos

| Produto | Nome | Repositório | Visão em uma linha |
| :--- | :--- | :--- | :--- |
| `produto-a` | | https://github.com/organizacao/repositorio-a | |
| `produto-b` | | https://github.com/organizacao/repositorio-b | |

## Partilha de dores, suposições e dúvidas

Todo item P e S do Módulo 1 aparece aqui. Situação: Exclusivo, Compartilhado ou Sem dono.

| Item | Descrição | Produto | Situação |
| :--- | :--- | :--- | :--- |
| P1 | | `produto-a` | Exclusivo |
| S1 | | `produto-a`, `produto-b` | Compartilhado |
| D1 | | — | Sem dono |

## Estágios da jornada

Preenchido ao fim do Módulo 3, quando a separação é no Módulo 4. Cada estágio tem um produto dono; a coluna "Passagem para" marca onde o usuário segue para outro produto.

| Estágio | Produto dono | Passagem para | O que passa de um produto ao outro |
| :--- | :--- | :--- | :--- |
| J1 | `produto-a` | — | |
| J2 | `produto-a` | `produto-b` | |

## Pontos de integração previstos

Derivados das passagens acima. Cada ponto vira, no Módulo 4, um par "Fornece para" / "Depende de" nos Feature Frames dos dois produtos.

| De | Para | O que passa | Estágio | Situação |
| :--- | :--- | :--- | :--- | :--- |
| `produto-a` | `produto-b` | | J2 | Previsto / Especificado / Em produção |
