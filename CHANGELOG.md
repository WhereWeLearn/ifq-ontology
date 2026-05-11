# Changelog

All notable changes to the IFQ Ontology are documented here.

Format follows [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).  
Versioning follows [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [1.0.0] — 2026-05-11

First stable public release.

### Ontology

- Core OWL vocabulary (`ifq-core.ttl`) — classes, properties, namespace
- 22-level SKOS concept scheme (`ifq-levels.ttl`) — canonical progression model
- SHACL validation constraints (`ifq-shacl-v2.ttl`) — structural validation
- Reference mapping examples (`ifq-mappings-example.ttl`)
- Generated country mappings (`ifq-country-mappings.ttl`) — 574 entries, 26 countries

### Coverage (26 countries, 574 entries)

| Code | Country | Entries |
|---|---|---|
| AE | United Arab Emirates | 22 |
| AT | Austria | 24 |
| AU | Australia | 22 |
| BO | Bolivia | 22 |
| BR | Brazil | 22 |
| CA | Canada | 22 |
| CN | China | 22 |
| DE | Germany | 22 |
| EN | England | 22 |
| ES | Spain | 22 |
| FI | Finland | 22 |
| FR | France | 22 |
| IE | Ireland | 22 |
| IN | India | 22 |
| IT | Italy | 22 |
| JP | Japan | 22 |
| KE | Kenya | 22 |
| KR | South Korea | 22 |
| NG | Nigeria | 22 |
| NL | Netherlands | 22 |
| NZ | New Zealand | 22 |
| PL | Poland | 22 |
| PT | Portugal | 22 |
| SG | Singapore | 22 |
| US | United States | 22 |
| ZA | South Africa | 22 |

### Scripts

- `ifq_sql_to_rdf.py` — SQL → RDF/Turtle export
- `ifq_validate_rdf.py` — SHACL validation runner (exit codes 0/1/2)

### Documentation

- `ifq_specification_v_1_0.md` — IFQ Specification v1.0
- `ifq-governance.md` — Ontology governance policy
- `ifq-publication-readiness.md` — Publication readiness and release process
- `ifq-paper.md` — Draft academic paper

### Stability commitment from 1.0.0

- The 22-level progression model is frozen
- The `ifq:` namespace URI (`https://wherewelearn.com/ontology/ifq#`) is permanent
- All `intIFQ_Id` values are stable and will never be reassigned
- Breaking changes require a new namespace and a MAJOR version bump

---

## [0.1.0-draft] — 2026-05-09

Initial draft. Ontology structure established, validation pipeline operational,
26-country mapping coverage complete. Not publicly released.

### Added

- Core OWL ontology vocabulary
- 22-level SKOS concept scheme
- SHACL validation constraints (v2)
- SQL → RDF export script
- SHACL validation runner
- Ireland, England, and US initial mappings
- Expanded to 26 countries (AE, AT, AU, BO, BR, CA, CN, DE, EN, ES, FI, FR, IE, IN, IT, JP, KE, KR, NG, NL, NZ, PL, PT, SG, US, ZA)
- IFQ Specification v1.0 drafted
- Formal specification foundation document
- Academic paper draft
- Integration PRD (phases 1–5)
