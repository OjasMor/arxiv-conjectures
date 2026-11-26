"""Core tools: configurations on an m x n grid, polynomial P_G, Gram affine space,
exact rank utilities.  Cell numbering: c = n*i + j."""
import itertools as it
from fractions import Fraction
import numpy as np
import scipy.sparse as sp


class Config:
    def __init__(self, m, n, E1, E2):
        self.m, self.n, self.E1, self.E2 = m, n, list(E1), [tuple(p) for p in E2]
        self.N = m * n
        used = list(self.E1) + [c for p in self.E2 for c in p]
        self.holes = [c for c in range(self.N) if c not in used]
        self.used = used

    def rc(self, c):
        return divmod(c, self.n)

    def validate(self):
        out = {}
        out["disjoint_supports"] = len(set(self.used)) == len(self.used)
        out["cells_in_range"] = all(0 <= c < self.N for c in self.used)
        out["pairs_distinct_cells"] = all(len(set(p)) == 2 for p in self.E2)
        out["n_E1"], out["n_E2"], out["n_holes"] = len(self.E1), len(self.E2), len(self.holes)
        out["R"] = len(self.E1) + len(self.E2)
        out["cell_identity_2R=mn+|E1|-H"] = 2 * out["R"] == self.N + len(self.E1) - len(self.holes)
        # C4-free one-edge graph: no two rows share two columns
        rows = {}
        for c in self.E1:
            i, j = self.rc(c)
            rows.setdefault(i, set()).add(j)
        c4 = 0
        for a, b in it.combinations(rows, 2):
            k = len(rows[a] & rows[b])
            c4 += k * (k - 1) // 2
        out["C4_count_of_E1_graph"] = c4
        return out

    def forms(self):
        """list of bilinear forms, each a list of cells (coefficient 1 each)."""
        return [(c,) for c in self.E1] + [tuple(p) for p in self.E2]

    def key(self, a, b):
        ia, ja = self.rc(a); ib, jb = self.rc(b)
        return (min(ia, ib), max(ia, ib), min(ja, jb), max(ja, jb))

    def poly(self):
        """P_G as dict monomial-key -> coefficient (coefficient of x_i x_k y_j y_l, i<=k, j<=l, after
        collecting all ordered products)."""
        P = {}
        for f in self.forms():
            for a in f:
                for b in f:
                    k = self.key(a, b)
                    P[k] = P.get(k, 0) + 1
        return P

    def Q0(self):
        Q = np.zeros((self.N, self.N))
        for f in self.forms():
            for a in f:
                for b in f:
                    Q[a, b] += 1
        return Q

    def constraint_matrix(self):
        """A (K x N^2) sparse with A vec(Q) = coefficient vector, using ordered products
        v_a v_b = x x y y with key; coefficient of monomial = sum over ordered (a,b) with that key."""
        keys = {}
        rows, cols = [], []
        for a in range(self.N):
            for b in range(self.N):
                k = self.key(a, b)
                r = keys.setdefault(k, len(keys))
                rows.append(r); cols.append(a * self.N + b)
        A = sp.csr_matrix((np.ones(len(rows)), (rows, cols)), shape=(len(keys), self.N ** 2))
        P = self.poly()
        b = np.zeros(len(keys))
        for k, r in keys.items():
            b[r] = P.get(k, 0)
        return A, b, keys

    def keymap(self):
        """N x N integer array of monomial index per (a,b)."""
        A, b, keys = self.constraint_matrix()
        K = np.zeros((self.N, self.N), dtype=int)
        for a in range(self.N):
            for b_ in range(self.N):
                K[a, b_] = keys[self.key(a, b_)]
        return K, b


def sym_nullspace(cfg):
    """Orthonormal basis (columns, as symmetric N x N matrices flattened) of the homogeneous
    symmetric solutions D with A vec(D) = 0, via exact-integer structure: use dense SVD."""
    N = cfg.N
    A, b, keys = cfg.constraint_matrix()
    iu = [(a, c) for a in range(N) for c in range(a, N)]
    # map symmetric param -> vec(Q)
    rows, cols, vals = [], [], []
    for t, (a, c) in enumerate(iu):
        rows.append(a * N + c); cols.append(t); vals.append(1.0)
        if a != c:
            rows.append(c * N + a); cols.append(t); vals.append(1.0)
    S = sp.csr_matrix((vals, (rows, cols)), shape=(N * N, len(iu)))
    M = (A @ S).toarray()
    u, s, vt = np.linalg.svd(M)
    rank = int((s > 1e-9).sum())
    ns = vt[rank:].T  # len(iu) x d
    mats = []
    for k in range(ns.shape[1]):
        D = np.zeros((N, N))
        for t, (a, c) in enumerate(iu):
            D[a, c] = ns[t, k]; D[c, a] = ns[t, k]
        mats.append(D)
    return mats, rank, len(iu)


def frac_rank(rows):
    """exact rank over Q of a list of integer vectors (dicts col->int)."""
    piv = {}
    r = 0
    for row in rows:
        v = {k: Fraction(x) for k, x in row.items() if x}
        while v:
            p = min(v)
            if p in piv:
                pv = piv[p]
                f = v[p] / pv[p]
                for k, x in pv.items():
                    nv = v.get(k, 0) - f * x
                    if nv:
                        v[k] = nv
                    else:
                        v.pop(k, None)
            else:
                piv[p] = v
                r += 1
                break
    return r


def product_rank(cfg, modulus=None):
    """Rank over Q of the span of the products w_i w_j (i<=j) of the displayed forms
    (as polynomials in x_i y_j monomials, i.e. over monomials x_i x_k y_j y_l)."""
    w = cfg.forms()
    rows = []
    for A_, B_ in it.combinations_with_replacement(range(len(w)), 2):
        d = {}
        for a in w[A_]:
            for b in w[B_]:
                k = cfg.key(a, b)
                d[k] = d.get(k, 0) + 1
        rows.append(d)
    return frac_rank(rows), len(rows)
