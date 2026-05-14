#!/usr/bin/env python3
"""Flatten working/data/json/*_google_serp.json into one row-wise CSV."""

from __future__ import annotations

import csv
import json
from pathlib import Path


def row_from_doc(doc: dict) -> dict:
    o = doc.get("openrice") or {}
    g = doc.get("google_local_knowledge_panel") or {}
    if isinstance(g, dict) and g.get("found") is False:
        return {
            "restaurant": doc.get("restaurant", ""),
            "source_html": doc.get("source_html", ""),
            "openrice_rank": o.get("rank", ""),
            "openrice_district": o.get("district", ""),
            "openrice_cuisine_tags": o.get("cuisine_tags", ""),
            "openrice_smile": o.get("smile", ""),
            "openrice_cry": o.get("cry", ""),
            "openrice_bookmarks": o.get("bookmarks", ""),
            "openrice_url": o.get("url", ""),
            "google_extracted": "0",
            "google_name": "",
            "google_rating": "",
            "google_rating_out_of": "",
            "google_review_count": "",
            "google_category": "",
            "google_price_range_text": "",
            "google_hours_status": "",
            "google_place_fid": "",
            "google_not_found_reason": g.get("reason", ""),
            "google_detected_source": g.get("detected_source", ""),
        }
    return {
        "restaurant": doc.get("restaurant", ""),
        "source_html": doc.get("source_html", ""),
        "openrice_rank": o.get("rank", ""),
        "openrice_district": o.get("district", ""),
        "openrice_cuisine_tags": o.get("cuisine_tags", ""),
        "openrice_smile": o.get("smile", ""),
        "openrice_cry": o.get("cry", ""),
        "openrice_bookmarks": o.get("bookmarks", ""),
        "openrice_url": o.get("url", ""),
        "google_extracted": "1",
        "google_name": g.get("name") or "",
        "google_rating": g.get("rating", ""),
        "google_rating_out_of": g.get("rating_out_of", ""),
        "google_review_count": g.get("review_count", ""),
        "google_category": g.get("category") or "",
        "google_price_range_text": g.get("price_range_text") or "",
        "google_hours_status": g.get("hours_status") or "",
        "google_place_fid": g.get("place_fid") or "",
        "google_not_found_reason": "",
        "google_detected_source": "",
    }


FIELDNAMES = [
    "restaurant",
    "source_html",
    "openrice_rank",
    "openrice_district",
    "openrice_cuisine_tags",
    "openrice_smile",
    "openrice_cry",
    "openrice_bookmarks",
    "openrice_url",
    "google_extracted",
    "google_name",
    "google_rating",
    "google_rating_out_of",
    "google_review_count",
    "google_category",
    "google_price_range_text",
    "google_hours_status",
    "google_place_fid",
    "google_not_found_reason",
    "google_detected_source",
]


def main() -> None:
    root = Path(__file__).resolve().parent
    json_dir = root / "json"
    out_csv = root / "google_serp_top30_from_json.csv"

    paths = sorted(json_dir.glob("*_google_serp.json"))
    rows = []
    for p in paths:
        doc = json.loads(p.read_text(encoding="utf-8"))
        rows.append(row_from_doc(doc))

    out_csv.parent.mkdir(parents=True, exist_ok=True)
    with out_csv.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDNAMES, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)

    print(f"Wrote {len(rows)} rows to {out_csv}")


if __name__ == "__main__":
    main()
