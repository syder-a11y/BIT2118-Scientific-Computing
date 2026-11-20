"""Task 13 - Interpolation: the SAME program with parameters / inputs CHANGED.

What was changed and why the result differs: see docs/Task_13_interpolation.md, section C.
"""
from pathlib import Path
import numpy as np
from scipy.interpolate import interp1d, CubicSpline
import matplotlib.pyplot as plt

FIG_DIR = Path(__file__).resolve().parents[2] / "figures"
FIG_DIR.mkdir(exist_ok=True)

# ---------------------------------------------------------------- Part A
print("=== PART A: fewer measurements ===")
hours = np.array([8, 9, 10, 11, 12, 13, 14], dtype=float)
temp = np.array([18.0, 20.0, 22.5, 24.0, 25.0, 25.5, 25.0])
reference = CubicSpline(hours, temp)(10.5)

coarse = np.array([8, 10, 12, 14], dtype=float)           # every second hour
coarse_temp = np.interp(coarse, hours, temp)
for label, h, t in [("hourly data", hours, temp), ("two-hourly data", coarse, coarse_temp)]:
    lin = float(interp1d(h, t)(10.5))
    cub = float(CubicSpline(h, t)(10.5))
    print(f"{label:16s} 10:30 -> linear {lin:.2f} C | cubic {cub:.2f} C")
print(f"(reference: cubic spline on the full hourly data = {reference:.2f} C)")
