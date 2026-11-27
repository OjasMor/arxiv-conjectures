"""Algorithmic implementation of the construction in runs/attempts/2611.31308__1faed.md.

Given (L, g) (L even, g real, g != 0) return VQCS angles (gamma_k, beta_k), k=1..L/2, for
|Psi> = prod_k exp(-i beta_k H_X) exp(-i gamma_k H_ZZ) |+..+>   (k=1 applied first)
H_X = -sum X_i, H_ZZ = -sum Z_i Z_{i+1} (periodic), H_TFIM = H_ZZ + g H_X   (Jiang 2611.31308 conventions)

Everything is done in mpmath at high precision (spectral factorisation has double roots).
Usage: python angles.py L g
"""
import sys
import mpmath as mp

mp.mp.dps = 120

# ---------- tiny polynomial toolkit (lists, low -> high) ----------
def padd(a, b):
    n = max(len(a), len(b)); return [(a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0) for i in range(n)]
def pscale(a, c): return [c * x for x in a]
def pmul(a, b):
    r = [mp.mpf(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b): r[i + j] += x * y
    return r
def peval(a, x):
    r = 0
    for c in reversed(a): r = r * x + c
    return r
def pcompose(a, q):  # a(q(t))
    r = [mp.mpf(0)]
    for c in reversed(a): r = padd(pmul(r, q), [c])
    return r
def pdivmod(num, den):
    num = list(num); out = [mp.mpf(0)] * max(1, len(num) - len(den) + 1)
    for i in range(len(num) - len(den), -1, -1):
        c = num[i + len(den) - 1] / den[-1]; out[i] = c
        for j, d in enumerate(den): num[i + j] -= c * d
    return out, num[:len(den) - 1]
def chebT(n):
    T0, T1 = [mp.mpf(1)], [mp.mpf(0), mp.mpf(1)]
    if n == 0: return T0
    for _ in range(n - 1):
        T0, T1 = T1, padd(pmul([0, 2], T1), pscale(T0, -1))
    return T1

def nodes(L):
    n = L // 2
    return [-mp.cos((2 * j - 1) * mp.pi / L) for j in range(1, n + 1)]

def construct(L, g, verbose=False):
    g = mp.mpf(g); n = L // 2
    assert g != 0 and L % 2 == 0 and L >= 2
    xs = nodes(L)
    lam = lambda x: 1 + g * g + 2 * g * x
    r_at = lambda x: mp.sqrt(lam(x))
    # Hermite interpolant H0 (deg <= 2n-1) of r, r' at the nodes
    N = 2 * n; M = mp.matrix(N, N); rhs = mp.matrix(N, 1)
    for j, x in enumerate(xs):
        for i in range(N):
            M[2 * j, i] = x ** i
            M[2 * j + 1, i] = i * x ** (i - 1) if i > 0 else 0
        rhs[2 * j] = r_at(x); rhs[2 * j + 1] = g / r_at(x)
    H0 = list(mp.lu_solve(M, rhs))
    T = chebT(n); T2 = pmul(T, T)
    l1 = (g + 1) - peval(H0, 1); lm = (g - 1) - peval(H0, -1)
    ell = [(l1 + lm) / 2, (l1 - lm) / 2]
    h = padd(H0, pmul(T2, ell))
    # P(t) = (t - h(x(t))) / (t - a(x(t))),  x(t) = (t^2-1-g^2)/(2g)
    xt = [-(1 + g * g) / (2 * g), 0, 1 / (2 * g)]
    num = padd([0, 1], pscale(pcompose(h, xt), -1))
    den = padd([0, 1], pscale(padd([g], xt), -1))
    P, rem = pdivmod(num, den)
    remn = max(abs(c) for c in rem)
    # divide out double roots at t_j = r(x_j)
    tj = [r_at(x) for x in xs]
    Q = P
    for t in tj:
        for _ in range(2):
            Q, rm = pdivmod(Q, [-t, 1])
    # roots of the cofactor Q (degree 2n), choose half
    while abs(Q[-1]) < mp.mpf(10) ** (-80) and len(Q) > 1: Q = Q[:-1]
    roots = mp.polyroots(list(reversed(Q)), maxsteps=2000, extraprec=2000) if len(Q) > 1 else []
    tol = mp.mpf(10) ** (-15)
    up = [z for z in roots if z.imag > tol]
    real = sorted([z for z in roots if abs(z.imag) <= tol], key=lambda z: z.real)
    ok_pair = (len(real) % 2 == 0) and (len(up) * 2 + len(real) == len(roots))
    # choose: upper-half-plane roots + one from each consecutive real pair
    chosen = list(up) + [mp.mpf(z.real) for z in real[::2]]
    F = [mp.mpc(mp.sqrt(Q[-1] if len(Q) > 1 else Q[0]))]
    # leading coefficient of P is Q[-1] (the t_j factors are monic)
    for z in tj + chosen: F = pmul(F, [-z, 1])
    F = [mp.mpc(c) for c in F]
    # split F(t) = A(x(t)) - (a(x(t)) + t) B(x(t)); t^2 = 2g x + 1 + g^2
    ev = [F[i] for i in range(0, len(F), 2)]; od = [F[i] for i in range(1, len(F), 2)]
    sq = [1 + g * g, 2 * g]
    B = pscale(pcompose(od, sq), -1) if od else [mp.mpc(0)]
    A = padd(pcompose(ev, sq), pmul([g, 1], B))
    while len(A) > n + 1 and abs(A[-1]) < mp.mpf(10) ** (-60): A = A[:-1]
    while len(B) > n and abs(B[-1]) < mp.mpf(10) ** (-60): B = B[:-1]
    info = dict(h=h, P=P, Q=Q, F=F, A=A, B=B, xs=xs, rem=remn, ok_pair=ok_pair,
                real_roots=len(real), degA=len(A) - 1, degB=len(B) - 1, T=T)
    return info

def extract_layers(A, B, n):
    """Peel layers per Section 4. Returns lists (b_k, v_k), k=1..n (k=1 innermost / first applied)."""
    A = [mp.mpc(c) for c in A] + [mp.mpc(0)] * (n + 1 - len(A))
    B = [mp.mpc(c) for c in B] + [mp.mpc(0)] * (n - len(B))
    bs, vs = [], []   # collected outermost first
    eps = mp.mpf(10) ** (-40)
    for m in range(n, 0, -1):
        Am, Bm = A[m], B[m - 1]
        if abs(Am) < eps and abs(Bm) < eps:
            bs.append(mp.mpf(0)); vs.append(mp.mpf(0)); continue
        # e^{2ib} = A_m / B_{m-1}
        b = mp.arg(Am / Bm) / 2
        U = [c * mp.exp(-1j * b) for c in A]; W = [c * mp.exp(1j * b) for c in B]
        d = U[m]
        y = (U[m - 1] - (W[m - 2] if m >= 2 else 0)) / d      # purely imaginary = i*y
        y = y.imag / 1  # (U_{m-1}-W_{m-2})/d = i y
        # c d - i q (i y d) = 0 -> c = -q y  -> v = acot(-y)
        v = mp.atan2(1, -y)   # c=cos v, q=sin v with c/q = -y
        c, q = mp.cos(v), mp.sin(v)
        # new polynomials A' = (c - i q x) U - i q (1-x^2) W ; B' = -i q U + (c + i q x) W
        Ap = [mp.mpc(0)] * (n + 3); Bp = [mp.mpc(0)] * (n + 2)
        for k in range(n + 1):
            Ap[k] += c * U[k]; Ap[k + 1] += -1j * q * U[k]
        for k in range(n):
            Ap[k] += -1j * q * W[k]; Ap[k + 2] += 1j * q * W[k]
            Bp[k] += c * W[k] + (-1j * q * 0) ; Bp[k + 1] += 1j * q * W[k]
        for k in range(n + 1): Bp[k] += -1j * q * U[k]
        A = Ap[:n + 1] ; B = Bp[:n]
        bs.append(b); vs.append(v)
    # outermost first -> reverse so index 0 is the first applied (innermost)
    return list(reversed(bs)), list(reversed(vs))

def angles(L, g):
    info = construct(L, g); n = L // 2
    b, v = extract_layers(info['A'], info['B'], n)
    beta = [x / 2 for x in b]; gamma = [x / 2 for x in v]
    return gamma, beta, info

if __name__ == "__main__":
    L = int(sys.argv[1]); g = mp.mpf(sys.argv[2])
    gam, bet, info = angles(L, g)
    print(f"L={L} g={g}  degA={info['degA']} degB={info['degB']} real roots of cofactor={info['real_roots']}")
    for k, (a, b) in enumerate(zip(gam, bet), 1):
        print(f"layer {k}: gamma={mp.nstr(a, 15)} beta={mp.nstr(b, 15)}")
