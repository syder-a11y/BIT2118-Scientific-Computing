"""Task 20 - Monte Carlo methods: the SAME program with parameters / inputs CHANGED.

What was changed and why the result differs: see docs/Task_20_monte_carlo.md, section C.
"""
from pathlib import Path
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

FIG_DIR = Path(__file__).resolve().parents[2] / "figures"
FIG_DIR.mkdir(exist_ok=True)

# ---------------------------------------------------------------- Part A
print("=== PART A: change N and the mean demand ===")
capacity, std = 1000.0, 120.0
rng = np.random.default_rng(7)
for mean in (850.0, 950.0):
    true_p = norm.sf(capacity, loc=mean, scale=std)         # exact answer for a normal distribution
    print(f"\nmean demand {mean:.0f}: exact overload probability = {true_p:.4%}")
    print(f"{'N':>10} {'estimate':>10} {'abs error':>10} {'std. error':>11}")
    for N in (100, 1_000, 10_000, 100_000, 1_000_000):
        est = (rng.normal(mean, std, N) > capacity).mean()
        se = np.sqrt(true_p * (1 - true_p) / N)
        print(f"{N:10,d} {est:10.4%} {abs(est - true_p):10.4%} {se:11.4%}")
