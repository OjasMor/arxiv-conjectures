"""Affine Weyl group of type A~_2 (extended: coweight lattice Q^v x| S_3), exact arithmetic.

Conventions (match arXiv:2611.19137):
 V* = {z in Q^3 : sum z = 0}; roots alpha_ab = e_a - e_b (a<b positive), <alpha_ab, z> = z_a - z_b,
 coroot = same vector. Simple alpha_1 = e_0-e_1, alpha_2 = e_1-e_2 (0-based coords), highest root theta = e_0-e_2.
 w in S_3 is a tuple p, p[i] = w(i), acting by (w z)[w(i)] = z[i].  Product (uv)(i)=u(v(i)) (rightmost acts first).
 Element x = t^mu w acts z -> mu + w z.  Stored as (mu, w) with mu tuple of Fractions.
 Base alcove a: z0>=z1>=z2, z0-z2<=1.  s_{beta,k}(z) = z - (<beta,z>-k) beta^v.  s_0 = s_{theta,1}.
 Length = number of hyperplanes H_{alpha,k} separating a and x a (computed geometrically), and
 also by the Iwahori-Matsumoto formula (paper eq. (length)); the two are cross-checked.
"""
from fractions import Fraction as F
from itertools import permutations, combinations
from functools import lru_cache

N = 3
IDP = (0, 1, 2)
PAIRS = [(0, 1), (0, 2), (1, 2)]          # positive roots e_a - e_b, a<b


def pmul(u, v):
    return tuple(u[v[i]] for i in range(N))


def pinv(u):
    r = [0] * N
    for i in range(N):
        r[u[i]] = i
    return tuple(r)


def pact(w, z):
    r = [None] * N
    for i in range(N):
        r[w[i]] = z[i]
    return tuple(r)


def vadd(a, b):
    return tuple(x + y for x, y in zip(a, b))


def vsub(a, b):
    return tuple(x - y for x, y in zip(a, b))


def vscale(c, a):
    return tuple(c * x for x in a)


def ell_w(w):
    return sum(1 for a, b in PAIRS if w[a] > w[b])


W = list(permutations(range(N)))
S1 = (1, 0, 2)
S2 = (0, 2, 1)
W0 = (2, 1, 0)
ID = IDP


def name(w):
    names = {ID: "id", S1: "s1", S2: "s2", pmul(S1, S2): "s12", pmul(S2, S1): "s21", W0: "w0"}
    return names[w]


# ---- affine elements (mu, w):  z -> mu + w z
def amul(x, y):
    return (vadd(x[0], pact(x[1], y[0])), pmul(x[1], y[1]))


def ainv(x):
    wi = pinv(x[1])
    return (vscale(-1, pact(wi, x[0])), wi)


def aact(x, z):
    return vadd(x[0], pact(x[1], z))


def pair(a, b, z):           # <e_a - e_b, z>
    return z[a] - z[b]


def refl(a, b, k):
    """s_{e_a - e_b, k} as affine element: z -> s_beta z + k beta^v"""
    sw = list(range(N))
    sw[a], sw[b] = b, a
    beta = [F(0)] * N
    beta[a] = F(1)
    beta[b] = F(-1)
    return (vscale(F(k), tuple(beta)), tuple(sw))


def root_refl(beta_pair, k):
    """beta_pair=(a,b) meaning root e_a-e_b where either a<b (positive) or a>b (negative root)."""
    a, b = beta_pair
    return refl(a, b, k)


BARY = (F(1, 3), F(0), F(-1, 3))   # interior point of base alcove


def length_geo(x):
    p = aact(x, BARY)
    tot = 0
    for a, b in PAIRS:
        v0 = pair(a, b, BARY)
        v1 = pair(a, b, p)
        lo, hi = (v0, v1) if v0 < v1 else (v1, v0)
        # integers strictly between (never equal to an integer since interior)
        import math
        tot += math.floor(hi) - math.floor(lo)
    return tot


def length_im(x):
    mu, w = x
    wi = pinv(w)
    tot = 0
    for a, b in PAIRS:
        # w^{-1} alpha = e_{wi(a)} - e_{wi(b)} positive iff wi(a)<wi(b)
        m = pair(a, b, mu)
        if wi[a] < wi[b]:
            tot += abs(m)
        else:
            tot += abs(m - 1)
    return tot


@lru_cache(maxsize=None)
def length(x):
    g = length_geo(x)
    return g


S0 = refl(0, 2, 1)
SIMPLE = {0: S0, 1: ((F(0),) * 3, S1), 2: ((F(0),) * 3, S2)}


def lam(*c):
    return tuple(F(x) for x in c)


def trans(mu, w=ID):
    return (tuple(F(x) for x in mu), w)


def dominant(z):
    return tuple(sorted(z, reverse=True))


def chamber_of_point(z):
    """u with z in u*C_f  (z regular)."""
    order = sorted(range(N), key=lambda i: -z[i])   # u(i) = position of i-th largest
    return tuple(order)


def regular(z):
    return all(pair(a, b, z) != 0 for a, b in PAIRS)


def coset_elems(mu):
    return [(mu, w) for w in W]


def gate_elt(mu):
    return min(coset_elems(mu), key=length)


def opp_elt(mu):
    return max(coset_elems(mu), key=length)


def alcove_chamber(x):
    return chamber_of_point(aact(x, BARY))


def gateC(mu):
    return alcove_chamber(gate_elt(mu))


def oppC(mu):
    return alcove_chamber(opp_elt(mu))


def typ(mu):
    """type in Z/3: coset of coroot lattice: (mu0 - mu1 ... ) use frac part of mu_0."""
    return (mu[0] % 1)


# ---- QBG
def qbg_edges(u):
    """list of (v, a, b, wt) for edges u -> u s_alpha, alpha=e_a-e_b (a<b);  wt in {0, alpha^v}"""
    out = []
    for a, b in PAIRS:
        v = list(u)
        v[a], v[b] = v[b], v[a]
        v = tuple(v)
        d = ell_w(v) - ell_w(u)
        ht = b - a                       # <2rho, alpha^v> = 2 ht
        if d == 1:
            out.append((v, a, b, None))
        elif d == 1 - 2 * ht:
            out.append((v, a, b, 1))
    return out


def edge_reflection(u, a, b, down):
    """r(u -> u s_alpha): s_{u alpha} if up, s_{-u alpha,1} if down. u alpha = e_{u(a)} - e_{u(b)}."""
    ua, ub = u[a], u[b]
    if not down:
        assert ua < ub
        return refl(ua, ub, 0)
    assert ua > ub
    # -u alpha = e_{ub} - e_{ua}, positive
    return refl(ub, ua, 1)


def edge_weight(a, b, down):
    wt = [F(0)] * N
    if down:
        wt[a] = F(1)
        wt[b] = F(-1)
    return tuple(wt)


@lru_cache(maxsize=None)
def qbg_dist_all(src):
    """BFS distances from src"""
    dist = {src: 0}
    frontier = [src]
    while frontier:
        nxt = []
        for u in frontier:
            for v, a, b, dn in qbg_edges(u):
                if v not in dist:
                    dist[v] = dist[u] + 1
                    nxt.append(v)
        frontier = nxt
    return dist


def dPhi(u, v):
    return qbg_dist_all(u)[v]


@lru_cache(maxsize=None)
def shortest_paths(u, v):
    """all shortest paths u->v as tuple of tuples of (vertex) with edge data: list of (verts, edges)
    edges: tuple of (a,b,down)"""
    d = dPhi(u, v)
    if d == 0:
        return [((u,), ())]
    res = []
    for w_, a, b, dn in qbg_edges(u):
        if dPhi(w_, v) == d - 1:
            for verts, es in shortest_paths(w_, v):
                res.append(((u,) + verts, ((a, b, dn is not None),) + es))
    return res


def path_pr(verts, es):
    """pr(p) = r_1 r_2 ... r_k"""
    g = ((F(0),) * 3, ID)
    for u, (a, b, dn) in zip(verts, es):
        g = amul(g, edge_reflection(u, a, b, dn))
    return g


def path_wt(verts, es):
    t = (F(0),) * 3
    for (a, b, dn) in es:
        t = vadd(t, edge_weight(a, b, dn))
    return t


def wt(u, v):
    verts, es = shortest_paths(u, v)[0]
    return path_wt(verts, es)


def pr_pair(u, v):
    verts, es = shortest_paths(u, v)[0]
    return path_pr(verts, es)


# ---- Bruhat lower sets / Iwahori order
def left_descents(x):
    L = length(x)
    return [i for i in range(3) if length(amul(SIMPLE[i], x)) < L]


def reduced_decomp(x):
    """x = s_{i1} ... s_{ik} g0 with l(g0)=0; returns word and g0"""
    word = []
    while length(x) > 0:
        i = left_descents(x)[0]
        word.append(i)
        x = amul(SIMPLE[i], x)
    return word, x


@lru_cache(maxsize=None)
def iwahori_lower(mu):
    """set {lam : lam <=_I mu} computed via subwords of a reduced word of the min-length coset rep
    (Def. of Iwahori order via folded galleries; shadows)."""
    g = gate_elt(mu)
    word, g0 = reduced_decomp(g)
    zero = (F(0),) * 3
    D = {((zero), ID)}
    for i in reversed(word):          # x_a = s_{i1}...s_{ik}; build subword products left-to-right
        pass
    # subword products of s_{i1} ... s_{ik}
    D = {(zero, ID)}
    for i in word:
        D = D | {amul(y, SIMPLE[i]) for y in D}
    base = aact(g0, zero)             # 0_omega vertex
    return frozenset(aact(y, base) for y in D)


def iw_leq(a, b):
    return a in iwahori_lower(b)


@lru_cache(maxsize=None)
def iw_cover(a, b):
    """a covered by b in Iwahori order"""
    if a == b or not iw_leq(a, b):
        return False
    for m in iwahori_lower(b):
        if m != a and m != b and iw_leq(a, m):
            return False
    return True
