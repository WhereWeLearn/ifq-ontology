#!/usr/bin/env python3
"""
ifq_sql_to_rdf.py

Export the WhereWeLearn IFQ SQL table to Turtle RDF.

This corrected version fixes the common SHACL validation failures:
- emits ifq:EducationSystem nodes
- emits ifq:belongsToSystem for every EducationStage
- emits source URLs as xsd:anyURI literals
- omits typicalMaxAge when SQL value is NULL, allowing open-ended doctoral stages

Requirements:
    pip install mysql-connector-python

Usage:
    python ifq_sql_to_rdf.py --output ifq-country-mappings.ttl
"""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Optional

import mysql.connector


# ============================================================================
# DATABASE CONFIG  (read from lib/const/env.php — no local credentials stored)
# ============================================================================

TABLE_NAME = "IFQ"


def load_db_config() -> dict:
    """
    Parse DB credentials from lib/const/env.php.

    Walks up from this script's directory to locate the repo root, then reads
    the PHP file as text and extracts the four $strGlobal_Db_* variables.
    $strGlobal_Db_Servername may be "host:port" — split if so.
    """
    candidate = Path(__file__).resolve().parent
    env_php = None
    for _ in range(6):
        probe = candidate / "lib" / "const" / "env.php"
        if probe.exists():
            env_php = probe
            break
        candidate = candidate.parent

    if env_php is None:
        raise FileNotFoundError(
            "env.php not found in lib/const/ within any parent directory of this script.\n"
            f"Started search from: {Path(__file__).resolve().parent}"
        )

    content = env_php.read_text(encoding="utf-8")

    def extract(var_name: str) -> str:
        match = re.search(
            r'\$' + re.escape(var_name) + r'\s*=\s*"(.*?)"',
            content,
        )
        if not match:
            raise ValueError(f"${var_name} not found in {env_php}")
        return match.group(1)

    server   = extract("strGlobal_Db_Servername")
    database = extract("strGlobal_Db_Database")
    user     = extract("strGlobal_Db_Username")
    password = extract("strGlobal_Db_Password")

    # Servername may be "host:port"
    if ":" in server:
        host, port_str = server.rsplit(":", 1)
        port = int(port_str)
    else:
        host = server
        port = 3306

    return {
        "host":     host,
        "user":     user,
        "password": password,
        "database": database,
        "port":     port,
    }


# ============================================================================
# RDF CONFIG
# ============================================================================

IFQ_PREFIX = "https://wherewelearn.com/ontology/ifq#"
MAP_PREFIX = "https://wherewelearn.com/ontology/ifq/mappings#"
DEFAULT_OUTPUT = "ifq-country-mappings.ttl"


# ============================================================================
# HELPERS
# ============================================================================

def turtle_string(value: Any, lang: Optional[str] = None, datatype: Optional[str] = None) -> str:
    if value is None:
        return '""'

    text = str(value)
    text = text.replace("\\", "\\\\")
    text = text.replace('"', '\\"')
    text = text.replace("\n", "\\n")
    text = text.replace("\r", "\\r")

    literal = f'"{text}"'

    if lang:
        return f"{literal}@{lang}"

    if datatype:
        return f"{literal}^^{datatype}"

    return literal


def turtle_int(value: Any) -> Optional[str]:
    if value is None or value == "":
        return None

    try:
        return str(int(value))
    except (TypeError, ValueError):
        return None


def turtle_uri_literal(value: Any) -> Optional[str]:
    if value is None:
        return None

    text = str(value).strip()

    if not text:
        return None

    if not (text.startswith("http://") or text.startswith("https://")):
        return None

    return turtle_string(text, datatype="xsd:anyURI")


def slug(value: Any, fallback: str) -> str:
    if value is None or str(value).strip() == "":
        value = fallback

    text = str(value).strip()
    text = re.sub(r"[^A-Za-z0-9_\\-]+", "_", text)
    text = re.sub(r"_+", "_", text).strip("_")

    return text or fallback


def add_literal(lines: list[str], predicate: str, value: Any, *, lang: Optional[str] = None) -> None:
    if value is None:
        return

    if isinstance(value, str) and value.strip() == "":
        return

    lines.append(f"    ifq:{predicate} {turtle_string(value, lang=lang)} ;")


def add_int(lines: list[str], predicate: str, value: Any) -> None:
    lit = turtle_int(value)

    if lit is not None:
        lines.append(f"    ifq:{predicate} {lit} ;")


def add_uri_literal(lines: list[str], predicate: str, value: Any) -> None:
    lit = turtle_uri_literal(value)

    if lit:
        lines.append(f"    ifq:{predicate} {lit} ;")


def finish_block(lines: list[str]) -> str:
    while lines and lines[-1].strip() == "":
        lines.pop()

    if not lines:
        return ""

    if lines[-1].rstrip().endswith(";"):
        lines[-1] = lines[-1].rstrip()[:-1] + "."

    return "\n".join(lines)


@dataclass
class IFQRow:
    data: dict[str, Any]

    def get(self, key: str) -> Any:
        return self.data.get(key)


# ============================================================================
# DATABASE FETCH
# ============================================================================

def fetch_rows() -> list[IFQRow]:
    connection = mysql.connector.connect(**load_db_config())

    try:
        cursor = connection.cursor(dictionary=True)


        query = f"""
            SELECT
                intIFQ_Id,
                strIFQ_Code,
                intIFQ_Level,
                strIFQ_ISCEDLevel,
                strIFQ_BroadStage,
                intIFQ_MinAge,
                intIFQ_MaxAge,
                intIFQ_NFQLevel,
                intIFQ_TargetAge,
                strIFQ_Country,
                strIFQ_Region,
                strIFQ_SchoolTitle,
                strIFQ_YearTitle,
                strIFQ_StateExam,
                strIFQ_QualificationType,
                strIFQ_ProgressionType,
                strIFQ_Confidence,
                txtIFQ_Notes,
                strIFQ_Link,
                strIFQ_Source
            FROM {TABLE_NAME}
            ORDER BY strIFQ_Country, intIFQ_Level, intIFQ_Id
        """

        cursor.execute(query)

        return [IFQRow(r) for r in cursor.fetchall()]

    finally:
        connection.close()


# ============================================================================
# RDF GENERATION
# ============================================================================

def emit_header() -> str:
    return f"""@prefix ifq: <{IFQ_PREFIX}> .
@prefix map: <{MAP_PREFIX}> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

map:IFQCountryMappings
    a owl:Ontology ;
    rdfs:label "IFQ Country and System Mappings"@en ;
    dcterms:title "IFQ Country and System Mappings"@en ;
    dcterms:description "Generated RDF export of IFQ country/system mappings from the WhereWeLearn IFQ SQL table."@en ;
    dcterms:creator "WhereWeLearn"@en ;
    owl:imports ifq:Ontology .

"""


def emit_systems(rows: list[IFQRow]) -> str:
    seen: set[str] = set()
    blocks: list[str] = []

    for row in rows:
        code = row.get("strIFQ_Country")

        if not code:
            continue

        code = str(code).strip()

        if code in seen:
            continue

        seen.add(code)

        system_uri = f"map:System_{slug(code, 'UNKNOWN')}"
        region = row.get("strIFQ_Region")

        lines = [
            f"{system_uri}",
            "    a ifq:EducationSystem ;",
            f"    rdfs:label {turtle_string(code + ' Education System', lang='en')} ;",
            f"    ifq:countryCode {turtle_string(code)} ;",
        ]

        if region:
            add_literal(lines, "notes", f"Region/reference context: {region}.", lang="en")
        else:
            add_literal(lines, "notes", f"Generated education-system node for IFQ country/system code {code}.", lang="en")

        blocks.append(finish_block(lines))

    return "\n\n".join(blocks) + "\n\n"


def emit_source(row: IFQRow) -> Optional[str]:
    row_id = row.get("intIFQ_Id")
    source_name = row.get("strIFQ_Source")
    source_url = row.get("strIFQ_Link")

    if not source_name and not source_url:
        return None

    source_uri = f"map:Source_{row_id}"

    lines = [
        f"{source_uri}",
        "    a ifq:Source ;",
        f"    rdfs:label {turtle_string('Source for IFQ row ' + str(row_id), lang='en')} ;",
    ]

    if source_name:
        add_literal(lines, "sourceName", source_name)

    if source_url:
        add_uri_literal(lines, "sourceURL", source_url)

    return finish_block(lines)


def emit_qualification(row: IFQRow, stage_uri: str) -> Optional[str]:
    row_id = row.get("intIFQ_Id")
    exam = row.get("strIFQ_StateExam")
    qtype = row.get("strIFQ_QualificationType")

    if not exam and not qtype:
        return None

    qual_uri = f"map:Qualification_{row_id}"
    label = exam or qtype or f"Qualification {row_id}"

    lines = [
        f"{qual_uri}",
        "    a ifq:Qualification ;",
        f"    rdfs:label {turtle_string(label, lang='en')} ;",
    ]

    if qtype:
        add_literal(lines, "qualificationType", qtype)

    if exam:
        add_literal(lines, "notes", f"Associated exam or qualification: {exam}.", lang="en")

    qual_block = finish_block(lines)
    rel_block = f"{stage_uri}\n    ifq:hasQualification {qual_uri} ."

    return qual_block + "\n\n" + rel_block


def emit_stage_and_assertion(row: IFQRow) -> str:
    row_id = row.get("intIFQ_Id")
    code = row.get("strIFQ_Code")
    country = row.get("strIFQ_Country") or "UNKNOWN"
    level = row.get("intIFQ_Level")

    safe_code = slug(code, f"ROW_{row_id}")
    stage_uri = f"map:Stage_{safe_code}"
    assertion_uri = f"map:Assertion_{safe_code}"
    system_uri = f"map:System_{slug(country, 'UNKNOWN')}"
    ifq_uri = f"ifq:IFQ_{int(level):02d}"

    label = (
        row.get("strIFQ_YearTitle")
        or row.get("strIFQ_SchoolTitle")
        or code
        or f"IFQ row {row_id}"
    )

    stage_lines = [
        f"{stage_uri}",
        "    a ifq:EducationStage ;",
        f"    rdfs:label {turtle_string(str(label), lang='en')} ;",
        f"    ifq:belongsToSystem {system_uri} ;",
        f"    ifq:mapsToIFQLevel {ifq_uri} ;",
    ]

    add_literal(stage_lines, "localStageName", label)
    add_literal(stage_lines, "broadStage", row.get("strIFQ_BroadStage"))
    add_literal(stage_lines, "alignedWithISCED", row.get("strIFQ_ISCEDLevel"))
    add_int(stage_lines, "typicalAge", row.get("intIFQ_TargetAge"))
    add_int(stage_lines, "typicalMinAge", row.get("intIFQ_MinAge"))
    add_int(stage_lines, "typicalMaxAge", row.get("intIFQ_MaxAge"))
    add_literal(stage_lines, "progressionType", row.get("strIFQ_ProgressionType"))
    add_literal(stage_lines, "confidence", row.get("strIFQ_Confidence") or "Approximate")
    add_literal(stage_lines, "qualificationType", row.get("strIFQ_QualificationType"))
    add_literal(stage_lines, "notes", row.get("txtIFQ_Notes"), lang="en")

    stage_block = finish_block(stage_lines)

    assertion_lines = [
        f"{assertion_uri}",
        "    a ifq:MappingAssertion ;",
        f"    rdfs:label {turtle_string('Mapping assertion for ' + str(label), lang='en')} ;",
        f"    ifq:assertsStage {stage_uri} ;",
        f"    ifq:assertsIFQLevel {ifq_uri} ;",
    ]

    add_literal(assertion_lines, "confidence", row.get("strIFQ_Confidence") or "Approximate")
    add_literal(assertion_lines, "notes", row.get("txtIFQ_Notes"), lang="en")

    if row.get("strIFQ_Source") or row.get("strIFQ_Link"):
        assertion_lines.append(f"    ifq:hasSource map:Source_{row_id} ;")

    assertion_block = finish_block(assertion_lines)

    blocks = [stage_block, assertion_block]

    source_block = emit_source(row)
    if source_block:
        blocks.append(source_block)

    qualification_block = emit_qualification(row, stage_uri)
    if qualification_block:
        blocks.append(qualification_block)

    return "\n\n".join(blocks)


def export_turtle(rows: list[IFQRow]) -> str:
    blocks: list[str] = [
        emit_header(),
        emit_systems(rows),
    ]

    for row in rows:
        if row.get("intIFQ_Level") is None:
            continue

        blocks.append(emit_stage_and_assertion(row))
        blocks.append("")

    return "\n".join(blocks)


def main() -> None:
    parser = argparse.ArgumentParser(description="Export IFQ SQL rows to Turtle RDF.")

    parser.add_argument(
        "--output",
        "-o",
        default=DEFAULT_OUTPUT,
        help=f"Output Turtle file path. Default: {DEFAULT_OUTPUT}",
    )

    args = parser.parse_args()

    rows = fetch_rows()
    turtle = export_turtle(rows)

    output = Path(args.output)
    output.write_text(turtle, encoding="utf-8")

    print(f"Exported {len(rows)} IFQ rows to {output}")


if __name__ == "__main__":
    main()
