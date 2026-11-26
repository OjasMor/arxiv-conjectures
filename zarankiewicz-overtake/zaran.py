"""z(m,n) via row-subset DP: max edges of C4-free bipartite m x n graph (no two rows share 2 columns)."""
import itertools as it, sys
from functools import lru_cache
def z(m, n):
    masks = [x for x in range(1 << n)]
    pairs = lambda x: [(a, b) for a, b in it.combinations(range(n), 2) if x >> a & 1 and x >> b & 1]
    pm = {x: frozenset(pairs(x)) for x in masks}
    best = 0
    @lru_cache(None)
    def rec(row, used):
        if row == m: return 0
        r = 0
        for x in masks:
            if not (pm[x] & used):
                r = max(r, bin(x).count("1") + rec(row + 1, used | pm[x]))
        return r
    return rec(0, frozenset())
for mn in [(4,3),(4,4),(5,5),(6,5),(6,4)]:
    print("z", mn, z(*mn))
print("(6,5): z=14, six-column formula z_2(5,6)=4*5=20 =>  H_limited = 6*5 + 14 - 2*20 =", 30 + 14 - 40)
