"""Task 4 - Floating-point errors: a SIMILAR program applied to a different REAL-WORLD case.

Assumptions, input data, output and interpretation: see docs/Task_04_numerical_errors.md, section E.
"""
import math
from decimal import Decimal
import numpy as np

# ---------------------------------------------------------------- Part B
print("\n=== PART B: adding 0.10 one million times (true total = 100000) ===")
n = 1_000_000

total64 = 0.0
for _ in range(n):
    total64 += 0.1

total32 = np.float32(0.0)
step32 = np.float32(0.1)
for _ in range(n):
    total32 += step32

total_fsum = math.fsum([0.1] * n)                    # error-compensated summation
total_decimal = sum(Decimal("0.1") for _ in range(n))  # exact decimal arithmetic

rows = [
    ("float64 loop", float(total64)),
    ("float32 loop", float(total32)),
    ("math.fsum", total_fsum),
    ("Decimal", float(total_decimal)),
]
print(f"{'method':<14} {'result':>16} {'absolute error':>16}")
for name, value in rows:
    print(f"{name:<14} {value:16.6f} {abs(value - 100000.0):16.6f}")
