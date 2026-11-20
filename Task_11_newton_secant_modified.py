"""Task 11 - Newton-Raphson and secant methods: the SAME program with parameters / inputs CHANGED.

What was changed and why the result differs: see docs/Task_11_newton_secant.md, section C.
"""
import math
import warnings
from scipy.optimize import root_scalar

def make_npv(cash_flows):
    def npv(r):
        return sum(cf / (1 + r) ** t for t, cf in enumerate(cash_flows))
    def d_npv(r):
        return sum(-t * cf / (1 + r) ** (t + 1) for t, cf in enumerate(cash_flows) if t > 0)
    return npv, d_npv

# ---------------------------------------------------------------- Part A
print("=== PART A: change cash flows and starting guess ===")
for label, flows in [("original cash flows ", [-10000, 3000, 3500, 4000, 2500]),
                     ("last inflow cut to 1500", [-10000, 3000, 3500, 4000, 1500])]:
    npv, d_npv = make_npv(flows)
    res = root_scalar(npv, fprime=d_npv, x0=0.10, method="newton", xtol=1e-12)
    print(f"{label}: IRR = {res.root:.4%} ({res.iterations} Newton iterations)")

npv, d_npv = make_npv([-10000, 3000, 3500, 4000, 2500])
print("\nEffect of the starting guess (original cash flows):")
for x0 in (0.01, 0.10, 0.50, 1.50, -0.50):
    try:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            res = root_scalar(npv, fprime=d_npv, x0=x0, method="newton", xtol=1e-12, maxiter=50)
        if res.converged and math.isfinite(res.root) and abs(npv(res.root)) < 1e-6:
            print(f"  x0 = {x0:5.2f}: IRR = {res.root:.4%} after {res.iterations} iterations")
        else:
            print(f"  x0 = {x0:5.2f}: did NOT find a valid root (Newton diverged, got {res.root})")
    except Exception as err:
        print(f"  x0 = {x0:5.2f}: failed ({type(err).__name__})")
