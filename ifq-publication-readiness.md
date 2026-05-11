# IFQ Ontology — Publication Readiness

**Document:** IFQ Ontology Publication Readiness  
**Version:** 1.0  
**Date:** 2026-05-11  
**Owner:** WhereWeLearn  
**Status:** Pre-publication — readiness assessment and plan

---

## Summary

The IFQ ontology is technically complete and SHACL-validated. The intellectual work — the sparse ontology argument, the 22-level model, 26-country mapping coverage, and the academic paper draft — is done. What remains before public release is infrastructure: a public repository, a stable namespace, a license, and a release process.

This document defines each of those and records what is and is not yet ready.

---

## 1. Namespace URI

### Chosen namespace

```
https://wherewelearn.com/ontology/ifq#
```

Already declared in `ifq-core.ttl`:

```turtle
@prefix ifq: <https://wherewelearn.com/ontology/ifq#> .
```

### Namespace stability commitment

Once version 1.0.0 is published, this URI is permanent. URIs in the `ifq:` namespace may never be removed or reassigned — they may only be deprecated with `owl:deprecated true` and a `rdfs:comment` explaining the replacement.

This is a hard requirement for Linked Data interoperability: external systems that reference `ifq:IFQLevel` must be able to dereference it indefinitely.

### Content negotiation (future)

When the namespace URI is visited in a browser, it should return a human-readable HTML description. When dereferenced by a semantic web client requesting `text/turtle`, it should return the ontology TTL. This requires web server configuration at `wherewelearn.com` and is a post-1.0.0 infrastructure task.

---

## 2. Licensing

### Ontology data (TTL files)

**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

This is the standard license for open ontology data. It allows:
- free use, sharing, and adaptation
- commercial and academic use
- with attribution to WhereWeLearn

**Attribution line to include in derivative works:**
> International Framework of Qualifications (IFQ) Ontology, WhereWeLearn, https://wherewelearn.com/ontology/ifq#, CC BY 4.0

### Scripts (`ifq_sql_to_rdf.py`, `ifq_validate_rdf.py`)

**License:** MIT

Scripts are utility code — MIT is appropriate. No usage restriction beyond attribution.

### Academic paper (`ifq-paper.md`)

**License:** CC BY 4.0 (same as ontology data, standard for open-access academic work)

### What to add to the repository

A `LICENSE` file at the root of the public ontology repository:

```
IFQ Ontology — © WhereWeLearn 2026
Ontology data (*.ttl): CC BY 4.0 — https://creativecommons.org/licenses/by/4.0/
Scripts (*.py): MIT License
```

Add license declarations to each TTL file header:

```turtle
dcterms:license <https://creativecommons.org/licenses/by/4.0/> ;
dcterms:rights "CC BY 4.0 — WhereWeLearn 2026" ;
```

---

## 3. Repository Structure

The public ontology repository (separate from the LEAST LMS codebase) should contain:

```
ifq-ontology/
├── README.md                        — project overview, quick-start, attribution
├── LICENSE                          — CC BY 4.0 / MIT dual license
├── CHANGELOG.md                     — version history
├── CONTRIBUTING.md                  — how to propose country mappings
│
├── ontology/
│   ├── ifq-core.ttl                 — core OWL vocabulary
│   ├── ifq-levels.ttl               — 22-level SKOS concept scheme
│   ├── ifq-country-mappings.ttl     — generated country mapping instances
│   ├── ifq-mappings-example.ttl     — reference example for contributors
│   └── ifq-shacl-v2.ttl            — SHACL validation constraints
│
├── scripts/
│   ├── ifq_sql_to_rdf.py            — SQL → RDF export
│   └── ifq_validate_rdf.py          — validation runner
│
├── docs/
│   ├── ifq_specification_v_1_0.md   — IFQ Specification v1.0
│   ├── ifq-governance.md            — ontology governance policy
│   └── ifq-paper.md                 — academic paper (draft)
│
└── validation/
    └── ifq-validation-report.ttl    — latest SHACL validation output
```

Note: `ifq-country-mappings.ttl` is generated — it should not be manually edited. The README must make this clear.

---

## 4. Release Process

### Pre-release checklist

Before any version is tagged and published:

- [ ] All SHACL constraints pass (`ifq_validate_rdf.py` exits clean)
- [ ] `owl:versionInfo` in `ifq-core.ttl` matches the intended version tag
- [ ] `dcterms:issued` in `ifq-core.ttl` is updated to the release date
- [ ] `CHANGELOG.md` entry written for this version
- [ ] `ifq-country-mappings.ttl` regenerated from current SQL (`ifq_sql_to_rdf.py`)
- [ ] License declarations present in all TTL files
- [ ] `README.md` reflects current country coverage count

### Versioning

Follow [Semantic Versioning](https://semver.org/) as defined in `ifq-governance.md`:

- **MAJOR** — breaking change to core vocabulary or 22-level model
- **MINOR** — new country mapping, new property, new SHACL constraint
- **PATCH** — label correction, source URL update, notes update

Tag format: `v1.0.0`, `v1.1.0`, `v1.0.1`

### Release steps

1. Make changes in development (SQL + TTL as appropriate)
2. Run `ifq_sql_to_rdf.py` if country mappings changed
3. Run `ifq_validate_rdf.py` — must pass
4. Update `owl:versionInfo` and `dcterms:issued` in `ifq-core.ttl`
5. Write `CHANGELOG.md` entry
6. Commit with message: `release: IFQ v{version}`
7. Tag the commit: `git tag v{version}`
8. Push tag to GitHub: `git push origin v{version}`
9. Create GitHub Release with changelog notes attached

---

## 5. Contribution Guidelines

External contributors may propose new country system mappings or corrections to existing mappings.

### What can be contributed

- New country system mappings (new rows in the `IFQ` table / new instances in `ifq-country-mappings.ttl`)
- Corrections to existing mappings (age ranges, exam names, source URLs)
- Translations of `rdfs:label` values into additional languages

### What cannot be contributed externally

- Changes to the 22-level progression model (`ifq-levels.ttl`)
- Changes to OWL class definitions (`ifq-core.ttl`)
- Changes to SHACL constraints (`ifq-shacl-v2.ttl`)

These are controlled by the Ontology Owner. See `ifq-governance.md`.

### How to submit a country mapping

1. Fork the repository
2. Add your mapping as new instances in `ifq-country-mappings.ttl` following the pattern in `ifq-mappings-example.ttl`
3. Ensure all required properties are present (see `ifq-governance.md` §5 for the full field list)
4. Run `ifq_validate_rdf.py` — all constraints must pass before submission
5. Include at least one authoritative national source URL per entry
6. Open a Pull Request with:
   - Country name and ISO 3166-1 alpha-2 code
   - Number of entries submitted
   - Any structural exceptions and their justification
   - Confidence level for each entry

### Review criteria

The Ontology Owner will assess:
- SHACL validation (automatic — PR will not be merged if it fails)
- Source quality (authoritative government or international body sources preferred)
- ISCED alignment accuracy
- Age range plausibility
- Justification for any entry count other than 22
- Compliance with the sparse ontology principle (no curriculum content, no competency detail)

---

## 6. Publication Targets

### Primary — GitHub

A dedicated public GitHub repository under the WhereWeLearn organisation:
`github.com/wherewelearn/ifq-ontology`

This is the canonical public location for the ontology, scripts, and documentation.

### Secondary — Linked Open Vocabularies (LOV)

[Linked Open Vocabularies](https://lov.linkeddata.es/) is the primary registry for open RDF/OWL ontologies. Registration requires:
- A stable namespace URI (ready: `https://wherewelearn.com/ontology/ifq#`)
- At least one version published on GitHub
- A contact email
- A description of the ontology's domain

LOV registration is a post-1.0.0 task.

### Tertiary — Zenodo (academic)

[Zenodo](https://zenodo.org/) provides DOI-minted archival for software and data. Publishing the ontology on Zenodo alongside the academic paper provides a citable artefact for journal submission.

---

## 7. Readiness Status

| Item | Status | Notes |
|---|---|---|
| Namespace URI | **Ready** | `https://wherewelearn.com/ontology/ifq#` declared in `ifq-core.ttl` |
| `owl:versionInfo` | **Ready** | `0.1.0-draft` in `ifq-core.ttl` |
| Core ontology files | **Ready** | `ifq-core.ttl`, `ifq-levels.ttl`, `ifq-shacl-v2.ttl` |
| Country mappings | **Ready** | 574 entries, 26 countries, SHACL-validated |
| SHACL validation | **Ready** | All constraints pass |
| Specification doc | **Ready** | `ifq_specification_v_1_0.md` |
| Academic paper | **Draft** | `ifq-paper.md` — requires editorial pass before submission |
| Governance policy | **Ready** | `ifq-governance.md` |
| License declarations in TTL | **Not yet** | `dcterms:license` and `dcterms:rights` not yet added to TTL headers |
| `LICENSE` file | **Not yet** | Needed before public repo |
| `CHANGELOG.md` | **Not yet** | Needed before first tagged release |
| `CONTRIBUTING.md` | **Not yet** | Needed for external contributors |
| `README.md` (public repo) | **Not yet** | |
| Public GitHub repository | **Not yet** | Currently inside the LEAST LMS monorepo |
| Content negotiation at namespace URI | **Not yet** | Post-1.0.0 infrastructure task |
| LOV registration | **Not yet** | Post-1.0.0 |
| Zenodo DOI | **Not yet** | Post-paper submission |

### Minimum viable release (1.0.0)

The following are the only blockers for a v1.0.0 public release:

1. Add `dcterms:license` and `dcterms:rights` to TTL file headers
2. Write `LICENSE` file
3. Write `CHANGELOG.md` with v1.0.0 entry
4. Write `README.md` for the public repository
5. Create public GitHub repository and push
6. Tag `v1.0.0`

The intellectual and technical work is complete. The blockers are documentation and infrastructure, not content.
