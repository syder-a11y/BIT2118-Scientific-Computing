"""Task 19 - Numerical optimization: a SIMILAR program applied to a different REAL-WORLD case.

Assumptions, input data, output and interpretation: see docs/Task_19_optimization.md, section E.
"""
import numpy as np
from scipy.optimize import minimize, linprog

# ---------------------------------------------------------------- Part B
print("\n=== PART B: bakery product mix ===")
# x = loaves per day, y = cakes per day. Profit: 12 per loaf, 45 per cake.
# Flour: 0.5 kg per loaf, 1.0 kg per cake, 100 kg available.
# Labour: 0.1 h per loaf, 0.3 h per cake, 24 h available.
# Oven/market limit: at most 70 cakes per day.
profit = lambda z: 12 * z[0] + 45 * z[1]
constraints = [
    {"type": "ineq", "fun": lambda z: 100 - (0.5 * z[0] + 1.0 * z[1])},
    {"type": "ineq", "fun": lambda z: 24 - (0.1 * z[0] + 0.3 * z[1])},
]
res = minimize(lambda z: -profit(z), x0=[10, 10], method="SLSQP",
               bounds=[(0, None), (0, 70)], constraints=constraints)
x, y = res.x
print(f"Optimum (SLSQP): {x:.2f} loaves, {y:.2f} cakes, daily profit {profit(res.x):.2f}")
print(f"Flour used {0.5 * x + y:.1f} / 100 kg | labour used {0.1 * x + 0.3 * y:.1f} / 24 h | cakes {y:.1f} / 70")

lp = linprog(c=[-12, -45], A_ub=[[0.5, 1.0], [0.1, 0.3]], b_ub=[100, 24], bounds=[(0, None), (0, 70)])
print(f"Cross-check with linprog: {lp.x.round(2)}, profit {-lp.fun:.2f}")

best = max(((profit([a, b]), a, b) for a in range(0, 251) for b in range(0, 71)
            if 0.5 * a + b <= 100 and 0.1 * a + 0.3 * b <= 24), key=lambda t: t[0])
print(f"Brute-force whole-number check (profit, loaves, cakes): {best}")
for name, z in [("only loaves", [200, 0]), ("only cakes", [0, 70]), ("balanced guess", [120, 40])]:
    ok = 0.5 * z[0] + z[1] <= 100 and 0.1 * z[0] + 0.3 * z[1] <= 24
    print(f"  {name:15s} {z}: profit {profit(z)}, feasible: {ok}")
