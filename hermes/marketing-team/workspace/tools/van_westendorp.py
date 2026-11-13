#!/usr/bin/env python3
# Modified from Jakeschincariol/founder-skill `skills/founder-pricing/van_westendorp.py` @ fd9385b (MIT) by 0xdonniechu, 2026-11-13
"""Price sensitivity (Van Westendorp) for real survey answers. Standard library only.

Every respondent answers four questions: at what price would it be too cheap to
trust, a bargain, getting expensive, and too expensive to buy. Plotted
together, those four answers give you an acceptable price range and the price
that leaves the fewest people unhappy.

    python3 van_westendorp.py price_survey_example.csv
    python3 van_westendorp.py survey.csv --currency VND --price 99000
    python3 van_westendorp.py survey.csv --out work/pricing-curve.md
    python3 van_westendorp.py survey.csv --json

Input is a CSV with the columns too_cheap, cheap, expensive, too_expensive (one
row per respondent; extra columns are ignored). Prices are plain numbers in any
currency: 99000 for VND, 6.5 for dollars. A thousands separator (99,000 or
99.000) is refused, because the dot and the comma mean different things in
vi-VN and en-US: write 99000. A respondent missing any of the four numbers, or
giving them out of order (too cheap must be the lowest, too expensive the
highest), is dropped and counted. Fewer than 10 usable respondents is refused.

`price_survey_example.csv` next to this file is FICTIONAL (20 invented
respondents, in VND), only there to show the format and to run the tool. It is
not market evidence.

The four points it reports:

    PMC  point of marginal cheapness   below this, too many think it's too cheap
    PME  point of marginal expensiveness above this, too many think it's too expensive
    OPP  optimal price point            as many say "too cheap" as "too expensive"
    IPP  indifference price point       as many say "a bargain" as "expensive"

PMC to PME is the acceptable range. Use the range to choose what to TEST, then
test it with real buyers.
"""

import argparse
import csv
import json
import re
import sys
from collections import Counter

KEYS = ("too_cheap", "cheap", "expensive", "too_expensive")
MIN_ROWS = 10
CLUMP_SHARE = 0.5      # one value given by half the people or more: warn
MIN_DISTINCT = 5       # fewer different values than this in one column: warn
NUMBER = re.compile(r"^-?[0-9]+(\.[0-9]+)?$")
DOT_THOUSANDS = re.compile(r"^-?[0-9]+\.[0-9]{3}$")


class PricingError(Exception):
    pass


def _f(v, line, key):
    s = (v or "").strip()
    if "," in s or DOT_THOUSANDS.match(s):
        raise PricingError("line %d, %s: %r has a thousands separator or an unclear dot; "
                           "write the price as a plain number (99000, or 6.5 for a decimal)" % (line, key, s))
    if not NUMBER.match(s):
        return None
    x = float(s)
    return x if x > 0 else None


def read(path):
    """Return (rows, dropped) where rows are (too_cheap, cheap, expensive, too_expensive)."""
    if not path.endswith(".csv"):
        raise PricingError("give a .csv file")
    raw = []
    with open(path, newline="", encoding="utf-8-sig") as fh:
        reader = csv.DictReader(fh)
        header = [h.strip() for h in (reader.fieldnames or [])]
        missing = [k for k in KEYS if k not in header]
        if missing:
            raise PricingError("%s: missing column(s) %s (need %s)" % (path, ", ".join(missing), ", ".join(KEYS)))
        for r in reader:
            r = {(k or "").strip(): v for k, v in r.items()}
            raw.append(tuple(_f(r.get(k), reader.line_num, k) for k in KEYS))
    rows, dropped = [], 0
    for r in raw:
        if r is None or any(v is None for v in r) or not (r[0] <= r[1] <= r[2] <= r[3]):
            dropped += 1
            continue
        rows.append(r)
    return rows, dropped


def curves(rows, grid):
    n = float(len(rows))
    tc = [sum(1 for r in rows if r[0] >= p) / n for p in grid]          # too cheap at p (falls)
    ch = [sum(1 for r in rows if r[1] >= p) / n for p in grid]          # a bargain at p (falls)
    ex = [sum(1 for r in rows if r[2] <= p) / n for p in grid]          # expensive at p (rises)
    te = [sum(1 for r in rows if r[3] <= p) / n for p in grid]          # too expensive at p (rises)
    return tc, ch, ex, te


def cross(grid, falling, rising):
    """First price where the rising curve meets the falling one (linear interpolation)."""
    for i in range(1, len(grid)):
        d0 = rising[i - 1] - falling[i - 1]
        d1 = rising[i] - falling[i]
        if d0 <= 0 <= d1 and d1 != d0:
            t = -d0 / (d1 - d0)
            return grid[i - 1] + t * (grid[i] - grid[i - 1])
        if d0 == 0:
            return grid[i - 1]
    return None


def analyse(rows, step=None, dropped=0):
    if len(rows) < MIN_ROWS:
        raise PricingError("không đủ câu trả lời: need at least %d complete answers, got %d%s" % (
            MIN_ROWS, len(rows), (" (%d dropped as incomplete or out of order)" % dropped) if dropped else ""))
    lo = min(r[0] for r in rows)
    hi = max(r[3] for r in rows)
    step = step or max(0.01, round((hi - lo) / 400, 2))
    grid, p = [], lo
    while p <= hi + 1e-9:
        grid.append(round(p, 4))
        p += step
    tc, ch, ex, te = curves(rows, grid)
    not_cheap = [1 - v for v in ch]
    not_exp = [1 - v for v in ex]
    pts = {
        "PMC": cross(grid, tc, not_cheap),
        "PME": cross(grid, not_exp, te),
        "OPP": cross(grid, tc, te),
        "IPP": cross(grid, ch, ex),
    }
    whole = all(v == int(v) for r in rows for v in r)
    # answers bunched on one round number make the curves steps; a crossing can then land on that number
    # so do answers spread over only a few values: the curves jump, with flat gaps between the steps
    clumped = [k for i, k in enumerate(KEYS)
               if max(Counter(r[i] for r in rows).values()) >= CLUMP_SHARE * len(rows)
               or len(set(r[i] for r in rows)) < MIN_DISTINCT]
    return {"n": len(rows), "points": pts, "range": [pts["PMC"], pts["PME"]], "whole": whole, "clumped": clumped,
            "median": {k: sorted(r[i] for r in rows)[len(rows) // 2] for i, k in enumerate(KEYS)}}


def report(res, dropped, price=None, currency="đ"):
    def m(v):
        if v is None:
            return "n/a"
        return ("{:,.0f}" if res["whole"] else "{:,.2f}").format(v) + " " + currency
    p = res["points"]
    L = ["# Price sensitivity", "",
         "Respondents: %d with four complete answers in order%s. The range is only as good as who was asked: "
         "check that they are people who would buy." % (
             res["n"], (", %d more dropped (incomplete or out of order)" % dropped) if dropped else ""), "",
         "| point | price | what it means |", "| --- | ---: | --- |",
         "| PMC | %s | below this, too many think it is too cheap to be good |" % m(p["PMC"]),
         "| OPP | %s | as many say too cheap as too expensive: the least resistance |" % m(p["OPP"]),
         "| IPP | %s | as many call it a bargain as call it expensive |" % m(p["IPP"]),
         "| PME | %s | above this, too many say it is too expensive to buy |" % m(p["PME"]), "",
         "**Acceptable range: %s to %s.**" % (m(p["PMC"]), m(p["PME"])), ""]
    md = res["median"]
    L.append("Median answers: too cheap %s, a bargain %s, getting expensive %s, too expensive %s." % (
        m(md["too_cheap"]), m(md["cheap"]), m(md["expensive"]), m(md["too_expensive"])))
    if price is not None and p["PMC"] is not None and p["PME"] is not None:
        where = "inside" if p["PMC"] <= price <= p["PME"] else ("below" if price < p["PMC"] else "above")
        L += ["", "Your current price, %s, is **%s** the acceptable range." % (m(price), where)]
    if res["clumped"]:
        L += ["", "**Warning: answers bunch on a few values** (%s: at least %d%% of people gave the same number, "
              "or fewer than %d different numbers were given). "
              "The curves are steps, so the range can land on that number itself. Read it as rough, and do not "
              "change a price on this run alone: ask more people, or compare with the median answers above." % (
                  ", ".join(res["clumped"]), round(CLUMP_SHARE * 100), MIN_DISTINCT)]
    return "\n".join(L) + "\n"


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("source", help="the survey CSV (too_cheap, cheap, expensive, too_expensive)")
    ap.add_argument("--currency", default="đ", help="label shown after every price (default: đ)")
    ap.add_argument("--price", type=float, help="your current price, to place it on the range")
    ap.add_argument("--out", help="write the report here (markdown)")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args(argv)
    try:
        rows, dropped = read(a.source)
        res = analyse(rows, dropped=dropped)
    except (PricingError, OSError, UnicodeDecodeError) as e:
        print("error: %s" % e, file=sys.stderr)
        return 2
    if a.json:
        print(json.dumps(dict(res, dropped=dropped, currency=a.currency), indent=1))
        return 0
    text = report(res, dropped, a.price, a.currency)
    if a.out:
        try:
            with open(a.out, "w", encoding="utf-8") as fh:
                fh.write(text)
        except OSError as e:
            print("error: cannot write %s: %s" % (a.out, e.strerror or e), file=sys.stderr)
            return 2
        print("wrote %s" % a.out)
    else:
        sys.stdout.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
