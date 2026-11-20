"""Task 19 - Numerical optimization: the SAME program with parameters / inputs CHANGED.

What was changed and why the result differs: see docs/Task_19_optimization.md, section C.
"""
import numpy as np
from scipy.optimize import minimize, linprog

# ---------------------------------------------------------------- Part A
print("=== PART A: change cost and required capacity ===")
def servers(cost_a, cost_b, need, cap_a=100.0, cap_b=170.0):
    res = minimize(lambda z: cost_a * z[0] + cost_b * z[1], x0=[5, 3], method="SLSQP",
                   bounds=[(0, None), (0, None)],
                   constraints={"type": "ineq", "fun": lambda z: cap_a * z[0] + cap_b * z[1] - need})
    best = None
    for a in range(0, 40):
        for b in range(0, 40):
            if cap_a * a + cap_b * b >= need:
                c = cost_a * a + cost_b * b
                if best is None or c < best[0]:
                    best = (c, a, b)
    return res, best

print(f"{'cost A':>7} {'cost B':>7} {'capacity':>9} | {'A':>6} {'B':>6} {'cost':>7} | whole servers (cost, A, B)")
for ca, cb, need in [(12, 18, 1000), (12, 18, 1500), (9, 18, 1000)]:
    res, best = servers(ca, cb, need)
    print(f"{ca:7d} {cb:7d} {need:9d} | {res.x[0]:6.2f} {res.x[1]:6.2f} {res.fun:7.2f} | {best}")
print("Cost per unit of capacity: A =", round(12 / 100, 4), " B =", round(18 / 170, 4),
      "-> the cheaper capacity wins, and it switches to A when A costs 9.")
