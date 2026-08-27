#!/usr/bin/env python3
"""Refresh the publications block in README.md from the ORCID public API.

Stdlib only — no dependencies, no pip install step in CI.

Fails loudly and non-zero on any error, and never writes a partial or empty
block: a broken run should show up as a red X in Actions, not as a silently
emptied section of the README.
"""

from __future__ import annotations

import json
import sys
import urllib.error
import urllib.request
from pathlib import Path

ORCID = "0000-0003-1129-4676"
README = Path("README.md")
MAX_ITEMS = 6
START = "<!-- PUBLICATIONS:START -->"
END = "<!-- PUBLICATIONS:END -->"
API = f"https://pub.orcid.org/v3.0/{ORCID}/works"
UA = "greensh16-profile-readme (+https://github.com/greensh16)"

# ORCID work types to keep, in the order they should be grouped.
KEEP_TYPES = {
    "journal-article",
    "preprint",
    "book-chapter",
    "conference-paper",
    "software",
    "dataset",
    "report",
}


def fetch_works() -> list[dict]:
    req = urllib.request.Request(
        API, headers={"Accept": "application/json", "User-Agent": UA}
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.load(resp).get("group", [])


def _first(mapping: dict | None, *keys: str):
    """Walk a chain of keys through possibly-null ORCID nesting."""
    node = mapping
    for key in keys:
        if not isinstance(node, dict):
            return None
        node = node.get(key)
    return node


def parse(group: dict) -> dict | None:
    summaries = group.get("work-summary") or []
    if not summaries:
        return None
    # Prefer the summary with the richest metadata (usually a DOI-bearing one).
    summary = max(summaries, key=lambda s: len(json.dumps(s)))

    title = _first(summary, "title", "title", "value")
    if not title:
        return None

    doi = None
    for eid in (_first(summary, "external-ids", "external-id") or []):
        if eid.get("external-id-type") == "doi":
            doi = (eid.get("external-id-value") or "").strip()
            break

    year_raw = _first(summary, "publication-date", "year", "value")
    month_raw = _first(summary, "publication-date", "month", "value")

    return {
        "title": " ".join(title.split()),
        "venue": _first(summary, "journal-title", "value"),
        "type": (summary.get("type") or "").lower(),
        "year": int(year_raw) if (year_raw or "").isdigit() else 0,
        "month": int(month_raw) if (month_raw or "").isdigit() else 0,
        "url": f"https://doi.org/{doi}" if doi else _first(summary, "url", "value"),
    }


def render(items: list[dict]) -> str:
    lines = []
    for item in items:
        title = item["title"]
        heading = f"**[{title}]({item['url']})**" if item["url"] else f"**{title}**"
        meta = " · ".join(
            part
            for part in (
                item["venue"],
                item["type"].replace("-", " ") if item["type"] else None,
                str(item["year"]) if item["year"] else None,
            )
            if part
        )
        lines.append(f"- {heading}" + (f"  \n  <sub>{meta}</sub>" if meta else ""))
    return "\n".join(lines)


def splice(text: str, block: str) -> str:
    try:
        head, rest = text.split(START, 1)
        _, tail = rest.split(END, 1)
    except ValueError:
        sys.exit(f"error: README.md is missing the {START} / {END} markers")
    return f"{head}{START}\n{block}\n{END}{tail}"


def main() -> None:
    try:
        groups = fetch_works()
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as exc:
        sys.exit(f"error: could not read works from ORCID: {exc}")

    items = [parsed for group in groups if (parsed := parse(group))]
    items = [i for i in items if not i["type"] or i["type"] in KEEP_TYPES]
    items.sort(key=lambda i: (i["year"], i["month"], i["title"]), reverse=True)
    items = items[:MAX_ITEMS]

    if not items:
        sys.exit("error: ORCID returned no usable works — refusing to empty the block")

    updated = splice(README.read_text(encoding="utf-8"), render(items))
    README.write_text(updated, encoding="utf-8")
    print(f"wrote {len(items)} item(s) to the publications block")


if __name__ == "__main__":
    main()