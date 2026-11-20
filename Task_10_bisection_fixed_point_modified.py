"""Task 10 - Bisection and fixed-point iteration: the SAME program with parameters / inputs CHANGED.

What was changed and why the result differs: see docs/Task_10_bisection_fixed_point.md, section C.
"""
from pathlib import Path
import numpy as np
from scipy.optimize import root_scalar
import matplotlib.pyplot as plt

FIG_DIR = Path(__file__).resolve().parents[2] / "figures"
FIG_DIR.mkdir(exist_ok=True)

def fixed_point(g, x0, tol=1e-10, max_iter=100):
    x = x0
    for i in range(1, max_iter + 1):
        x_new = g(x)
        if abs(x_new - x) < tol:
            return x_new, i
        x = x_new
    return x, max_iter

# ---------------------------------------------------------------- Part A
print("=== PART A: change tau, the bracket and the rearrangement ===")
for tau in (20.0, 10.0):
    f = lambda T, tau=tau: T - 25 - 10 * np.exp(-T / tau)
    g = lambda T, tau=tau: 25 + 10 * np.exp(-T / tau)
    for bracket in ([20, 40], [27, 28] if tau == 20 else [25, 26]):
        s = root_scalar(f, bracket=bracket, method="bisect", xtol=1e-10)
        print(f"tau={tau:4.0f}, bracket={bracket}: root {s.root:.6f} C in {s.iterations} bisection steps")
    root_fp, its = fixed_point(g, 30.0)
    print(f"tau={tau:4.0f}, fixed point T=25+10exp(-T/tau): {root_fp:.6f} C in {its} steps")

print("\nA different rearrangement of the SAME equation: T = -20 ln((T-25)/10)")
T = 30.0
with np.errstate(invalid="ignore", divide="ignore"):
    for step in range(1, 6):
        T = -20 * np.log((T - 25) / 10)
        print(f"  step {step}: T = {T}")
        if not np.isfinite(T):
            print("  -> the iteration has left the valid domain: it diverges")
            break
