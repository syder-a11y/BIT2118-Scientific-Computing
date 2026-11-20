"""Task 6 - Systems of linear equations: a SIMILAR program applied to a different REAL-WORLD case.

Assumptions, input data, output and interpretation: see docs/Task_06_linear_systems.md, section E.
"""
import numpy as np

# ---------------------------------------------------------------- Part B
print("\n=== PART B: three-loop circuit (mesh-current analysis) ===")
# Resistors in ohms, sources in volts (assumed values for the exercise)
R1, R2, R3, R4, R5 = 10.0, 20.0, 30.0, 15.0, 25.0
V1, V2 = 24.0, 12.0

# Kirchhoff's voltage law around each loop:
#   loop 1: (R1+R2) I1 - R2 I2            = V1
#   loop 2: -R2 I1 + (R2+R3+R4) I2 - R4 I3 = 0
#   loop 3: -R4 I2 + (R4+R5) I3            = -V2
A = np.array([
    [R1 + R2, -R2,          0.0],
    [-R2,      R2 + R3 + R4, -R4],
    [0.0,     -R4,          R4 + R5],
])
b = np.array([V1, 0.0, -V2])

I = np.linalg.solve(A, b)
print("Mesh currents (A):", np.round(I, 5))
print("Residual norm:", np.linalg.norm(b - A @ I))
print("Condition number of A:", round(np.linalg.cond(A), 2))
print(f"Current through shared resistor R2 (I1 - I2): {I[0] - I[1]:.5f} A")
print(f"Current through shared resistor R4 (I2 - I3): {I[1] - I[2]:.5f} A")
print(f"Power delivered by source 1: {V1 * I[0]:.4f} W")
