"""Task 12 - Polynomial and nonlinear equation solving: a SIMILAR program applied to a different REAL-WORLD case.

Assumptions, input data, output and interpretation: see docs/Task_12_nonlinear_equations.md, section E.
"""
import numpy as np
from scipy.optimize import root

# ---------------------------------------------------------------- Part B1
print("\n=== PART B1: overlap of two tower coverage areas ===")
# Tower 1 at (0, 0) km with 5 km range; tower 2 at (6, 0) km with 4 km range.
def towers(z):
    x, y = z
    return [x ** 2 + y ** 2 - 5 ** 2, (x - 6) ** 2 + y ** 2 - 4 ** 2]

for guess in ([3.0, 3.0], [3.0, -3.0]):
    sol = root(towers, guess)
    print(f"guess {guess}: edge point of the overlap = {np.round(sol.x, 4)} "
          f"(residual {np.abs(towers(sol.x)).max():.1e})")
x_exact = (6 ** 2 + 5 ** 2 - 4 ** 2) / (2 * 6)
print(f"Algebra check: x = {x_exact:.4f}, y = +/-{np.sqrt(25 - x_exact ** 2):.4f}")

# ---------------------------------------------------------------- Part B2
print("\n=== PART B2: cardboard box, 30 cm x 20 cm sheet ===")
# Cut a square of side x from each corner and fold up: V(x) = x (30-2x)(20-2x).
# Which x gives a volume of 1000 cm^3?  4x^3 - 100x^2 + 600x - 1000 = 0
coeffs = [4, -100, 600, -1000]
roots = np.roots(coeffs)
print("All roots of the polynomial:", np.round(roots, 4))
valid = sorted(r.real for r in roots if abs(r.imag) < 1e-9 and 0 < r.real < 10)
for r in valid:
    volume = r * (30 - 2 * r) * (20 - 2 * r)
    print(f"  cut size {r:.3f} cm -> volume {volume:.2f} cm^3")
print("Only 0 < x < 10 cm is physically possible (the sheet is 20 cm wide).")
