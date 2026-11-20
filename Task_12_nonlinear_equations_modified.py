"""Task 12 - Polynomial and nonlinear equation solving: the SAME program with parameters / inputs CHANGED.

What was changed and why the result differs: see docs/Task_12_nonlinear_equations.md, section C.
"""
import numpy as np
from scipy.optimize import root

# ---------------------------------------------------------------- Part A
print("=== PART A: circle x^2+y^2=4 and parabola y = x^2 - 3 ===")
def make_equations(c):
    def eq(z):
        x, y = z
        return [x ** 2 + y ** 2 - 4, y - (x ** 2 - c)]
    return eq

eq = make_equations(3.0)
for guess in ([1.0, 1.0], [-1.0, 1.0], [1.0, -1.0], [-1.0, -1.0], [0.0, 0.0]):
    sol = root(eq, guess)
    print(f"guess {guess}: converged={sol.success}, point={np.round(sol.x, 4)}, "
          f"max |residual|={np.abs(eq(sol.x)).max():.1e}")
print("Each of the first four guesses lands on a different intersection (four in total).")
print("The guess [0, 0] is a poor start (the Jacobian is singular there) but SciPy's hybrid")
print("solver still recovers and lands on just one of them - which point you get depends")
print("on where you start, so always try several guesses.")
