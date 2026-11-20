"""Task 20 - Monte Carlo methods: a SIMILAR program applied to a different REAL-WORLD case.

Assumptions, input data, output and interpretation: see docs/Task_20_monte_carlo.md, section E.
"""
from pathlib import Path
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

FIG_DIR = Path(__file__).resolve().parents[2] / "figures"
FIG_DIR.mkdir(exist_ok=True)

# ---------------------------------------------------------------- Part B
print("\n=== PART B: project completion time ===")
rng = np.random.default_rng(42)
N = 100_000
# Task durations in days as (shortest, most likely, longest) - triangular distributions
design = rng.triangular(4, 6, 10, N)
build = rng.triangular(10, 14, 25, N)
test = rng.triangular(3, 5, 9, N)
total = design + build + test                      # tasks happen one after another

print(f"Planned time if everything goes as 'most likely': {6 + 14 + 5} days")
print(f"Simulated mean completion time: {total.mean():.2f} days (std {total.std():.2f})")
for q in (50, 80, 90, 95):
    print(f"  {q}% of simulated projects finish within {np.percentile(total, q):.1f} days")
for deadline in (25, 30, 35):
    print(f"Probability of finishing within {deadline} days: {(total <= deadline).mean():.2%}")

plt.hist(total, bins=60, color="tab:blue", alpha=0.8)
plt.axvline(30, color="red", linestyle="--", label="30-day deadline")
plt.axvline(total.mean(), color="black", linestyle=":", label="mean")
plt.xlabel("Total project duration (days)")
plt.ylabel("Number of simulations")
plt.title("Monte Carlo simulation of project duration")
plt.legend()
plt.savefig(FIG_DIR / "Task_20_modified_project.png", dpi=150, bbox_inches="tight")
plt.show()
