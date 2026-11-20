"""Task 5 - Matrix algebra: a SIMILAR program applied to a different REAL-WORLD case.

Assumptions, input data, output and interpretation: see docs/Task_05_matrix_algebra.md, section E.
"""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

FIG_DIR = Path(__file__).resolve().parents[2] / "figures"
FIG_DIR.mkdir(exist_ok=True)

def rot(deg):
    a = np.deg2rad(deg)
    return np.array([[np.cos(a), -np.sin(a)], [np.sin(a), np.cos(a)]])

def poly_area(p):
    """Shoelace formula for the area of a polygon given as rows of [x, y]."""
    x, y = p[:, 0], p[:, 1]
    return 0.5 * abs(np.dot(x, np.roll(y, -1)) - np.dot(y, np.roll(x, -1)))

# ---------------------------------------------------------------- Part B
print("\n=== PART B: robot footprint, homogeneous coordinates ===")
triangle = np.array([[0, 0], [4, 0], [2, 3]], dtype=float)     # metres
centroid = triangle.mean(axis=0)

def translate(tx, ty):
    return np.array([[1, 0, tx], [0, 1, ty], [0, 0, 1.0]])

R = np.eye(3)
R[:2, :2] = rot(30)

# rotate 30 deg about the centroid, then move the robot 5 m east and 2 m north
M = translate(5, 2) @ translate(*centroid) @ R @ translate(*-centroid)

homog = np.column_stack([triangle, np.ones(3)])     # each row = [x, y, 1]
moved = (M @ homog.T).T[:, :2]

print("Combined 3x3 matrix:\n", np.round(M, 4))
print("Original corners:\n", triangle)
print("New corners:\n", np.round(moved, 4))
print("New centroid:", np.round(moved.mean(axis=0), 4), "(expected [7. 3.])")

def sides(p):
    return np.linalg.norm(p - np.roll(p, -1, axis=0), axis=1)

print("Side lengths before:", np.round(sides(triangle), 4))
print("Side lengths after: ", np.round(sides(moved), 4))
print(f"Area before {poly_area(triangle):.3f} m^2, after {poly_area(moved):.3f} m^2")

fig, ax = plt.subplots(figsize=(5, 4))
for p, lab in [(triangle, "start"), (moved, "after rotate + move")]:
    closed = np.vstack([p, p[0]])
    ax.plot(closed[:, 0], closed[:, 1], marker="o", label=lab)
ax.set_aspect("equal")
ax.set_xlabel("x (m)")
ax.set_ylabel("y (m)")
ax.set_title("Robot footprint before and after transformation")
ax.grid(True)
ax.legend()
fig.savefig(FIG_DIR / "Task_05_modified_robot.png", dpi=150, bbox_inches="tight")
plt.show()
