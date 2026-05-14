#!/usr/bin/env python3
"""Parse OpenRice explore/chart desktop grid HTML into CSV matching openrice_most_bookmarked_top30.csv columns."""

from __future__ import annotations

import argparse
import csv
import re
import sys
from html import unescape
from pathlib import Path


def _norm_ws(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()


def parse_chart_grid_html(html: str) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    chunks = re.split(
        r'(?=<div class="poi-chart-main-grid-item-desktop-wrapper">)', html
    )
    for ch in chunks:
        if "rank-icon rank-" not in ch:
            continue
        mr = re.search(r"rank-icon rank-(\d+) large", ch)
        if not mr:
            continue
        rank = mr.group(1)
        mname = re.search(
            r'pcmgidtr-left-section-poi-info-name[^>]*>\s*<a[^>]*class="link"[^>]*>([\s\S]*?)</a>',
            ch,
        )
        name = _norm_ws(unescape(mname.group(1))) if mname else ""

        mdet = re.search(
            r'pcmgidtr-left-section-poi-info-details">([\s\S]*?)</div>\s*</div>\s*</div>\s*<div class="pcmgidtr-right-section">',
            ch,
        )
        tag_texts: list[str] = []
        if mdet:
            for ma in re.finditer(
                r'<a[^>]*class="link"[^>]*>([\s\S]*?)</a>', mdet.group(1)
            ):
                tag_texts.append(_norm_ws(unescape(ma.group(1))))
        district = tag_texts[0] if tag_texts else ""
        cuisine_tags = " | ".join(tag_texts[1:]) if len(tag_texts) > 1 else ""

        counts = re.findall(
            r'pcmgidr-face-icon (?:smile|cry)"></div><div class="pcmgidr-count">(\d+)</div>',
            ch,
        )
        smile = counts[0] if len(counts) > 0 else ""
        cry = counts[1] if len(counts) > 1 else ""

        bm = re.search(r'<div class="tbb-count">([^<]+)</div>', ch)
        bookmarks = bm.group(1).strip() if bm else ""

        # Door photo <a> usually has href before class="pcmgidtr-left-section-door-photo"
        hrefm = re.search(
            r'<a href="([^"]+)"[^>]*class="pcmgidtr-left-section-door-photo"', ch
        )
        if not hrefm:
            hrefm = re.search(
                r'class="pcmgidtr-left-section-door-photo"[^>]*href="([^"]+)"', ch
            )
        if not hrefm:
            hrefm = re.search(
                r'pcmgidtr-left-section-poi-info-name[^>]*>\s*<a href="([^"]+)"', ch
            )
        path = hrefm.group(1).strip() if hrefm else ""
        if path.startswith("/"):
            url = "https://www.openrice.com" + path
        else:
            url = path

        rows.append(
            {
                "rank": rank,
                "name": name,
                "district": district,
                "cuisine_tags": cuisine_tags,
                "smile": smile,
                "cry": cry,
                "bookmarks": bookmarks,
                "url": url,
            }
        )
    rows.sort(key=lambda r: int(r["rank"]))
    return rows


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("html_path", type=Path)
    ap.add_argument(
        "-o",
        "--out",
        type=Path,
        default=None,
        help="Write CSV here (default: stdout)",
    )
    args = ap.parse_args()
    html = args.html_path.read_text(encoding="utf-8", errors="replace")
    rows = parse_chart_grid_html(html)
    fieldnames = [
        "rank",
        "name",
        "district",
        "cuisine_tags",
        "smile",
        "cry",
        "bookmarks",
        "url",
    ]
    if args.out:
        f = args.out.open("w", newline="", encoding="utf-8")
    else:
        f = sys.stdout
    try:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(rows)
    finally:
        if args.out:
            f.close()


if __name__ == "__main__":
    main()
