#!/usr/bin/env python3
# Parts adapted from Jakeschincariol/founder-skill `skills/founder-cfo/unit_economics.py` @ fd9385b (MIT)
# (structure, money formatting, error style, the what-if idea). The subscription maths below is new code by 0xdonniechu, 2026-11-13.
"""Unit economics of a monthly subscription business. Standard library only, no network.

Takes one JSON file and prints what one paying user earns each month after every
cost that grows with users (variable cost, payment fee, the free-tier load,
partner commission), how long a user stays, what a user is worth over that
life, how many paying users cover the fixed costs, and what the next months look
like for a plan of new paying users.

    python3 saas_economics.py saas_example.json
    python3 saas_economics.py saas_example.json --out work/economics.md
    python3 saas_economics.py saas_example.json --json
    python3 saas_economics.py saas_example.json --price 0.9 --churn 0.08 --volume 0.8

`saas_example.json` next to this file is FICTIONAL ("Ví dụ (số giả)", in VND).

The input. Every field is required unless marked optional; a missing field is an
error, never a default guess:

    business           name, for the report
    currency           label shown after money, e.g. "đ"
    months             length of the plan in months (optional, default 12)
    plans              [{name, price_month, mix, variable_month}]
                         price_month     price of one month, before tax
                         mix             share of paying users on this plan; all mixes sum to 1
                         variable_month  [{label, cost}] cost of ONE paying user for ONE month
                                         (AI cost, hosting, ...)
    payment_fee_rate   share of the price taken by the payment provider, e.g. 0.02
                       (optional; if absent it counts as 0 and the report says "not given")
    free               optional; absent means no free tier
                         users_per_paying  free users carried for each paying user
                         cost_month        cost of one free user for one month
    partner            optional; absent means no partners
                         share_of_new      share of NEW paying users who come through partners
                         commission_rate   share of the price paid to the partner
                         commission_months how many months the partner is paid (whole number)
    monthly_churn      share of paying users lost each month, above 0 up to 1
    fixed_monthly      [{label, cost}] paid every month whatever you sell (may be [])
    startup            [{label, cost}] one-off spend before the first month (may be [])
    new_paying_per_month  `months` numbers: new paying users in each month

How the months are rolled forward (so every number can be checked by hand):

    churned in a month = users at the start of the month x monthly_churn
    end users          = start + new - churned
    users who pay      = end users (a new user pays the month they join; a
                         user who churns does not pay the month they leave)
    mean stay          = 1 / monthly_churn months, which is what this gives

Partner commission is paid on the price for the first `commission_months`
months of each partner-referred user, and only while that user is still there:
on average (1 - (1 - churn)^commission_months) / churn months, in the per-user
numbers and in the month table alike.

Every number in the report comes from that file (or from a what-if flag).
Nothing is looked up or guessed.

What-ifs without editing the file:

    --price X        multiplier on every plan price (0.9 = 10 percent cheaper)
    --churn X        replaces monthly_churn (absolute, 0.08 = 8 percent a month)
    --free-cost X    multiplier on the cost of one free user
    --commission X   replaces commission_rate (absolute, 0.40 = 40 percent)
    --volume X       multiplier on new_paying_per_month

The report also shows a default what-if table: price x0.9, churn x1.5, free
cost x2, commission 0.40, volume x0.8, each against the file as written.
"""

import argparse
import json
import math
import sys


class NumbersError(Exception):
    pass


LTV_DIVISOR = 3  # convention: spend at most a third of a user's lifetime contribution to win them


def _money(v, cur):
    sign = "-" if v < 0 else ""
    digits = "{:,.0f}" if abs(v) >= 1000 or v == round(v) else "{:,.2f}"
    return "%s%s %s" % (sign, digits.format(abs(v)), cur)


def _whole(v, cur):
    sign = "-" if v < 0 else ""
    return "%s%s %s" % (sign, "{:,.0f}".format(abs(round(v))), cur)


def _users(v):
    return "{:,.1f}".format(v)


def _num(v, name, minimum=0.0, maximum=None, above=False):
    if isinstance(v, bool) or not isinstance(v, (int, float)) or not math.isfinite(v):
        raise NumbersError("%s is not a number: %r" % (name, v))
    if (v <= minimum) if above else (v < minimum):
        raise NumbersError("%s must be %s %s, got %s" % (name, "above" if above else "at least", minimum, v))
    if maximum is not None and v > maximum:
        raise NumbersError("%s must be at most %s, got %s" % (name, maximum, v))
    return float(v)


def _need(spec, key, where=""):
    if not isinstance(spec, dict) or key not in spec:
        raise NumbersError("'%s%s' is missing" % (where, key))
    return spec[key]


def _items(spec, key, prefix=""):
    raw = _need(spec, key, prefix)
    if not isinstance(raw, list):
        raise NumbersError("'%s%s' must be a list of {label, cost}" % (prefix, key))
    out = []
    for i, it in enumerate(raw):
        where = "%s%s[%d]" % (prefix, key, i)
        label = _need(it, "label", where + ".")
        if not isinstance(label, str) or not label.strip():
            raise NumbersError("%s.label must be a non-empty text" % where)
        out.append((label, _num(_need(it, "cost", where + "."), where + ".cost")))
    return out


def load(path):
    try:
        with open(path, encoding="utf-8-sig") as fh:
            return json.load(fh)
    except FileNotFoundError:
        raise NumbersError("no such file: %s" % path)
    except json.JSONDecodeError as e:
        raise NumbersError("%s is not valid JSON: %s" % (path, e))


def parse(spec):
    """Check the input and return it as plain numbers. Missing or odd fields raise NumbersError."""
    if not isinstance(spec, dict):
        raise NumbersError("the input must be a JSON object")
    business = _need(spec, "business")
    currency = _need(spec, "currency")
    if not isinstance(business, str) or not isinstance(currency, str) or not currency.strip():
        raise NumbersError("'business' and 'currency' must be text (currency is not empty)")
    months = spec.get("months", 12)
    if isinstance(months, bool) or not isinstance(months, int) or months < 1:
        raise NumbersError("months must be a whole number, 1 or more, got %r" % (months,))

    raw_plans = _need(spec, "plans")
    if not isinstance(raw_plans, list) or not raw_plans:
        raise NumbersError("'plans' must be a list with at least one plan")
    plans = []
    for i, pl in enumerate(raw_plans):
        where = "plans[%d]." % i
        name = _need(pl, "name", where)
        if not isinstance(name, str) or not name.strip():
            raise NumbersError("%sname must be a non-empty text" % where)
        plans.append({
            "name": name,
            "price": _num(_need(pl, "price_month", where), where + "price_month", above=True),
            "mix": _num(_need(pl, "mix", where), where + "mix", maximum=1.0),
            "variable": _items(pl, "variable_month", where),
        })
    total_mix = sum(p["mix"] for p in plans)
    if abs(total_mix - 1.0) > 1e-6:
        raise NumbersError("plan mixes add up to %s, not 1" % round(total_mix, 6))

    fee_given = "payment_fee_rate" in spec
    fee_rate = _num(spec["payment_fee_rate"], "payment_fee_rate", maximum=0.999999) if fee_given else 0.0

    free = None
    if "free" in spec:
        f = spec["free"]
        free = {"per_paying": _num(_need(f, "users_per_paying", "free."), "free.users_per_paying"),
                "cost": _num(_need(f, "cost_month", "free."), "free.cost_month")}
    partner = None
    if "partner" in spec:
        p = spec["partner"]
        cm = _need(p, "commission_months", "partner.")
        if isinstance(cm, bool) or not isinstance(cm, int) or cm < 0:
            raise NumbersError("partner.commission_months must be a whole number, 0 or more, got %r" % (cm,))
        partner = {"share": _num(_need(p, "share_of_new", "partner."), "partner.share_of_new", maximum=1.0),
                   "rate": _num(_need(p, "commission_rate", "partner."), "partner.commission_rate", maximum=1.0),
                   "months": cm}

    churn = _num(_need(spec, "monthly_churn"), "monthly_churn", above=True, maximum=1.0)
    fixed = _items(spec, "fixed_monthly")
    startup = _items(spec, "startup")
    new = _need(spec, "new_paying_per_month")
    if not isinstance(new, list) or len(new) != months:
        raise NumbersError("'new_paying_per_month' needs %d numbers (one per month), got %s" % (
            months, len(new) if isinstance(new, list) else "no list"))
    new = [_num(v, "new_paying_per_month[%d]" % i) for i, v in enumerate(new)]
    return {"business": business, "currency": currency, "months": months, "plans": plans,
            "fee_rate": fee_rate, "fee_given": fee_given, "free": free, "partner": partner,
            "churn": churn, "fixed": fixed, "startup": startup, "new": new}


def analyse(spec, price=1.0, churn=None, free_cost=1.0, commission=None, volume=1.0):
    """Return a dict of every number in the report. Pure function, easy to test.

    price and free_cost and volume are multipliers; churn and commission replace the input.
    """
    c = parse(spec)
    price = _num(price, "--price", above=True)
    free_cost = _num(free_cost, "--free-cost")
    volume = _num(volume, "--volume")
    if churn is not None:
        c["churn"] = _num(churn, "--churn", above=True, maximum=1.0)
    if commission is not None:
        if c["partner"] is None:
            raise NumbersError("--commission needs a 'partner' block in the input")
        c["partner"]["rate"] = _num(commission, "--commission", maximum=1.0)
    if free_cost != 1.0 and c["free"] is None:
        raise NumbersError("--free-cost needs a 'free' block in the input")
    cur, n_months, churn = c["currency"], c["months"], c["churn"]

    plan_rows = [dict(p, price=p["price"] * price, variable_total=sum(v for _, v in p["variable"])) for p in c["plans"]]
    blended_price = sum(p["mix"] * p["price"] for p in plan_rows)
    variable = sum(p["mix"] * p["variable_total"] for p in plan_rows)
    fee = c["fee_rate"] * blended_price
    free_load = c["free"]["per_paying"] * c["free"]["cost"] * free_cost if c["free"] else 0.0

    lifetime = 1.0 / churn
    if c["partner"]:
        p = c["partner"]
        commission_per_partner_user = p["rate"] * blended_price
        # expected months a partner user is paid for: month k is paid only if the user is still there,
        # (1 - churn)^k, for k = 0 .. months-1. The same rule as the month table below.
        commission_months_paid = (1 - (1 - churn) ** p["months"]) / churn
        commission_lifetime = p["share"] * commission_per_partner_user * commission_months_paid
    else:
        commission_per_partner_user = commission_months_paid = commission_lifetime = 0.0
    commission_avg = commission_lifetime / lifetime

    before_commission = blended_price - variable - fee - free_load
    contribution = before_commission - commission_avg
    margin = contribution / blended_price
    ltv = contribution * lifetime
    max_cac = ltv / LTV_DIVISOR
    fixed = sum(v for _, v in c["fixed"])
    startup = sum(v for _, v in c["startup"])
    breakeven_users = math.inf if contribution <= 0 else fixed / contribution

    new = [v * volume for v in c["new"]]
    rows, start, cum = [], 0.0, -startup
    break_even_month = payback_month = None
    lowest = cum
    for m in range(1, n_months + 1):
        churned = start * churn
        end = start + new[m - 1] - churned
        revenue = end * blended_price
        user_costs = end * (variable + fee + free_load)
        comm = 0.0
        if c["partner"]:
            for k in range(1, m + 1):
                age = m - k
                if age < c["partner"]["months"]:
                    comm += c["partner"]["share"] * new[k - 1] * (1 - churn) ** age * commission_per_partner_user
        op = revenue - user_costs - comm - fixed
        cum += op
        lowest = min(lowest, cum)
        if break_even_month is None and op >= 0:
            break_even_month = m
        if payback_month is None and cum >= 0:
            payback_month = m
        rows.append({"month": m, "start": start, "new": new[m - 1], "churned": churned, "end": end,
                     "revenue": revenue, "user_costs": user_costs + comm, "commission": comm,
                     "fixed": fixed, "operating": op, "cumulative": cum})
        start = end

    flags = []
    if contribution <= 0:
        flags.append("Each paying user loses money every month before fixed costs: contribution is %s." % _money(contribution, cur))
    if break_even_month is None:
        flags.append("No month in the %d-month plan covers its fixed costs (operating result stays below 0)." % n_months)
    if payback_month is None:
        flags.append("The startup spend and the losses are not earned back within the %d-month plan." % n_months)

    return {
        "business": c["business"], "currency": cur, "months": n_months, "plans": plan_rows,
        "blended_price": blended_price, "variable": variable, "payment_fee_rate": c["fee_rate"],
        "payment_fee_given": c["fee_given"], "payment_fee": fee, "free": c["free"], "free_load": free_load,
        "partner": c["partner"], "commission_per_partner_user": commission_per_partner_user,
        "commission_months_paid": commission_months_paid, "commission_lifetime": commission_lifetime,
        "commission_avg": commission_avg, "contribution_before_commission": before_commission,
        "contribution": contribution, "margin": margin, "monthly_churn": churn, "lifetime_months": lifetime,
        "ltv": ltv, "max_cac": max_cac, "fixed_monthly": fixed, "startup": startup,
        "fixed_items": c["fixed"], "startup_items": c["startup"], "breakeven_users": breakeven_users,
        "break_even_month": break_even_month, "payback_month": payback_month,
        "cash_needed": -lowest, "end_cumulative": rows[-1]["cumulative"], "rows": rows, "flags": flags,
        "applied": {"price": price, "churn": churn if churn != parse(spec)["churn"] else None,
                    "free_cost": free_cost, "commission": commission, "volume": volume},
    }


def sensitivity(spec):
    """The default what-ifs: each against the file as written. Returns (rows, not_run)."""
    c = parse(spec)
    rows = [("Base (the file)", analyse(spec))]
    rows.append(("Price x0.9", analyse(spec, price=0.9)))
    rows.append(("Churn x1.5 (%.1f%% a month)" % (c["churn"] * 150), analyse(spec, churn=min(1.0, c["churn"] * 1.5))))
    not_run = []
    if c["free"]:
        rows.append(("Free-user cost x2", analyse(spec, free_cost=2.0)))
    else:
        not_run.append("Free-user cost x2: no 'free' block in the input")
    if c["partner"]:
        rows.append(("Partner commission 40%", analyse(spec, commission=0.40)))
    else:
        not_run.append("Partner commission 40%: no 'partner' block in the input")
    rows.append(("New users x0.8", analyse(spec, volume=0.8)))
    return rows, not_run


def _be(a):
    return "never" if math.isinf(a["breakeven_users"]) else "{:,.0f}".format(math.ceil(a["breakeven_users"]))


def _month(v):
    return "month %d" % v if v else "not within the plan"


def report(spec, a):
    cur = a["currency"]
    n = a["months"]
    L = ["# Subscription economics: %s" % (a["business"] or "your business"), "",
         "Every number below comes from the input file (and any what-if flag). Nothing is looked up or guessed.", ""]
    ap = a["applied"]
    flags_on = []
    if ap["price"] != 1.0:
        flags_on.append("price x%g" % ap["price"])
    if ap["churn"] is not None:
        flags_on.append("monthly churn %g" % ap["churn"])
    if ap["free_cost"] != 1.0:
        flags_on.append("free-user cost x%g" % ap["free_cost"])
    if ap["commission"] is not None:
        flags_on.append("commission rate %g" % ap["commission"])
    if ap["volume"] != 1.0:
        flags_on.append("new users x%g" % ap["volume"])
    if flags_on:
        L += ["**What-if applied to this whole report: %s.**" % ", ".join(flags_on), ""]

    L += ["## Plans", "", "| plan | price a month | share of paying users | variable cost a month |",
          "| --- | ---: | ---: | ---: |"]
    for p in a["plans"]:
        L.append("| %s | %s | %.0f%% | %s |" % (p["name"], _money(p["price"], cur), p["mix"] * 100,
                                                  _money(p["variable_total"], cur)))
    L += ["", "## One paying user, one month", "",
          "| line | per paying user-month |", "| --- | ---: |",
          "| Blended price (plans weighted by their share) | %s |" % _money(a["blended_price"], cur),
          "| Variable cost (blended) | -%s |" % _money(a["variable"], cur)]
    if a["payment_fee_given"]:
        L.append("| Payment fee (%.1f%% of price) | -%s |" % (a["payment_fee_rate"] * 100, _money(a["payment_fee"], cur)))
    else:
        L.append("| Payment fee: not given (không có số), counted as 0 | -%s |" % _money(0, cur))
    if a["free"]:
        L.append("| Free-tier load (%s free users x %s) | -%s |" % (
            "{:g}".format(a["free"]["per_paying"]), _money(a["free"]["cost"] * ap["free_cost"], cur), _money(a["free_load"], cur)))
    else:
        L.append("| Free tier: none | -%s |" % _money(0, cur))
    if a["partner"]:
        p = a["partner"]
        L.append("| Partner commission, average (%.0f%% of new users, %.0f%% of price, %d months, over the stay) | -%s |" % (
            p["share"] * 100, p["rate"] * 100, p["months"], _money(a["commission_avg"], cur)))
    else:
        L.append("| Partner commission: no partners | -%s |" % _money(0, cur))
    L.append("| **Contribution** (what one paying user leaves to pay the fixed costs) | **%s** (%.0f%%) |" % (
        _money(a["contribution"], cur), a["margin"] * 100))
    L += ["", "## How long a user stays and what that is worth", "",
          "- Monthly churn: %.1f%%, so a paying user stays **%.1f months** on average (1 / churn)." % (
              a["monthly_churn"] * 100, a["lifetime_months"]),
          "- **Contribution LTV: %s** (contribution x months stayed)." % _whole(a["ltv"], cur)]
    if a["partner"]:
        L.append("  - includes commission paid on partner users: %s per partner user, for the first %d months while the user stays, "
                 "on average %.2f months ((1 - (1 - churn)^%d) / churn), the same rule as the month table below." % (
                     _whole(a["commission_per_partner_user"] * a["commission_months_paid"], cur),
                     a["partner"]["months"], a["commission_months_paid"], a["partner"]["months"]))
    if a["ltv"] > 0:
        L.append("- **Maximum acquisition cost per paying user: %s** = LTV / %d. That is a convention (spend at most a third of "
                 "what a user is worth), not a law; it is not tested against your channels." % (_whole(a["max_cac"], cur), LTV_DIVISOR))
    else:
        L.append("- Maximum acquisition cost: none, LTV is not above 0.")
    L += ["", "## Break-even", "",
          "Fixed costs: %s a month (%s)." % (_whole(a["fixed_monthly"], cur), ", ".join(
              "%s %s" % (lab, _whole(v, cur)) for lab, v in a["fixed_items"]) or "none given"), "",
          "- **Break-even: %s paying users** (fixed costs / contribution). Below that you lose money every month." % (
              "never (each paying user loses money)" if math.isinf(a["breakeven_users"]) else _be(a)),
          "- Startup spend: %s (%s)." % (_whole(a["startup"], cur), ", ".join(
              "%s %s" % (lab, _whole(v, cur)) for lab, v in a["startup_items"]) or "none given"), "",
          "## Month by month (%d months)" % n, "",
          "Churned = start x churn. End users pay; a new user pays the month they join. Cash starts at minus the startup spend.", "",
          "| month | start users | new | churned | end users | revenue | variable + free + commission | fixed | operating result | cumulative cash |",
          "| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |"]
    for r in a["rows"]:
        L.append("| %d | %s | %s | %s | %s | %s | %s | %s | %s | %s |" % (
            r["month"], _users(r["start"]), _users(r["new"]), _users(r["churned"]), _users(r["end"]),
            _whole(r["revenue"], cur), _whole(r["user_costs"], cur), _whole(r["fixed"], cur),
            _whole(r["operating"], cur), _whole(r["cumulative"], cur)))
    L += ["", "- Month the operating result first reaches 0 (break-even): **%s**." % _month(a["break_even_month"]),
          "- Month the cumulative cash first reaches 0 (payback of startup and early losses): **%s**." % _month(a["payback_month"]),
          "- Cash needed (the lowest cumulative cash): **%s**." % _whole(a["cash_needed"], cur), ""]

    rows, not_run = sensitivity(spec)
    L += ["## What if", "", "Each row changes one thing in the file as written (the flags above are not applied here).", "",
          "| scenario | contribution a user-month | LTV | max acquisition cost | break-even users | break-even month | payback month | cash needed | cash at month %d |" % n,
          "| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |"]
    for name, s in rows:
        L.append("| %s | %s | %s | %s | %s | %s | %s | %s | %s |" % (
            name, _money(s["contribution"], cur), _whole(s["ltv"], cur), _whole(max(s["max_cac"], 0), cur), _be(s),
            s["break_even_month"] or "none", s["payback_month"] or "none", _whole(s["cash_needed"], cur),
            _whole(s["end_cumulative"], cur)))
    for note in not_run:
        L.append("")
        L.append("Not run: %s." % note)
    L.append("")
    if a["flags"]:
        L += ["## Red flags", ""] + ["- %s" % f for f in a["flags"]]
    else:
        L.append("No red flags in these numbers. They are only as good as the inputs: check every cost and the churn against real data.")
    return "\n".join(L) + "\n"


def _json_ready(a, rows):
    def clean(v):
        if isinstance(v, float) and math.isinf(v):
            return None
        if isinstance(v, dict):
            return {k: clean(x) for k, x in v.items()}
        if isinstance(v, (list, tuple)):
            return [clean(x) for x in v]
        return v
    out = {k: v for k, v in a.items() if not k.endswith("_items")}
    out["what_if"] = [{"scenario": name, "contribution": s["contribution"], "ltv": s["ltv"], "max_cac": s["max_cac"],
                       "breakeven_users": s["breakeven_users"], "break_even_month": s["break_even_month"],
                       "payback_month": s["payback_month"], "cash_needed": s["cash_needed"],
                       "end_cumulative": s["end_cumulative"]} for name, s in rows]
    return clean(out)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("numbers", help="the business's JSON file (see saas_example.json)")
    ap.add_argument("--out", help="write the report here (markdown)")
    ap.add_argument("--json", action="store_true", help="print the numbers as JSON")
    ap.add_argument("--price", type=float, default=1.0, help="what-if: multiplier on every plan price")
    ap.add_argument("--churn", type=float, help="what-if: monthly churn, absolute")
    ap.add_argument("--free-cost", type=float, default=1.0, dest="free_cost", help="what-if: multiplier on the cost of a free user")
    ap.add_argument("--commission", type=float, help="what-if: partner commission rate, absolute")
    ap.add_argument("--volume", type=float, default=1.0, help="what-if: multiplier on new paying users")
    args = ap.parse_args(argv)
    try:
        spec = load(args.numbers)
        a = analyse(spec, price=args.price, churn=args.churn, free_cost=args.free_cost,
                    commission=args.commission, volume=args.volume)
        text = None if args.json else report(spec, a)
        rows = sensitivity(spec)[0] if args.json else None
    except (NumbersError, OSError, UnicodeDecodeError) as e:
        print("error: %s" % e, file=sys.stderr)
        return 2
    if args.json:
        print(json.dumps(_json_ready(a, rows), indent=1, ensure_ascii=False))
        return 0
    if args.out:
        try:
            with open(args.out, "w", encoding="utf-8") as fh:
                fh.write(text)
        except OSError as e:
            print("error: cannot write %s: %s" % (args.out, e.strerror or e), file=sys.stderr)
            return 2
        print("wrote %s" % args.out)
    else:
        sys.stdout.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
