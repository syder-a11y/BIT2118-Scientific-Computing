"""Task 10 - Bisection and fixed-point iteration: a SIMILAR program applied to a different REAL-WORLD case.

Assumptions, input data, output and interpretation: see docs/Task_10_bisection_fixed_point.md, section E.
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

# ---------------------------------------------------------------- Part B
print("\n=== PART B: break-even sales ===")
# Revenue shows diminishing returns: R(q) = 300*sqrt(q); cost: C(q) = 4000 + 2q.
# Profit f(q) = R(q) - C(q). Break-even means f(q) = 0.
def profit(q):
    return 300 * np.sqrt(q) - 2 * q - 4000

low = root_scalar(profit, bracket=[100, 400], method="bisect", xtol=1e-8)
high = root_scalar(profit, bracket=[5625, 100000], method="bisect", xtol=1e-8)
check = root_scalar(profit, bracket=[100, 400], method="brentq")
best_q = 75.0 ** 2                      # profit is largest where dR/dq = dC/dq -> sqrt(q)=75

print(f"Lower break-even: {low.root:,.2f} units ({low.iterations} bisection steps; brentq gives {check.root:,.2f})")
print(f"Upper break-even: {high.root:,.2f} units ({high.iterations} bisection steps)")
print(f"Most profitable volume: {best_q:,.0f} units, profit = {profit(best_q):,.0f}")
print(f"Profit at 100 units: {profit(100):,.0f}  |  at 400 units: {profit(400):,.0f}")

q = np.linspace(1, 20000, 600)
plt.plot(q, profit(q))
plt.axhline(0, color="k", linewidth=0.8)
plt.axvline(low.root, linestyle="--", color="g", label=f"break-even {low.root:,.0f}")
plt.axvline(high.root, linestyle="--", color="r", label=f"break-even {high.root:,.0f}")
plt.xlabel("Units sold per month")
plt.ylabel("Profit")
plt.title("Break-even points with diminishing returns")
plt.legend()
plt.grid(True)
plt.savefig(FIG_DIR / "Task_10_modified_breakeven.png", dpi=150, bbox_inches="tight")
plt.show()
