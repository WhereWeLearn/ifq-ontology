#!/usr/bin/env python3
"""
ifq_validate_rdf.py

Validate the IFQ RDF/OWL/Turtle files against the IFQ SHACL rules.

Purpose
-------
This script loads the IFQ ontology files and generated RDF mappings, then runs
SHACL validation using pySHACL.

Expected files
--------------
By default, the script expects these files in the current directory:

    ifq-core.ttl
    ifq-levels.ttl
    ifq-mappings-example.ttl
    ifq-country-mappings.ttl
    ifq-shacl.ttl

You can override paths with command-line arguments.

Requirements
------------
pip install rdflib pyshacl

Usage
-----
Basic:

    python ifq_validate_rdf.py

With explicit files:

    python ifq_validate_rdf.py \
        --core ifq-core.ttl \
        --levels ifq-levels.ttl \
        --examples ifq-mappings-example.ttl \
        --mappings ifq-country-mappings.ttl \
        --shacl ifq-shacl.ttl

Write SHACL report to file:

    python ifq_validate_rdf.py --report ifq-validation-report.ttl

Exit codes
----------
0 = validation passed
1 = validation failed
2 = file/load/runtime error
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Iterable

from rdflib import Graph
from pyshacl import validate


DEFAULT_CORE = "ifq-core.ttl"
DEFAULT_LEVELS = "ifq-levels.ttl"
DEFAULT_EXAMPLES = "ifq-mappings-example.ttl"
DEFAULT_MAPPINGS = "ifq-country-mappings.ttl"
DEFAULT_SHACL = "ifq-shacl.ttl"


def existing_files(paths: Iterable[str | None]) -> list[Path]:
    """Return only paths that exist and are not None/empty."""
    found: list[Path] = []

    for raw in paths:
        if not raw:
            continue

        path = Path(raw)

        if path.exists():
            found.append(path)
        else:
            print(f"WARNING: File not found and will be skipped: {path}")

    return found


def load_graph(paths: list[Path], label: str) -> Graph:
    """Load one or more Turtle files into an RDF graph."""
    graph = Graph()

    for path in paths:
        print(f"Loading {label}: {path}")

        try:
            graph.parse(path, format="turtle")
        except Exception as exc:
            raise RuntimeError(f"Failed to parse {path}: {exc}") from exc

    print(f"Loaded {len(graph):,} triples into {label} graph.")
    return graph


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate IFQ RDF files using SHACL."
    )

    parser.add_argument("--core", default=DEFAULT_CORE, help="Path to ifq-core.ttl")
    parser.add_argument("--levels", default=DEFAULT_LEVELS, help="Path to ifq-levels.ttl")
    parser.add_argument("--examples", default=DEFAULT_EXAMPLES, help="Path to ifq-mappings-example.ttl")
    parser.add_argument("--mappings", default=DEFAULT_MAPPINGS, help="Path to generated ifq-country-mappings.ttl")
    parser.add_argument("--shacl", default=DEFAULT_SHACL, help="Path to ifq-shacl.ttl")
    parser.add_argument("--report", default=None, help="Optional path to write SHACL report graph as Turtle")
    parser.add_argument(
        "--allow-missing-examples",
        action="store_true",
        help="Do not fail if ifq-mappings-example.ttl is missing.",
    )
    parser.add_argument(
        "--allow-missing-mappings",
        action="store_true",
        help="Do not fail if ifq-country-mappings.ttl is missing.",
    )
    parser.add_argument(
        "--advanced",
        action="store_true",
        help="Enable pySHACL advanced mode.",
    )
    parser.add_argument(
        "--debug",
        action="store_true",
        help="Enable pySHACL debug output.",
    )

    args = parser.parse_args()

    required_data_files = [
        Path(args.core),
        Path(args.levels),
    ]

    optional_data_files = [
        Path(args.examples),
        Path(args.mappings),
    ]

    required_shape_file = Path(args.shacl)

    try:
        for path in required_data_files:
            if not path.exists():
                print(f"ERROR: Required file not found: {path}")
                return 2

        if not required_shape_file.exists():
            print(f"ERROR: Required SHACL file not found: {required_shape_file}")
            return 2

        if not Path(args.examples).exists() and not args.allow_missing_examples:
            print(f"ERROR: Example mappings file not found: {args.examples}")
            print("Use --allow-missing-examples to skip it.")
            return 2

        if not Path(args.mappings).exists() and not args.allow_missing_mappings:
            print(f"ERROR: Country mappings file not found: {args.mappings}")
            print("Use --allow-missing-mappings to skip it.")
            return 2

        data_paths = existing_files(
            [
                args.core,
                args.levels,
                args.examples,
                args.mappings,
            ]
        )

        shacl_paths = existing_files([args.shacl])

        data_graph = load_graph(data_paths, "data")
        shacl_graph = load_graph(shacl_paths, "SHACL")

        print("\nRunning SHACL validation...\n")

        conforms, report_graph, report_text = validate(
            data_graph=data_graph,
            shacl_graph=shacl_graph,
            inference="rdfs",
            abort_on_first=False,
            allow_infos=True,
            allow_warnings=True,
            meta_shacl=False,
            advanced=args.advanced,
            debug=args.debug,
        )

        print(report_text)

        if args.report:
            report_path = Path(args.report)
            report_path.write_text(
                report_graph.serialize(format="turtle"),
                encoding="utf-8",
            )
            print(f"\nWrote SHACL report graph to: {report_path}")

        if conforms:
            print("\n✅ IFQ RDF validation PASSED.")
            return 0

        print("\n❌ IFQ RDF validation FAILED.")
        return 1

    except Exception as exc:
        print(f"\nERROR: {exc}")
        return 2


if __name__ == "__main__":
    main()
