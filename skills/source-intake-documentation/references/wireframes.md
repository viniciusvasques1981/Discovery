# Guia: wireframes e desenhos

Para rascunhos de tela, fotos de quadro com desenho, capturas de protótipo e telas de sistemas existentes. Tipo no cabeçalho: **Leitura de wireframe**.

## O que esta leitura é

Um wireframe trazido para a imersão registra uma ideia de alguém, não uma decisão. A leitura entra no Módulo 1 como evidência do tipo Esboço e pode servir de referência no Módulo 5. Não é especificação de interface.

## Antes de começar

Abrir a imagem e confirmar que é legível. Foto de quadro inclinada, com reflexo ou letra pequena pode não ser lida com segurança: dizer isso ao usuário e pedir nova foto ou a transcrição dos textos, em vez de adivinhar.

## Formato

Um bloco por tela ou quadro do desenho, na ordem em que aparecem:

```text
## Tela 1 — "Reservar sala"   (título como escrito; sem título: Tela 1 [inferência]: ...)

Regiões, de cima para baixo e da esquerda para a direita:
1. Barra superior: texto "Nimbo"; ícone de menu à direita.
2. Dois seletores lado a lado: "Unidade", "Dia".
3. Grade de 4 linhas por 6 colunas; células com "livre" e "ocupado".
4. Botão "Reservar" abaixo da grade.

Navegação desenhada: seta do botão "Reservar" para a Tela 2.
Anotações: "membro vê só a própria unidade?" (ao lado dos seletores, com interrogação).
[inferência] Finalidade provável: consulta de disponibilidade antes da reserva.
```

## Regras

1. **Texto literal entre aspas.** Rótulos, títulos e anotações são transcritos como estão, inclusive com erros. Palavra não legível: `[ilegível]`.
2. **Elementos pelo que são no desenho.** "Retângulo com o texto 'Reservar'" é um botão provável; registrar "botão" quando o desenho deixa claro, e `[inferência]` quando não deixa.
3. **Setas e ligações** são registradas como desenhadas: de onde saem e onde chegam.
4. **Anotações à margem** costumam ser o conteúdo mais valioso: dúvidas, restrições e decisões. Transcrever todas, com a posição.
5. **Não completar o desenho.** Estado de erro, tela vazia ou campo que não foi desenhado não entra na leitura.
6. **Finalidade da tela** é sempre `[inferência]`, em linha separada, ao fim do bloco.
7. Quem desenhou e quando, se o usuário informar, vão no cabeçalho do arquivo.

## Tela de sistema existente

Captura de um sistema em uso é registro do estado atual, não proposta. Usar o mesmo formato e indicar no cabeçalho "Método: captura de tela do sistema [nome]". Dados pessoais visíveis na captura não são transcritos: registrar `[dado pessoal omitido]`.

## Limites a registrar

Trechos ilegíveis, partes do desenho fora do enquadramento, elementos de sentido ambíguo e a quantidade de inferências feitas.
