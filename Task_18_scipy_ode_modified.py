"""Task 18 - ODEs with SciPy: the SAME program with parameters / inputs CHANGED.

What was changed and why the result differs: see docs/Task_18_scipy_ode.md, section C.
"""
from pathlib import Path
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

FIG_DIR = Path(__file__).resolve().parents[2] / "figures"
FIG_DIR.mkdir(exist_ok=True)

# ---------------------------------------------------------------- Part A
print("=== PART A: change R and C ===")
def rc(Vs, R, C, V0, t_end=5.0):
    f = lambda t, V: [(Vs - V[0]) / (R * C)]
    return solve_ivp(f, (0, t_end), [V0], t_eval=np.linspace(0, t_end, 501), rtol=1e-9, atol=1e-11)

print(f"{'R (ohm)':>8} {'C (F)':>8} {'tau=RC (s)':>11} {'time to 63.2 % (s)':>19} {'V at 1 s':>9}")
for R, C in [(1000, 1e-3), (1000, 2e-4), (2200, 1e-3)]:
    s = rc(5.0, R, C, 0.0)
    v = s.y[0]
    t63 = np.interp(0.632 * 5.0, v, s.t)
    print(f"{R:8.0f} {C:8.4f} {R * C:11.2f} {t63:19.3f} {np.interp(1.0, s.t, v):9.3f}")

d = rc(0.0, 1000, 1e-3, 5.0)                    # discharging: supply removed, start at 5 V
t37 = np.interp(0.368 * 5.0, d.y[0][::-1], d.t[::-1])
print(f"\nDischarging from 5 V (R=1000, C=0.001): voltage falls to 36.8 % at {t37:.3f} s (tau = 1 s)")
print(f"Voltage after 5 s of discharge: {d.y[0, -1]:.4f} V")
