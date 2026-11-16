# Guia: áudio e vídeo

Para gravações de reuniões, entrevistas e sessões da imersão. Tipo no cabeçalho: **Transcrição de áudio** ou **Transcrição de vídeo**.

## Antes de começar: o ambiente processa o arquivo?

| Situação | O que fazer |
| :--- | :--- |
| O modelo em uso recebe áudio ou vídeo diretamente | Transcrever a partir do arquivo |
| Há ferramenta de transcrição no ambiente (programa local ou serviço conectado) | Usar a ferramenta e registrar o nome em "Método" |
| Nenhuma das duas | Informar o usuário e pedir a transcrição (arquivo `.vtt`, `.srt` ou texto). Não produzir texto a partir do nome do arquivo ou do contexto |

Transcrição feita por terceiros ou pela ferramenta de reunião já é texto: fica direto em `00-insumos/`, sem esta etapa. Se vier sem identificação de falantes, registrar isso em "Limites".

## Formato

Uma fala por linha, com marcação de tempo e falante:

```text
[00:03:12] **Helena:** Quero zerar conflito de reserva.
[00:03:20] **Rui:** Em outubro foram 41, na coluna de ocorrências.
```

- Falante não identificado: `**Participante 1:**`, mantendo o mesmo rótulo ao longo da gravação. Não atribuir nome por suposição.
- Marcação de tempo no início de cada fala, quando o método a fornece.
- Fala longa é dividida em linhas por frase, repetindo o falante.

## Regras

1. Transcrever o que foi dito, sem resumir nem corrigir o conteúdo. Vícios de linguagem e repetições podem ser removidos; números, nomes e termos técnicos são mantidos como falados.
2. Trecho incompreensível: `[inaudível 00:14:05–00:14:20]`. Palavra duvidosa: a palavra seguida de `[?]`.
3. Sobreposição de vozes: transcrever o que for compreensível e marcar `[falas sobrepostas]`.
4. Não registrar tom ou emoção, salvo quando alterar o sentido (por exemplo, ironia evidente), e então com `[inferência]`.

## Vídeo

Além da fala, registrar o que aparece na tela quando for conteúdo da reunião:

- tela compartilhada ou slide: uma linha `[00:10:00] [tela] Planilha de reservas de outubro, coluna "Ocorrências" com 41 linhas marcadas`;
- texto legível na tela é transcrito entre aspas; o restante é descrição, com `[inferência]`;
- desenho feito ao vivo em quadro: descrever conforme o guia de wireframes e indicar o intervalo de tempo.

Se o ambiente processa apenas o áudio do vídeo, registrar em "Limites" que o conteúdo visual não foi lido.

## Limites a registrar

Duração total e duração processada, trechos inaudíveis, falantes não identificados, qualidade do áudio e, em vídeo, se a imagem foi lida.
