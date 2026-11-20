"""Task 18 - ODEs with SciPy: a SIMILAR program applied to a different REAL-WORLD case.

Assumptions, input data, output and interpretation: see docs/Task_18_scipy_ode.md, section E.
"""
from pathlib import Path
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

FIG_DIR = Path(__file__).resolve().parents[2] / "figures"
FIG_DIR.mkdir(exist_ok=True)

# ---------------------------------------------------------------- Part B
print("\n=== PART B: SIR epidemic in a town of 1000 people ===")
def sir(t, y, beta, gamma):
    S, I, R = y
    return [-beta * S * I, beta * S * I - gamma * I, gamma * I]

N = 1000
y0 = [1 - 1 / N, 1 / N, 0.0]                    # one infected person at the start
t_eval = np.linspace(0, 200, 801)
gamma = 0.1                                      # recovery rate: infection lasts about 10 days

plt.figure(figsize=(7, 4.5))
for beta, style in [(0.35, "-"), (0.20, "--")]:
    s = solve_ivp(sir, (0, 200), y0, t_eval=t_eval, args=(beta, gamma), rtol=1e-8, atol=1e-10)
    S, I, R = s.y
    peak = I.argmax()
    print(f"beta = {beta:.2f} (R0 = {beta / gamma:.1f}): peak {I[peak] * N:.0f} infected at day {s.t[peak]:.1f}; "
          f"total ever infected {R[-1] * N:.0f} ({R[-1]:.1%}); never infected {S[-1] * N:.0f}")
    plt.plot(s.t, I * N, style, label=f"infected, beta={beta}")
    if beta == 0.35:
        plt.plot(s.t, S * N, ":", label="susceptible, beta=0.35")
        plt.plot(s.t, R * N, "-.", label="recovered, beta=0.35")
plt.xlabel("Day")
plt.ylabel("People")
plt.title("SIR epidemic model")
plt.legend()
plt.grid(True)
plt.savefig(FIG_DIR / "Task_18_modified_sir.png", dpi=150, bbox_inches="tight")
plt.show()
