"""Task 17 - Euler's method: the SAME program with parameters / inputs CHANGED.

What was changed and why the result differs: see docs/Task_17_euler_ode.md, section C.
"""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

FIG_DIR = Path(__file__).resolve().parents[2] / "figures"
FIG_DIR.mkdir(exist_ok=True)

def euler(f, y0, h, end):
    t = np.arange(0, end + h / 2, h)
    y = np.zeros_like(t)
    y[0] = y0
    for i in range(len(t) - 1):
        y[i + 1] = y[i] + h * f(y[i])
    return t, y

# ---------------------------------------------------------------- Part A
print("=== PART A: change the step size h (cooling, k = 0.12) ===")
T_amb, T0, k = 25.0, 90.0, 0.12
cool = lambda T: -k * (T - T_amb)
exact_30 = T_amb + (T0 - T_amb) * np.exp(-k * 30)

hs = [5.0, 2.0, 1.0, 0.5, 0.1, 0.01]
errors = []
print(f"{'h (min)':>8} {'Euler at 30 min':>16} {'error':>10}")
for h in hs:
    _, T = euler(cool, T0, h, 30.0)
    errors.append(abs(T[-1] - exact_30))
    print(f"{h:8.2f} {T[-1]:16.4f} {errors[-1]:10.5f}")
print(f"Exact value: {exact_30:.4f} C. Halving h roughly halves the error (first-order method).")

print("\nToo-large step: stability limit is h < 2/k =", round(2 / k, 2), "minutes")
for h in (10.0, 20.0):
    _, T = euler(cool, T0, h, 60.0)
    print(f"  h = {h:4.1f}: temperatures {np.round(T, 1)}")

plt.figure()
plt.loglog(hs, errors, "o-")
plt.xlabel("step size h (minutes)")
plt.ylabel("absolute error at 30 min (C)")
plt.title("Euler error shrinks in proportion to h")
plt.grid(True, which="both")
plt.savefig(FIG_DIR / "Task_17_modified_error_vs_h.png", dpi=150, bbox_inches="tight")
plt.show()
