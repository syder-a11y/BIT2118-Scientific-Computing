"""Task 9 - Eigenvalues and eigenvectors: the SAME program with parameters / inputs CHANGED.

What was changed and why the result differs: see docs/Task_09_eigenvalues.md, section C.
"""
import numpy as np

nodes = ["A", "B", "C", "D"]

def importance(adj):
    vals, vecs = np.linalg.eig(adj)
    i = np.argmax(np.real(vals))
    v = np.abs(np.real(vecs[:, i]))
    return np.real(vals[i]), v / v.sum()

# ---------------------------------------------------------------- Part A
print("=== PART A: change the links ===")
base = np.array([[0, 1, 1, 0], [1, 0, 1, 1], [1, 1, 0, 1], [0, 1, 1, 0]], dtype=float)

remove_bc = base.copy()
remove_bc[1, 2] = remove_bc[2, 1] = 0               # cut the link between B and C
add_ad = base.copy()
add_ad[0, 3] = add_ad[3, 0] = 1                      # add a link between A and D

for label, adj in [("original network", base),
                   ("link B-C removed", remove_bc),
                   ("link A-D added (everyone connected)", add_ad)]:
    lam, score = importance(adj)
    scores = {n: round(float(s), 4) for n, s in zip(nodes, score)}
    print(f"{label:38s} dominant eigenvalue {lam:.4f} | importance {scores}")
