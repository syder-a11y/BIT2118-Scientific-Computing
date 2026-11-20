"""Task 17 - Euler's method: a SIMILAR program applied to a different REAL-WORLD case.

Assumptions, input data, output and interpretation: see docs/Task_17_euler_ode.md, section E.
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

# ---------------------------------------------------------------- Part B
print("\n=== PART B: fish population in a pond (logistic growth) ===")
# dP/dt = r P (1 - P/K): P = number of fish, r = growth rate per month, K = pond capacity
r, K, P0 = 0.4, 1000.0, 50.0
growth = lambda P: r * P * (1 - P / K)
exact = lambda t: K / (1 + (K - P0) / P0 * np.exp(-r * t))

t1, P1 = euler(growth, P0, 1.0, 24.0)
t2, P2 = euler(growth, P0, 0.1, 24.0)
print(f"After 24 months: exact {exact(24):.2f} | Euler h=1 month {P1[-1]:.2f} | Euler h=0.1 month {P2[-1]:.2f}")
print(f"Largest error over the 24 months: h=1 -> {np.max(np.abs(P1 - exact(t1))):.2f} fish, "
      f"h=0.1 -> {np.max(np.abs(P2 - exact(t2))):.2f} fish")
t_half_exact = np.log((K - P0) / P0) / r
t_half_euler = np.interp(K / 2, P2, t2)
print(f"Time to reach half the capacity (500 fish): exact {t_half_exact:.2f} months, Euler(h=0.1) {t_half_euler:.2f}")
print(f"Maximum growth rate {r * K / 4:.0f} fish/month occurs at P = K/2 = {K / 2:.0f}")

tt = np.linspace(0, 24, 300)
plt.figure()
plt.plot(tt, exact(tt), label="exact")
plt.plot(t1, P1, "o-", markersize=4, label="Euler h = 1 month")
plt.plot(t2, P2, "--", label="Euler h = 0.1 month")
plt.xlabel("Months")
plt.ylabel("Fish in pond")
plt.title("Logistic growth of a pond population")
plt.legend()
plt.grid(True)
plt.savefig(FIG_DIR / "Task_17_modified_fish_pond.png", dpi=150, bbox_inches="tight")
plt.show()
