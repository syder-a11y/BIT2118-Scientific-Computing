"""Task 3 - Vectorization: the SAME program with parameters / inputs CHANGED.

What was changed and why the result differs: see docs/Task_03_vectorization.md, section C.
"""
import time
import numpy as np

rng = np.random.default_rng(42)

def timed(func, repeats=1):
    start = time.perf_counter()
    for _ in range(repeats):
        out = func()
    return (time.perf_counter() - start) / repeats, out

# ---------------------------------------------------------------- Part A
print("=== PART A: change N (number of readings) ===")
print(f"{'N':>10} {'loop (s)':>10} {'vector (s)':>12} {'speed-up':>10}")
for n in [100_000, 1_000_000, 5_000_000]:
    data = rng.uniform(5, 250, n)

    def loop():
        out = []
        for v in data:
            out.append((v / 1000.0) ** 2)
        return out

    def vec():
        return (data / 1000.0) ** 2

    t_loop, _ = timed(loop)
    t_vec, _ = timed(vec, repeats=3)
    print(f"{n:>10,} {t_loop:>10.4f} {t_vec:>12.5f} {t_loop / t_vec:>9.1f}x")
