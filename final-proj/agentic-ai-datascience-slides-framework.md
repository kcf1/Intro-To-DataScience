# Slide framework: Agentic AI in data science (OpenRice as example)

**Format:** ~10 minutes · **Angle:** workflow and complementary strengths, not “can you trust the platform?” (see `openrice-proposal.md` for that line of work).

---

## Timing map (target ~10 min)

| Block | Slides (suggested) | Time |
|--------|-------------------|------|
| Hook + framing | 1–2 | ~1:30 |
| Agentic AI in DS (definition) | 1 | ~1:00 |
| OpenRice as running example | 1 | ~1:00 |
| Humans vs AI (complementarity) | 2 | ~2:00 |
| Deep dive: unstructured data | 2 | ~2:00 |
| Deep dive: coding & automation | 2 | ~1:30 |
| Risks, limits, human-in-the-loop | 1 | ~0:30 |
| Close + Q&A buffer | 1 | ~0:30 |

---

## Slide 1 — Title

**Title:** Agentic AI in data science: what changes when the assistant can *act*?  
**Subtitle:** OpenRice as a concrete example (reviews, pages, messy web data).

**Speaker notes:** One sentence: you are not pitching OpenRice trust analysis; you are illustrating how agentic workflows show up in a real DS task.

---

## Slide 2 — Hook: the boring part is the bottleneck

**Bullets:**
- Hypothesis: the *idea* of a study is often quick; the *grunt work* (find data, clean it, wire scripts) dominates calendar time.
- OpenRice: semi-structured HTML, changing layouts, language mix, rate limits — classic “unstructured + engineering” pain.

**Speaker notes:** Bridge to “agentic” = systems that plan, call tools, and iterate (scrape, parse, fix code) rather than only answer one-shot prompts.

---

## Slide 3 — What “agentic AI” means here (tight definition)

**Bullets:**
- **Plan:** break a goal into steps (discover URLs → fetch → parse → validate → store).
- **Act:** run code, hit endpoints or pages, read errors, adjust selectors or logic.
- **Remember (short-term):** carry context across steps in one session.

**Speaker notes:** Avoid vendor jargon; map to familiar DS loop: explore → implement → debug → document.

---

## Slide 4 — OpenRice as the example canvas

**Bullets:**
- **Unstructured inputs:** review text, timestamps, reviewer pages, restaurant metadata.
- **Why it is illustrative:** not a clean CSV drop; judgment + iteration + compliance matter.

**Speaker notes:** Optional one screenshot or diagram of a listing page vs review page (if allowed in deck).

---

## Slide 5 — Where humans still win

**Bullets:**
- **Problem framing:** what should *not* be automated (ethics, ToS, proportionality).
- **Domain sense:** what “good” data looks like for Cantonese/mixed text; what failure modes matter.
- **Interpretation:** turning patterns into claims; responsibility for conclusions.

**Speaker notes:** This slide earns trust with instructors; it shows you are not “AI replaces scientists.”

---

## Slide 6 — Where agentic AI wins (overview)

**Bullets:**
- **Throughput:** many variants of parsers, schemas, and checks in one sitting.
- **Consistency:** repeatable extraction rules once validated.
- **Pairing:** accelerates the coding layer so humans spend time on questions, not boilerplate.

**Speaker notes:** Preview the next two slides as the “main part.”

---

## Slide 7 — Main part A: power on unstructured data (OpenRice-shaped)

**Bullets:**
- **Navigation of mess:** HTML quirks, pagination, inconsistent fields — rapid prototyping of extractors.
- **Cleaning glue:** regex / parsers / normalization pipelines; quick experiments on sample pages.
- **Scale (with guardrails):** batching, logging, deduplication, schema drift detection.

**Speaker notes:** One concrete mini-story: “first pass missed timestamps → agent proposes patch → re-run on subset → human approves schema.”

---

## Slide 8 — Main part A (optional split): multilingual & text-heavy edge

**Bullets:**
- Reviews mix languages and informal phrasing; agents help scaffold NLP steps (tokenization, labeling helpers), humans validate labels and claims.

**Speaker notes:** Keep high level unless you demo code; this slide can merge into Slide 7 if you need to save time.

---

## Slide 9 — Main part B: power on coding & integration

**Bullets:**
- **Pipeline code:** fetch → parse → `pandas` / DB → QC plots.
- **Debugging loops:** stack traces → hypothesized fix → rerun tests.
- **Reproducibility:** project layout, configs, small CLI or notebook boundaries.

**Speaker notes:** Emphasize *iteration speed* and *testable units* (functions for parse, not one giant script).

---

## Slide 10 — Main part B (optional): “agent as junior engineer”

**Bullets:**
- Writes first drafts of tests, docstrings, and data contracts.
- Human reviews merges the same way as a PR from a teammate.

**Speaker notes:** If short on time, fold this into Slide 9.

---

## Slide 11 — Risks & how you stay in control

**Bullets:**
- Legal/ethical: scraping policies, robots, personal data minimization.
- Technical: silent data corruption beats loud failure — QC checks and spot audits.
- Scientific: automation amplifies wrong assumptions faster.

**Speaker notes:** One line: agentic AI is a *force multiplier*; it multiplies good and bad workflows.

---

## Slide 12 — Close: the punchline

**Bullets:**
- **AI:** excels at unstructured ingestion + code iteration under human-defined constraints.
- **Human:** excels at defining the question, the ethics, and the evidentiary bar.
- **OpenRice:** a small but vivid instance of why agentic tooling is entering DS practice.

**Speaker notes:** Invite one question; keep Q&A in the buffer minute.

---

## Assets you might add (optional)

- Simple **diagram:** human (goal, constraints) ↔ agent (tools: browser, terminal, files) ↔ data store.
- **One** before/after: time to first clean table with vs without agent assist (even rough, honest estimate).

---

## File purpose

This document is a **slide outline and speaker-note skeleton** for a ~10-minute presentation on **agentic AI in data science**, using **OpenRice** only as a motivating example of unstructured web + text work — distinct from the drafted project proposal’s focus on platform trust and fake-review signals.
