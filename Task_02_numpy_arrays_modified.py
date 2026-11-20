"""Task 2 - NumPy arrays: the SAME program with parameters / inputs CHANGED.

What was changed and why the result differs: see docs/Task_02_numpy_arrays.md, section C.
"""
import numpy as np

# ---------------------------------------------------------------- Part A
print("=== PART A: change one input value ===")
temperatures_c = np.array([
    18.5, 18.0, 17.8, 17.5, 17.9, 19.0,
    21.5, 23.8, 25.6, 27.1, 28.3, 29.0,
    29.4, 29.1, 28.5, 27.6, 26.2, 24.8,
    23.4, 22.1, 21.0, 20.2, 19.6, 19.0
])

faulty = temperatures_c.copy()
faulty[11] = 45.0          # the 11:00 reading jumps from 29.0 C to 45.0 C (faulty sensor)

for label, data in [("original", temperatures_c), ("with faulty reading", faulty)]:
    print(f"{label:20s} mean={data.mean():.2f}  median={np.median(data):.2f}  "
          f"min={data.min():.2f}  max={data.max():.2f}")
