"""Task 3 - Vectorization: a SIMILAR program applied to a different REAL-WORLD case.

Assumptions, input data, output and interpretation: see docs/Task_03_vectorization.md, section E.
"""
import time
import numpy as np

rng = np.random.default_rng(42)

def timed(func, repeats=1):
    start = time.perf_counter()
    for _ in range(repeats):
        out = func()
    return (time.perf_counter() - start) / repeats, out

# ---------------------------------------------------------------- Part B
print("\n=== PART B: tiered transaction fees ===")
# Illustrative tariff (NOT a real operator's tariff):
#   up to 100 -> 0 | 101-500 -> 7 | 501-1000 -> 13 | 1001-5000 -> 30 | above 5000 -> 60
amounts = rng.lognormal(mean=6.0, sigma=1.2, size=1_000_000)   # transaction values

def fee_loop():
    fees = []
    for a in amounts:
        if a <= 100:
            f = 0.0
        elif a <= 500:
            f = 7.0
        elif a <= 1000:
            f = 13.0
        elif a <= 5000:
            f = 30.0
        else:
            f = 60.0
        fees.append(f)
    return np.array(fees)

def fee_vectorized():
    return np.select(
        [amounts <= 100, amounts <= 500, amounts <= 1000, amounts <= 5000],
        [0.0, 7.0, 13.0, 30.0],
        default=60.0,
    )

t_loop, fees_loop = timed(fee_loop)
t_vec, fees_vec = timed(fee_vectorized, repeats=3)

print("Both methods give the same fees:", np.array_equal(fees_loop, fees_vec))
print(f"Total transaction value: {amounts.sum():,.0f}")
print(f"Total fees collected:    {fees_vec.sum():,.0f}")
print(f"Average fee per transaction: {fees_vec.mean():.2f}")
print(f"Fees as % of value moved: {100 * fees_vec.sum() / amounts.sum():.3f} %")
print(f"Loop time {t_loop:.3f} s | vectorized {t_vec:.4f} s | speed-up {t_loop / t_vec:.1f}x")
