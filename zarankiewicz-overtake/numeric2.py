"""Better-conditioned numerics for the witness (the first script's SCS/L-BFGS numbers are limited because the
feasible set has empty interior: no Slater point).
 (A) eps-relaxed SDP: feasible set {Q PSD, |A vec Q - b|_inf <= eps}; diameter vs eps (should shrink to 0).
 (B) Gauss-Newton/TRF low-rank fits with exact Jacobian: rank R vs R-1."""
import sys
import numpy as np, cvxpy as cp
from scipy.optimize import least_squares
sys.path.insert(0, "/Users/Ojas/Desktop/open-math-problems/results/zarankiewicz-overtake")
from zk import *

def P(*a): print(*a, flush=True)

def eps_sdp(cfg, epss=(1e-1, 1e-2, 1e-3, 1e-4, 1e-5, 1e-6), nfun=6, seed=0):
    N = cfg.N; A, b, _ = cfg.constraint_matrix(); Aden = A.toarray(); Q0 = cfg.Q0()
    rng = np.random.default_rng(seed)
    Cs = []
    for _ in range(nfun):
        C = rng.standard_normal((N, N)); Cs.append((C + C.T) / 2)
    for eps in epss:
        Qv = cp.Variable((N, N), symmetric=True)
        cons = [Qv >> 0, cp.abs(Aden @ cp.reshape(Qv, (N * N,), order="C") - b) <= eps]
        sols = []
        for C in Cs:
            for s in (1, -1):
                pr = cp.Problem(cp.Minimize(s * cp.trace(C @ Qv)), cons)
                try:
                    pr.solve(solver=cp.CLARABEL)
                except Exception as e:
                    continue
                if Qv.value is not None and pr.status in ("optimal", "optimal_inaccurate"):
                    sols.append(Qv.value.copy())
        if sols:
            diam = max(np.abs(S1 - S2).max() for S1 in sols for S2 in sols)
            dist0 = max(np.abs(S - Q0).max() for S in sols)
            P(f"  eps={eps:.0e}: {len(sols)} solves, max pairwise entry diff {diam:.3e}, max |Q-Q0| {dist0:.3e}")
        else:
            P(f"  eps={eps:.0e}: no solves")

def lowrank(cfg, r, starts, maxit=2000, seed0=0):
    N = cfg.N; K, bb = cfg.keymap(); nk = len(bb)
    def resid(x):
        B = x.reshape(r, N); Qm = B.T @ B
        return np.bincount(K.ravel(), weights=Qm.ravel(), minlength=nk) - bb
    def jac(x):
        B = x.reshape(r, N)
        J = np.zeros((nk, r * N))
        for c in range(N):
            for bq in range(N):
                k = K[c, bq]
                J[k, np.arange(r) * N + c] += 2 * B[:, bq]
        return J
    best = (1e99, None)
    vals = []
    for s in range(starts):
        rg = np.random.default_rng(seed0 + s)
        o = least_squares(resid, rg.standard_normal(r * N) * 0.7, jac=jac, method="trf",
                          xtol=1e-15, ftol=1e-15, gtol=1e-15, max_nfev=maxit)
        v = 0.5 * np.sum(o.fun ** 2)
        vals.append(v)
    return np.array(vals)

SDP = False
def run(name, cfg, starts=12):
    R = len(cfg.forms())
    P("=" * 60); P(name, "R =", R)
    if SDP:
        P("(A) eps-relaxed SDP diameter:")
        eps_sdp(cfg)
    P("(B) trust-region least squares, Q=B^T B:")
    for r in (R, R - 1, R - 2):
        v = lowrank(cfg, r, starts)
        P(f"  rank {r}: {starts} starts; best 0.5||res||^2 = {v.min():.3e}; median {np.median(v):.3e}; #<1e-20: {(v<1e-20).sum()}")

if __name__ == "__main__":
    m, n = 6, 5
    run("overtaking witness", Config(m, n, [0,1,2,5,8,11,13,15,19,22,24,28,29],
        [[6,4],[14,10],[16,21],[7,12],[26,18],[27,9],[17,3],[20,23]]))
