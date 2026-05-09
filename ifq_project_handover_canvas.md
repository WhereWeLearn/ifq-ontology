# IFQ Project Handover Notes

## Project
International Framework of Qualifications (IFQ) for WhereWeLearn.

## Core Definition
IFQ is an approximate international educational progression scale intended to compare mainstream educational stages across different national systems.

## Current Formal Framing
IFQ is a sparse international educational progression ontology.

It is designed to support:
- educational interoperability,
- lesson recommendation,
- AI-assisted explanation routing,
- learner-facing educational discovery,
- and cross-national education-stage comparison.

## Core Principle
IFQ models approximate educational progression, not educational equivalence.

## What IFQ Does Not Model
IFQ does not model:
- intelligence,
- learner capability,
- competency mastery,
- curriculum equivalence,
- educational quality,
- institutional prestige,
- labour-market value,
- legal qualification recognition.

## Architecture
The IFQ core remains a simple 22-level linear comparator model.

Complexity is held in metadata overlays rather than additional dimensions.

## IFQ Level Bands
| Band | IFQ Levels |
|---|---|
| Early Years | 1–3 |
| Primary | 4–9 |
| Lower Secondary | 10–12 |
| Upper Secondary | 13–15 |
| Post-Secondary / Short-cycle | 16–17 |
| Undergraduate | 18–19 |
| Postgraduate | 20–21 |
| Doctoral | 22 |

## Mapping Methodology
Primary mapping signals:
1. Typical learner age
2. Educational continuity
3. Progression stage
4. Exit qualification
5. ISCED alignment

Secondary signals are retained as metadata only:
- pathway type,
- vocational structure,
- examination intensity,
- regional variation,
- institutional hierarchy,
- confidence level,
- notes.

## Metadata Overlay Fields
Important overlay fields:
- BroadStage
- ISCED
- ProgressionType
- Confidence
- Notes
- Source
- Link
- QualificationType

## Confidence Semantics
| Confidence | Meaning |
|---|---|
| High | Strong structural alignment |
| Medium | Approximate structural alignment |
| Approximate | Constructed comparator stage |

## Systems Mapped So Far
Systems discussed or mapped include:
- Ireland
- England
- United States
- Bologna / EHEA
- Australia
- New Zealand
- Canada / Ontario reference
- India
- China
- Japan
- South Korea
- Singapore
- Nigeria
- Kenya
- UAE / Gulf reference
- Spain
- Germany
- France
- Portugal
- Italy
- Poland
- Finland
- Switzerland
- Netherlands
- Austria
- Brazil
- South Africa

## Important Design Decisions
1. Keep the IFQ core sparse.
2. Do not overfit national complexity into the core model.
3. Treat vocational and academic route differences as overlay metadata.
4. Treat ISCED as alignment metadata, not as the identity of IFQ.
5. Treat approximation as a formal property, not a flaw.

## Existing RDF / OWL Files Created
- `ifq-core.ttl`
- `ifq-levels.ttl`

## Next RDF Files Planned
- `ifq-mappings-example.ttl`
- `ifq-shacl.ttl`

## Intended RDF Architecture
Use:
- SKOS for IFQ levels as a concept scheme,
- OWL/RDFS for classes and properties,
- SHACL later for validation,
- RDF mapping assertions for country/system mappings.

## Example Mapping Intention
Examples should include:
- Ireland 5th Year → IFQ Level 14
- England Year 11 / GCSE → IFQ Level 13
- Switzerland Matura / VET Completion → IFQ Level 15
- A learning resource targeting IFQ Level 10

## Academic Direction
Potential paper title:

“IFQ: A Sparse International Educational Progression Ontology”

Core academic claim:

A globally interoperable educational progression ontology can remain useful by intentionally prioritising sparse abstraction over exhaustive educational precision.

## Immediate Next Step
Create `ifq-mappings-example.ttl`, then create `ifq-shacl.ttl` validation constraints.

