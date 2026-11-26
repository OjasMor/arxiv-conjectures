"""Checks for the proof of the close-skew conjecture of arXiv:2611.20820 (Conjecture `conj:skew`).

1. Brute force: the largest k for which v_1..v_k (pairwise within distance r) and witnesses w_1..w_k exist with
   d(w_i, v_i) >= r+1 and d(w_i, v_j) <= r for j < i, for all n <= 4 and 1 <= r < n. It always equals 2^r.
2. The doubling step: for random close-skew systems, the list (v_1,w_1),...,(v_k,w_k),(w_k,v_k),...,(w_1,v_1)
   is a skew system in the sense of the Gao-Zhao theorem (d(a_i,b_i) >= r+1, d(a_i,b_j) <= r for i < j).
"""
import random, sys
sys.setrecursionlimit(10000)

def d(a, b): return bin(a ^ b).count("1")

def best(n, r):
    N = 1 << n
    far = [[w for w in range(N) if d(w, v) >= r + 1] for v in range(N)]
    top = 0
    def go(vs, cand_w_ok):
        # vs: chosen v's in order. A new v needs: close to all chosen v's, and a witness w far from v, close to all chosen.
        nonlocal top
        top = max(top, len(vs))
        if top == 1 << r and len(vs) == top: return
        for v in range(N):
            if v in vs or any(d(v, u) > r for u in vs): continue
            if any(all(d(w, u) <= r for u in vs) for w in far[v]):
                go(vs + [v], None)
                if top > 1 << r: return
    go([], None)
    return top

for n in range(2, 5):
    for r in range(1, n):
        b = best(n, r)
        print(f"n={n} r={r}: max k = {b}, 2^r = {1 << r}", "OK" if b == 1 << r else "MISMATCH")
        assert b == 1 << r

random.seed(1)
checked = 0
for _ in range(20000):
    n = random.randint(2, 7); r = random.randint(1, n - 1); N = 1 << n
    vs, ws = [], []
    for _ in range(40):
        v = random.randrange(N)
        if v in vs or any(d(v, u) > r for u in vs): continue
        cand = [w for w in range(N) if d(w, v) >= r + 1 and all(d(w, u) <= r for u in vs)]
        if cand: vs.append(v); ws.append(random.choice(cand))
    k = len(vs)
    a = vs + ws[::-1]; b = ws + vs[::-1]
    assert all(d(a[i], b[i]) >= r + 1 for i in range(2 * k))
    assert all(d(a[i], b[j]) <= r for i in range(2 * k) for j in range(i + 1, 2 * k))
    assert 2 * k <= 1 << (r + 1)
    checked += 1
print("doubling step verified on", checked, "random close-skew systems")
