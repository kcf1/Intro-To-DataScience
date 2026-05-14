#!/usr/bin/env python3
"""
Save Google web-search HTML for restaurant names (Chrome).

Use this when you need Google’s own results (e.g. links to Google Maps / review pages).
DuckDuckGo is not used: it does not expose Google’s review UI or the same result set.

Blocked Google pages (\"unusual traffic\" / reCAPTCHA) are not written as the main .html file;
instead a .blocked.html sidecar is written and the run reports BLOCKED for that name.

Requires: Chrome; `pip install -r requirements-selenium-google.txt` (undetected-chromedriver recommended).

By default the browser window is visible and the script waits ~5s after each results page loads
(`--settle`); use `--headless` only if you explicitly want no window.
"""

from __future__ import annotations

import argparse
import csv
import random
import sys
import time
from pathlib import Path
from typing import Any
from urllib.parse import quote_plus

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def safe_filename(name: str, max_len: int = 180) -> str:
    illegal = set('<>:"/\\|?*&\n\r\t')
    out = "".join(c if c not in illegal and ord(c) >= 32 else "_" for c in name)
    out = out.strip(" .")
    if len(out) > max_len:
        out = out[:max_len].rstrip(" .")
    return out or "unnamed"


def google_search_url(query: str) -> str:
    return "https://www.google.com/search?hl=en&gbv=1&q=" + quote_plus(query)


def is_google_blocked(html: str) -> bool:
    low = html.lower()
    return (
        "unusual traffic" in low
        or 'id="captcha-form"' in low
        or "g-recaptcha" in low and "our systems have detected" in low
    )


def google_serp_ready(driver: Any, timeout: float = 25.0) -> str:
    """Wait for either real SERP or a known block page. Returns 'ok', 'blocked', or 'timeout'."""
    end = time.time() + timeout
    while time.time() < end:
        src = driver.page_source
        if is_google_blocked(src):
            return "blocked"
        # Main organic results container (desktop)
        if 'id="rso"' in src or "id='rso'" in src or 'id="center_col"' in src:
            return "ok"
        # Consent / interstitial sometimes precedes results
        if "before you continue" in src.lower() or "consent.google.com" in src.lower():
            try_click_consent(driver)
        time.sleep(0.35)
    return "timeout"


def try_click_consent(driver: Any) -> None:
    """Best-effort: accept all / agree on Google consent dialogs."""
    for sel in (
        "button#L2AGLb",  # "Accept all" (EU)
        "form[action*='consent'] button",
        "button[aria-label*='Accept']",
    ):
        try:
            els = driver.find_elements(By.CSS_SELECTOR, sel)
            for e in els:
                if e.is_displayed():
                    e.click()
                    time.sleep(1.0)
                    return
        except Exception:
            pass


def build_driver_google(headless: bool, user_data_dir: Path | None) -> Any:
    """Prefer undetected-chromedriver; fall back to patched Selenium Chrome."""
    try:
        import undetected_chromedriver as uc

        opts = uc.ChromeOptions()
        opts.add_argument("--window-size=1400,900")
        opts.add_argument("--lang=en-GB")
        if not headless:
            opts.add_argument("--start-maximized")
        if headless:
            opts.add_argument("--headless=new")
        if user_data_dir is not None:
            opts.add_argument(f"--user-data-dir={user_data_dir.resolve()}")
        try:
            return uc.Chrome(options=opts, use_subprocess=True)
        except Exception as e1:
            print(f"WARN: uc.Chrome(options=...) failed ({e1}); trying bare uc.Chrome().", file=sys.stderr)
            try:
                return uc.Chrome(headless=headless, use_subprocess=True)
            except Exception as e2:
                print(f"WARN: uc.Chrome() failed ({e2}); using stock Chrome.", file=sys.stderr)
    except ImportError as e:
        print(f"WARN: undetected_chromedriver not importable ({e}); using stock Chrome.", file=sys.stderr)

    opts = Options()
    if not headless:
        opts.add_argument("--start-maximized")
    if headless:
        opts.add_argument("--headless=new")
    opts.add_argument("--disable-gpu")
    opts.add_argument("--no-sandbox")
    opts.add_argument("--window-size=1400,900")
    opts.add_argument("--lang=en-GB")
    opts.add_argument(
        "--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
    )
    opts.add_argument("--disable-blink-features=AutomationControlled")
    opts.add_experimental_option("excludeSwitches", ["enable-automation"])
    opts.add_experimental_option("useAutomationExtension", False)
    if user_data_dir is not None:
        opts.add_argument(f"--user-data-dir={user_data_dir.resolve()}")

    driver = webdriver.Chrome(options=opts)
    driver.execute_cdp_cmd(
        "Page.addScriptToEvaluateOnNewDocument",
        {
            "source": "Object.defineProperty(navigator, 'webdriver', {get: () => undefined});",
        },
    )
    return driver


def fetch_html_google(driver: Any, query: str, settle_s: float) -> tuple[str, str]:
    """
    Returns (status, html) where status is 'ok', 'blocked', or 'timeout'.
    """
    url = google_search_url(query)
    driver.get("https://www.google.com/")
    time.sleep(0.8 + random.random() * 0.5)
    try_click_consent(driver)
    driver.get(url)
    time.sleep(max(0.0, settle_s))
    try_click_consent(driver)
    state = google_serp_ready(driver, timeout=25.0)
    html = driver.page_source
    if state == "ok" and not is_google_blocked(html):
        return "ok", html
    if state == "blocked" or is_google_blocked(html):
        return "blocked", html
    return "timeout", html


def names_from_csv(path: Path, column: str, limit: int | None) -> list[str]:
    rows: list[str] = []
    with path.open(encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        if column not in (reader.fieldnames or []):
            raise SystemExit(f"CSV has no column {column!r}; columns: {reader.fieldnames}")
        for row in reader:
            v = (row.get(column) or "").strip()
            if v:
                rows.append(v)
            if limit is not None and len(rows) >= limit:
                break
    return rows


def main() -> None:
    p = argparse.ArgumentParser(description="Save Google search HTML for restaurant name queries.")
    p.add_argument("names", nargs="*", help="Restaurant names (if not using --from-csv).")
    p.add_argument("--from-csv", type=Path, metavar="PATH", help="Read names from CSV.")
    p.add_argument("--csv-column", default="name", help="Column for --from-csv.")
    p.add_argument("--limit", type=int, default=None, help="Max rows for --from-csv.")
    p.add_argument(
        "--out-dir",
        type=Path,
        default=Path(__file__).resolve().parent / "web",
        help="Output directory (default: working/web).",
    )
    p.add_argument(
        "--query-suffix",
        default=" restaurant Hong Kong",
        help="Appended to each name for the query.",
    )
    p.add_argument(
        "--delay-min",
        type=float,
        default=5.0,
        help="Min seconds between restaurant queries (after saving HTML).",
    )
    p.add_argument(
        "--delay-max",
        type=float,
        default=7.0,
        help="Max seconds between restaurant queries (after saving HTML).",
    )
    p.add_argument(
        "--settle",
        type=float,
        default=5.0,
        help="Seconds to wait after opening the Google results URL so the page can load.",
    )
    p.add_argument(
        "--headless",
        action="store_true",
        help="Run Chrome without a window (default: visible browser). More likely to hit CAPTCHA.",
    )
    p.add_argument(
        "--user-data-dir",
        type=Path,
        default=None,
        metavar="DIR",
        help="Persistent Chrome profile dir (can reduce Google challenges when reused).",
    )
    p.add_argument("--dry-run", action="store_true")
    p.add_argument("--skip-existing", action="store_true")
    args = p.parse_args()

    if args.from_csv:
        names = names_from_csv(args.from_csv, args.csv_column, args.limit)
    else:
        names = [n.strip() for n in args.names if n.strip()]

    if not names:
        p.error("Provide names or --from-csv.")

    out_dir: Path = args.out_dir
    out_dir.mkdir(parents=True, exist_ok=True)

    if args.dry_run:
        for name in names:
            q = (name + args.query_suffix).strip()
            fn = safe_filename(name) + ".html"
            print(f"{fn}\t{google_search_url(q)}")
        return

    driver = build_driver_google(args.headless, args.user_data_dir)
    if not args.headless:
        print("Chrome: visible window (default). Use --headless to hide it.", flush=True)

    try:
        last = len(names) - 1
        for i, name in enumerate(names):
            fname = safe_filename(name) + ".html"
            out_path = out_dir / fname
            blocked_path = out_dir / (safe_filename(name) + ".blocked.html")

            if args.skip_existing and out_path.is_file():
                print(f"[{i + 1}/{len(names)}] skip (exists): {out_path.name}", flush=True)
                continue

            q = (name + args.query_suffix).strip()
            print(f"[{i + 1}/{len(names)}] google {name!r}", flush=True)

            try:
                status, html = fetch_html_google(driver, q, args.settle)
            except Exception as e:
                print(f"ERROR {name!r}: {e}", file=sys.stderr, flush=True)
                continue

            if status == "ok":
                out_path.write_text(html, encoding="utf-8")
                if blocked_path.exists():
                    blocked_path.unlink(missing_ok=True)
                print(f"  wrote {out_path} ({len(html)} bytes)", flush=True)
            else:
                blocked_path.write_text(html, encoding="utf-8")
                print(
                    f"  BLOCKED ({status}) — wrote {blocked_path.name}. "
                    "Try: do not pass --headless (visible Chrome is default), use --user-data-dir with a logged-in profile, "
                    "or install undetected-chromedriver.",
                    file=sys.stderr,
                    flush=True,
                )

            if i < last:
                time.sleep(random.uniform(args.delay_min, args.delay_max))
    finally:
        driver.quit()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nInterrupted.", file=sys.stderr)
        sys.exit(130)
