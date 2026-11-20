"""Task 16 - Numerical integration: the SAME program with parameters / inputs CHANGED.

What was changed and why the result differs: see docs/Task_16_numerical_integration.md, section C.
"""
import numpy as np
from scipy.integrate import simpson

# ---------------------------------------------------------------- Part A
print("=== PART A: change the number of sample points ===")
print(f"{'points':>7} {'trapezoid error':>17} {'Simpson error':>15}")
for n in (3, 5, 9, 17, 33):
    x = np.linspace(0, np.pi, n)
    y = np.sin(x)
    print(f"{n:7d} {abs(np.trapezoid(y, x) - 2):17.3e} {abs(simpson(y, x=x) - 2):15.3e}")
