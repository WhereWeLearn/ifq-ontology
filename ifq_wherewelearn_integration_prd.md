# Product Requirements Document (PRD)

# IFQ + WhereWeLearn Integration Roadmap

Version: 1.0-draft  
Date: 10 May 2026  
Organisation: WhereWeLearn

---

# 1. Executive Summary

The International Framework of Qualifications (IFQ) has evolved from:
- educational comparison research,
into:
- a validated sparse educational progression ontology.

The next phase is no longer conceptual discovery.

The next phase is:
1. stabilisation,
2. operationalisation,
3. integration into WhereWeLearn,
4. and long-term publishability.

This PRD defines actionable engineering, ontology, AI, and product tasks required to:
- continue IFQ as a long-term ontology initiative,
- and integrate IFQ meaningfully into the WhereWeLearn platform.

---

# 2. Strategic Goals

## Goal 1 — Long-Term Ontology Stability

Create a stable educational progression ontology that:
- survives international educational diversity,
- remains computationally sparse,
- and is academically defensible.

---

## Goal 2 — Educational Interoperability

Enable lessons to be classified independently of:
- nationality,
- educational system,
- qualification naming,
- or local curriculum structure.

---

## Goal 3 — AI-Compatible Educational Routing

Allow AI systems to:
- adapt explanation depth,
- scale pedagogical complexity,
- and recommend learning resources appropriately.

---

## Goal 4 — WhereWeLearn Integration

Use IFQ operationally within WhereWeLearn to:
- classify content,
- recommend lessons,
- support learner progression,
- and improve educational accessibility globally.

---

# 3. Core Product Philosophy

## Sparse Over Dense

The ontology should remain:
- sparse,
- stable,
- understandable,
- and globally interoperable.

Avoid:
- excessive dimensions,
- competency explosion,
- over-modelling educational nuance,
- or curriculum decomposition.

---

## Approximation Over False Precision

IFQ is an approximate progression ontology.

It intentionally does NOT attempt to:
- determine intelligence,
- determine competency mastery,
- define curriculum equivalence,
- or rank educational systems.

---

## Overlay Complexity

Complex educational nuance should remain:
- metadata overlays,
not:
- core ontology dimensions.

---

# 4. Current State

## Completed

### Ontology
- IFQ core philosophy defined
- 22-level progression model defined
- RDF ontology created
- OWL structure created
- SHACL validation created
- Validation pipeline operational
- SQL → RDF export operational

### Documentation
- IFQ Specification v1.0 drafted
- Ontology roadmap created
- Handover documentation created
- Academic framing established

### Mapping Coverage
Multiple educational systems mapped including:
- Ireland
- UK
- US
- Bologna
- Germany
- Switzerland
- Finland
- South Africa
- India
- China
- Japan
- South Korea
- Singapore
- Gulf systems
- and additional European systems.

---

# 5. Desired End State

## Technical End State

WhereWeLearn should eventually support:
- IFQ-tagged lessons,
- learner IFQ profiles,
- AI-adjusted explanation depth,
- progression-aware recommendations,
- ontology-backed educational routing,
- and linked educational interoperability.

---

## Ontology End State

The IFQ ontology should eventually exist as:
- a stable RDF/OWL ontology,
- publicly versioned,
- machine-readable,
- SHACL-validated,
- academically publishable,
- and operationally useful.

---

# 6. Phase 1 — Immediate Engineering Priorities

## Objective
Stabilise the ontology and integrate basic operational support into WhereWeLearn.

---

## Task Group 1 — Repository and Infrastructure

### Priority: Critical

### Tasks
- [ ] Create GitHub repository
- [ ] Publish ontology files
- [ ] Publish validation scripts
- [ ] Publish specification documents
- [ ] Add semantic versioning
- [ ] Add changelog
- [ ] Add open-source license
- [ ] Create issue templates
- [ ] Create pull request templates

### Deliverables
- Public ontology repository
- Version-controlled ontology releases

---

## Task Group 2 — Ontology Stabilisation

### Priority: Critical

### Tasks
- [ ] Freeze core ontology vocabulary
- [ ] Freeze 22-level structure
- [ ] Freeze progression semantics
- [ ] Freeze approximation semantics
- [ ] Review SHACL constraints
- [ ] Finalise namespace structure
- [ ] Add ontology version metadata
- [ ] Create governance policy

### Deliverables
- Stable ontology core
- Governance model

---

## Task Group 3 — Automated Validation

### Priority: High

### Tasks
- [ ] Create validation shell script
- [ ] Create CI validation workflow
- [ ] Automatically validate RDF exports
- [ ] Automatically validate SHACL constraints
- [ ] Add regression tests
- [ ] Add malformed data tests

### Deliverables
- Automated ontology validation pipeline

---

# 7. Phase 2 — WhereWeLearn Integration

## Objective
Begin operational usage of IFQ within WhereWeLearn.

---

## Task Group 4 — Lesson Classification

### Priority: Critical

### Tasks
- [ ] Add `ifq_level` to lessons table
- [ ] Add IFQ tagging UI
- [ ] Add IFQ selection dropdown
- [ ] Add IFQ display badges
- [ ] Add IFQ search filtering
- [ ] Add IFQ metadata overlays
- [ ] Add IFQ recommendation metadata

### Deliverables
- IFQ-tagged lesson system

---

## Task Group 5 — Learner Profiles

### Priority: High

### Tasks
- [ ] Add learner IFQ profile field
- [ ] Add self-declared IFQ level
- [ ] Add optional country/system context
- [ ] Add learner confidence selection
- [ ] Add progression tracking support

### Deliverables
- IFQ-aware learner profiles

---

## Task Group 6 — Recommendation Engine

### Priority: High

### Tasks
- [ ] Create IFQ recommendation rules
- [ ] Define progression windows
- [ ] Define progression tolerances
- [ ] Add difficulty scaling
- [ ] Add fallback recommendation logic
- [ ] Add exploratory learning support

### Example

```text
Learner: IFQ 10
Recommended lessons: IFQ 9–11
Stretch lessons: IFQ 12
Support lessons: IFQ 7–8
```

### Deliverables
- IFQ-aware recommendation engine

---

# 8. Phase 3 — AI Integration

## Objective
Use IFQ as an AI pedagogical routing layer.

---

## Task Group 7 — Prompt Semantics

### Priority: High

### Tasks
- [ ] Define IFQ explanation semantics
- [ ] Create IFQ prompt templates
- [ ] Create explanation scaling rules
- [ ] Create AI fallback heuristics
- [ ] Create subject-specific adaptation guidance

### Example

```text
Explain gravity at IFQ 6
Explain gravity at IFQ 18
```

### Deliverables
- AI-compatible IFQ routing layer

---

## Task Group 8 — Adaptive Pedagogy

### Priority: Medium

### Tasks
- [ ] Add AI lesson adaptation
- [ ] Add simplification heuristics
- [ ] Add complexity scaling
- [ ] Add terminology scaling
- [ ] Add pacing heuristics

### Deliverables
- Adaptive AI educational explanations

---

# 9. Phase 4 — Academic Formalisation

## Objective
Transform IFQ into a publishable ontology framework.

---

## Task Group 9 — Academic Paper

### Priority: High

### Tasks
- [ ] Create `ifq-paper.md`
- [ ] Write Introduction
- [ ] Write ontology rationale
- [ ] Write sparse ontology principle section
- [ ] Write international survivability section
- [ ] Write RDF/OWL/SHACL formalisation section
- [ ] Write limitations section
- [ ] Add diagrams and ontology visualisations

### Deliverables
- Publishable ontology paper

---

## Task Group 10 — Academic References

### Priority: Medium

### Tasks
- [ ] Expand Harvard references
- [ ] Add semantic web references
- [ ] Add linked-data references
- [ ] Add educational ontology references
- [ ] Add qualification framework references

### Deliverables
- Formal academic bibliography

---

# 10. Phase 5 — Public Interoperability

## Objective
Publish IFQ as a usable linked-data ontology.

---

## Task Group 11 — Public Namespace

### Priority: Medium

### Tasks
- [ ] Publish ontology namespace
- [ ] Add downloadable RDF
- [ ] Add JSON-LD export
- [ ] Add ontology browser
- [ ] Add SPARQL endpoint (optional)

### Deliverables
- Public ontology infrastructure

---

## Task Group 12 — Community Contributions

### Priority: Medium

### Tasks
- [ ] Create mapping contribution guidelines
- [ ] Create validation contribution process
- [ ] Create country review process
- [ ] Create ontology governance process

### Deliverables
- Sustainable ontology contribution workflow

---

# 11. Explicit Non-Goals

The following are intentionally NOT part of the IFQ core ontology:
- IQ/intelligence modelling
- psychometrics
- curriculum equivalence
- educational ranking
- institutional prestige
- labour-market value
- cognitive science modelling
- fine-grained competency decomposition

These may exist as future overlays or adjacent ontologies.

---

# 12. Risks

## Major Risk — Ontology Complexity Explosion

The greatest risk is:
- over-modelling educational nuance.

Mitigation:
- protect the sparse ontology principle.

---

## Major Risk — Semantic Drift

The ontology may gradually lose coherence.

Mitigation:
- governance,
- semantic versioning,
- SHACL validation,
- automated regression testing.

---

## Major Risk — Educational Ideology Encoding

The ontology may accidentally begin embedding:
- value judgements,
- prestige assumptions,
- or national educational bias.

Mitigation:
- preserve progression-first semantics.

---

# 13. Key Architectural Rule

Every proposed addition should be tested against:

> “Does this improve interoperability more than it increases complexity?”

If not:
- reject the addition.

---

# 14. Success Criteria

The project succeeds if:
- IFQ remains sparse,
- the ontology remains stable,
- international mappings remain survivable,
- AI systems can use IFQ operationally,
- and WhereWeLearn can meaningfully classify lessons globally.

---

# 15. Long-Term Vision

Long-term, IFQ may become:
- an educational interoperability ontology,
- a lesson classification standard,
- an AI educational routing layer,
- or a linked-data educational framework.

However:

The sparse ontology principle should remain protected.

The simplicity of IFQ is not a limitation.

It is the primary reason the framework currently survives international educational diversity.

