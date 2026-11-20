"""Task 15 - Numerical differentiation: a SIMILAR program applied to a different REAL-WORLD case.

Assumptions, input data, output and interpretation: see docs/Task_15_numerical_differentiation.md, section E.
"""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

FIG_DIR = Path(__file__).resolve().parents[2] / "figures"
FIG_DIR.mkdir(exist_ok=True)

# ---------------------------------------------------------------- Part B
print("\n=== PART B: motorbike acceleration from velocity data ===")
t = np.arange(0, 11, dtype=float)                      # seconds
v = np.array([0.0, 2.1, 4.3, 6.2, 8.4, 10.1, 11.8, 13.0, 13.8, 14.2, 14.3])   # m/s

acc = np.zeros_like(v)
acc[0] = (v[1] - v[0]) / (t[1] - t[0])                 # forward difference
acc[1:-1] = (v[2:] - v[:-2]) / (t[2:] - t[:-2])        # central differences
acc[-1] = (v[-1] - v[-2]) / (t[-1] - t[-2])            # backward difference
acc_np = np.gradient(v, t, edge_order=2)               # NumPy's built-in version

print(f"{'t (s)':>6} {'v (m/s)':>8} {'a manual':>9} {'a np.gradient':>14}")
for ti, vi, ai, bi in zip(t, v, acc, acc_np):
    print(f"{ti:6.0f} {vi:8.1f} {ai:9.2f} {bi:14.2f}")
print(f"Peak acceleration {acc.max():.2f} m/s^2 at t = {t[acc.argmax()]:.0f} s")
print(f"Acceleration at the end of the run: {acc[-1]:.2f} m/s^2 (bike is reaching top speed)")

fig, ax = plt.subplots(2, 1, sharex=True, figsize=(6, 5))
ax[0].plot(t, v, "o-")
ax[0].set_ylabel("velocity (m/s)")
ax[0].grid(True)
ax[1].plot(t, acc, "o-", color="tab:red")
ax[1].set_ylabel("acceleration (m/s^2)")
ax[1].set_xlabel("time (s)")
ax[1].grid(True)
fig.suptitle("Motorbike velocity and estimated acceleration")
fig.savefig(FIG_DIR / "Task_15_modified_motorbike.png", dpi=150, bbox_inches="tight")
plt.show()
