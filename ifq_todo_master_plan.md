# IFQ — Master TODO / Roadmap

## International Framework of Qualifications

Status: Active Development  
Organisation: WhereWeLearn  
Current Phase: Ontology Stabilisation

---

# 1. Overall Goal

The goal of IFQ is to create:

> A sparse, internationally interoperable educational progression ontology.

The framework should:
- approximately compare educational progression stages across countries,
- support AI-assisted educational recommendation,
- classify lessons independently of nationality,
- and remain computationally simple enough to survive global educational diversity.

IFQ is NOT intended to:
- determine intelligence,
- measure competency,
- replace national qualifications,
- or define educational quality.

The long-term objective is:
- a stable educational progression ontology,
- formally represented in RDF/OWL,
- validated using SHACL,
- publishable academically,
- and operationally usable by educational systems and AI platforms.

---

# 2. Current Status

## Completed

### Conceptual Foundation
- [x] Defined IFQ core philosophy
- [x] Defined sparse ontology principle
- [x] Defined progression-first semantics
- [x] Defined approximation as a formal property
- [x] Defined 22-level IFQ model
- [x] Defined metadata overlay strategy

### SQL Model
- [x] Initial IFQ SQL schema created
- [x] Country/system mappings added
- [x] Stress-tested against heterogeneous systems
- [x] Expanded mapping coverage internationally

### Ontology Layer
- [x] Created `ifq-core.ttl`
- [x] Created `ifq-levels.ttl`
- [x] Created `ifq-mappings-example.ttl`
- [x] Created `ifq-shacl.ttl`
- [x] Created SQL → RDF exporter
- [x] Created RDF validator
- [x] Passed SHACL validation

### Documentation
- [x] Created IFQ Specification v1.0 draft
- [x] Created ontology handover canvas

---

# 3. Immediate Priority — Stabilise the Ontology

This is the current highest-priority phase.

The objective is:
- prevent ontology drift,
- freeze semantics,
- and establish long-term structural stability.

---

# 4. Phase 1 — Freeze Core Semantics

## Goal
Define which parts of IFQ are stable and which are extensible.

## Tasks

### Core Semantics
- [ ] Freeze the definition of IFQ
- [ ] Freeze the sparse ontology principle
- [ ] Freeze progression-first semantics
- [ ] Freeze approximation semantics
- [ ] Freeze the 22-level structure
- [ ] Freeze relationship to ISCED

### Ontology Vocabulary
- [ ] Review all RDF classes
- [ ] Review all RDF properties
- [ ] Review naming consistency
- [ ] Freeze core vocabulary namespace
- [ ] Add ontology version metadata

### SHACL Stabilisation
- [ ] Review all SHACL rules
- [ ] Remove unnecessary constraints
- [ ] Ensure SHACL validates structure only
- [ ] Ensure SHACL does not encode educational ideology
- [ ] Lock stable validation rules

---

# 5. Phase 2 — Governance and Versioning

## Goal
Create sustainable ontology governance.

## Tasks

### Semantic Versioning
- [ ] Define ontology versioning strategy
- [ ] Create semantic version policy
- [ ] Establish release process
- [ ] Create changelog format

### Governance
- [ ] Define ontology maintainers
- [ ] Define approval process for ontology changes
- [ ] Define approval process for mapping additions
- [ ] Define extension policy
- [ ] Define deprecation policy

### Namespace Stability
- [ ] Secure persistent ontology namespace
- [ ] Define canonical URI structure
- [ ] Create namespace documentation

---

# 6. Phase 3 — Operational Validation Pipeline

## Goal
Ensure all future changes are automatically validated.

## Tasks

### Validation Automation
- [ ] Create automated validation pipeline
- [ ] Create validation shell script
- [ ] Create CI/CD validation workflow
- [ ] Ensure all RDF exports validate automatically

### Regression Testing
- [ ] Create ontology regression tests
- [ ] Create RDF export tests
- [ ] Create SHACL validation regression suite
- [ ] Create malformed data tests

### Data Quality
- [ ] Audit missing metadata
- [ ] Audit confidence semantics
- [ ] Audit source completeness
- [ ] Audit multilingual handling

---

# 7. Phase 4 — Academic Formalisation

## Goal
Turn IFQ into a formally publishable ontology framework.

## Tasks

### Academic Paper
- [ ] Create `ifq-paper.md`
- [ ] Write Introduction
- [ ] Write Existing Framework Analysis
- [ ] Write Sparse Ontology Principle section
- [ ] Write IFQ Architecture section
- [ ] Write Metadata Overlay Model section
- [ ] Write RDF/OWL/SHACL Formalisation section
- [ ] Write International Survivability section
- [ ] Write AI Recommendation Applications section
- [ ] Write Limitations section
- [ ] Write Conclusion

### References
- [ ] Expand Harvard references
- [ ] Add UNESCO references
- [ ] Add Eurydice references
- [ ] Add national qualification references
- [ ] Add semantic web references

### Publication Preparation
- [ ] Select publication target
- [ ] Prepare diagrams
- [ ] Prepare ontology visualisations
- [ ] Prepare mapping examples
- [ ] Prepare ontology figures

---

# 8. Phase 5 — Public Infrastructure

## Goal
Prepare IFQ for public use and interoperability.

## Tasks

### Repository
- [ ] Create GitHub repository
- [ ] Publish ontology files
- [ ] Publish validation scripts
- [ ] Publish documentation
- [ ] Add open-source license

### Documentation
- [ ] Create README
- [ ] Create ontology usage guide
- [ ] Create RDF export guide
- [ ] Create validation guide
- [ ] Create mapping contribution guide

### Linked Data Infrastructure
- [ ] Publish ontology namespace
- [ ] Publish downloadable RDF
- [ ] Add JSON-LD exports
- [ ] Add SPARQL endpoint (optional)
- [ ] Add ontology visualisation

---

# 9. Phase 6 — Mapping Expansion

## Goal
Expand international coverage while preserving sparse ontology integrity.

## Tasks

### Remaining Countries
- [ ] Add remaining EU systems
- [ ] Add Southeast Asian systems
- [ ] Add Latin American systems
- [ ] Add African systems
- [ ] Add post-Soviet systems
- [ ] Add additional Gulf systems

### Metadata Quality
- [ ] Add mapping confidence values
- [ ] Add provenance sources
- [ ] Add multilingual stage names
- [ ] Add regional notes
- [ ] Add pathway overlays

### Mapping Review
- [ ] Review outlier systems
- [ ] Review vocational complexity
- [ ] Review hybrid systems
- [ ] Review non-linear systems

---

# 10. Phase 7 — AI Integration

## Goal
Operationalise IFQ within AI-assisted educational systems.

## Tasks

### Lesson Classification
- [ ] Add IFQ tagging to lessons
- [ ] Add IFQ recommendation engine support
- [ ] Add learner progression modelling
- [ ] Add adaptive explanation scaling

### AI Routing
- [ ] Define IFQ prompt semantics
- [ ] Create AI explanation templates
- [ ] Create AI progression heuristics
- [ ] Create AI recommendation constraints

### Recommendation Systems
- [ ] Define progression matching rules
- [ ] Define supported progression windows
- [ ] Define learner fallback logic
- [ ] Define uncertainty handling

---

# 11. Phase 8 — Future Research

## Goal
Explore optional advanced extensions WITHOUT destabilising the sparse core.

## Tasks

### Optional Research Areas
- [ ] Competency overlays
- [ ] Probabilistic mappings
- [ ] Subject-specific overlays
- [ ] Curriculum graph overlays
- [ ] Learning pathway graphs
- [ ] Multilingual semantic layers

### Explicitly Deferred
The following are intentionally NOT part of the current IFQ core:
- intelligence modelling,
- psychometrics,
- educational ranking,
- curriculum equivalence,
- labour-market valuation,
- cognitive science modelling.

---

# 12. Key Architectural Rules

## Preserve Simplicity

Always ask:

> “Does this improve interoperability more than it increases complexity?”

If not:
- reject the change.

---

## Protect the Sparse Core

The sparse ontology principle is the strongest architectural property of IFQ.

Avoid:
- over-modelling,
- competency explosion,
- ontology fragmentation,
- educational ideology encoding.

---

# 13. Success Criteria

IFQ succeeds if it becomes:
- internationally interoperable,
- structurally stable,
- machine-readable,
- AI-compatible,
- academically defensible,
- and operationally useful.

The ideal long-term structure is:

```text
Small core.
Large ecosystem.
```

---

# 14. Long-Term Vision

Long-term, IFQ could become:
- an educational interoperability layer,
- an AI pedagogical routing layer,
- a lesson classification standard,
- or a linked-data educational ontology.

However:

The ontology should remain sparse.

That simplicity is not a weakness.

It is the primary reason the framework currently survives international educational diversity.

