"""Task 2 - NumPy arrays: a SIMILAR program applied to a different REAL-WORLD case.

Assumptions, input data, output and interpretation: see docs/Task_02_numpy_arrays.md, section E.
"""
import numpy as np

# ---------------------------------------------------------------- Part B
print("\n=== PART B: greenhouse soil-moisture sensor ===")
# 12 readings, one every 2 hours (00:00 to 22:00), soil moisture in percent
hours = np.arange(0, 24, 2)
moisture = np.array([42, 40, 38, 35, 31, 28, 26, 33, 41, 45, 44, 43], dtype=float)
threshold = 30.0            # irrigation is needed when moisture falls below 30 %

print(f"Mean moisture: {moisture.mean():.2f} %")
print(f"Minimum: {moisture.min():.1f} % at {hours[moisture.argmin()]:02d}:00")
print(f"Maximum: {moisture.max():.1f} % at {hours[moisture.argmax()]:02d}:00")

below = moisture < threshold                       # boolean mask, no loop needed
print("Readings below threshold:", int(below.sum()),
      "at hours", hours[below].tolist())

# Min-max normalisation to a 0-1 scale (vectorized)
normalised = (moisture - moisture.min()) / (moisture.max() - moisture.min())
print("Normalised readings:", np.round(normalised, 2))
