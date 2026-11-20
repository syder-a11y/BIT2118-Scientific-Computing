"""Task 9 - Eigenvalues and eigenvectors: a SIMILAR program applied to a different REAL-WORLD case.

Assumptions, input data, output and interpretation: see docs/Task_09_eigenvalues.md, section E.
"""
import numpy as np

nodes = ["A", "B", "C", "D"]

def importance(adj):
    vals, vecs = np.linalg.eig(adj)
    i = np.argmax(np.real(vals))
    v = np.abs(np.real(vecs[:, i]))
    return np.real(vals[i]), v / v.sum()

# ---------------------------------------------------------------- Part B
print("\n=== PART B: PageRank for a five-page website ===")
pages = ["Home", "News", "Shop", "Blog", "Contact"]
links = {                      # page index -> pages it links to
    0: [1, 2, 3],              # Home -> News, Shop, Blog
    1: [0, 3],                 # News -> Home, Blog
    2: [0, 4],                 # Shop -> Home, Contact
    3: [0, 1, 2],              # Blog -> Home, News, Shop
    4: [0],                    # Contact -> Home
}
n = len(pages)
M = np.zeros((n, n))           # column j spreads page j's score equally over its outgoing links
for src, outs in links.items():
    for dst in outs:
        M[dst, src] = 1 / len(outs)

def pagerank_eig(d):
    G = d * M + (1 - d) / n * np.ones((n, n))        # Google matrix with damping factor d
    vals, vecs = np.linalg.eig(G)
    i = np.argmax(np.real(vals))
    v = np.abs(np.real(vecs[:, i]))
    return np.real(vals[i]), v / v.sum(), G

def pagerank_power(G, tol=1e-12):
    r = np.ones(n) / n
    for it in range(1, 1000):
        r_new = G @ r
        if np.abs(r_new - r).sum() < tol:
            return r_new, it
        r = r_new
    return r, it

for d in (0.85, 0.50):
    lam, r_eig, G = pagerank_eig(d)
    r_pow, iters = pagerank_power(G)
    print(f"\ndamping factor d = {d}: dominant eigenvalue = {lam:.6f} (should be 1)")
    for p, s in sorted(zip(pages, r_eig), key=lambda t: -t[1]):
        print(f"  {p:8s} {s:.4f}")
    print(f"  power iteration agrees with eig: {np.allclose(r_pow, r_eig)} ({iters} iterations)")
