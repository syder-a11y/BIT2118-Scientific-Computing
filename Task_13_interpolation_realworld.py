"""Task 13 - Interpolation: a SIMILAR program applied to a different REAL-WORLD case.

Assumptions, input data, output and interpretation: see docs/Task_13_interpolation.md, section E.
"""
from pathlib import Path
import numpy as np
from scipy.interpolate import interp1d, CubicSpline
import matplotlib.pyplot as plt

FIG_DIR = Path(__file__).resolve().parents[2] / "figures"
FIG_DIR.mkdir(exist_ok=True)

# ---------------------------------------------------------------- Part B
print("\n=== PART B: river gauge with a missing reading ===")
def true_level(t):                      # 'real' river level in metres (used only to judge errors)
    return 2.5 + 1.2 * np.sin(2 * np.pi * t / 24 - 1.0)

t_all = np.arange(0, 27, 3, dtype=float)          # readings every 3 hours, 0 to 24
level_all = true_level(t_all)
lost = 12.0                                        # the reading at 12:00 was never received
keep = t_all != lost
t_known, level_known = t_all[keep], level_all[keep]

lin = interp1d(t_known, level_known, kind="linear")
cub = CubicSpline(t_known, level_known)

print(f"True level at 12:00:        {float(true_level(lost)):.4f} m")
print(f"Linear estimate:            {float(lin(lost)):.4f} m  (error {abs(float(lin(lost)) - true_level(lost)):.4f} m)")
print(f"Cubic spline estimate:      {float(cub(lost)):.4f} m  (error {abs(float(cub(lost)) - true_level(lost)):.4f} m)")

fine = np.linspace(0, 24, 241)
rmse_lin = np.sqrt(np.mean((lin(fine) - true_level(fine)) ** 2))
rmse_cub = np.sqrt(np.mean((cub(fine) - true_level(fine)) ** 2))
print(f"RMSE over the whole day (every 6 min): linear {rmse_lin:.4f} m | cubic {rmse_cub:.4f} m")

plt.plot(fine, true_level(fine), "k:", label="true level")
plt.plot(fine, lin(fine), label="linear")
plt.plot(fine, cub(fine), label="cubic spline")
plt.scatter(t_known, level_known, zorder=3, label="received readings")
plt.scatter([lost], [true_level(lost)], marker="x", s=80, color="red", zorder=4, label="lost reading")
plt.xlabel("Hour of day")
plt.ylabel("River level (m)")
plt.title("Recovering a missing river-gauge reading")
plt.legend()
plt.grid(True)
plt.savefig(FIG_DIR / "Task_13_modified_river.png", dpi=150, bbox_inches="tight")
plt.show()
