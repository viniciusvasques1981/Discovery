# Iniciativas

Cada iniciativa conduzida pela esteira ocupa uma pasta `iniciativas/<slug>/`, com um artefato numerado por módulo e o arquivo `contexto.md`, que acumula o resumo usado na passagem entre módulos.

Referência de preenchimento: [`exemplo-reserva-salas/`](exemplo-reserva-salas/README.md), iniciativa fictícia completa.

Ajustes pequenos não abrem iniciativa: usam a skill `pocket-feature-frame` e geram um arquivo em `iniciativas/<slug>/ajustes/` ou, sem iniciativa relacionada, em `ajustes/` na raiz.

Para abrir uma iniciativa:

1. Criar `iniciativas/<slug>/` e copiar [`templates/contexto.md`](../templates/contexto.md) para dentro dela.
2. Colocar o material bruto em `iniciativas/<slug>/00-insumos/`.
3. Acionar a skill `esteira-orchestration`, que conduz a iniciativa módulo a módulo, ou diretamente a skill `discovery-product-strategy`.

A pasta `00-insumos/` está no `.gitignore` (com exceção da iniciativa de exemplo): transcrições e documentos de imersão podem conter dados confidenciais e não devem ser versionados em repositório público. Avalie o mesmo cuidado para os artefatos numerados antes de publicá-los.
