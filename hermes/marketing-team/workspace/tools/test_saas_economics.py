#!/usr/bin/env python3
"""Tests for saas_economics.py. Run: python3 tools/test_saas_economics.py

Every expected number is worked out by hand in the comments, from the fixture below.
"""

import contextlib
import copy
import io
import json
import math
import os
import sys
import tempfile
import unittest

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import saas_economics as se  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))


def spec():
    """Blended price 0.5*100 + 0.5*200 = 150; blended variable 0.5*10 + 0.5*30 = 20.
    Fee 0.02*150 = 3. Free load 4 x 0.5 = 2. Lifetime 1/0.1 = 10 months.
    Commission paid per partner user: 0.2*150 = 30 a month for its first 3 months while it stays:
    1 + 0.9 + 0.81 = 2.71 months on average, on 0.5 of users: 0.5*30*2.71 = 40.65 over a life,
    4.065 a month.
    """
    return {
        "business": "Test", "currency": "đ", "months": 3,
        "plans": [
            {"name": "Basic", "price_month": 100, "mix": 0.5, "variable_month": [{"label": "AI", "cost": 10}]},
            {"name": "Pro", "price_month": 200, "mix": 0.5, "variable_month": [{"label": "AI", "cost": 30}]},
        ],
        "payment_fee_rate": 0.02,
        "free": {"users_per_paying": 4, "cost_month": 0.5},
        "partner": {"share_of_new": 0.5, "commission_rate": 0.2, "commission_months": 3},
        "monthly_churn": 0.1,
        "fixed_monthly": [{"label": "rent", "cost": 5000}, {"label": "tools", "cost": 1025}],
        "startup": [{"label": "build", "cost": 1000}],
        "new_paying_per_month": [100, 50, 0],
    }


def run(path, *args):
    out, err = io.StringIO(), io.StringIO()
    with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
        code = se.main([path, *args])
    return code, out.getvalue(), err.getvalue()


def tmp_json(s):
    f = tempfile.NamedTemporaryFile("w", suffix=".json", delete=False, encoding="utf-8")
    json.dump(s, f)
    f.close()
    return f.name


class Unit(unittest.TestCase):
    def test_contribution_ltv_and_break_even_users(self):
        a = se.analyse(spec())
        self.assertAlmostEqual(a["blended_price"], 150)
        self.assertAlmostEqual(a["variable"], 20)
        self.assertAlmostEqual(a["payment_fee"], 3)
        self.assertAlmostEqual(a["free_load"], 2)                       # 4 free users x 0.5
        self.assertAlmostEqual(a["lifetime_months"], 10)
        self.assertAlmostEqual(a["commission_months_paid"], 2.71)       # 1 + 0.9 + 0.81
        self.assertAlmostEqual(a["commission_lifetime"], 40.65)         # 0.5 x 30 x 2.71
        self.assertAlmostEqual(a["commission_avg"], 4.065)              # 40.65 / 10
        self.assertAlmostEqual(a["contribution_before_commission"], 125)  # 150 - 20 - 3 - 2
        self.assertAlmostEqual(a["contribution"], 120.935)              # 125 - 4.065
        self.assertAlmostEqual(a["margin"], 120.935 / 150)
        self.assertAlmostEqual(a["ltv"], 1209.35)                       # 125 x 10 - 40.65
        self.assertAlmostEqual(a["max_cac"], 1209.35 / 3)
        self.assertAlmostEqual(a["fixed_monthly"], 6025)
        self.assertAlmostEqual(a["breakeven_users"], 6025 / 120.935)    # 49.8, shown as 50

    def test_commission_months_are_the_expected_paid_months_under_churn(self):
        s = spec()
        s["partner"]["commission_months"] = 24
        a = se.analyse(s)
        paid = (1 - 0.9 ** 24) / 0.1                                    # 9.20, below the 10-month stay
        self.assertAlmostEqual(a["commission_months_paid"], paid)
        self.assertLess(a["commission_months_paid"], a["lifetime_months"])
        self.assertAlmostEqual(a["commission_lifetime"], 0.5 * 30 * paid)
        self.assertAlmostEqual(a["ltv"], 125 * 10 - 0.5 * 30 * paid)

    def test_per_user_commission_matches_the_month_table_at_steady_state(self):
        s = spec()
        s["months"] = 300
        s["new_paying_per_month"] = [100] * 300
        s["partner"]["commission_months"] = 12
        a = se.analyse(s)
        last = a["rows"][-1]
        # once cohorts are steady, commission per paying user in the table equals the per-user average
        self.assertAlmostEqual(last["commission"] / last["end"], a["commission_avg"], places=6)

    def test_no_free_tier_no_partner_no_fee_given(self):
        s = spec()
        del s["free"], s["partner"], s["payment_fee_rate"]
        a = se.analyse(s)
        self.assertEqual(a["free_load"], 0)
        self.assertEqual(a["commission_avg"], 0)
        self.assertFalse(a["payment_fee_given"])
        self.assertAlmostEqual(a["contribution"], 130)                  # 150 - 20
        text = se.report(s, a)
        self.assertIn("not given (không có số)", text)
        self.assertIn("Free tier: none", text)
        self.assertIn("no partners", text)
        # the default what-if table skips what the file does not have, and says so
        self.assertIn("Not run: Free-user cost x2: no 'free' block", text)
        self.assertIn("Not run: Partner commission 40%: no 'partner' block", text)

    def test_roll_forward_three_months(self):
        r = se.analyse(spec())["rows"]
        # start / new / churned / end
        #   1:   0 / 100 /  0 / 100
        #   2: 100 /  50 / 10 / 140
        #   3: 140 /   0 / 14 / 126
        for row, exp in zip(r, [(0, 100, 0, 100), (100, 50, 10, 140), (140, 0, 14, 126)]):
            for key, want in zip(("start", "new", "churned", "end"), exp):
                self.assertAlmostEqual(row[key], want, msg=(row["month"], key))
        # revenue = end x 150
        self.assertAlmostEqual(r[0]["revenue"], 15000)
        self.assertAlmostEqual(r[1]["revenue"], 21000)
        self.assertAlmostEqual(r[2]["revenue"], 18900)
        # partner users paying: 50 | 50x0.9 + 25 = 70 | 50x0.81 + 25x0.9 = 63, each costs 0.2 x 150 = 30
        self.assertAlmostEqual(r[0]["commission"], 1500)
        self.assertAlmostEqual(r[1]["commission"], 2100)
        self.assertAlmostEqual(r[2]["commission"], 1890)
        # user costs = end x (20 + 3 + 2) + commission
        self.assertAlmostEqual(r[0]["user_costs"], 2500 + 1500)
        self.assertAlmostEqual(r[1]["user_costs"], 3500 + 2100)
        self.assertAlmostEqual(r[2]["user_costs"], 3150 + 1890)
        # operating = revenue - costs - 6025
        self.assertAlmostEqual(r[0]["operating"], 4975)
        self.assertAlmostEqual(r[1]["operating"], 9375)
        self.assertAlmostEqual(r[2]["operating"], 7835)
        # cumulative cash starts at -1000
        self.assertAlmostEqual(r[0]["cumulative"], 3975)
        self.assertAlmostEqual(r[1]["cumulative"], 13350)
        self.assertAlmostEqual(r[2]["cumulative"], 21185)

    def test_commission_stops_after_commission_months(self):
        s = spec()
        s["months"] = 5
        s["new_paying_per_month"] = [100, 0, 0, 0, 0]
        s["partner"]["commission_months"] = 3
        r = se.analyse(s)["rows"]
        # one cohort of 50 partner users, paid in its months 1-3 only; 0.9 survive each month
        self.assertAlmostEqual(r[0]["commission"], 50 * 30)
        self.assertAlmostEqual(r[1]["commission"], 50 * 0.9 * 30)
        self.assertAlmostEqual(r[2]["commission"], 50 * 0.81 * 30)
        self.assertEqual(r[3]["commission"], 0)
        self.assertEqual(r[4]["commission"], 0)

    def test_break_even_payback_and_cash_needed(self):
        s = spec()
        s["fixed_monthly"] = [{"label": "all", "cost": 12000}]
        a = se.analyse(s)
        # operating: 15000-4000-12000 = -1000 | 21000-5600-12000 = 3400 | 18900-5040-12000 = 1860
        # cumulative from -1000: -2000 | 1400 | 3260
        self.assertEqual(a["break_even_month"], 2)
        self.assertEqual(a["payback_month"], 2)
        self.assertAlmostEqual(a["cash_needed"], 2000)
        self.assertEqual(a["flags"], [])

    def test_flags_no_break_even_and_no_payback(self):
        s = spec()
        s["fixed_monthly"] = [{"label": "all", "cost": 20000}]
        a = se.analyse(s)
        # operating: -9000 | -4600 | -6140; cumulative from -1000: -10000 | -14600 | -20740
        self.assertIsNone(a["break_even_month"])
        self.assertIsNone(a["payback_month"])
        self.assertAlmostEqual(a["cash_needed"], 20740)
        self.assertEqual(len(a["flags"]), 2)
        self.assertIn("No month", a["flags"][0])
        self.assertIn("not earned back", a["flags"][1])

    def test_flag_contribution_not_positive(self):
        s = spec()
        s["plans"][0]["variable_month"] = [{"label": "AI", "cost": 500}]
        s["plans"][1]["variable_month"] = [{"label": "AI", "cost": 500}]
        a = se.analyse(s)                                               # 150 - 500 - 3 - 2 - 4.065 < 0
        self.assertLess(a["contribution"], 0)
        self.assertTrue(math.isinf(a["breakeven_users"]))
        self.assertTrue(any("loses money" in f for f in a["flags"]))
        self.assertIn("none, LTV is not above 0", se.report(s, a))
        code, out, _ = run(tmp_json(s), "--json")
        self.assertEqual(code, 0)
        self.assertIsNone(json.loads(out)["breakeven_users"])

    def test_zero_new_users_never_breaks_even_with_fixed_costs(self):
        s = spec()
        s["new_paying_per_month"] = [0, 0, 0]
        a = se.analyse(s)
        self.assertIsNone(a["break_even_month"])
        self.assertAlmostEqual(a["cash_needed"], 1000 + 3 * 6025)


class WhatIf(unittest.TestCase):
    def test_price_multiplier(self):
        a = se.analyse(spec(), price=0.9)
        # price 135, variable 20, fee 2.7, free 2 -> 110.3; commission 0.5 x 0.2 x 135 x 2.71 = 36.585 -> 3.6585 a month
        self.assertAlmostEqual(a["blended_price"], 135)
        self.assertAlmostEqual(a["contribution"], 110.3 - 3.6585)

    def test_churn_is_absolute(self):
        a = se.analyse(spec(), churn=0.2)
        # life 5 months; commission months 1 + 0.8 + 0.64 = 2.44 -> 0.5 x 30 x 2.44 = 36.6; LTV = 125 x 5 - 36.6
        self.assertAlmostEqual(a["lifetime_months"], 5)
        self.assertAlmostEqual(a["commission_months_paid"], 2.44)
        self.assertAlmostEqual(a["ltv"], 588.4)
        self.assertAlmostEqual(a["contribution"], 125 - 36.6 / 5)
        self.assertAlmostEqual(a["rows"][1]["churned"], 20)

    def test_free_cost_multiplier(self):
        a = se.analyse(spec(), free_cost=2)
        self.assertAlmostEqual(a["free_load"], 4)
        self.assertAlmostEqual(a["ltv"], 123 * 10 - 40.65)

    def test_commission_is_absolute(self):
        a = se.analyse(spec(), commission=0.4)
        self.assertAlmostEqual(a["commission_lifetime"], 0.5 * 0.4 * 150 * 2.71)  # 81.3
        self.assertAlmostEqual(a["ltv"], 1250 - 81.3)

    def test_volume_multiplier(self):
        a = se.analyse(spec(), volume=0.8)
        self.assertAlmostEqual(a["rows"][0]["new"], 80)
        self.assertAlmostEqual(a["rows"][0]["end"], 80)
        self.assertAlmostEqual(a["rows"][1]["end"], 40 + 72)            # 80 x 0.9 + 40
        self.assertAlmostEqual(a["contribution"], 120.935)              # per-user numbers do not move

    def test_flags_that_do_not_fit_the_input_are_errors(self):
        s = spec()
        del s["partner"]
        with self.assertRaises(se.NumbersError):
            se.analyse(s, commission=0.4)
        s = spec()
        del s["free"]
        with self.assertRaises(se.NumbersError):
            se.analyse(s, free_cost=2)
        for kw in ({"price": 0}, {"churn": 0}, {"churn": 1.5}, {"commission": 1.5}, {"volume": -1}, {"free_cost": -1}):
            with self.assertRaises(se.NumbersError, msg=kw):
                se.analyse(spec(), **kw)

    def test_default_what_if_table_has_the_five_scenarios(self):
        rows, not_run = se.sensitivity(spec())
        self.assertEqual([n.split(" (")[0] for n, _ in rows],
                         ["Base", "Price x0.9", "Churn x1.5", "Free-user cost x2",
                          "Partner commission 40%", "New users x0.8"])
        self.assertEqual(not_run, [])
        by = dict(rows)
        self.assertAlmostEqual(by["Price x0.9"]["contribution"], 110.3 - 3.6585)
        self.assertAlmostEqual(by["Partner commission 40%"]["ltv"], 1168.7)
        self.assertAlmostEqual(by["Free-user cost x2"]["ltv"], 1189.35)
        churn_row = [s for n, s in rows if n.startswith("Churn")][0]
        self.assertAlmostEqual(churn_row["lifetime_months"], 1 / 0.15)

    def test_cli_flags_change_the_report(self):
        path = tmp_json(spec())
        try:
            code, out, _ = run(path, "--price", "0.9", "--churn", "0.2", "--commission", "0.4", "--free-cost", "2", "--volume", "0.8")
        finally:
            os.unlink(path)
        self.assertEqual(code, 0)
        self.assertIn("What-if applied to this whole report: price x0.9, monthly churn 0.2, free-user cost x2, commission rate 0.4, new users x0.8", out)


class BadInput(unittest.TestCase):
    def test_every_required_field_missing_is_an_error_naming_it(self):
        for key in ("business", "currency", "plans", "monthly_churn", "fixed_monthly", "startup", "new_paying_per_month"):
            s = spec()
            del s[key]
            with self.assertRaises(se.NumbersError, msg=key) as cm:
                se.analyse(s)
            self.assertIn("'%s' is missing" % key, str(cm.exception))

    def test_missing_plan_and_nested_fields(self):
        for where, key in (("plans[0].", "name"), ("plans[0].", "price_month"), ("plans[0].", "mix"), ("plans[0].", "variable_month")):
            s = spec()
            del s["plans"][0][key]
            with self.assertRaises(se.NumbersError, msg=key) as cm:
                se.analyse(s)
            self.assertIn(where + key, str(cm.exception))
        s = spec()
        del s["free"]["cost_month"]
        with self.assertRaisesRegex(se.NumbersError, "free.cost_month"):
            se.analyse(s)
        s = spec()
        del s["partner"]["commission_months"]
        with self.assertRaisesRegex(se.NumbersError, "partner.commission_months"):
            se.analyse(s)
        s = spec()
        del s["fixed_monthly"][0]["cost"]
        with self.assertRaisesRegex(se.NumbersError, r"fixed_monthly\[0\].cost"):
            se.analyse(s)

    def test_mixes_must_add_up_to_one(self):
        s = spec()
        s["plans"][0]["mix"] = 0.6
        with self.assertRaisesRegex(se.NumbersError, "add up to 1.1, not 1"):
            se.analyse(s)
        s["plans"][0]["mix"] = 0.4
        with self.assertRaisesRegex(se.NumbersError, "add up to 0.9, not 1"):
            se.analyse(s)

    def test_new_paying_length_must_match_months(self):
        s = spec()
        s["new_paying_per_month"] = [1, 2]
        with self.assertRaisesRegex(se.NumbersError, "needs 3 numbers"):
            se.analyse(s)
        s = spec()
        del s["months"]                                                 # default is 12
        with self.assertRaisesRegex(se.NumbersError, "needs 12 numbers"):
            se.analyse(s)
        s["new_paying_per_month"] = [10] * 12
        self.assertEqual(len(se.analyse(s)["rows"]), 12)

    def test_odd_values_are_refused_not_guessed(self):
        bad = [("monthly_churn", 0), ("monthly_churn", 1.2), ("monthly_churn", "0.1"), ("monthly_churn", True),
               ("payment_fee_rate", -0.1), ("payment_fee_rate", 1), ("months", 0), ("months", 2.5), ("months", True)]
        for key, value in bad:
            s = spec()
            s[key] = value
            with self.assertRaises(se.NumbersError, msg=(key, value)):
                se.analyse(s)
        s = spec()
        s["plans"][0]["price_month"] = 0
        with self.assertRaises(se.NumbersError):
            se.analyse(s)
        s = spec()
        s["plans"][0]["variable_month"][0]["cost"] = "lots"
        with self.assertRaisesRegex(se.NumbersError, "not a number"):
            se.analyse(s)
        s = spec()
        s["new_paying_per_month"][0] = -5
        with self.assertRaises(se.NumbersError):
            se.analyse(s)
        s = spec()
        s["plans"] = []
        with self.assertRaises(se.NumbersError):
            se.analyse(s)

    def test_cli_error_exit_code_and_message(self):
        s = spec()
        del s["monthly_churn"]
        path = tmp_json(s)
        try:
            code, _, err = run(path)
        finally:
            os.unlink(path)
        self.assertEqual(code, 2)
        self.assertIn("error: 'monthly_churn' is missing", err)
        with contextlib.redirect_stderr(io.StringIO()):
            self.assertEqual(se.main(["/no/such/file.json"]), 2)

    def test_unreadable_input_and_unwritable_out_are_errors_not_tracebacks(self):
        with tempfile.TemporaryDirectory() as d:
            bad = os.path.join(d, "bad.json")
            with open(bad, "wb") as fh:
                fh.write(b"\xff\xfe\x00bad")
            for path in (bad, d):
                code, _, err = run(path)
                self.assertEqual(code, 2, path)
                self.assertIn("error:", err)
            path = tmp_json(spec())
            try:
                code, _, err = run(path, "--out", os.path.join(d, "no", "such", "x.md"))
            finally:
                os.unlink(path)
            self.assertEqual(code, 2)
            self.assertIn("cannot write", err)

    def test_input_is_not_changed_by_a_run(self):
        s = spec()
        before = copy.deepcopy(s)
        se.analyse(s, price=0.9, churn=0.2, commission=0.4, free_cost=2, volume=0.8)
        se.sensitivity(s)
        self.assertEqual(s, before)


class Report(unittest.TestCase):
    def test_report_has_the_key_numbers(self):
        s = spec()
        text = se.report(s, se.analyse(s))
        for needle in ("150 đ", "**120.94 đ** (81%)", "10.0 months", "1,209 đ", "403 đ", "on average 2.71 months", "= LTV / 3", "a convention",
                       "**Break-even: 50 paying users**", "**month 1**", "21,185 đ", "## What if", "No red flags"):
            self.assertIn(needle, text, needle)

    def test_json_and_out_file(self):
        path = tmp_json(spec())
        out_path = path + ".md"
        try:
            code, out, _ = run(path, "--json")
            self.assertEqual(code, 0)
            data = json.loads(out)
            self.assertAlmostEqual(data["ltv"], 1209.35)
            self.assertEqual(len(data["what_if"]), 6)
            code, out, _ = run(path, "--out", out_path)
            self.assertEqual(code, 0)
            self.assertIn("wrote", out)
            with open(out_path, encoding="utf-8") as fh:
                self.assertIn("# Subscription economics: Test", fh.read())
        finally:
            os.unlink(path)
            if os.path.exists(out_path):
                os.unlink(out_path)

    def test_example_file_runs_and_is_fictional(self):
        with open(os.path.join(HERE, "saas_example.json"), encoding="utf-8") as fh:
            s = json.load(fh)
        self.assertEqual(s["business"], "Ví dụ (số giả)")
        a = se.analyse(s)
        # 0.7 x 99000 + 0.3 x 199000 = 129000
        self.assertAlmostEqual(a["blended_price"], 129000)
        self.assertEqual(len(a["rows"]), 12)
        self.assertIn("Ví dụ (số giả)", se.report(s, a))


if __name__ == "__main__":
    unittest.main()
