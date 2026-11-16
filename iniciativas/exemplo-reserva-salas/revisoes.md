# Revisões Independentes: Reserva de salas (exemplo fictício)

Registro das revisões do agente `artifact-reviewer`, uma seção por bloco. O exemplo detalha os blocos dos Módulos 2 e 6; os demais constam pelo parecer em `aprovacoes.md`.

## Revisão do bloco do Módulo 2 — 2026-11-03

**Artefatos revisados:** `evidencias.md`, `01-discovery.md`, `02-estrategia.md`
**Comparados com:** linhas de origem citadas pelas evidências (saída de `iniciativa.py citar --evidencias`)
**Verificação mecânica:** 0 erro(s), 0 aviso(s)

### Parecer

Aprovado com ressalvas

### Apontamentos

| # | Tipo | Local no artefato | Apontamento | Evidência | Severidade | Situação |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| R-01 | Classificação | `01-discovery.md`, C1, C4 e C5 | Certezas apoiadas em fala de participante, sem documento. Aceitáveis por tratarem de fatos estruturais informados por quem responde por eles (E001 é Dado; E010, E014 e E017 são Restrição ou Decisão) | E001, E010, E014, E017 | Menor | Aceito pelo aprovador |
| R-02 | Números | `02-estrategia.md`, KR1 | A linha de base usa um único mês; o artefato declara a limitação, mas a meta de zero é avaliada contra uma referência sem variação conhecida | E003 cita apenas outubro | Menor | Aceito pelo aprovador |

### Itens conferidos sem apontamento

| Verificação | Resultado |
| :--- | :--- |
| As 22 evidências dizem o mesmo que as linhas de origem, sem acréscimo | Conforme |
| Números (3 unidades, 14 salas, 612 reservas, 41 conflitos) idênticos aos das evidências | Conforme (E001, E003) |
| Estimativas sem registro (2 horas por dia, 20% de não comparecimento) classificadas como Suposição | Conforme (E007, E008 → S3, S2) |
| Percentual de 6,7% marcado como inferência e restrito a um mês | Conforme |
| Dúvidas em forma de pergunta; nenhuma solução proposta no Módulo 1 | Conforme |
| Hipóteses derivadas de Suposições existentes; meta de 70% presente nas evidências | Conforme (E009) |
| KR3 como Instrumentação, sem linha de base estimada | Conforme |

### Limites desta revisão

A cobertura não foi conferida: as linhas dos insumos não citadas por nenhuma evidência não foram lidas. O "Como" do Golden Circle está marcado como inferência; a adequação estratégica não é objeto desta revisão.

## Revisão do bloco do Módulo 6 — 2026-11-04

**Artefatos revisados:** `05-prototipacao.md`, `06-handoff.md`
**Comparados com:** `04-feature-frames.md`, `02-estrategia.md`
**Verificação mecânica:** 1 erro(s) na primeira execução, 0 após a correção

### Parecer

Reprovado na primeira revisão; Aprovado com ressalvas após a correção de R-03.

### Apontamentos

| # | Tipo | Local no artefato | Apontamento | Evidência | Severidade | Situação |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| R-03 | Erro do script | `06-handoff.md`, Plano de Instrumentação | "KR3 sem evento ou medida no Plano de Instrumentação". FF-05, que registraria o comparecimento, está fora do MVP | `02-estrategia.md` define o KR3; `04-feature-frames.md` classifica FF-05 como "MVP: Não" | Bloqueante | Corrigido: incluída a medida manual pela recepção por 4 semanas |
| R-04 | Campo incompleto | `06-handoff.md`, Dados pessoais e conformidade | Retenção não informada e responsável não identificado | D3 em `01-discovery.md` | Relevante | Aceito pelo aprovador; marcado como a validar |

### Itens conferidos sem apontamento

| Verificação | Resultado |
| :--- | :--- |
| Nenhuma tela implementa item de Out of Scope | Conforme |
| Mensagens dos cenários iguais às do Guia de Microcopy | Conforme |
| Contratos de API marcados como a validar | Conforme |
| Cenários cobrem as regras críticas (sobreposição, concorrência, titularidade) | Conforme |

Cobertura de issues, cenários mínimos e blocos derivados foram conferidos pelo script e não foram refeitos.

### Limites desta revisão

A adequação técnica dos contratos propostos e da restrição de banco não foi avaliada: depende do esquema atual, não fornecido.
