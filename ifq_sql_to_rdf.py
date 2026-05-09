#!/usr/bin/env python3
"""
ifq_sql_to_rdf.py

Export the WhereWeLearn IFQ SQL table to Turtle RDF.

Purpose
-------
This script treats the SQL IFQ table as the operational source of truth and
generates RDF/Turtle mapping instances compatible with:

- ifq-core.ttl
- ifq-levels.ttl
- ifq-shacl.ttl

It does not replace the database. It creates a semantic export layer.

Requirements
------------
pip install mysql-connector-python

Usage
-----
Run from anywhere inside the repository:

    python ontology/ifq_sql_to_rdf.py

Credentials are read automatically from lib/const/env.php.
No local configuration is required.

Optional:

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

IFQ_PREFIX = "https://wherewelearn.org/ontology/ifq#"
MAP_PREFIX = "https://wherewelearn.org/ontology/ifq/mappings#"

DEFAULT_OUTPUT = "ifq-country-mappings.ttl"


# ============================================================================
# HELPERS
# ============================================================================

def turtle_string(value: Any, lang: Optional[str] = None) -> str:
    if value is None:
        return '""'

    text = str(value)
    text = text.replace("\\", "\\\\")
    text = text.replace('"', '\\"')
    text = text.replace("\n", "\\n")
    text = text.replace("\r", "\\r")

    if lang:
        return f'"{text}"@{lang}'

    return f'"{text}"'


def turtle_int(value: Any) -> Optional[str]:
    if value is None or value == "":
        return None

    try:
        return str(int(value))
    except (TypeError, ValueError):
        return None


def turtle_uri(value: Any) -> Optional[str]:
    if value is None:
        return None

    text = str(value).strip()

    if not text:
        return None

    if not (
        text.startswith("http://")
        or text.startswith("https://")
    ):
        return None

    text = text.replace(" ", "%20")

    return f"<{text}>"


def slug(value: Any, fallback: str) -> str:
    if value is None or str(value).strip() == "":
        value = fallback

    text = str(value).strip()

    text = re.sub(r"[^A-Za-z0-9_\\-]+", "_", text)
    text = re.sub(r"_+", "_", text).strip("_")

    return text or fallback


def add_literal(lines, predicate, value, lang=None):
    if value is None:
        return

    if isinstance(value, str) and value.strip() == "":
        return

    lines.append(
        f'    ifq:{predicate} {turtle_string(value, lang=lang)} ;'
    )


def add_int(lines, predicate, value):
    lit = turtle_int(value)

    if lit is not None:
        lines.append(f"    ifq:{predicate} {lit} ;")


def add_uri_literal(lines, predicate, value):
    uri = turtle_uri(value)

    if uri:
        lines.append(f"    ifq:{predicate} {uri} ;")


def finish_block(lines):
    while lines and lines[-1].strip() == "":
        lines.pop()

    if lines[-1].rstrip().endswith(";"):
        lines[-1] = lines[-1].rstrip()[:-1] + "."

    return "\n".join(lines)


@dataclass
class IFQRow:
    data: dict

    def get(self, key):
        return self.data.get(key)


# ============================================================================
# DATABASE FETCH
# ============================================================================

def fetch_rows():
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
            ORDER BY strIFQ_Country, intIFQ_Level
        """

        cursor.execute(query)

        return [IFQRow(r) for r in cursor.fetchall()]

    finally:
        connection.close()


# ============================================================================
# RDF GENERATION
# ============================================================================

def emit_header():
    return f"""@prefix ifq: <{IFQ_PREFIX}> .
@prefix map: <{MAP_PREFIX}> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

"""


def emit_stage(row):
    row_id = row.get("intIFQ_Id")

    code = row.get("strIFQ_Code")
    country = row.get("strIFQ_Country") or "UNKNOWN"

    safe_code = slug(code, f"ROW_{row_id}")

    uri = f"map:Stage_{safe_code}"

    level = row.get("intIFQ_Level")

    ifq_uri = f"ifq:IFQ_{int(level):02d}"

    label = (
        row.get("strIFQ_YearTitle")
        or row.get("strIFQ_SchoolTitle")
        or safe_code
    )

    lines = [
        uri,
        "    a ifq:EducationStage ;",
        f'    rdfs:label "{label}"@en ;',
        f"    ifq:mapsToIFQLevel {ifq_uri} ;",
    ]

    add_literal(lines, "localStageName", label)
    add_literal(lines, "broadStage", row.get("strIFQ_BroadStage"))
    add_literal(lines, "alignedWithISCED", row.get("strIFQ_ISCEDLevel"))

    add_int(lines, "typicalMinAge", row.get("intIFQ_MinAge"))
    add_int(lines, "typicalMaxAge", row.get("intIFQ_MaxAge"))
    add_int(lines, "typicalAge", row.get("intIFQ_TargetAge"))

    add_literal(lines, "progressionType", row.get("strIFQ_ProgressionType"))
    add_literal(lines, "confidence", row.get("strIFQ_Confidence"))

    add_literal(
        lines,
        "qualificationType",
        row.get("strIFQ_QualificationType")
    )

    add_literal(lines, "notes", row.get("txtIFQ_Notes"), lang="en")

    return finish_block(lines)


def export_turtle(rows):
    blocks = [emit_header()]

    for row in rows:
        if row.get("intIFQ_Level") is None:
            continue

        blocks.append(emit_stage(row))
        blocks.append("")

    return "\n".join(blocks)


# ============================================================================
# MAIN
# ============================================================================

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--output",
        "-o",
        default=DEFAULT_OUTPUT,
        help="Output Turtle file"
    )

    args = parser.parse_args()

    rows = fetch_rows()

    turtle = export_turtle(rows)

    output = Path(args.output)

    output.write_text(turtle, encoding="utf-8")

    print(f"Exported {len(rows)} rows to {output}")


if __name__ == "__main__":
    main()