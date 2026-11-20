"""Task 6 - Systems of linear equations: the SAME program with parameters / inputs CHANGED.

What was changed and why the result differs: see docs/Task_06_linear_systems.md, section C.
"""
import numpy as np

# ---------------------------------------------------------------- Part A
print("=== PART A: change the right-hand side / the matrix ===")
A = np.array([[4.0, 2.0], [8.0, 12.0]])

for label, b in [("original totals (20 CPU, 72 GB)", [20.0, 72.0]),
                 ("new totals      (26 CPU, 84 GB)", [26.0, 84.0])]:
    x = np.linalg.solve(A, np.array(b))
    print(f"{label}: Type A = {x[0]:.3f}, Type B = {x[1]:.3f}")
print("-> the second answer is not a whole number of servers, so those totals cannot")
print("   come from real servers; the measurements must be wrong or incomplete.")

A_bad = np.array([[4.0, 2.0], [8.0, 4.0]])          # row 2 = 2 x row 1
print("\nDeterminant when the two server types look identical:", np.linalg.det(A_bad))
try:
    np.linalg.solve(A_bad, np.array([20.0, 40.0]))
except np.linalg.LinAlgError as err:
    print("np.linalg.solve failed:", err)
