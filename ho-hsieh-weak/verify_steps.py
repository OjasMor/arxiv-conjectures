"""Step-by-step high-precision (mpmath, 120 digits) check of every analytic claim in the attempt.
Usage: python verify_steps.py   (prints PASS/FAIL per claim; summary at the end)"""
import itertools, random
import mpmath as mp
from angles import *
import numpy as np
from check import ground, ham, simulate

mp.mp.dps = 120
random.seed(1)
fails = []
def rec(name, ok, detail=""):
    print(("PASS " if ok else "FAIL ") + name + (("  " + detail) if detail else ""))
    if not ok: fails.append(name)

Ls = [2, 4, 6, 8, 10, 12, 14]
gs = [-50, -4, -3, -1.2, -1.0001, -1, -0.9999, -0.5, -0.01, -1e-4, 1e-4, 0.01, 0.3, 0.9999, 1, 1.0001, 1.5, 4, 50]

# ---- Step 1: mode decomposition ----
print("== Step 1: free-fermion reduction ==")
worst_root = 0
for L in Ls:
    n = L // 2; T = chebT(n)
    worst_root = max(worst_root, max(abs(peval(T, x)) for x in nodes(L)))
rec("nodes x_j=-cos((2j-1)pi/L) are roots of T_n", worst_root < mp.mpf(10) ** -100, f"max|T_n(x_j)|={mp.nstr(worst_root,3)}")
worst = 0
for L in [2, 4, 6, 8, 10, 12]:
    for g in gs:
        if g == 0: continue
        E, v, gap = ground(L, g)
        Efree = -2 * sum(mp.sqrt(1 + mp.mpf(g) ** 2 + 2 * mp.mpf(g) * x) for x in nodes(L))
        worst = max(worst, abs(float(Efree) - E))
rec("exact even-sector E0 == -2 sum_j r(x_j) (incl. g<0)", worst < 1e-9, f"max err={worst:.2e}")
# global (both parity) ground energy equals even-sector one where resolvable
H = ham(8, 0.5).toarray(); w = np.linalg.eigvalsh(H)
rec("global ground state lies in even sector (L=8, g=0.5 and -0.5 sample)", abs(w[0] - ground(8, 0.5)[0]) < 1e-10 and abs(np.linalg.eigvalsh(ham(8, -0.5).toarray())[0] - ground(8, -0.5)[0]) < 1e-10)

# ---- Step 2: Hermite error identity ----
print("== Step 2: Hermite error identity for 1/(u+lambda) ==")
worst = 0
for L in [2, 4, 8, 12]:
    n = L // 2; xs = nodes(L); T = chebT(n)
    for g in [mp.mpf(-3), mp.mpf('-0.4'), mp.mpf('0.7'), mp.mpf(2)]:
        for u in [mp.mpf('0.01'), mp.mpf(1), mp.mpf(37)]:
            f = lambda x: 1 / (u + 1 + g * g + 2 * g * x); fp = lambda x: -2 * g / (u + 1 + g * g + 2 * g * x) ** 2
            N = 2 * n; M = mp.matrix(N, N); rhs = mp.matrix(N, 1)
            for j, x in enumerate(xs):
                for i in range(N):
                    M[2 * j, i] = x ** i; M[2 * j + 1, i] = i * x ** (i - 1) if i else 0
                rhs[2 * j] = f(x); rhs[2 * j + 1] = fp(x)
            Hc = list(mp.lu_solve(M, rhs)); xi = -(1 + g * g + u) / (2 * g)
            for x in [mp.mpf('0.123'), mp.mpf('-0.77'), mp.mpf('1.9'), mp.mpf('-2.4')]:
                lhs = f(x) - peval(Hc, x)
                rhsv = peval(T, x) ** 2 / ((u + 1 + g * g + 2 * g * x) * peval(T, xi) ** 2)
                worst = max(worst, abs(lhs - rhsv) / (abs(rhsv) + mp.mpf(10) ** -30))
rec("f - Hermite(f) == T_n(x)^2 / ((u+lambda) T_n(xi_u)^2)", worst < mp.mpf(10) ** -80, f"max rel err={mp.nstr(worst,3)}")

# ---- Step 3: integral formula (3), concavity of D and E, bounds (2) ----
print("== Step 3: D, E concavity and sign bounds (2) ==")
def Jrange(g):
    c = (1 + g * g) / (2 * abs(g))
    return (-c, mp.inf) if g > 0 else (-mp.inf, c)
def grid(g, k=60):
    lo, hi = Jrange(g); pts = [mp.mpf(i) / k * 2 - 1 + mp.mpf('0.00137') for i in range(k + 1)]
    pts = [p for p in pts if abs(p) < 1]
    ext = []
    for e in (-1, 1):
        # exterior portion of J beyond e
        if e == 1:
            top = hi if hi != mp.inf else mp.mpf(10) ** 6
            if top > 1:
                ext += [1 + (top - 1) * (1 - mp.mpf(10) ** (-q)) for q in [0.5, 1, 2, 3, 5]] + [1 + (top - 1) * s / 10 for s in range(1, 10)] if hi != mp.inf else [1 + mp.mpf(10) ** (q / 2) for q in range(-8, 11)]
        else:
            bot = lo if lo != -mp.inf else -mp.mpf(10) ** 6
            if bot < -1:
                ext += [-1 + (bot + 1) * (1 - mp.mpf(10) ** (-q)) for q in [0.5, 1, 2, 3, 5]] + [-1 + (bot + 1) * s / 10 for s in range(1, 10)] if lo != -mp.inf else [-1 - mp.mpf(10) ** (q / 2) for q in range(-8, 11)]
    return pts, [x for x in ext if lambda_ok(g, x)]
def lambda_ok(g, x): return 1 + g * g + 2 * g * x > 0

viol_conc = viol_bound = viol_ext = 0; checked = 0; minmargin = mp.inf
for L in Ls:
    n = L // 2
    for g in gs:
        g = mp.mpf(str(g)); info = construct(L, g); h = info['h']; T = info['T']
        r = lambda x: mp.sqrt(1 + g * g + 2 * g * x)
        D = lambda x: (r(x) - peval(h, x)) / peval(T, x) ** 2
        E = lambda x: 2 * r(x) - D(x)
        pin, pex = grid(g)
        d = mp.mpf(10) ** -12
        for x in pin + pex:
            checked += 1
            if abs(x) < 1 and (-r(x) - peval(h, x) > mp.mpf(10) ** -60 or peval(h, x) - r(x) > mp.mpf(10) ** -60): viol_bound += 1
            if abs(x) > 1:
                a = g + x; hx = peval(h, x)
                if (a > 0 and hx < r(x) - mp.mpf(10) ** -60) or (a < 0 and hx > -r(x) + mp.mpf(10) ** -60): viol_ext += 1
            # concavity by second difference where x+-d in J
            if lambda_ok(g, x - d) and lambda_ok(g, x + d):
                for F in (D, E):
                    sd = (F(x + d) - 2 * F(x) + F(x - d)) / d ** 2
                    if sd > mp.mpf(10) ** -20: viol_conc += 1
rec("bounds -r<=h<=r on [-1,1]", viol_bound == 0, f"violations={viol_bound}")
rec("exterior bounds h>=r (a>0), h<=-r (a<0) on J\\[-1,1]", viol_ext == 0, f"violations={viol_ext}")
rec("D'' <= 0 and E'' <= 0 on grids in J", viol_conc == 0, f"violations={viol_conc} of {checked} pts x2")
# integral formula (3) at one case
L, g = 6, mp.mpf('0.7'); n = 3; info = construct(L, g); h = info['h']; T = info['T']; x0 = mp.mpf('0.31')
lam = 1 + g * g + 2 * g * x0; xi = lambda u: -(1 + g * g + u) / (2 * g)
# recompute ell and H0 explicitly through construct internals
xs = nodes(L); Nn = 2 * n; M = mp.matrix(Nn, Nn); rhs = mp.matrix(Nn, 1)
for j, x in enumerate(xs):
    for i in range(Nn):
        M[2 * j, i] = x ** i; M[2 * j + 1, i] = i * x ** (i - 1) if i else 0
    rhs[2 * j] = mp.sqrt(1 + g * g + 2 * g * x); rhs[2 * j + 1] = g / mp.sqrt(1 + g * g + 2 * g * x)
H0 = list(mp.lu_solve(M, rhs)); T2 = pmul(T, T)
l1 = (g + 1) - peval(H0, 1); lm = (g - 1) - peval(H0, -1); ell = lambda x: (l1 + lm) / 2 + x * (l1 - lm) / 2
Dnum = (mp.sqrt(lam) - peval(h, x0)) / peval(T, x0) ** 2
Dint = -ell(x0) - mp.quad(lambda u: mp.sqrt(u) / ((u + lam) * peval(T, xi(u)) ** 2), [0, 1, 10, mp.inf]) / mp.pi
rec("integral representation (3) of D", abs(Dnum - Dint) < mp.mpf(10) ** -30, f"|diff|={mp.nstr(abs(Dnum-Dint),3)}")

# ---- Step 4: P polynomial, nonnegativity ----
print("== Step 4: P(t) polynomial and P>=0 on R ==")
bad_rem = 0; bad_neg = 0; minQ = mp.inf; realroots = {}
for L in Ls:
    for g in gs:
        g = mp.mpf(str(g)); info = construct(L, g); P = info['P']
        bad_rem = max(bad_rem, info['rem'])
        tmax = mp.sqrt(1 + g * g + 2 * abs(g) * 1000)
        for i in range(-400, 401):
            t = tmax * i / 400 + mp.mpf('0.000123')
            if peval(P, t) < -mp.mpf(10) ** -60: bad_neg += 1
        if info['real_roots']: realroots[(L, float(g))] = info['real_roots']
rec("t - h(x(t)) divisible by t - a(x(t)) (remainder ~0)", bad_rem < mp.mpf(10) ** -60, f"max rem={mp.nstr(bad_rem,3)}")
rec("P(t) >= 0 on dense real grids", bad_neg == 0, f"violations={bad_neg}")
print("   (L,g) where cofactor Q has (numerically) real roots:", realroots if realroots else "none")

# ---- Step 5: A, B degrees and identity (1) ----
print("== Step 5: existence/degree of A,B and identity (1) ==")
worst_id = 0; baddeg = 0; worst_node = 0
for L in Ls:
    n = L // 2
    for g in gs:
        g = mp.mpf(str(g)); info = construct(L, g); A, B = info['A'], info['B']
        if info['degA'] > n or info['degB'] > n - 1: baddeg += 1
        # polynomial identity |A|^2 + (1-x^2)|B|^2 = 1 : test at many real x (poly of degree 2n)
        for x in [mp.mpf(i) / 7 - 1.3 for i in range(0, 20)]:
            va = peval(A, x); vb = peval(B, x)
            worst_id = max(worst_id, abs(abs(va) ** 2 + (1 - x * x) * abs(vb) ** 2 - 1))
        for x in info['xs']:
            r = mp.sqrt(1 + g * g + 2 * g * x); a = g + x; s = mp.sqrt(1 - x * x)
            va = peval(A, x); vb = peval(B, x)
            worst_node = max(worst_node, abs(va - (r + a) * vb))
rec("deg A <= n, deg B <= n-1", baddeg == 0)
rec("identity (1) as polynomial identity (checked at 20 real x)", worst_id < mp.mpf(10) ** -50, f"max resid={mp.nstr(worst_id,3)}")
rec("A=(r+a)B at nodes (target spinor)", worst_node < mp.mpf(10) ** -50, f"max resid={mp.nstr(worst_node,3)}")

# ---- Step 6: layer extraction lemma ----
print("== Step 6: layer extraction (QSP-type lemma) ==")
def forward(n, bs, vs, x):
    """spinor after layers e^{i b_k Z} e^{i v_k (xZ+sX)} acting on (1,0), k=1 first"""
    s = mp.sqrt(1 - x * x); G = mp.matrix([[x, s], [s, -x]]); psi = mp.matrix([1, 0])
    for b, v in zip(bs, vs):
        psi = mp.expm(1j * v * G) * psi
        psi = mp.matrix([mp.exp(1j * b) * psi[0], mp.exp(-1j * b) * psi[1]])
    return psi
mp.mp.dps = 40
worst_rt = 0
for n in [1, 2, 3, 5, 7]:
    for trial in range(5):
        bs = [mp.mpf(random.uniform(-3, 3)) for _ in range(n)]; vs = [mp.mpf(random.uniform(-3, 3)) for _ in range(n)]
        # polynomial A,B of the random circuit by interpolation at n+... points (A deg n, B deg n-1)
        pts = [mp.cos(mp.pi * (2 * j + 1) / (2 * (2 * n + 2))) * mp.mpf('0.9') for j in range(2 * n + 2)]
        vals = []
        for x in pts:
            ps = forward(n, bs, vs, x); s = mp.sqrt(1 - x * x); vals.append((ps[0], ps[1] / s))
        # fit A (n+1 coeffs) and B (n coeffs) by least squares on the points
        Vm = mp.matrix([[x ** i for i in range(n + 1)] for x in pts]); cA = mp.lu_solve(Vm, mp.matrix([v[0] for v in vals]))
        Vb = mp.matrix([[x ** i for i in range(n)] for x in pts]); cB = mp.lu_solve(Vb, mp.matrix([v[1] for v in vals]))
        A = list(cA); B = list(cB)
        b2, v2 = extract_layers(A, B, n)
        for x in [mp.mpf('0.3'), mp.mpf('-0.6')]:
            p1 = forward(n, bs, vs, x); p2 = forward(n, b2, v2, x)
            ov = abs(p1[0].conjugate() * p2[0] + p1[1].conjugate() * p2[1])
            worst_rt = max(worst_rt, 1 - ov)
rec("random n-layer circuits: polynomial pair -> extracted n layers reproduces the spinor (to phase)", worst_rt < mp.mpf(10) ** -25, f"max 1-overlap={mp.nstr(worst_rt,3)}")
mp.mp.dps = 120
# Hermite-built A,B -> layers -> pair-spinor equals target at every node
worst_fin = 0; nzero = 0
for L in [2, 4, 6, 8, 10, 12]:
    n = L // 2
    for g in gs:
        g = mp.mpf(str(g)); gam, bet, info = angles(L, g)
        b = [2 * x for x in bet]; v = [2 * x for x in gam]
        for x in info['xs']:
            r = mp.sqrt(1 + g * g + 2 * g * x); a = g + x; s = mp.sqrt(1 - x * x)
            ps = forward(n, b, v, x); tgt = mp.matrix([r + a, s]); tgt = tgt / mp.norm(tgt)
            ov = abs(tgt[0] * ps[0] + tgt[1] * ps[1])  # tgt real
            worst_fin = max(worst_fin, 1 - ov)
        nzero += sum(1 for q in gam if abs(q) < mp.mpf(10) ** -30)
rec("extracted n layers (no extra rotations) prepare target pair state at every node, mp 120 digits", worst_fin < mp.mpf(10) ** -50, f"max 1-overlap={mp.nstr(worst_fin,3)}; identity-padded layers={nzero}")

print("\nFAILED:", fails if fails else "none")
