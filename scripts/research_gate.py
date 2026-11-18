#!/usr/bin/env python3
"""Research gate: verify a research file meets minimums before drafting.

Usage: python3 research_gate.py ./copy-project/01-research.md [--mode standard|full]
Exit code 0 = pass, 1 = fail. Prints what is missing.
"""
import re
import sys
from pathlib import Path

REQUIRED = {
    "standard": {"quotes": 10, "competitors": 3, "sources": 3, "objections": 4, "gaps": 2},
    "full": {"quotes": 20, "competitors": 3, "sources": 5, "objections": 5, "gaps": 3},
}
SECTIONS = [
    "Customer Language Bank", "Competitor Matrix", "Opportunity Gaps",
    "Proof Inventory", "Objection List", "Sources",
]


def section_text(text, title):
    m = re.search(rf"^#+\s*{re.escape(title)}.*?$(.*?)(?=^#+\s|\Z)", text, re.S | re.M | re.I)
    return m.group(1) if m else ""


def table_rows(block):
    rows = []
    for line in block.splitlines():
        s = line.strip()
        if s.startswith("|") and not re.match(r"^\|[\s:\-|]+\|?$", s):
            cells = [c.strip() for c in s.strip("|").split("|")]
            rows.append(cells)
    return rows[1:] if rows else []  # drop header


def filled(rows):
    return [r for r in rows if any(c and not re.fullmatch(r"[\[\(].*[\]\)]", c) for c in r)]


def list_items(block):
    return [l for l in block.splitlines() if re.match(r"^\s*(?:[-*]|\d+\.)\s+\S", l)
            and len(l.strip()) > 6]


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    mode = "standard"
    if "--mode" in sys.argv:
        mode = sys.argv[sys.argv.index("--mode") + 1]
        args = [a for a in args if a != mode]
    if not args:
        print(__doc__)
        sys.exit(2)
    p = Path(args[0])
    if not p.exists():
        print(f"FAIL: {p} not found. Do the research phase first.")
        sys.exit(1)
    text = p.read_text(encoding="utf-8")
    req = REQUIRED.get(mode, REQUIRED["standard"])
    problems = []

    for s in SECTIONS:
        if not re.search(rf"^#+\s*{re.escape(s)}", text, re.M | re.I):
            problems.append(f"missing section: {s}")

    quotes = len(filled(table_rows(section_text(text, "Customer Language Bank"))))
    comps = len(filled(table_rows(section_text(text, "Competitor Matrix"))))
    objs = len(filled(table_rows(section_text(text, "Objection List")))) or \
        len(list_items(section_text(text, "Objection List")))
    gaps = len(list_items(section_text(text, "Opportunity Gaps")))
    urls = set(re.findall(r"https?://\S+", section_text(text, "Sources")))
    srcs = len(urls) or len(list_items(section_text(text, "Sources")))

    checks = [("customer quotes", quotes, req["quotes"]), ("competitors", comps, req["competitors"]),
              ("objections", objs, req["objections"]), ("opportunity gaps", gaps, req["gaps"]),
              ("sources", srcs, req["sources"])]
    for name, have, need in checks:
        status = "ok" if have >= need else "LOW"
        print(f"{status:4} {name}: {have}/{need}")
        if have < need:
            problems.append(f"{name}: {have} found, {need} required ({mode} mode)")

    if problems:
        print("\nRESEARCH GATE: FAIL")
        for pr in problems:
            print(" -", pr)
        print("\nIf web tools are unavailable, gather customer words and competitor facts via the "
              "interview scripts (references/02-research-playbook.md, addendum A) and mark limits "
              "explicitly in the file, then re-run with the user's approval to proceed.")
        sys.exit(1)
    print("\nRESEARCH GATE: PASS")


if __name__ == "__main__":
    main()
