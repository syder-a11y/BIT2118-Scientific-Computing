"""Task 16 - Numerical integration: a SIMILAR program applied to a different REAL-WORLD case.

Assumptions, input data, output and interpretation: see docs/Task_16_numerical_integration.md, section E.
"""
import numpy as np
from scipy.integrate import simpson

# ---------------------------------------------------------------- Part B
print("\n=== PART B: delivery motorbike distance ===")
minutes = np.arange(0, 65, 5, dtype=float)                 # a reading every 5 minutes
speed_kmh = np.array([0, 18, 32, 41, 38, 25, 0, 0, 20, 35, 42, 30, 0], dtype=float)
hours = minutes / 60.0

dist_trap = np.trapezoid(speed_kmh, hours)                 # km
dist_simp = simpson(speed_kmh, x=hours)

print(f"Distance by trapezoidal rule: {dist_trap:.3f} km")
print(f"Distance by Simpson's rule:   {dist_simp:.3f} km")
print(f"Difference: {abs(dist_simp - dist_trap):.3f} km")
print(f"Average speed over the hour: {dist_trap / 1.0:.2f} km/h")
print(f"Time stationary (two consecutive zero readings): "
      f"{5 * np.sum((speed_kmh[:-1] == 0) & (speed_kmh[1:] == 0))} minutes")
