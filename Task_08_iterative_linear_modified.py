"""Task 8 - Iterative methods: the SAME program with parameters / inputs CHANGED.

What was changed and why the result differs: see docs/Task_08_iterative_linear.md, section C.
"""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

FIG_DIR = Path(__file__).resolve().parents[2] / "figures"
FIG_DIR.mkdir(exist_ok=True)

def jacobi(A, b, tol=1e-8, max_iter=20000):
    D = np.diag(A)
    R = A - np.diagflat(D)
    x = np.zeros_like(b)
    count = 0
    for count in range(1, max_iter + 1):
        x_new = (b - R @ x) / D
        done = np.linalg.norm(x_new - x, ord=np.inf) < tol
        x = x_new
        if done:
            break
    return x, count

def gauss_seidel(A, b, tol=1e-8, max_iter=20000):
    x = np.zeros_like(b)
    count = 0
    for count in range(1, max_iter + 1):
        old = x.copy()
        for i in range(len(b)):
            x[i] = (b[i] - A[i, :i] @ x[:i] - A[i, i + 1:] @ old[i + 1:]) / A[i, i]
        if np.linalg.norm(x - old, ord=np.inf) < tol:
            break
    return x, count

# ---------------------------------------------------------------- Part A
print("=== PART A: change tolerance and boundary temperatures ===")
A = 2 * np.eye(5) - np.eye(5, k=1) - np.eye(5, k=-1)
for left, right in [(100.0, 20.0), (80.0, 30.0)]:
    b = np.array([left, 0, 0, 0, right])
    exact = np.linalg.solve(A, b)
    print(f"\nboundaries {left:.0f} C / {right:.0f} C -> exact interior temps {np.round(exact, 3)}")
    for tol in (1e-4, 1e-8, 1e-12):
        xj, nj = jacobi(A, b, tol)
        xg, ng = gauss_seidel(A, b, tol)
        print(f"  tol={tol:.0e}: Jacobi {nj:3d} iterations (max error {np.abs(xj - exact).max():.1e}) | "
              f"Gauss-Seidel {ng:3d} iterations (max error {np.abs(xg - exact).max():.1e})")
