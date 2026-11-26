import sys, time
import numpy as np
import cvxpy as cp
from scipy.optimize import minimize, linprog
sys.path.insert(0, "/Users/Ojas/Desktop/open-math-problems/results/zarankiewicz-overtake")
from zk import *

def P(*a):
    print(*a, flush=True)

def analyse(name, cfg, ntrials_fit=30, rseed=0, do_forcing=True):
    P("=" * 70); P("CONFIG", name, "m,n =", cfg.m, cfg.n)
    v = cfg.validate(); P("validation:", v)
    N = cfg.N
    Q0 = cfg.Q0()
    A, b, keys = cfg.constraint_matrix()
    P("Q0 feasibility residual (A vec(Q0)-b):", np.abs(A @ Q0.ravel() - b).max(),
      " rank(Q0)=", np.linalg.matrix_rank(Q0), " R=", v["R"])
    mats, rk, nparam = sym_nullspace(cfg)
    d = len(mats)
    P(f"affine space of symmetric Q: {nparam} entries, {rk} independent constraints -> {d} free parameters")
    # ---- SDP extremes
    rng = np.random.default_rng(rseed)
    # PSD variable Q (N x N) with the affine constraints A vec(Q)=b imposed directly (symmetric).
    Qv = cp.Variable((N, N), symmetric=True)
    Aden = A.toarray()
    cons = [Qv >> 0, Aden @ cp.reshape(Qv, (N * N,), order="C") == b]
    sols = []
    ok = True
    for trial in range(8):
        C = rng.standard_normal((N, N)); C = (C + C.T) / 2
        for sense in (1, -1):
            prob = cp.Problem(cp.Minimize(sense * cp.trace(C @ Qv)), cons)
            try:
                prob.solve(solver=cp.SCS, eps=1e-9, max_iters=200000)
            except Exception as e:
                P("SCS failed", e); ok = False; break
            if Qv.value is None:
                P("no value, status", prob.status); ok = False; break
            sols.append(Qv.value.copy())
        if not ok: break
    if sols:
        mx = max(np.abs(S1 - S2).max() for S1 in sols for S2 in sols)
        P(f"SDP (SCS): {len(sols)} extreme-point solves (min/max of random functionals): "
          f"max pairwise entrywise difference = {mx:.3e}; max |sol - Q0| = {max(np.abs(S-Q0).max() for S in sols):.3e}")
        ev = np.linalg.eigvalsh(sols[0])
        P("eigenvalues of first solution (ascending):", np.round(ev, 5).tolist())
        P("numerical rank (tol 1e-5) of solutions:", sorted(set(int((np.linalg.eigvalsh(S) > 1e-5).sum()) for S in sols)))
    # ---- low-rank factorisation fit
    K, bb = cfg.keymap()
    def fit(r, seed):
        rg = np.random.default_rng(seed)
        def f(x):
            B = x.reshape(r, N)
            Qm = B.T @ B
            res = np.bincount(K.ravel(), weights=Qm.ravel(), minlength=len(bb)) - bb
            Rm = res[K]
            return 0.5 * (res ** 2).sum(), (2 * B @ Rm).ravel()
        x0 = rg.standard_normal(r * N) * 0.5
        o = minimize(f, x0, jac=True, method="L-BFGS-B", options=dict(maxiter=20000, maxfun=40000, ftol=1e-30, gtol=1e-12))
        return o.fun
    R = v["R"]
    for r in (R, R - 1, R - 2):
        res = [fit(r, s) for s in range(ntrials_fit)]
        P(f"low-rank fit Q=B^T B, B is {r}x{N}, {ntrials_fit} random starts: best residual(0.5||.||^2) = {min(res):.3e}, "
          f"median = {np.median(res):.3e}, #<1e-12: {sum(x<1e-12 for x in res)}")
    # ---- exact product independence
    pr, np_ = product_rank(cfg)
    P(f"exact: rank over Q of the {np_} products w_i w_j = {pr}")
    if do_forcing:
        forcing(cfg, mats, Q0)

def forcing(cfg, mats, Q0):
    """LP forcing: D = sum d_k mats_k.  Constraints: hole rows D=0 (Q_hx=0); for displayed pair (a,b):
    D_ab <= 0 (since Q_ab<=1); all |Q_ab|<=1; iteratively, when D_ab forced 0 for pair, add Q_ac=Q_bc."""
    N = cfg.N; d = len(mats)
    if d == 0:
        P("forcing: no free parameters."); return
    M = np.array([m.ravel() for m in mats]).T  # N^2 x d
    def row(a, c): return M[a * N + c]
    eqs, eqb = [], []
    for h in cfg.holes:
        for x in range(N):
            eqs.append(row(h, x)); eqb.append(-Q0[h, x])
    ub, ubb = [], []
    for a in range(N):
        for c in range(a + 1, N):
            ub.append(row(a, c)); ubb.append(1 - Q0[a, c])
            ub.append(-row(a, c)); ubb.append(1 + Q0[a, c])
    pairs = [tuple(p) for p in cfg.E2]
    forced = set()
    for it_ in range(10):
        newly = []
        for (a, c) in pairs:
            if (a, c) in forced: continue
            # minimise D_ac subject to constraints (D_ac<=0 known); forced iff min == 0
            res = linprog(row(a, c), A_ub=np.array(ub), b_ub=ubb, A_eq=np.array(eqs) if eqs else None,
                          b_eq=eqb if eqs else None, bounds=[(None, None)] * d, method="highs")
            if res.status == 0 and res.fun > -1e-9:
                newly.append((a, c))
        if not newly:
            break
        for (a, c) in newly:
            forced.add((a, c))
            for x in range(N):
                if x in (a, c): continue
                eqs.append(row(a, x) - row(c, x)); eqb.append(Q0[c, x] - Q0[a, x])
        P(f"forcing pass {it_+1}: newly forced pairs {newly}")
    P(f"forcing: {len(forced)} of {len(pairs)} displayed pairs forced to have coinciding Gram vectors")
    # remaining freedom in D under equalities
    if eqs:
        E = np.array(eqs)
        s = np.linalg.svd(E, compute_uv=False)
        rank_e = int((s > 1e-9).sum())
        P(f"remaining free dimension of D after equalities: {d - rank_e}")
    # also check: LP max |D| over feasible set
    mxs = []
    for k in range(d):
        for sg in (1, -1):
            res = linprog(sg * np.eye(d)[k], A_ub=np.array(ub), b_ub=ubb, A_eq=np.array(eqs) if eqs else None,
                          b_eq=eqb if eqs else None, bounds=[(None, None)] * d, method="highs")
            if res.status == 0: mxs.append(abs(res.fun))
    P(f"LP range of every free coordinate after forcing: max |d_k| = {max(mxs) if mxs else None}")

if __name__ == "__main__":
    m, n = 6, 5
    E1 = [0,1,2,5,8,11,13,15,19,22,24,28,29]
    E2 = [[6,4],[14,10],[16,21],[7,12],[26,18],[27,9],[17,3],[20,23]]
    analyse("overtaking witness (claimed rank 21)", Config(m, n, E1, E2))
    E1L = [0,1,2,6,8,12,13,16,19,22,24,25,28,29]
    E2L = [[3,17],[4,11],[5,20],[9,27],[10,15],[23,26]]
    analyse("limited witness (claimed rank 20)", Config(m, n, E1L, E2L))
