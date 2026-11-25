"""Independent check of a counterexample to Conjecture (conj:grado3) of arXiv:2611.14718.

Paper's definitions:
  sequential model: repeatedly pick a uniformly random still-available vertex, occupy it, block its neighbours.
  static model: uniform over all maximal independent sets.
  "sequential dominates static" means P[N_stat <= k] >= P[N_seq <= k] for every k.
Conjecture: this holds on every graph of maximum degree <= 3.

Counterexample candidate (found by GPT-6.2 Astra): a tree on 15 vertices, max degree 3.
This file re-derives both distributions with our own code (exact rationals) and adds a Monte Carlo check.
"""
import random
import sys
from fractions import Fraction as Fr
from itertools import combinations

EDGES = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6),   # path 0..6
         (0, 7), (7, 8), (3, 9), (9, 10), (6, 11), (11, 12),  # three pendant paths of length 2
         (0, 13), (6, 14)]                                    # two leaves


def analyse(n, edges):
    adj = [0] * n
    for u, v in edges:
        adj[u] |= 1 << v
        adj[v] |= 1 << u
    # static: brute force over all subsets
    stat = {}
    for S in range(1 << n):
        ok = True
        for v in range(n):
            if S >> v & 1:
                if adj[v] & S:
                    ok = False
                    break
            elif not adj[v] & S:
                ok = False
                break
        if ok:
            k = bin(S).count("1")
            stat[k] = stat.get(k, 0) + 1
    # sequential: exact distribution of the final count, DP over the set of available vertices
    memo = {}

    def dist(avail):
        if avail == 0:
            return {0: Fr(1)}
        if avail in memo:
            return memo[avail]
        vs = [v for v in range(n) if avail >> v & 1]
        out = {}
        for v in vs:
            for k, p in dist(avail & ~(1 << v) & ~adj[v]).items():
                out[k + 1] = out.get(k + 1, 0) + p / len(vs)
        memo[avail] = out
        return out

    return adj, stat, dist((1 << n) - 1)


def cdf(d, total=None):
    ks = sorted(d)
    tot = total if total is not None else sum(d.values())
    acc, out = 0, {}
    for k in ks:
        acc += d[k]
        out[k] = Fr(acc, 1) / tot if not isinstance(acc, Fr) else acc / tot
    return out


if __name__ == "__main__":
    n = 15
    assert len(EDGES) == n - 1
    deg = [0] * n
    for u, v in EDGES:
        deg[u] += 1
        deg[v] += 1
    # connected + n-1 edges => tree
    comp = {0}
    grew = True
    while grew:
        grew = False
        for u, v in EDGES:
            if (u in comp) != (v in comp):
                comp |= {u, v}
                grew = True
    print("vertices", n, "edges", len(EDGES), "connected", len(comp) == n, "max degree", max(deg))
    adj, stat, seq = analyse(n, EDGES)
    print("maximal independent sets by size:", dict(sorted(stat.items())), "total", sum(stat.values()))
    print("sequential law:", {k: str(p) for k, p in sorted(seq.items())}, "sum", sum(seq.values()))
    cs, cq = cdf(stat), cdf(seq, Fr(1))
    for k in sorted(set(cs) | set(cq)):
        a = cs.get(k, Fr(0) if k < min(cs) else Fr(1))
        b = cq.get(k, Fr(0) if k < min(cq) else Fr(1))
        flag = "  <-- VIOLATES conjecture (needs static >= sequential)" if a < b else ""
        print(f"k={k}: P[N_stat<=k] = {a} = {float(a):.6f}   P[N_seq<=k] = {b} = {float(b):.6f}{flag}")
    # Monte Carlo, straight from the verbal definition
    trials = int(sys.argv[1]) if len(sys.argv) > 1 else 2_000_000
    rng = random.Random(12345)
    nb = [[v for v in range(n) if adj[u] >> v & 1] for u in range(n)]
    hits = 0
    for _ in range(trials):
        avail = list(range(n))
        alive = [True] * n
        cnt = 0
        while avail:
            v = avail[rng.randrange(len(avail))]
            cnt += 1
            alive[v] = False
            for w in nb[v]:
                alive[w] = False
            avail = [x for x in avail if alive[x]]
        hits += cnt <= 6
    p = hits / trials
    se = (p * (1 - p) / trials) ** 0.5
    print(f"Monte Carlo ({trials} runs): P[N_seq<=6] ~ {p:.6f} +- {se:.6f};  exact 64/3375 = {64/3375:.6f};  static 1/55 = {1/55:.6f}")
