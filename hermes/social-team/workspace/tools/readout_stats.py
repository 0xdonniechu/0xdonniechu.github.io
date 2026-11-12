#!/usr/bin/env python3
"""Weekly readout numbers for Team Social (Xaiyan, skill measurement-loop).

The agent never computes medians or rates by hand: it copies the owner's
exports into one CSV and runs this script, then pastes the tables it prints.
Standard library only; reads one local file; no network.

CSV columns (one row per published post, each platform + post_id once):
  platform, post_id, boosted (yes/no, never blank), then any number columns
  such as reach, impressions, engagements, followers, views, saves, shares.
Numbers are whole numbers written plainly: 1200, not 1.200 or 1,200
(the dot and the comma mean different things in vi-VN and en-US, so both
are refused). A column named with --decimal may use one dot as decimal
point (watch time 12.5). An empty cell means "no number": left out, never
guessed. Numbers are never negative: a net change (followers gained minus
lost) goes in as two columns, gained and lost.

Usage:
  python3 tools/readout_stats.py work/numbers-2026-W46.csv \
      --rate ERR=engagements/reach --rate ERI=engagements/impressions [--top 3]

Each --rate is one entry of the locked metric dictionary: NAME=numerator/denominator.
The first --rate ranks best and worst posts (organic only).
"""

import argparse
import csv
import re
import statistics
import sys

REQUIRED = ("platform", "post_id", "boosted")
YES = {"yes", "y", "true", "1", "có", "co"}
NO = {"no", "n", "false", "0", "không", "khong"}
WHOLE = re.compile(r"^[0-9]+$")
DECIMAL = re.compile(r"^[0-9]+(\.[0-9]+)?$")


class InputError(Exception):
    pass


def parse_rate(text):
    try:
        name, formula = text.split("=", 1)
        num, den = formula.split("/", 1)
    except ValueError:
        raise argparse.ArgumentTypeError(f"rate must look like NAME=numerator/denominator, got {text!r}")
    name, num, den = name.strip(), num.strip(), den.strip()
    if not (name and num and den):
        raise argparse.ArgumentTypeError(f"rate must look like NAME=numerator/denominator, got {text!r}")
    return name, num, den


def positive_int(text):
    value = int(text)
    if value < 1:
        raise argparse.ArgumentTypeError("--top must be 1 or more")
    return value


def to_number(cell, decimal):
    cell = (cell or "").strip()
    if cell == "":
        return None
    if WHOLE.match(cell) or (decimal and DECIMAL.match(cell)):
        return float(cell)
    hint = "a plain non-negative number with one dot" if decimal else "a plain whole number (1200, not 1.200 or 1,200)"
    raise ValueError(hint)


def load(path, decimal_columns):
    with open(path, newline="", encoding="utf-8-sig") as f:
        reader = csv.reader(f)
        try:
            header = [h.strip() for h in next(reader)]
        except StopIteration:
            raise InputError(f"{path}: empty file")
        if any(h == "" for h in header):
            raise InputError(f"{path}: a column has no name (check for a trailing comma in the header)")
        dupes = sorted({h for h in header if header.count(h) > 1})
        if dupes:
            raise InputError(f"{path}: repeated column(s) {', '.join(dupes)}")
        missing = [c for c in REQUIRED if c not in header]
        if missing:
            raise InputError(f"{path}: missing column(s) {', '.join(missing)}")
        unknown = [c for c in decimal_columns if c not in header]
        if unknown:
            raise InputError(f"--decimal column(s) not in the CSV: {', '.join(unknown)}")
        rows, seen = [], {}
        for line_no, cells in enumerate(reader, start=2):
            if not any(c.strip() for c in cells):
                continue
            if len(cells) != len(header):
                raise InputError(f"{path}:{line_no}: {len(cells)} cells, header has {len(header)}")
            row = dict(zip(header, (c.strip() for c in cells)))
            row["platform"] = row["platform"].lower()
            if not row["platform"] or not row["post_id"]:
                raise InputError(f"{path}:{line_no}: platform and post_id must not be blank")
            key = (row["platform"], row["post_id"])
            if key in seen:
                raise InputError(f"{path}:{line_no}: post {key[1]} on {key[0]} already on line {seen[key]}")
            seen[key] = line_no
            boosted = row["boosted"].lower()
            if boosted in YES:
                row["boosted"] = True
            elif boosted in NO:
                row["boosted"] = False
            else:
                raise InputError(f"{path}:{line_no}: boosted must be yes or no, got {row['boosted']!r}")
            numbers = {}
            for key_name in header:
                if key_name in REQUIRED:
                    continue
                try:
                    numbers[key_name] = to_number(row[key_name], key_name in decimal_columns)
                except ValueError as e:
                    raise InputError(f"{path}:{line_no}: column {key_name!r} must be {e}, got {row[key_name]!r}")
            row["numbers"] = numbers
            rows.append(row)
    return header, rows


def rate_of(row, num, den):
    """Return (value, problem); problem is 'missing' or 'zero' when value is None."""
    a, b = row["numbers"].get(num), row["numbers"].get(den)
    if a is None or b is None:
        return None, "missing"
    if b == 0:
        return None, "zero"
    return a / b, None


def fmt(value, is_rate, decimal=False):
    if value is None:
        return "không có số"
    if is_rate:
        return f"{value * 100:.2f}%"
    if decimal:
        return f"{value:,.2f}"
    # a median of whole numbers can end in .5; show it instead of rounding it away
    return f"{value:,.0f}" if value == int(value) else f"{value:,.1f}"


def cell(text):
    """Keep pasted text from breaking a Markdown table row."""
    return text.replace("|", "\\|").replace("\n", " ")


def readout(rows, rates, count_columns, top, decimal_columns=frozenset()):
    for name, num, den in rates:
        for col in (num, den):
            if col not in count_columns:
                raise InputError(f"rate {name}: column {col!r} is not in the CSV")
    platforms = sorted({r["platform"] for r in rows})
    out = ["## Từ điển chỉ số (khoá)"]
    out.extend(f"- **{name}** = {num} ÷ {den}" for name, num, den in rates)
    out.append("")
    out.append("## Trung vị theo nền tảng")
    head = ["Nền tảng", "Loại", "Số bài"] + [n for n, _, _ in rates] + count_columns
    out.append("| " + " | ".join(cell(h) for h in head) + " |")
    out.append("|" + "---|" * len(head))
    notes = []
    for platform in platforms:
        for boosted in (False, True):
            group = [r for r in rows if r["platform"] == platform and r["boosted"] == boosted]
            if not group:
                continue
            kind = "quảng cáo" if boosted else "tự nhiên"
            cells = [cell(platform), kind, str(len(group))]
            for name, num, den in rates:
                results = [rate_of(r, num, den) for r in group]
                values = [v for v, _ in results if v is not None]
                cells.append(fmt(statistics.median(values), True) if values else fmt(None, True))
                n_missing = sum(1 for _, p in results if p == "missing")
                n_zero = sum(1 for _, p in results if p == "zero")
                if n_missing:
                    notes.append(f"{platform} {kind}: {name} thiếu số ở {n_missing}/{len(group)} bài")
                if n_zero:
                    notes.append(f"{platform} {kind}: {name} có {den} = 0 ở {n_zero}/{len(group)} bài, bỏ khỏi trung vị")
                over = [r["post_id"] for r in group if (rate_of(r, num, den)[0] or 0) > 1]
                if over:
                    notes.append(f"{platform} {kind}: {name} trên 100% ở {', '.join(over)}; kiểm lại số trước khi dùng")
            for col in count_columns:
                values = [r["numbers"][col] for r in group if r["numbers"].get(col) is not None]
                cells.append(fmt(statistics.median(values), False, col in decimal_columns) if values else fmt(None, False))
            out.append("| " + " | ".join(cells) + " |")
    out.append("")
    if rates:
        name, num, den = rates[0]
        out.append(f"## Tốt nhất và kém nhất theo {name} (chỉ bài tự nhiên)")
        for platform in platforms:
            organic = [r for r in rows if r["platform"] == platform and not r["boosted"]]
            if not organic:
                out.append(f"- {platform}: chỉ có bài quảng cáo, không xếp hạng")
                continue
            scored = sorted(((rate_of(r, num, den)[0], r["post_id"]) for r in organic
                             if rate_of(r, num, den)[0] is not None), key=lambda s: (-s[0], s[1]))
            k = min(top, len(scored) // 2)
            if k == 0:
                out.append(f"- {platform}: {len(scored)} bài có {name}, quá ít để xếp hạng")
                continue
            best = ", ".join(f"{cell(pid)} ({fmt(v, True)})" for v, pid in scored[:k])
            worst = ", ".join(f"{cell(pid)} ({fmt(v, True)})" for v, pid in reversed(scored[-k:]))
            out.append(f"- {platform}: tốt nhất {best}; kém nhất {worst}")
        out.append("")
    small = [p for p in platforms if sum(1 for r in rows if r["platform"] == p and not r["boosted"]) < 5]
    if notes or small:
        out.append("## Thiếu số, số lạ và mẫu nhỏ")
        out.extend(f"- {n}" for n in notes)
        out.extend(f"- {p}: dưới 5 bài tự nhiên, chưa đủ để gọi là xu hướng" for p in small)
        out.append("")
    return "\n".join(out)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("csv")
    parser.add_argument("--rate", action="append", type=parse_rate, default=[],
                        help="NAME=numerator/denominator, repeatable; the first one ranks posts")
    parser.add_argument("--decimal", action="append", default=[],
                        help="column that may hold a decimal with a dot (e.g. watch_time), repeatable")
    parser.add_argument("--top", type=positive_int, default=3, help="best and worst posts per platform (default 3)")
    args = parser.parse_args(argv)
    try:
        header, rows = load(args.csv, set(args.decimal))
        if not rows:
            raise InputError(f"{args.csv}: no rows")
        count_columns = [h for h in header if h not in REQUIRED]
        print(readout(rows, args.rate, count_columns, args.top, set(args.decimal)))
    except InputError as e:
        print(f"error: {e}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
