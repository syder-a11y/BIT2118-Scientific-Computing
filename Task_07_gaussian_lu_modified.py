"""Task 7 - Gaussian elimination and LU decomposition: the SAME program with parameters / inputs CHANGED.

What was changed and why the result differs: see docs/Task_07_gaussian_lu.md, section C.
"""
import time
import numpy as np
from scipy.linalg import lu, lu_factor, lu_solve

# ---------------------------------------------------------------- Part A
print("=== PART A: change the size and number of measurement vectors ===")
A_small = np.array([[4.0, -1.0, 0.0], [-1.0, 4.0, -1.0], [0.0, -1.0, 3.0]])
P, L, U = lu(A_small)
print("L =\n", np.round(L, 4))
print("U =\n", np.round(U, 4))
print("max |P L U - A| =", np.abs(P @ L @ U - A_small).max())

rng = np.random.default_rng(1)
for n, m in [(3, 3), (600, 300)]:
    A = rng.random((n, n)) + n * np.eye(n)        # diagonally dominant, well behaved
    B = rng.random((n, m))                        # m different measurement vectors

    t0 = time.perf_counter()
    X1 = np.column_stack([np.linalg.solve(A, B[:, j]) for j in range(m)])
    t_each = time.perf_counter() - t0

    t0 = time.perf_counter()
    lu_piv = lu_factor(A)
    X2 = np.column_stack([lu_solve(lu_piv, B[:, j]) for j in range(m)])
    t_lu = time.perf_counter() - t0

    print(f"n={n:4d}, {m:3d} vectors: solve each time {t_each:.4f} s | "
          f"factor once {t_lu:.4f} s | same answer: {np.allclose(X1, X2)}")
