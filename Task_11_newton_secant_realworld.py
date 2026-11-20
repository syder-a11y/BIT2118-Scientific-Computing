"""Task 11 - Newton-Raphson and secant methods: a SIMILAR program applied to a different REAL-WORLD case.

Assumptions, input data, output and interpretation: see docs/Task_11_newton_secant.md, section E.
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

# ---------------------------------------------------------------- Part B
print("\n=== PART B: the real cost of a short-term loan ===")
loan = 100_000.0           # amount received today
instalment = 9_500.0       # paid at the end of each month
months = 12
flows = [loan] + [-instalment] * months          # money in (+), money out (-)
npv_loan, d_loan = make_npv(flows)

newton = root_scalar(npv_loan, fprime=d_loan, x0=0.02, method="newton", xtol=1e-12)
secant = root_scalar(npv_loan, x0=0.01, x1=0.05, method="secant", xtol=1e-12)

monthly = newton.root
print(f"Monthly rate (Newton): {monthly:.6%} in {newton.iterations} iterations")
print(f"Monthly rate (secant): {secant.root:.6%} in {secant.iterations} iterations")
print(f"Nominal annual rate (12 x monthly): {12 * monthly:.2%}")
print(f"Effective annual rate (compounded): {(1 + monthly) ** 12 - 1:.2%}")
total_paid = instalment * months
print(f"Total repaid {total_paid:,.0f} on a loan of {loan:,.0f}: simple 'flat' cost = "
      f"{(total_paid - loan) / loan:.1%} - much lower than the true annual rate because the "
      f"borrower keeps repaying the principal during the year.")
print(f"Check: NPV at the solution = {npv_loan(monthly):.8f}")
