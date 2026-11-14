# Iniciativas

Cada iniciativa conduzida pela esteira ocupa uma pasta `iniciativas/<slug>/`, com um artefato numerado por módulo e o arquivo `contexto.md`, que acumula o resumo usado na passagem entre módulos.

Para abrir uma iniciativa:

1. Criar `iniciativas/<slug>/` e copiar [`templates/contexto.md`](../templates/contexto.md) para dentro dela.
2. Colocar o material bruto em `iniciativas/<slug>/00-insumos/`.
3. Acionar o agente `esteira-orchestrator` ou a skill `discovery-product-strategy`.

A pasta `00-insumos/` está no `.gitignore`: transcrições e documentos de imersão podem conter dados confidenciais e não devem ser versionados em repositório público. Avalie o mesmo cuidado para os artefatos numerados antes de publicá-los.
