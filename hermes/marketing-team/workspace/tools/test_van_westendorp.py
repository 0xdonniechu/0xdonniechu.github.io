#!/usr/bin/env python3
"""Tests for van_westendorp.py. Run: python3 tools/test_van_westendorp.py

Adapted from Jakeschincariol/founder-skill `tests/test_pricing.py` @ fd9385b (MIT).
"""

import contextlib
import io
import os
import sys
import tempfile
import unittest

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import van_westendorp as vw  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
HEAD = "too_cheap,cheap,expensive,too_expensive\n"


def rows(n=40):
    out = []
    for i in range(n):
        k = i / float(n - 1)
        out.append((2.5 + k, 4.0 + k, 6.0 + 1.5 * k, 7.5 + 2 * k))
    return out


def linear():
    """Ten respondents, answers 10+i, 20+i, 30+i, 40+i for i = 0..9."""
    return [(10.0 + i, 20.0 + i, 30.0 + i, 40.0 + i) for i in range(10)]


def csv_text(rs, extra=""):
    return HEAD + "".join("%s,%s,%s,%s\n" % r for r in rs) + extra


def write(text):
    f = tempfile.NamedTemporaryFile("w", suffix=".csv", delete=False, encoding="utf-8", newline="")
    f.write(text)
    f.close()
    return f.name


def run(text, *args):
    path = write(text)
    try:
        out, err = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            code = vw.main([path, *args])
        return code, out.getvalue(), err.getvalue()
    finally:
        os.unlink(path)


class Pricing(unittest.TestCase):
    def test_points_are_ordered_and_inside_the_answers(self):
        res = vw.analyse(rows())
        p = res["points"]
        for k in ("PMC", "PME", "OPP", "IPP"):
            self.assertIsNotNone(p[k], k)
            self.assertTrue(2.5 <= p[k] <= 9.5, (k, p[k]))
        self.assertLess(p["PMC"], p["PME"])
        self.assertLessEqual(p["PMC"], p["OPP"])
        self.assertLessEqual(p["OPP"], p["PME"])

    def test_hand_computed_points(self):
        # step is 0.1 (39 / 400 rounds to 0.1). Both "too cheap" and "too expensive"
        # curves are 0 between 19.1 and 40, so OPP and PMC land on 19.1; "a bargain"
        # and "expensive" are both 0 from 29.1; "not expensive" and "too expensive"
        # are both 0 at 39.0.
        res = vw.analyse(linear())
        p = res["points"]
        self.assertAlmostEqual(p["PMC"], 19.1, places=6)
        self.assertAlmostEqual(p["OPP"], 19.1, places=6)
        self.assertAlmostEqual(p["IPP"], 29.1, places=6)
        self.assertAlmostEqual(p["PME"], 39.0, places=6)
        # median = the answer at position n // 2 of the sorted list
        self.assertEqual(res["median"], {"too_cheap": 15.0, "cheap": 25.0, "expensive": 35.0, "too_expensive": 45.0})

    def test_vnd_integers_scale_the_same_way(self):
        res = vw.analyse([tuple(v * 1000 for v in r) for r in linear()])
        self.assertTrue(res["whole"])
        self.assertAlmostEqual(res["points"]["PMC"], 19100, delta=100)
        self.assertAlmostEqual(res["points"]["PME"], 39000, delta=100)

    def test_out_of_order_and_incomplete_rows_are_dropped(self):
        path = write(csv_text(rows(10), "9,4,6,8\n3,,6,8\n"))
        try:
            got, dropped = vw.read(path)
        finally:
            os.unlink(path)
        self.assertEqual((len(got), dropped), (10, 2))

    def test_fewer_than_10_rows_is_refused(self):
        with self.assertRaises(vw.PricingError) as cm:
            vw.analyse(rows(9))
        self.assertIn("không đủ câu trả lời", str(cm.exception))
        vw.analyse(rows(10))  # exactly 10 is enough
        code, _, err = run(csv_text(rows(12), "9,4,6,8\n3,,6,8\n5,1,1,1\n"))  # 12 good, 3 dropped
        self.assertEqual(code, 0)
        code, _, err = run(csv_text(rows(8), "9,4,6,8\n"))
        self.assertEqual(code, 2)
        self.assertIn("không đủ câu trả lời", err)
        self.assertIn("got 8", err)
        self.assertIn("1 dropped", err)

    def test_report_says_number_of_respondents(self):
        res = vw.analyse(linear())
        self.assertIn("Respondents: 10", vw.report(res, 0))
        self.assertIn("Respondents: 10 with four complete answers in order, 3 more dropped", vw.report(res, 3))

    def test_report_places_the_price(self):
        res = vw.analyse(rows())
        self.assertIn("**inside** the acceptable range", vw.report(res, 0, price=6.5, currency="$"))
        self.assertIn("**above** the acceptable range", vw.report(res, 0, price=40, currency="$"))
        self.assertIn("**below** the acceptable range", vw.report(res, 0, price=1, currency="$"))

    def test_currency_label_and_number_format(self):
        res = vw.analyse([tuple(v * 1000 for v in r) for r in linear()])
        self.assertRegex(vw.report(res, 0), r"\*\*Acceptable range: 19,\d{3} đ to 39,\d{3} đ\.\*\*")
        self.assertRegex(vw.report(res, 0, currency="VND"), r"\| PMC \| 19,\d{3} VND \|")
        self.assertIn("Median answers: too cheap 15,000 đ", vw.report(res, 0))
        self.assertIn(" $", vw.report(vw.analyse(rows()), 0, currency="$"))
        self.assertIn("6.50 $", vw.report(vw.analyse(rows()), 0, price=6.5, currency="$"))

    def test_separators_are_refused_not_guessed(self):
        for bad in ('"99,000"', "99.000", "0.500"):
            code, _, err = run(csv_text(rows(10), "1,2,%s,300\n" % bad))
            self.assertEqual(code, 2, bad)
            self.assertIn("thousands separator", err)

    def test_missing_column_and_missing_file_fail(self):
        code, _, err = run("too_cheap,cheap,expensive\n1,2,3\n")
        self.assertEqual(code, 2)
        self.assertIn("missing column(s) too_expensive", err)
        with contextlib.redirect_stderr(io.StringIO()):
            self.assertEqual(vw.main(["/no/such/file.csv"]), 2)

    def test_bunched_answers_warn(self):
        code, out, _ = run(csv_text([(100000, 150000, 200000, 300000)] * 12), "--price", "211700")
        self.assertEqual(code, 0)
        self.assertIn("Warning: answers bunch on a few values", out)
        code, out, _ = run(csv_text(linear()))
        self.assertNotIn("Warning", out)
        # spread evenly over three values each: no value has half, but the curves are steps with gaps
        spread = [(40000 + i * 1000, 90000 + i * 1000, e, t) for i, (e, t) in
                  enumerate(zip([150000, 180000, 200000] * 4, [250000, 300000, 350000] * 4))]
        code, out, _ = run(csv_text(spread), "--price", "211700")
        self.assertEqual(code, 0)
        self.assertIn("Warning: answers bunch on a few values", out)

    def test_unreadable_input_and_unwritable_out_are_errors_not_tracebacks(self):
        with tempfile.TemporaryDirectory() as d:
            bad = os.path.join(d, "bad.csv")
            with open(bad, "wb") as fh:
                fh.write(b"\xff\xfe\x00bad")
            for argv in ([bad], [os.path.join(d, "dir.csv")]):
                if argv[0].endswith("dir.csv"):
                    os.mkdir(argv[0])
                err = io.StringIO()
                with contextlib.redirect_stderr(err):
                    self.assertEqual(vw.main(argv), 2, argv)
                self.assertIn("error:", err.getvalue())
            code, _, err = run(csv_text(linear()), "--out", os.path.join(d, "no", "such", "x.md"))
            self.assertEqual(code, 2)
            self.assertIn("cannot write", err)

    def test_extra_columns_bom_and_crlf_are_fine(self):
        text = "﻿too_cheap,cheap,expensive,too_expensive,note\r\n" + "".join(
            "%s,%s,%s,%s,x\r\n" % r for r in linear())
        code, out, _ = run(text)
        self.assertEqual(code, 0)
        self.assertIn("Respondents: 10", out)

    def test_json_output_has_currency_and_count(self):
        code, out, _ = run(csv_text(linear()), "--json", "--currency", "VND")
        self.assertEqual(code, 0)
        self.assertIn('"n": 10', out)
        self.assertIn('"currency": "VND"', out)

    def test_example_file_runs(self):
        path = os.path.join(HERE, "price_survey_example.csv")
        got, dropped = vw.read(path)
        self.assertEqual((len(got), dropped), (20, 0))
        res = vw.analyse(got)
        self.assertLess(res["points"]["PMC"], res["points"]["PME"])
        self.assertIn("Respondents: 20", vw.report(res, 0))


if __name__ == "__main__":
    unittest.main()
