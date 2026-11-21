"""Significance thresholds and MDE for a two-arm app-vs-control C-BARQ study.

Variance inputs come from Bohland 2023 pairs (``domain_dedup.csv``,
``source == 'bohland_2023'``): SD of the change between two waves and the
between-wave correlation r per domain. Outputs, per domain, in C-BARQ points:

- ``crit``: |difference in mean change| above which p < alpha (two-sided);
- ``mde``: true effect detected with the requested power.

Two analyses: change-score t-test and ANCOVA (follow-up ~ arm + baseline),
residual SD = sd_follow * sqrt(1 - r^2). Multiplicity: Bonferroni over
``--primary`` domains.

Examples::

    python rct_power_thresholds.py
    python rct_power_thresholds.py --n 60 --primary 2 --dropout 0.16
    python rct_power_thresholds.py --domains separation_related_problems stranger_directed_fear
    python rct_power_thresholds.py --solve-n 0.3 --primary 2
"""

from __future__ import annotations

import argparse
import math
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats

ROOT = Path(__file__).resolve().parents[1]
DOMAIN_CSV = ROOT / "datasets" / "unified" / "domain_dedup.csv"

DOMAINS = [
    "stranger_directed_aggression",
    "owner_directed_aggression",
    "dog_directed_aggression",
    "familiar_dog_aggression",
    "stranger_directed_fear",
    "nonsocial_fear",
    "dog_directed_fear",
    "touch_sensitivity",
    "separation_related_problems",
    "attachment_attention_seeking",
    "training_difficulty",
    "excitability",
    "chasing",
    "energy",
]


def domain_variance(baseline: str, follow: str) -> pd.DataFrame:
    d = pd.read_csv(DOMAIN_CSV)
    d = d[d["source"] == "bohland_2023"]
    a = d[d["wave"] == baseline].set_index("dog_id")
    b = d[d["wave"] == follow].set_index("dog_id")
    rows = []
    for dom in DOMAINS:
        pair = pd.concat([a[dom], b[dom]], axis=1, keys=["x0", "x1"]).dropna()
        r = pair["x0"].corr(pair["x1"])
        rows.append(
            {
                "domain": dom,
                "n_pairs": len(pair),
                "mean_change": (pair["x1"] - pair["x0"]).mean(),
                "sd_change": (pair["x1"] - pair["x0"]).std(ddof=1),
                "r": r,
                "sd_resid": pair["x1"].std(ddof=1) * math.sqrt(1 - r**2),
            }
        )
    return pd.DataFrame(rows).set_index("domain")


def t_quantiles(n1: float, n2: float, alpha: float, power: float, n_cov: int) -> tuple[float, float]:
    df = max(n1 + n2 - 2 - n_cov, 1)
    return stats.t.ppf(1 - alpha / 2, df), stats.t.ppf(power, df)


def thresholds(var: pd.DataFrame, n1: float, n2: float, alpha: float, power: float) -> pd.DataFrame:
    k = math.sqrt(1 / n1 + 1 / n2)
    out = var.copy()
    for method, sd_col, n_cov in (("change", "sd_change", 0), ("ancova", "sd_resid", 1)):
        t_a, t_b = t_quantiles(n1, n2, alpha, power, n_cov)
        se = out[sd_col] * k
        out[f"{method}_se"] = se
        out[f"{method}_crit"] = t_a * se
        out[f"{method}_mde"] = (t_a + t_b) * se
    return out


def solve_n(sd: float, delta: float, alpha: float, power: float) -> int:
    for n in range(4, 5000):
        t_a, t_b = t_quantiles(n, n, alpha, power, 1)
        if (t_a + t_b) * sd * math.sqrt(2 / n) <= delta:
            return n
    return -1


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--n", type=int, default=40, help="enrolled per arm (app)")
    p.add_argument("--n-ctrl", type=int, default=None, help="enrolled in control arm; default = --n")
    p.add_argument("--dropout", type=float, default=0.0, help="share lost by follow-up, e.g. 0.16")
    p.add_argument("--primary", type=int, default=None, help="number of primary domains for Bonferroni; default = number of domains shown")
    p.add_argument("--domains", nargs="+", choices=DOMAINS, default=None)
    p.add_argument("--alpha", type=float, default=0.05)
    p.add_argument("--power", type=float, default=0.80)
    p.add_argument("--baseline", default="d7", choices=["d7", "d30", "d90", "d180"])
    p.add_argument("--follow", default="d30", choices=["d7", "d30", "d90", "d180"])
    p.add_argument("--solve-n", type=float, default=None, metavar="DELTA", help="report n per arm (after dropout) to detect DELTA points with ANCOVA")
    args = p.parse_args()

    domains = args.domains or [d for d in DOMAINS if d != "familiar_dog_aggression"]
    m = args.primary or len(domains)
    alpha_adj = args.alpha / m
    keep = 1 - args.dropout
    n1 = args.n * keep
    n2 = (args.n_ctrl or args.n) * keep

    var = domain_variance(args.baseline, args.follow).loc[domains]
    res = thresholds(var, n1, n2, alpha_adj, args.power)

    print(
        f"waves {args.baseline}->{args.follow}; analysed n = {n1:.0f} + {n2:.0f}; "
        f"alpha = {args.alpha}/{m} = {alpha_adj:.4f}; power = {args.power}"
    )
    cols = ["n_pairs", "mean_change", "sd_change", "r", "change_crit", "change_mde", "ancova_crit", "ancova_mde"]
    with pd.option_context("display.width", 200, "display.float_format", "{:.2f}".format):
        print(res[cols].to_string())

    t_a, t_b = t_quantiles(n1, n2, alpha_adj, args.power, 0)
    print(f"\nstandardised MDE (Cohen d, change-score) = {(t_a + t_b) * math.sqrt(1 / n1 + 1 / n2):.3f}")

    if args.solve_n is not None:
        print(f"\nn per arm (analysed) for ANCOVA MDE <= {args.solve_n}:")
        for dom, sd in res["sd_resid"].items():
            n = solve_n(sd, args.solve_n, alpha_adj, args.power)
            enrol = math.ceil(n / keep) if n > 0 else -1
            print(f"  {dom:30s} analysed {n:4d}  enrol {enrol:4d}")


if __name__ == "__main__":
    main()
