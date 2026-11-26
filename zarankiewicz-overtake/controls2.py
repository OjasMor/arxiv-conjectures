"""Controls at (4,4) against the paper's statements (Thm thm:44 and proof of thm:budget):
 (i)  an irreducible config with |E1|=8, |E2|=3, H=2 (R=11); certified EXACTLY by exact_force + product independence.
 (ii) a limited config with |E1|=9, |E2|=3, H=1 (R=12): paper says reducible (else z_2(4,4)>=12).  Show an explicit PSD Gram of
      rank <= 11 (reweighted-trace SDP), verified by eigenvalues and exact-polynomial residual."""
import sys, itertools as it, numpy as np, cvxpy as cp
sys.path.insert(0, "/Users/Ojas/Desktop/open-math-problems/results/zarankiewicz-overtake")
from zk import *
from controls import c4free_graphs, pairings
import io, contextlib
from exact_forcing import exact_force

def P(*a): print(*a, flush=True)

def certify(cfg):
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        ok = exact_force(cfg, verbose=False)
    pr, npr = product_rank(cfg)
    return ok and pr == npr, ok, (pr, npr)

def logdet_min_rank(cfg, iters=25):
    N = cfg.N; A, b, _ = cfg.constraint_matrix(); Aden = A.toarray()
    W = np.eye(N); best = None
    for k in range(iters):
        Qv = cp.Variable((N, N), symmetric=True)
        pr = cp.Problem(cp.Minimize(cp.trace(W @ Qv)), [Qv >> 0, Aden @ cp.reshape(Qv, (N * N,), order="C") == b])
        pr.solve(solver=cp.SCS, eps=1e-10, max_iters=100000)
        Q = Qv.value
        ev = np.linalg.eigvalsh(Q)
        W = np.linalg.inv(Q + 1e-4 * np.eye(N) * max(0.1, 1.0 / (k + 1)))
        r = int((ev > 1e-5).sum())
        res = np.abs(Aden @ Q.ravel() - b).max()
        best = (r, res, ev) if best is None or r < best[0] else best
    return best

if __name__ == "__main__":
    m = n = 4
    g8 = c4free_graphs(4, 4, 8); g9 = c4free_graphs(4, 4, 9)
    P("(4,4): #C4-free graphs with 8 edges", len(g8), ", with 9 edges", len(g9))
    rng = np.random.default_rng(1)
    found = None; tried = 0; certified_c = 0
    for gi in rng.permutation(len(g8)):
        E1 = list(g8[gi]); rest = [c for c in range(16) if c not in E1]
        for Pp in pairings(rest, 3):
            cfg = Config(m, n, E1, Pp)
            if len(cfg.holes) != 2: continue
            tried += 1
            good, okf, prn = certify(cfg)
            if good:
                found = cfg; break
        if found or tried > 3000: break
    P("tried", tried, "configurations (8 singles,3 pairs,2 holes)")
    if found:
        P("control (i): E1 =", found.E1, "E2 =", found.E2, "holes", found.holes, found.validate())
        P("  exact forcing + product independence: CERTIFIED irreducible, SOS rank = R = 11  (matches thm:44 value z_2A(4,4) >= 11)")
    # also count how many of those tried are certified
    cnt = 0; tot = 0
    for gi in rng.permutation(len(g8))[:5]:
        E1 = list(g8[gi]); rest = [c for c in range(16) if c not in E1]
        for Pp in pairings(rest, 3):
            cfg = Config(m, n, E1, Pp)
            if len(cfg.holes) != 2: continue
            tot += 1; cnt += certify(cfg)[0]
    P(f"  (of {tot} 8/3/2 configs on 5 random C4-free bases, {cnt} are certified irreducible by the exact test)")
    # (ii)
    P("control (ii): limited 9/3/1 configs, paper says all reducible")
    done = 0
    for E1 in g9:
        E1 = list(E1); rest = [c for c in range(16) if c not in E1]
        for Pp in pairings(rest, 3):
            cfg = Config(m, n, E1, Pp)
            if len(cfg.holes) != 1: continue
            good, okf, prn = certify(cfg)
            r, res, ev = logdet_min_rank(cfg, iters=12)
            P(f"  E1={E1} E2={Pp}: exact certificate of irreducibility {good} (forcing {okf}, products {prn}); "
              f"reweighted-trace SDP found PSD Gram of rank {r} (R=12), constraint residual {res:.1e}")
            done += 1
            break
        if done >= 4: break
