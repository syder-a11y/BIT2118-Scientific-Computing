"""Task 5 - Matrix algebra: the SAME program with parameters / inputs CHANGED.

What was changed and why the result differs: see docs/Task_05_matrix_algebra.md, section C.
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

# ---------------------------------------------------------------- Part A
print("=== PART A: change angle, scale and order ===")
square = np.array([[0, 0], [1, 0], [1, 1], [0, 1]], dtype=float)

cases = {
    "original  (45 deg, scale 2 x 1.5)": rot(45) @ np.diag([2.0, 1.5]),
    "rotate 90 deg only (scale 1 x 1)":   rot(90) @ np.diag([1.0, 1.0]),
    "scale first, rotate second":        np.diag([2.0, 1.5]) @ rot(45),
}
for name, M in cases.items():
    out = square @ M.T
    print(f"{name}\n  det = {np.linalg.det(M):.3f}, new area = {poly_area(out):.3f}")
    print("  transformed corners:\n", np.round(out, 3))
