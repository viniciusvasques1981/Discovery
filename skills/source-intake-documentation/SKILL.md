---
name: source-intake-documentation
description: "Documentar o material bruto de uma imersão antes do Discovery: converter documentos (PDF, Word, apresentações), áudio e vídeo, wireframes e desenhos de tela, protótipos do Figma, do Paper e do Penpot e boards do Miro em texto citável, com origem, método e situação de validação registrados. Etapa 0 da esteira. Use quando houver insumo que não esteja em texto, quando receber gravações, fotos de quadro, rascunhos de tela, links de protótipo ou de board, ou antes de executar o Módulo 1 com material de formatos variados."
---

# Entrada e Documentação de Insumos

Etapa 0 da Esteira de Produto AI-Enhanced. Transforma o que a imersão produziu em texto que o Módulo 1 consegue citar linha a linha.

| | |
| :--- | :--- |
| **Entradas** | Arquivos em `00-insumos/originais/` e links de protótipos e de boards informados pelo usuário |
| **Saídas** | Um arquivo `.md` por original em `00-insumos/` e `00-insumos/INVENTARIO.md`, gerado por script |
| **Próxima skill** | `discovery-product-strategy` |

## Por que existe

A esteira exige que cada afirmação cite a linha de origem. Áudio, imagem e board não têm linha. A etapa cria, para cada original, um texto citável com o registro de como foi obtido. Sem ela, a conversão é feita à mão e não deixa rastro.

## Estrutura

```text
00-insumos/
├── originais/        arquivos como recebidos: gravações, imagens, PDFs, exportações de protótipo e de board, ou nota com o link lido
├── <nome>.md         texto citável derivado de um original, ou insumo recebido já em texto
├── INVENTARIO.md     gerado por script a partir do cabeçalho de cada insumo
└── numerados/        gerado no Módulo 1
```

Insumo que já chega em texto (`.md`, `.txt`, `.vtt`, `.srt`, `.csv`) fica direto em `00-insumos/` e não precisa desta etapa.

## Regras de execução

1. **Converter não é interpretar.** O texto citável registra o que o material contém. Conclusões ficam para o Módulo 1.
2. **Não inventar conteúdo.** Trecho inaudível, ilegível ou não processado é marcado como `[inaudível]`, `[ilegível]` ou `[não processado]`. Nunca completar por contexto.
3. **Distinguir o literal do descrito.** Texto escrito no material (fala, rótulo de botão, post-it) é transcrito entre aspas ou como fala. Tudo o que o modelo descreve por conta própria (função de uma tela, agrupamento de post-its) recebe a marca `[inferência]`.
4. **Declarar a capacidade.** Se o ambiente não processa o tipo de material (por exemplo, áudio), dizer isso ao usuário e pedir a transcrição ou a exportação. Não simular a conversão.
5. **Um original, um arquivo.** Cada texto citável começa pelo cabeçalho do modelo `assets/insumo-derivado.md`, com Origem, Tipo, Método e Validação. O script lê esse cabeçalho.
6. **Validação é de uma pessoa.** Toda conversão nasce com "Validação: Pendente". Só o usuário muda para "Validado por [nome] em [data]", depois de conferir com o original.
7. **Um original por vez.** Processar e gravar cada arquivo antes de abrir o seguinte.

## Algoritmo de Execução

### 1. Inventariar

```bash
python3 scripts/iniciativa.py inventariar iniciativas/<slug>
```

O script lista os originais sem texto citável, com o tipo de cada um e o guia a usar, e os textos ainda não validados.

### 2. Converter, conforme o tipo

Abrir apenas o guia do tipo em mãos:

| Material | Guia |
| :--- | :--- |
| PDF, Word, apresentações, planilhas | `references/documentos.md` |
| Gravações de áudio e de vídeo | `references/audio-video.md` |
| Wireframes, rascunhos de tela, fotos de quadro com desenho | `references/wireframes.md` |
| Protótipos e telas no Figma, no Paper e no Penpot | `references/prototipos.md` |
| Boards do Miro e ferramentas semelhantes | `references/miro.md` |

### 3. Registrar

Gravar o arquivo com o cabeçalho preenchido e a seção "Limites desta conversão". Executar `inventariar` de novo para atualizar `INVENTARIO.md`.

### 4. Pedir a validação

Apresentar ao usuário a lista de conversões pendentes, em ordem de risco: leitura de wireframe, de protótipo e extração de board primeiro, depois transcrições, depois documentos. Indicar em cada uma os trechos marcados como ilegíveis, inaudíveis ou inferidos.

## Efeito nos módulos seguintes

| Tipo de insumo | Tipo de evidência no Módulo 1 | Sustenta |
| :--- | :--- | :--- |
| Documento convertido | Dado, Restrição ou Decisão, conforme o conteúdo | Certeza, se o documento for fonte oficial |
| Transcrição de áudio ou vídeo | Declaração ou Relato | Suposição; Certeza apenas com dado de suporte |
| Leitura de wireframe | Esboço | Suposição ou Pedido; referência para o Módulo 5, nunca especificação |
| Leitura de protótipo | Protótipo | Suposição ou Pedido; referência para o Módulo 5, nunca especificação. Estilos e componentes só viram Design System com confirmação do usuário |
| Extração de board | Nota de dinâmica | Suposição; reflete o que o grupo escreveu, não um fato |

Conversão não validada sustenta apenas Suposição, qualquer que seja o tipo. O script de verificação avisa enquanto houver conversão pendente de validação ou original sem texto citável.

## Fechamento

Atualizar em `contexto.md` apenas a linha "Detalhes" da seção "1–2. Por quê", acrescentando `00-insumos/INVENTARIO.md`. Devolver à conversa principal: quantos originais foram convertidos, quantos ficaram pendentes e por quê.
