"""Task 14 - Curve fitting: a SIMILAR program applied to a different REAL-WORLD case.

Assumptions, input data, output and interpretation: see docs/Task_14_curve_fitting.md, section E.
"""
from pathlib import Path
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

FIG_DIR = Path(__file__).resolve().parents[2] / "figures"
FIG_DIR.mkdir(exist_ok=True)

def rmse(y, yhat):
    return float(np.sqrt(np.mean((y - yhat) ** 2)))

# ---------------------------------------------------------------- Part B
print("\n=== PART B: logistic growth of app users ===")
# Synthetic monthly active users (thousands) for the first ten months after launch.
months = np.arange(1, 11, dtype=float)
active = np.array([4, 7, 12, 21, 35, 52, 71, 88, 99, 107], dtype=float)

def logistic(t, L, k, t0):
    return L / (1 + np.exp(-k * (t - t0)))

p, cov = curve_fit(logistic, months, active, p0=[120, 0.6, 6])
L, k, t0 = p
err = np.sqrt(np.diag(cov))
fitted = logistic(months, *p)
ss_res = np.sum((active - fitted) ** 2)
ss_tot = np.sum((active - active.mean()) ** 2)

print(f"Carrying capacity L = {L:.1f} +/- {err[0]:.1f} thousand users")
print(f"Growth rate k = {k:.3f} +/- {err[1]:.3f} per month")
print(f"Midpoint t0 = {t0:.2f} +/- {err[2]:.2f} months")
print(f"RMSE = {rmse(active, fitted):.2f} thousand, R^2 = {1 - ss_res / ss_tot:.4f}")
for m in (11, 12, 18):
    print(f"Forecast for month {m}: {logistic(m, *p):.1f} thousand users")

t_plot = np.linspace(1, 18, 300)
plt.scatter(months, active, label="observed")
plt.plot(t_plot, logistic(t_plot, *p), label="logistic fit")
plt.axhline(L, linestyle="--", color="gray", label="fitted limit L")
plt.xlabel("Month since launch")
plt.ylabel("Active users (thousands)")
plt.title("Logistic growth of app users")
plt.legend()
plt.grid(True)
plt.savefig(FIG_DIR / "Task_14_modified_logistic.png", dpi=150, bbox_inches="tight")
plt.show()
