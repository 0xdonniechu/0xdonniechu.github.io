#!/usr/bin/env python3
"""Tests for readout_stats.py. Run: python3 tools/test_readout_stats.py"""

import contextlib
import io
import os
import sys
import tempfile
import unittest

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import readout_stats  # noqa: E402

CSV = """platform,post_id,boosted,reach,impressions,engagements
facebook,f1,no,1000,1500,50
facebook,f2,no,2000,2500,40
facebook,f3,no,500,800,
facebook,f4,yes,10000,12000,900
tiktok,t1,no,3000,,300
tiktok,t2,no,1000,,10
"""


def run(text, *args):
    """Return (exit code, stdout, stderr)."""
    with tempfile.NamedTemporaryFile("w", suffix=".csv", delete=False, encoding="utf-8") as f:
        f.write(text)
        path = f.name
    try:
        out, err = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            code = readout_stats.main([path, *args])
        return code, out.getvalue(), err.getvalue()
    finally:
        os.unlink(path)


def ok(text, *args):
    code, out, err = run(text, *args)
    assert code == 0, err
    return out


def fails(text, *args):
    code, _, err = run(text, *args)
    assert code == 2, f"expected exit 2, got {code}"
    return err


class ReadoutTest(unittest.TestCase):
    def test_medians_split_organic_and_boosted(self):
        out = ok(CSV, "--rate", "ERR=engagements/reach")
        # organic facebook ERR: 5% and 2%, f3 has no engagements -> median 3.50%
        self.assertIn("| facebook | tự nhiên | 3 | 3.50% | 1,000 | 1,500 | 45 |", out)
        self.assertIn("| facebook | quảng cáo | 1 | 9.00% |", out)

    def test_missing_number_is_reported_not_guessed(self):
        out = ok(CSV, "--rate", "ERI=engagements/impressions")
        self.assertIn("| tiktok | tự nhiên | 2 | không có số |", out)
        self.assertIn("facebook tự nhiên: ERI thiếu số ở 1/3 bài", out)

    def test_ranking_uses_first_rate_and_organic_only(self):
        out = ok(CSV, "--rate", "ERR=engagements/reach", "--top", "1")
        self.assertIn("- facebook: tốt nhất f1 (5.00%); kém nhất f2 (2.00%)", out)
        self.assertNotIn("f4 (", out)
        self.assertIn("- tiktok: tốt nhất t1 (10.00%); kém nhất t2 (1.00%)", out)

    def test_small_sample_flagged(self):
        self.assertIn("- facebook: dưới 5 bài tự nhiên", ok(CSV, "--rate", "ERR=engagements/reach"))

    def test_unknown_rate_column_fails(self):
        self.assertIn("'likes' is not in the CSV", fails(CSV, "--rate", "X=likes/reach"))

    def test_blank_or_bad_boosted_fails(self):
        self.assertIn("boosted must be yes or no", fails("platform,post_id,boosted,reach\nfacebook,f1,,10\n"))
        self.assertIn("boosted must be yes or no", fails("platform,post_id,boosted,reach\nfacebook,f1,maybe,10\n"))

    def test_separators_and_odd_numbers_refused(self):
        head = "platform,post_id,boosted,reach\n"
        for bad in ('"1,200"', "1.200", '"1,5"', "-100", "nan", "inf", "12.5"):
            self.assertIn("plain whole number", fails(head + f"facebook,f1,no,{bad}\n"), bad)
        # an unquoted comma splits the cell: refused too, by the cell count check
        self.assertIn("5 cells, header has 4", fails(head + "facebook,f1,no,1,5\n"))

    def test_decimal_column_allowed_when_named(self):
        out = ok("platform,post_id,boosted,watch_time\nyoutube,y1,no,12.5\n", "--decimal", "watch_time")
        self.assertIn("| youtube | tự nhiên | 1 | 12.50 |", out)
        out = ok("platform,post_id,boosted,watch_time\nyt,a,no,0.4\nyt,b,no,0.6\nyt,c,no,12.5\n", "--decimal", "watch_time")
        self.assertIn("| yt | tự nhiên | 3 | 0.60 |", out)
        self.assertIn("plain non-negative number", fails("platform,post_id,boosted,watch_time\nyoutube,y1,no,1,5\n".replace("1,5", '"1,5"'), "--decimal", "watch_time"))

    def test_repeated_column_and_post_fail(self):
        self.assertIn("repeated column(s) reach", fails("platform,post_id,boosted,reach,reach\nfacebook,f1,no,100,9999\n"))
        self.assertIn("already on line 2", fails("platform,post_id,boosted,reach\nfacebook,c,no,1\nFacebook,c,no,2\n"))

    def test_platform_case_merged(self):
        out = ok("platform,post_id,boosted,reach\nFacebook,a,no,10\nfacebook,b,no,30\n")
        self.assertIn("| facebook | tự nhiên | 2 | 20 |", out)

    def test_zero_denominator_and_over_100_flagged(self):
        out = ok("platform,post_id,boosted,reach,engagements\nx,a,no,0,5\nx,b,no,10,20\n", "--rate", "ERR=engagements/reach")
        self.assertIn("x tự nhiên: ERR có reach = 0 ở 1/2 bài", out)
        self.assertIn("x tự nhiên: ERR trên 100% ở b", out)

    def test_boosted_only_platform_still_listed(self):
        out = ok("platform,post_id,boosted,reach,engagements\nlinkedin,l1,yes,100,5\n", "--rate", "ERR=engagements/reach")
        self.assertIn("- linkedin: chỉ có bài quảng cáo, không xếp hạng", out)

    def test_non_ascii_digits_and_blank_header_refused(self):
        self.assertIn("plain whole number", fails("platform,post_id,boosted,reach\nfacebook,f1,no,\u0661\u0662\u0663\n"))
        self.assertIn("has no name", fails("platform,post_id,boosted,reach,\nfacebook,f1,no,10,\n"))

    def test_pipe_in_text_escaped(self):
        out = ok("platform,post_id,boosted,reach,engagements\nfb|x,a|b,no,10,1\nfb|x,c,no,10,2\n", "--rate", "ERR=engagements/reach", "--top", "1")
        self.assertIn("| fb\\|x | tự nhiên | 2 |", out)
        self.assertIn("kém nhất a\\|b (10.00%)", out)

    def test_half_median_of_counts_kept(self):
        out = ok("platform,post_id,boosted,engagements\nx,a,no,2\nx,b,no,3\n")
        self.assertIn("| x | tự nhiên | 2 | 2.5 |", out)

    def test_top_must_be_positive(self):
        with self.assertRaises(SystemExit), contextlib.redirect_stderr(io.StringIO()):
            readout_stats.main(["x.csv", "--top", "0"])


if __name__ == "__main__":
    unittest.main()
