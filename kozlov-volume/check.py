"""Check for the proof of the volume-monotonicity conjecture of arXiv:2611.26110.
V(n,d) is the normalised volume of Koz(n;0,d) from the paper's rank-two volume corollary, 0 <= d <= n-1."""
from math import comb, prod

def A(n, d, j):
    return comb(n - 1 + d, d + j - 1) * prod(comb(n, k) for k in range(j + 1, j + d + 1))

def V(n, d):
    return prod(comb(n, k) for k in range(2, n + 1)) * sum(A(n, d, j) for j in range(1, n - d + 1))

# the paper's table of normalised volumes
assert [V(3, d) for d in range(3)] == [12, 36, 54]
assert [V(4, d) for d in range(4)] == [192, 1248, 6720, 11520]
assert [V(5, d) for d in range(5)] == [8000, 102500, 1287500, 9625000, 17500000]
for n in range(1, 81):
    for d in range(0, n - 1):
        for j in range(1, n - d):
            # the Pascal identity used in the proof
            assert A(n, d + 1, j) == comb(n, j + d + 1) * A(n, d, j) + comb(n, j + 1) * A(n, d, j + 1)
        assert V(n, d + 1) >= V(n, d) and (n < 3 or V(n, d + 1) > V(n, d))
print("paper table reproduced; identity and monotonicity hold for n <= 80")
