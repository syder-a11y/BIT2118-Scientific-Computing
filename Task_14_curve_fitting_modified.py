"""Task 14 - Curve fitting: the SAME program with parameters / inputs CHANGED.

What was changed and why the result differs: see docs/Task_14_curve_fitting.md, section C.
"""
from pathlib import Path
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

FIG_DIR = Path(__file__).resolve().parents[2] / "figures"
FIG_DIR.mkdir(exist_ok=True)

def rmse(y, yhat):
    return float(np.sqrt(np.mean((y - yhat) ** 2)))

# ---------------------------------------------------------------- Part A
print("=== PART A: change the model and add an outlier ===")
users = np.array([50, 100, 150, 200, 250, 300, 350], dtype=float)
resp = np.array([82, 95, 115, 145, 185, 238, 305], dtype=float)

linear = lambda x, a, b: a * x + b
quad = lambda x, a, b, c: a * x ** 2 + b * x + c
expo = lambda x, a, b, c: a * np.exp(b * x) + c

print(f"{'model':<12} {'RMSE (ms)':>10} {'prediction at 400 users':>26}")
for name, f, p0 in [("linear", linear, None), ("quadratic", quad, None),
                    ("exponential", expo, [10, 0.006, 70])]:
    p, _ = curve_fit(f, users, resp, p0=p0, maxfev=20000)
    print(f"{name:<12} {rmse(resp, f(users, *p)):>10.2f} {f(400, *p):>22.1f} ms")

resp_out = resp.copy()
resp_out[-1] = 500.0                      # one bad measurement at 350 users
p_ok, _ = curve_fit(quad, users, resp)
p_bad, _ = curve_fit(quad, users, resp_out)
print("\nQuadratic fit, a / b / c:")
print("  clean data     :", np.round(p_ok, 5))
print("  with an outlier:", np.round(p_bad, 5))
print(f"  prediction at 400 users: {quad(400, *p_ok):.1f} ms (clean) vs {quad(400, *p_bad):.1f} ms (outlier)")
