"""Controls against statements in the paper at (4,4):
 (i) Thm thm:44 (Qi-Cui): a non-limited config |E1|=8, |E2|=3, H=2, R=11 exists with SOS rank 11 (irreducible),
 (ii) Proof of thm:budget: a limited config |E1|=9, |E2|=3, H=1, R=12 is 'necessarily reducible' (rank <= 11).
Both are found by search, the SOS rank is bracketed by the same machinery used on the (6,5) witness."""
import sys, itertools as it
import numpy as np
from scipy.optimize import minimize
sys.path.insert(0, "/Users/Ojas/Desktop/open-math-problems/results/zarankiewicz-overtake")
from zk import *

def fit_min_resid(cfg, r, starts):
    N = cfg.N
    K, bb = cfg.keymap()
    best = 1e9
    for s in range(starts):
        rg = np.random.default_rng(s)
        def f(x):
            B = x.reshape(r, N); Qm = B.T @ B
            res = np.bincount(K.ravel(), weights=Qm.ravel(), minlength=len(bb)) - bb
            return 0.5 * (res ** 2).sum(), (2 * B @ res[K]).ravel()
        o = minimize(f, rg.standard_normal(r * N) * 0.5, jac=True, method="L-BFGS-B",
                     options=dict(maxiter=20000, maxfun=40000, ftol=1e-30, gtol=1e-12))
        best = min(best, o.fun)
        if best < 1e-14: break
    return best

def c4free_graphs(m, n, e):
    cells = list(range(m * n))
    out = []
    for E in it.combinations(cells, e):
        rows = {}
        for c in E: rows.setdefault(c // n, set()).add(c % n)
        if all(len(rows[a] & rows[b]) < 2 for a, b in it.combinations(rows, 2)):
            out.append(E)
    return out

def pairings(cells, k):
    """all sets of k disjoint pairs among cells (unordered)."""
    cells = list(cells)
    def rec(rem, k):
        if k == 0:
            yield []; return
        if len(rem) < 2 * k: return
        a = rem[0]
        # a is paired
        for b in rem[1:]:
            rest = [x for x in rem if x not in (a, b)]
            for p in rec(rest, k - 1):
                yield [(a, b)] + p
        # a is a hole
        yield from rec(rem[1:], k)
    yield from rec(cells, k)

def run():
    m = n = 4
    # canonical-ish: just take the first few C4-free 8-edge graphs, random pairings
    rng = np.random.default_rng(1)
    g8 = c4free_graphs(4, 4, 8); g9 = c4free_graphs(4, 4, 9)
    print("(4,4): #C4-free graphs with 8 edges", len(g8), " with 9 edges", len(g9))
    # (i) 8 singles, 3 pairs, 2 holes
    found = None; tried = 0
    for gi in rng.permutation(len(g8))[:40]:
        E1 = list(g8[gi]); rest = [c for c in range(16) if c not in E1]
        for P in pairings(rest, 3):
            if sum(2 for _ in P) != 6: continue
            cfg = Config(m, n, E1, P)
            if len(cfg.holes) != 2: continue
            tried += 1
            pr, npairs = product_rank(cfg)
            if pr == npairs:      # candidate irreducible: products independent
                r10 = fit_min_resid(cfg, 10, 15)
                r11 = fit_min_resid(cfg, 11, 15)
                print(f"  cand E1={E1} E2={P}: product-rank {pr}/{npairs}, fit resid rank10={r10:.2e}, rank11={r11:.2e}")
                if r10 > 1e-8 and r11 < 1e-12:
                    found = cfg; break
        if found: break
    print("tried", tried)
    if found:
        cfg = found
        print("control (i) config:", cfg.E1, cfg.E2, "holes", cfg.holes, cfg.validate())
        # affine-space dimension, forcing
        from check_witness import analyse
        analyse("(4,4) Qi-Cui-type witness", cfg, ntrials_fit=15)
    # (ii) 9 singles, 3 pairs, 1 hole -> R=12, paper says reducible
    cnt = 0
    for E1 in g9[:200]:
        E1 = list(E1); rest = [c for c in range(16) if c not in E1]
        for P in pairings(rest, 3):
            cfg = Config(m, n, E1, P)
            if len(cfg.holes) != 1: continue
            r11 = fit_min_resid(cfg, 11, 15)
            r12 = fit_min_resid(cfg, 12, 3)
            pr, npairs = product_rank(cfg)
            print(f"  limited R=12 cfg E1={E1} E2={P}: fit resid rank11={r11:.2e}, rank12={r12:.2e}, product rank {pr}/{npairs}")
            cnt += 1
            break
        if cnt >= 3: break

if __name__ == "__main__":
    run()
