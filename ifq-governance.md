# IFQ Ontology Governance

**Document:** IFQ Ontology Governance Policy  
**Version:** 1.0  
**Date:** 2026-05-11  
**Owner:** WhereWeLearn  
**Status:** Active

---

## Purpose

This document defines who can change the IFQ ontology, what kinds of changes are permitted, how changes are versioned, and how the operational SQL layer and the formal RDF/OWL ontology layer are kept in sync.

It exists to prevent conceptual drift — the gradual erosion of the sparse ontology principle through incremental additions that seem individually reasonable but collectively undermine the framework's global survivability.

---

## 1. Ownership and Decision Authority

| Role | Responsibility |
|---|---|
| **Ontology Owner** (WhereWeLearn) | Final authority on all changes to the core ontology (`ifq-core.ttl`, `ifq-levels.ttl`, `ifq-shacl-v2.ttl`) and the 22-level progression model |
| **Country Mapping Contributor** | May propose new country entries or corrections to existing entries via the defined process |
| **External Reviewer** | May raise issues against the published ontology; has no merge authority |

The Ontology Owner is responsible for:
- maintaining the sparse ontology principle
- approving all changes to the core vocabulary
- approving all new country system mappings
- triggering version releases
- maintaining the SHACL constraints

---

## 2. The Sparse Ontology Principle — Non-Negotiable

Every proposed addition to the core ontology must pass this test:

> "Does this improve interoperability more than it increases complexity?"

If the answer is no, or uncertain, the addition is rejected.

This principle is structural, not stylistic. The IFQ works globally precisely because it is sparse. An IFQ entry for a Nigerian learner and an IFQ entry for a Finnish learner share the same 22-level structure because the core does not encode the educational content, competency expectations, or cultural assumptions of any specific system.

**What must remain outside the core ontology:**
- Curriculum content
- Competency standards
- Assessment criteria
- Institutional quality rankings
- Labour-market value judgements
- Legal qualification equivalence

These belong in national metadata overlays, not in the core progression model.

---

## 3. Semantic Versioning

The IFQ ontology follows [Semantic Versioning](https://semver.org/): `MAJOR.MINOR.PATCH`

Current version: `0.1.0-draft` (declared in `ifq-core.ttl` via `owl:versionInfo`)

### What triggers each level

| Level | Trigger | Examples |
|---|---|---|
| **MAJOR** | Breaking change to the core vocabulary or the 22-level model | Renaming a class, removing a property, restructuring the level scheme |
| **MINOR** | Backwards-compatible addition to the ontology | New OWL property, new SKOS relationship, new SHACL constraint, new country system mapping |
| **PATCH** | Correction that does not change semantics | Fixing a `rdfs:label` typo, updating `strIFQ_Notes`, correcting a source URL |

### Stability commitment

Once version 1.0.0 is published:
- The 22-level progression model is frozen — no levels may be added, removed, or renumbered
- The `ifq:` namespace URI is permanent
- All existing `intIFQ_Id` values are stable — they may never be reassigned or deleted
- Breaking changes (MAJOR version) require a new namespace

The current `0.x.x-draft` series does not carry this stability commitment.

---

## 4. The Two Layers — SQL and RDF

The IFQ exists in two layers that serve different purposes. Changes must be applied correctly to both.

| Layer | Location | System of Record for | Change trigger |
|---|---|---|---|
| **SQL operational** | `IFQ` database table | Production runtime, lesson classification, EKOS browser | DB migration (K-series) |
| **RDF ontology** | `ontology/*.ttl` | Published ontology, academic publication, external interoperability | TTL file edit + `ifq_sql_to_rdf.py` run |

### Sync rule

**The SQL database is the source of truth for country mapping data.** The RDF `ifq-country-mappings.ttl` is generated from it, not authored directly. After any change to the `IFQ` table:

1. Run `ontology/ifq_sql_to_rdf.py` to regenerate `ifq-country-mappings.ttl`
2. Run `ontology/ifq_validate_rdf.py` to validate all constraints
3. Confirm the validation report passes before committing

Changes to the core vocabulary (`ifq-core.ttl`, `ifq-levels.ttl`, `ifq-shacl-v2.ttl`) are made directly in the TTL files and do not require a DB change. After editing:

1. Run `ontology/ifq_validate_rdf.py`
2. Confirm the validation report passes
3. Update `owl:versionInfo` in `ifq-core.ttl`
4. Add a changelog entry
5. Commit

---

## 5. Adding a New Country System

New country systems require only new rows in the `IFQ` table — no schema change and no change to the core ontology.

### Required fields for a new country entry

| Field | Required | Notes |
|---|---|---|
| `strIFQ_Country` | Yes | ISO 3166-1 alpha-2 code |
| `intIFQ_Level` | Yes | 1–22, sequential within the country |
| `strIFQ_BroadStage` | Yes | One of the 8 canonical bands |
| `intIFQ_MinAge` | Yes | Typical minimum learner age |
| `intIFQ_MaxAge` | Yes | Typical maximum learner age |
| `strIFQ_ISCEDLevel` | Yes | UNESCO ISCED alignment |
| `strIFQ_SchoolTitle` | Yes | National school stage name |
| `strIFQ_YearTitle` | Yes | Year/grade label in the national system |
| `strIFQ_StateExam` | Recommended | Exit qualification name if applicable |
| `strIFQ_QualificationType` | Recommended | Certificate / Diploma / Degree / etc. |
| `strIFQ_ProgressionType` | Recommended | Academic / Vocational / Apprenticeship |
| `strIFQ_Confidence` | Yes | High / Medium / Approximate |
| `txtIFQ_Notes` | Recommended | Structural exceptions, caveats, split pathways |
| `strIFQ_Source` | Yes | Authoritative source URL or reference |

### Standard entry count

Most systems map to exactly 22 entries (one per IFQ level). Exceptions are permitted only for structural reasons, documented in `txtIFQ_Notes`:
- Vocational pathway splits at upper secondary (e.g. Austria: 24 entries)
- Systems with a formal Transition Year (e.g. Irish TY: documented in notes, not an extra level)

### Confidence assignment

| Confidence | When to use |
|---|---|
| High | Direct ISCED alignment, authoritative national source available, age ranges confirmed |
| Medium | ISCED alignment probable, some uncertainty in age range or exam mapping |
| Approximate | System differs substantially from ISCED model; mapping is a best-effort approximation |

### Proposal process

1. Prepare the 22 rows (or justified exception count) with all required fields populated
2. Include at least one authoritative national source URL per row (`strIFQ_Source`)
3. Run `ifq_sql_to_rdf.py` and `ifq_validate_rdf.py` — all constraints must pass
4. Submit for Ontology Owner review with a brief note on any structural exceptions
5. On approval: apply DB migration, regenerate RDF, update validation report, bump MINOR version

---

## 6. Changing Existing Country Mappings

Corrections to existing entries (wrong age range, updated exam name, improved ISCED alignment) follow the same validation and approval process as new entries.

**What cannot change without a MAJOR version:**
- `intIFQ_Id` values — these are foreign keys used across the platform (`EKOS.intEKOS_IFQId`)
- The total number of IFQ progression levels (22) — this is a core ontology property

**What can change freely (PATCH):**
- `strIFQ_YearTitle`, `strIFQ_SchoolTitle` — labels only
- `txtIFQ_Notes` — explanatory text
- `strIFQ_Source`, `strIFQ_Link` — reference URLs
- `strIFQ_Confidence` — if new evidence warrants updating

---

## 7. EKOS Classification Governance

EKOS records (the operational dual-axis classifications linking lessons to UDC + IFQ) are governed separately from the ontology.

### Who can classify

Any educator with access to the EKOS classification form can submit a classification. Submissions enter `intEKOS_Status = 3` (For Review).

### Approval

An approving educator sets `intEKOS_Status = 1` (Approved). Rejection sets status 2.

### Disputes

If two educators disagree on the correct UDC node or IFQ level for a lesson:
1. The more specific classification is preferred if both axes can be justified
2. If IFQ level is in dispute, prefer the lower (more accessible) level — the framework is inclusive by design
3. The Ontology Owner has final say on IFQ level disputes; the subject matter educator has final say on UDC node disputes

### AI-assisted classification (AI-06)

AI suggestions are stored in AI suggestion columns on `EKOS` and are not the canonical classification until an educator explicitly accepts them. The AI confidence score (0–100) and reasoning are stored as supporting context. An educator may override any AI suggestion.

---

## 8. What This Document Does Not Cover

- AI pipeline approval gates — see `docs/10-architecture/ai-enrichment-architecture.md`
- EKOS database schema — see `docs/10-architecture/ekos-engine.md`
- Publication process — see `ontology/ifq-publication-readiness.md`
- Academic formalisation — see `ontology/ifq-paper.md`
