"""Task 15 - Numerical differentiation: the SAME program with parameters / inputs CHANGED.

What was changed and why the result differs: see docs/Task_15_numerical_differentiation.md, section C.
"""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

FIG_DIR = Path(__file__).resolve().parents[2] / "figures"
FIG_DIR.mkdir(exist_ok=True)

# ---------------------------------------------------------------- Part A
print("=== PART A: change the step size h ===")
x0, exact = 1.0, np.cos(1.0)
hs = 10.0 ** -np.arange(1, 16)
fwd_err, cen_err = [], []
print(f"{'h':>8} {'forward error':>15} {'central error':>15}")
for h in hs:
    fwd = (np.sin(x0 + h) - np.sin(x0)) / h
    cen = (np.sin(x0 + h) - np.sin(x0 - h)) / (2 * h)
    fwd_err.append(abs(fwd - exact))
    cen_err.append(abs(cen - exact))
    print(f"{h:8.0e} {fwd_err[-1]:15.3e} {cen_err[-1]:15.3e}")
best = hs[int(np.argmin(cen_err))]
print(f"Smallest central-difference error occurs near h = {best:.0e}")

plt.figure()
plt.loglog(hs, fwd_err, "o-", label="forward difference")
plt.loglog(hs, cen_err, "s-", label="central difference")
plt.xlabel("step size h")
plt.ylabel("absolute error")
plt.title("Error of numerical derivative of sin(x) at x = 1")
plt.legend()
plt.grid(True, which="both")
plt.savefig(FIG_DIR / "Task_15_modified_step_size.png", dpi=150, bbox_inches="tight")
plt.show()
