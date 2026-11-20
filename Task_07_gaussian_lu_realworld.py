"""Task 7 - Gaussian elimination and LU decomposition: a SIMILAR program applied to a different REAL-WORLD case.

Assumptions, input data, output and interpretation: see docs/Task_07_gaussian_lu.md, section E.
"""
import time
import numpy as np
from scipy.linalg import lu, lu_factor, lu_solve

# ---------------------------------------------------------------- Part B
print("\n=== PART B: Leontief input-output model ===")
# C[i][j] = input from sector i needed to produce 1 unit of sector j's output.
# Sector order: Agriculture, Manufacturing, Services. (Illustrative coefficients.)
sectors = ["Agriculture", "Manufacturing", "Services"]
C = np.array([
    [0.20, 0.10, 0.05],
    [0.15, 0.25, 0.10],
    [0.10, 0.20, 0.15],
])
# Gross output x must satisfy x - C x = d  ->  (I - C) x = d
A = np.eye(3) - C
lu_piv = lu_factor(A)                              # factor the economy once

# Final demand (millions of shillings) for three different years
demand_years = {
    "Year 1": np.array([100.0, 150.0, 200.0]),
    "Year 2": np.array([110.0, 160.0, 230.0]),
    "Year 3": np.array([ 90.0, 190.0, 260.0]),
}
for year, d in demand_years.items():
    x = lu_solve(lu_piv, d)
    print(f"{year}: final demand {d} -> gross output "
          + ", ".join(f"{s}={v:.1f}" for s, v in zip(sectors, x)))
    print(f"        residual norm {np.linalg.norm(d - A @ x):.2e}, "
          f"total output / total demand = {x.sum() / d.sum():.3f}")
