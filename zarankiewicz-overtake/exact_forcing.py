"""Exact (rational arithmetic) forcing argument for uniqueness of the Gram matrix, then product independence.

Setup: Q feasible PSD, Q0 = displayed Gram. D = Q - Q0 (symmetric, 465 unknowns D_ab, a<=b).
Linear facts (all exact):
  (1) D_aa = 0, D_ab = 0 if cells a,b share a row or column  (coefficient of x_i^2 y_j y_l etc. is determined).
  (2) for a rectangle rows i<k, cols j<l:  D[(ij),(kl)] + D[(il),(kj)] = 0.
  (3) hole h: Q_hh = 0 and Q PSD => row h of Q is 0 => D_hx = -Q0_hx = 0.
Inequality: for a displayed pair (a,b), Q_aa=Q_bb=1 and PSD give Q_ab <= 1, so D_ab = Q_ab - 1 <= 0.
 If D_ab = 0 then (Q_aa-2Q_ab+Q_bb = |u_a-u_b|^2 = 0) u_a=u_b so Q_ac = Q_bc for all c:  D_ac - D_bc = Q0_bc - Q0_ac (linear).
A pair is forced when, modulo the current equalities, e_p is 0 (D_p=0) or e_p = -lam e_q for another displayed pair q, lam>0
 (then D_p = -lam D_q >= 0 and D_p <= 0)."""
import sys, itertools as it
from fractions import Fraction
sys.path.insert(0, "/Users/Ojas/Desktop/open-math-problems/results/zarankiewicz-overtake")
from zk import *

def exact_force(cfg, verbose=True):
    N, n = cfg.N, cfg.n
    idx = {}
    for a in range(N):
        for c in range(a, N):
            idx[(a, c)] = len(idx)
    def var(a, c): return idx[(min(a, c), max(a, c))]
    Q0 = cfg.Q0()
    class Elim:
        def __init__(s): s.piv = {}   # pivot var -> (row dict, rhs)
        def reduce(s, row):
            row = dict(row)
            changed = True
            while True:
                ps = [k for k in row if k in s.piv]
                if not ps: return row
                k = min(ps)
                f = row[k]
                prow = s.piv[k]
                for kk, x in prow.items():
                    nv = row.get(kk, 0) - f * x
                    if nv: row[kk] = nv
                    else: row.pop(kk, None)
        def add(s, row):
            row = {k: Fraction(x) for k, x in row.items() if x}
            row = s.reduce(row)
            if not row:
                return False
            k = min(row); f = row[k]
            row = {kk: x / f for kk, x in row.items()}
            # keep fully reduced (eliminate k from other pivots)
            for pk, prow in list(s.piv.items()):
                if k in prow:
                    g = prow[k]
                    for kk, x in row.items():
                        nv = prow.get(kk, 0) - g * x
                        if nv: prow[kk] = nv
                        else: prow.pop(kk, None)
            s.piv[k] = row
            return True
    # NOTE: homogeneous system only (rhs handled by affine shift): we need inhomogeneous for (3) and identifications.
    # Use an extra variable 'one' (index -1) multiplying the constant: row . D = const  <=>  row . D - const*one = 0.
    ONE = len(idx)
    E = Elim()
    def eq(d, const=0):
        r = dict(d)
        if const: r[ONE] = r.get(ONE, 0) - const
        E.add(r)
    for a in range(N):
        eq({var(a, a): 1})
    rcs = [cfg.rc(c) for c in range(N)]
    for a, c in it.combinations(range(N), 2):
        if rcs[a][0] == rcs[c][0] or rcs[a][1] == rcs[c][1]:
            eq({var(a, c): 1})
    for i, k in it.combinations(range(cfg.m), 2):
        for j, l in it.combinations(range(cfg.n), 2):
            a, b = i * n + j, k * n + l
            c, d = i * n + l, k * n + j
            eq({var(a, b): 1, var(c, d): 1})
    for h in cfg.holes:
        for x in range(N):
            if x != h:
                eq({var(h, x): 1}, -int(Q0[h, x]))  # D_hx = -Q0_hx
    pairs = [tuple(p) for p in cfg.E2]
    forced = []
    for it_ in range(20):
        newly = []
        reds = {p: E.reduce({var(*p): Fraction(1)}) for p in pairs if p not in forced}
        for p, rp in reds.items():
            if not rp:           # D_p == 0 exactly
                newly.append((p, "e_p in span(equalities)")); continue
            for q, rq in reds.items():
                if q == p or not rq: continue
                # rp == -lam * rq with lam>0 ?
                k = min(rq)
                if k not in rp: continue
                lam = -rp[k] / rq[k]
                if lam > 0 and set(rp) == set(rq) and all(rp[x] == -lam * rq[x] for x in rq):
                    newly.append((p, f"D_{p} = -{lam} * D_{q}  with both <= 0")); break
        if not newly: break
        for p, why in newly:
            forced.append(p)
            a, c = p
            for x in range(N):
                if x not in p:
                    # D_ax - D_cx = Q0_cx - Q0_ax
                    eq({var(a, x): 1, var(c, x): -1}, int(Q0[c, x] - Q0[a, x]))
        if verbose:
            print(f"  pass {it_+1}: forced {[ (p, why) for p, why in newly ]}")
    ok = len(forced) == len(pairs)
    print(f"  exact forcing: {len(forced)}/{len(pairs)} displayed pairs forced")
    return ok

def prove(name, cfg):
    print("=" * 60); print(name)
    ok = exact_force(cfg)
    pr, npr = product_rank(cfg)
    print(f"  exact rank over Q of the {npr} products w_i w_j: {pr}")
    R = len(cfg.forms())
    if ok and pr == npr:
        print(f"  => every feasible PSD Gram Q = W^T M W with M a PSD {R}x{R} Gram of the displayed forms,"
              f" sum M_fg w_f w_g = sum w_f^2 + independence => M = I => Q = Q0, rank {R}. SOS rank = {R} exactly.")
    else:
        print("  forcing/independence NOT both established (forced all:", ok, ", independent:", pr == npr, ")")

if __name__ == "__main__":
    m, n = 6, 5
    prove("overtaking witness", Config(m, n, [0,1,2,5,8,11,13,15,19,22,24,28,29],
          [[6,4],[14,10],[16,21],[7,12],[26,18],[27,9],[17,3],[20,23]]))
    prove("limited witness", Config(m, n, [0,1,2,6,8,12,13,16,19,22,24,25,28,29],
          [[3,17],[4,11],[5,20],[9,27],[10,15],[23,26]]))
