# International Framework of Qualifications (IFQ) Ontology

**Version:** 1.0.0  
**Namespace:** `https://wherewelearn.com/ontology/ifq#`  
**License:** CC BY 4.0 (ontology data) / MIT (scripts)  
**Organisation:** [WhereWeLearn](https://wherewelearn.com)

---

## What is the IFQ?

The **International Framework of Qualifications (IFQ)** is a sparse international educational progression ontology. It maps national educational systems from 26 countries onto a shared 22-level progression scale, allowing educational content to be classified and recommended to any learner regardless of their nationality, educational background, or national system.

The IFQ is:
- **Comparative, not authoritative** — it provides approximate equivalence, not legal recognition
- **Progression-first** — it classifies educational stage, not intelligence, competency, or curriculum content
- **Sparse by design** — it deliberately encodes the minimum necessary to achieve global interoperability

The IFQ is not a qualification authority. It does not certify competency, determine immigration equivalence, or replace national frameworks.

---

## Coverage

**574 entries across 26 countries:**

| Code | Country | Code | Country | Code | Country |
|---|---|---|---|---|---|
| AE | United Arab Emirates | FR | France | NL | Netherlands |
| AT | Austria | IE | Ireland | NZ | New Zealand |
| AU | Australia | IN | India | PL | Poland |
| BO | Bolivia | IT | Italy | PT | Portugal |
| BR | Brazil | JP | Japan | SG | Singapore |
| CA | Canada | KE | Kenya | US | United States |
| CN | China | KR | South Korea | ZA | South Africa |
| DE | Germany | NG | Nigeria | — | — |
| EN | England | — | — | — | — |

Each country entry maps 22 IFQ levels (Austria has 24 due to vocational pathway splits at upper secondary).

---

## The 22-Level Scale

| Band | Levels | Scope |
|---|---|---|
| Early Years | 1–3 | Pre-school, Nursery, Kindergarten |
| Primary | 4–9 | Junior and senior primary school |
| Lower Secondary | 10–12 | Junior Cycle, Middle School |
| Upper Secondary | 13–15 | Leaving Cert, A-Levels, SAT year |
| Post-Secondary | 16–17 | Further Education, Associate Degrees |
| Undergraduate | 18–19 | Bachelor's degrees |
| Postgraduate | 20–21 | Master's degrees |
| Doctoral | 22 | PhD |

---

## Files

| File | Purpose | Edit? |
|---|---|---|
| `ifq-core.ttl` | Core OWL vocabulary — classes, properties, namespace | Yes |
| `ifq-levels.ttl` | 22-level SKOS concept scheme | Yes |
| `ifq-shacl-v2.ttl` | SHACL validation constraints | Yes |
| `ifq-mappings-example.ttl` | Reference mapping examples for contributors | Yes |
| `ifq-country-mappings.ttl` | **Generated** — 574 country mapping instances | **No — run `ifq_sql_to_rdf.py`** |
| `ifq_sql_to_rdf.py` | SQL → RDF export script | — |
| `ifq_validate_rdf.py` | SHACL validation runner | — |
| `ifq_specification_v_1_0.md` | IFQ Specification v1.0 | — |
| `ifq-governance.md` | Ontology governance policy | — |
| `ifq-paper.md` | Draft academic paper | — |
| `CHANGELOG.md` | Version history | — |

---

## Quick Start

### Validate the ontology

```bash
cd ontology/
pip install rdflib pyshacl
python ifq_validate_rdf.py
```

Expected output: `✅ IFQ RDF validation PASSED.` (exit code 0)

Write a validation report:

```bash
python ifq_validate_rdf.py --report ifq-validation-report.ttl
```

### Regenerate country mappings from SQL

```bash
python ifq_sql_to_rdf.py
python ifq_validate_rdf.py
```

Run this after any change to the `IFQ` database table.

---

## Technology Stack

| Technology | Role |
|---|---|
| RDF | Graph-based knowledge representation |
| OWL | Ontology class hierarchy and semantics |
| SKOS | Concept scheme modelling for the 22-level scale |
| SHACL | Structural validation constraints |
| Turtle (.ttl) | Serialisation format |

---

## Using the Ontology

### Prefixes

```turtle
@prefix ifq: <https://wherewelearn.com/ontology/ifq#> .
```

### Key classes

| Class | Description |
|---|---|
| `ifq:IFQLevel` | An approximate international educational progression stage (levels 1–22) |
| `ifq:EducationSystem` | A national or regional education system |
| `ifq:EducationStage` | A local year, grade, stage, or programme within a system |
| `ifq:Qualification` | A formal exam, certificate, diploma, or degree |
| `ifq:LearningResource` | A lesson or resource targeting one or more IFQ levels |
| `ifq:MappingAssertion` | An evidence-backed mapping between a local stage and an IFQ level |

### Key properties

| Property | Description |
|---|---|
| `ifq:mapsToIFQLevel` | Relates a local education stage to its approximate IFQ level |
| `ifq:targetsIFQLevel` | Relates a learning resource to the IFQ level it is intended for |
| `ifq:ifqLevelNumber` | The canonical level number (1–22) |
| `ifq:broadStage` | The educational band (e.g. "Primary", "Undergraduate") |
| `ifq:alignedWithISCED` | UNESCO ISCED level alignment |
| `ifq:confidence` | Mapping confidence: High / Medium / Approximate |

See `ifq-mappings-example.ttl` for worked examples.

---

## Contributing

We welcome contributions of new country system mappings and corrections to existing entries.

**What can be contributed:**
- New country system mappings (22 entries per system, with justified exceptions)
- Corrections to existing entries (age ranges, exam names, source URLs)
- Translations of `rdfs:label` values

**What cannot be contributed without Ontology Owner approval:**
- Changes to the 22-level progression model
- Changes to OWL class definitions
- Changes to SHACL constraints

**How to contribute:**
1. Fork this repository
2. Add your mapping following the pattern in `ifq-mappings-example.ttl`
3. Run `ifq_validate_rdf.py` — all constraints must pass
4. Open a Pull Request — include country name, entry count, source references, and any structural exceptions

Full contribution criteria are in `ifq-governance.md`.

---

## Citation

If you use the IFQ ontology in academic work, please cite:

```
WhereWeLearn (2026). International Framework of Qualifications (IFQ) Ontology, v1.0.0.
https://wherewelearn.com/ontology/ifq# — CC BY 4.0
```

A formal academic paper is in preparation. See `ifq-paper.md`.

---

## License

- **Ontology data (*.ttl):** [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
- **Scripts (*.py):** MIT
- **Documentation (*.md):** CC BY 4.0

See `LICENSE` for full terms.
