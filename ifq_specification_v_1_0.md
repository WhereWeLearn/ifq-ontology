# IFQ Specification v1.0

## International Framework of Qualifications

Version: 1.0-draft  
Date: 9 May 2026  
Organisation: WhereWeLearn

---

# 1. Introduction

The International Framework of Qualifications (IFQ) is a sparse international educational progression ontology intended to provide approximate interoperability between heterogeneous educational systems.

The framework enables educational progression stages from different countries and systems to be approximately compared using a stable 22-level abstraction model.

IFQ is designed primarily for:
- educational recommendation systems,
- AI-assisted pedagogical routing,
- cross-border educational interpretation,
- globally interoperable lesson classification,
- and educational progression comparison.

---

# 2. Design Philosophy

## 2.1 Sparse Ontology Principle

IFQ intentionally prioritises:
- simplicity,
- survivability,
- interoperability,
- and extensibility

over exhaustive educational precision.

The ontology therefore remains deliberately sparse.

Educational complexity is externalised into metadata overlays rather than encoded into the core progression structure.

---

## 2.2 Progression-First Semantics

IFQ models:
- educational progression stages.

IFQ does not model:
- intelligence,
- educational quality,
- institutional prestige,
- labour-market value,
- curriculum equivalence,
- competency mastery,
- or legal qualification equivalence.

---

## 2.3 Approximation as a Formal Property

Approximation is considered a formal architectural property of the framework.

IFQ therefore defines itself as:

> “An approximate international educational progression ontology.”

---

# 3. IFQ Level Structure

## 3.1 Canonical IFQ Levels

The ontology defines 22 progression levels.

| IFQ Band | Levels |
|---|---|
| Early Years | 1–3 |
| Primary | 4–9 |
| Lower Secondary | 10–12 |
| Upper Secondary | 13–15 |
| Post-Secondary / Short-cycle | 16–17 |
| Undergraduate | 18–19 |
| Postgraduate | 20–21 |
| Doctoral | 22 |

---

## 3.2 Mapping Signals

Mappings are derived using primary progression signals:

1. Typical learner age
2. Educational continuity
3. Progression stage
4. Exit qualification
5. ISCED alignment

Secondary signals are retained only as metadata overlays.

---

# 4. Metadata Overlay Model

IFQ intentionally separates:
- core progression structure,
from:
- educational nuance.

Nuance is represented using overlays.

## 4.1 Overlay Fields

| Field | Purpose |
|---|---|
| BroadStage | High-level educational band |
| ISCED | UNESCO alignment |
| ProgressionType | Academic/vocational pathway metadata |
| Confidence | Mapping certainty |
| Notes | Caveats and interpretation |
| Source | Provenance |
| QualificationType | Qualification semantics |

---

# 5. RDF / OWL Architecture

## 5.1 Core Ontology Files

| File | Purpose |
|---|---|
| `ifq-core.ttl` | Core ontology vocabulary |
| `ifq-levels.ttl` | Canonical IFQ concept scheme |
| `ifq-mappings-example.ttl` | Reference mapping examples |
| `ifq-shacl.ttl` | SHACL validation constraints |
| `ifq-country-mappings.ttl` | Generated mapping instances |

---

## 5.2 Ontology Technologies

The ontology stack uses:

| Technology | Role |
|---|---|
| RDF | Graph representation |
| OWL | Ontology semantics |
| SKOS | Concept scheme modelling |
| SHACL | Structural validation |
| Turtle | Serialization format |

---

# 6. SQL Operational Model

The operational source of truth for mappings is the IFQ SQL database.

RDF is generated from SQL using:

```text
ifq_sql_to_rdf.py
```

This creates:

```text
ifq-country-mappings.ttl
```

The SQL database remains authoritative.

RDF acts as the semantic interoperability layer.

---

# 7. Validation Pipeline

Validation is performed using:

```text
ifq_validate_rdf.py
```

The validation process:
1. loads ontology files,
2. loads generated mappings,
3. runs SHACL validation,
4. emits validation reports.

Validation technologies:
- rdflib
- pySHACL

---

# 8. SHACL Validation Principles

SHACL validation intentionally validates:
- ontology structure,
- required progression semantics,
- mapping integrity,
- confidence semantics,
- and source structure.

Validation intentionally does not attempt to validate:
- educational correctness,
- curriculum equivalence,
- prestige,
- labour-market value,
- or legal recognition.

---

# 9. International Survivability

The ontology has been tested against:
- Anglo-American systems,
- Bologna systems,
- Germanic vocational systems,
- Gulf systems,
- postcolonial hybrid systems,
- and competency-oriented Nordic systems.

Countries and systems mapped include:
- Ireland,
- England,
- United States,
- Germany,
- Austria,
- Switzerland,
- Netherlands,
- Finland,
- Brazil,
- South Africa,
- India,
- China,
- Japan,
- South Korea,
- Singapore,
- UAE,
- Portugal,
- Italy,
- Poland,
- France,
- Spain.

The sparse model continues to survive because educational nuance is externalised into metadata overlays.

---

# 10. Relationship to ISCED

IFQ is not a replacement for UNESCO ISCED.

ISCED acts primarily as:
- a statistical educational classification system.

IFQ acts as:
- an approximate progression abstraction layer.

ISCED alignment is therefore treated as metadata interoperability rather than ontology identity.

---

# 11. Example Applications

## 11.1 Educational Recommendation

Lessons may be tagged with approximate IFQ levels:

```text
Lesson: IFQ Level 11
Learner: IFQ Level 9
Recommendation: Supported progression
```

---

## 11.2 AI Pedagogical Routing

AI systems may dynamically adapt explanation depth:

```text
Explain photosynthesis at IFQ 7
```

versus:

```text
Explain photosynthesis at IFQ 18
```

---

## 11.3 Cross-Border Interpretation

IFQ enables approximate educational progression understanding without requiring legal equivalence.

---

# 12. Governance Principles

The IFQ core ontology should remain:
- sparse,
- stable,
- internationally interoperable,
- and understandable.

Future extensions should prefer:
- overlays,
- annotations,
- and optional metadata

over additional core dimensions.

---

# 13. Non-goals

IFQ intentionally does not model:
- intelligence,
- competency,
- educational quality,
- prestige,
- labour-market outcomes,
- cognitive maturity,
- or institutional ranking.

These domains require separate ontologies.

---

# 14. Future Work

Potential future work includes:
- competency overlays,
- multilingual semantic layers,
- graph-based progression inference,
- probabilistic confidence models,
- adaptive AI learning systems,
- and linked open data publication.

The IFQ core ontology should nevertheless remain sparse.

---

# 15. Validation Milestone

The IFQ ontology has successfully survived transition through:

```text
Spreadsheet
→ SQL
→ RDF
→ OWL
→ SHACL Validation
```

This demonstrates that the ontology maintains structural coherence across multiple semantic representations.

---

# 16. References

UNESCO Institute for Statistics (2012) *International Standard Classification of Education: ISCED 2011*. Montreal: UNESCO Institute for Statistics.

European Commission/EACEA/Eurydice (2026) *Organisation of education systems in Europe*.

South African Qualifications Authority (SAQA) (2026) *National Qualifications Framework*.

Brazil (1996) *Lei de Diretrizes e Bases da Educação Nacional (Lei No. 9.394/1996)*.

Swiss Confederation (2026) *The Swiss Education System*.

WhereWeLearn Internal Research Notes and Mapping Methodology (2025–2026).
