"""Task 8 - Iterative methods: a SIMILAR program applied to a different REAL-WORLD case.

Assumptions, input data, output and interpretation: see docs/Task_08_iterative_linear.md, section E.
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

# ---------------------------------------------------------------- Part B
print("\n=== PART B: 2-D heated plate (8 x 8 interior grid) ===")
n = 8                                               # interior points per side -> 64 unknowns
K = 2 * np.eye(n) - np.eye(n, k=1) - np.eye(n, k=-1)
A2 = np.kron(np.eye(n), K) + np.kron(K, np.eye(n))  # 4 on the diagonal, -1 for each neighbour
b2 = np.zeros(n * n)
b2[:n] = 100.0                                       # top edge held at 100 C, other edges at 0 C

x_j, it_j = jacobi(A2, b2, tol=1e-6)
x_g, it_g = gauss_seidel(A2, b2, tol=1e-6)
x_d = np.linalg.solve(A2, b2)
print(f"Jacobi: {it_j} iterations, max error vs direct solve {np.abs(x_j - x_d).max():.2e}")
print(f"Gauss-Seidel: {it_g} iterations, max error vs direct solve {np.abs(x_g - x_d).max():.2e}")
print(f"Hottest interior point: {x_d.max():.2f} C, coolest: {x_d.min():.2f} C")
print(f"Centre of the plate: {x_d.reshape(n, n)[n // 2, n // 2]:.2f} C")

plate = np.zeros((n + 2, n + 2))
plate[0, :] = 100.0
plate[1:-1, 1:-1] = x_g.reshape(n, n)
fig, ax = plt.subplots(figsize=(5.5, 4.5))
im = ax.imshow(plate, cmap="inferno")
fig.colorbar(im, label="Temperature (C)")
ax.set_title("Steady-state temperature of a heated plate")
ax.set_xlabel("column")
ax.set_ylabel("row (top edge = 100 C)")
fig.savefig(FIG_DIR / "Task_08_modified_plate.png", dpi=150, bbox_inches="tight")
plt.show()
