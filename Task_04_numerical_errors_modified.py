"""Task 4 - Floating-point errors: the SAME program with parameters / inputs CHANGED.

What was changed and why the result differs: see docs/Task_04_numerical_errors.md, section C.
"""
import math
from decimal import Decimal
import numpy as np

# ---------------------------------------------------------------- Part A
print("=== PART A: change tolerance and x ===")
calc, expected = 0.1 + 0.2, 0.3
print("difference |calc - expected| =", abs(calc - expected))
for rtol in (1e-9, 1e-12, 1e-16):
    print(f"np.isclose with rtol={rtol:.0e}:", np.isclose(calc, expected, rtol=rtol, atol=0.0))

print("\n(sqrt(1+x)-1)/x  (direct)  versus  1/(sqrt(1+x)+1)  (stable)")
print(f"{'x':>8} {'direct':>18} {'stable':>18} {'relative error of direct':>26}")
for x in [1e-4, 1e-8, 1e-12, 1e-15]:
    direct = (np.sqrt(1 + x) - 1) / x
    stable = 1 / (np.sqrt(1 + x) + 1)
    print(f"{x:8.0e} {direct:18.12f} {stable:18.12f} {abs(direct - stable) / stable:26.3e}")
