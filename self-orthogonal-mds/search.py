"""Search for q-ary [q+2,3] Euclidean self-orthogonal MDS codes, q even, from hyperovals.
A [q+2,3] MDS code has generator matrix whose columns are v_i*P_i with {P_i} a hyperoval of PG(2,q).
Self-orthogonal  <=>  sum_i w_i * P_i P_i^T = 0 with w_i = v_i^2 (every element of F_{2^h} is a square).
So we need a nowhere-zero vector w in the kernel of the 6 x (q+2) matrix of quadratic monomials."""
import itertools, random, json, sys

class GF2m:
    def __init__(self, m, poly):
        self.m, self.q, self.poly = m, 1 << m, poly
        self.exp, self.log = [0]*(2*self.q), [0]*self.q
        x = 1
        for i in range(self.q-1):
            self.exp[i] = x; self.log[x] = i
            x <<= 1
            if x & self.q: x ^= poly
        assert x == 1, "poly not primitive"
        for i in range(self.q-1, 2*self.q): self.exp[i] = self.exp[i-(self.q-1)]
    def mul(self, a, b): return 0 if a == 0 or b == 0 else self.exp[self.log[a]+self.log[b]]
    def inv(self, a): return self.exp[(self.q-1-self.log[a]) % (self.q-1)]
    def pw(self, a, e):
        if a == 0: return 0 if e else 1
        return self.exp[(self.log[a]*e) % (self.q-1)]
    def sqrt(self, a): return self.pw(a, self.q//2)

def det3(F, a, b, c):
    m = F.mul
    return m(a[0], m(b[1],c[2]) ^ m(b[2],c[1])) ^ m(a[1], m(b[0],c[2]) ^ m(b[2],c[0])) ^ m(a[2], m(b[0],c[1]) ^ m(b[1],c[0]))

def is_arc(F, pts): return all(det3(F,a,b,c) for a,b,c in itertools.combinations(pts,3))

def kernel(F, rows, n):
    """basis of {w : rows * w = 0} over F"""
    M = [r[:] for r in rows]; piv = []; r = 0
    for c in range(n):
        p = next((i for i in range(r, len(M)) if M[i][c]), None)
        if p is None: continue
        M[r], M[p] = M[p], M[r]
        iv = F.inv(M[r][c]); M[r] = [F.mul(iv, x) for x in M[r]]
        for i in range(len(M)):
            if i != r and M[i][c]:
                f = M[i][c]; M[i] = [x ^ F.mul(f, y) for x, y in zip(M[i], M[r])]
        piv.append(c); r += 1
        if r == len(M): break
    free = [c for c in range(n) if c not in piv]; basis = []
    for f in free:
        w = [0]*n; w[f] = 1
        for i, c in enumerate(piv): w[c] = M[i][f]
        basis.append(w)
    return basis, len(piv)

def attempt(F, pts, name, seed=1, tries=200000):
    n = len(pts); assert n == F.q + 2 and is_arc(F, pts), "not a hyperoval"
    mons = [(0,0),(1,1),(2,2),(0,1),(0,2),(1,2)]
    rows = [[F.mul(P[a], P[b]) for P in pts] for a, b in mons]
    basis, rank = kernel(F, rows, n)
    forced = [i for i in range(n) if all(b[i] == 0 for b in basis)]
    print(f"{name}: q={F.q} n={n} rank={rank} kernel_dim={len(basis)} forced_zero_coords={forced}")
    if forced or not basis: return None
    rng = random.Random(seed)
    for _ in range(tries):
        w = [0]*n
        for b in basis:
            c = rng.randrange(F.q)
            if c: w = [x ^ F.mul(c, y) for x, y in zip(w, b)]
        if all(w):
            v = [F.sqrt(x) for x in w]
            G = [[F.mul(v[i], pts[i][r]) for i in range(n)] for r in range(3)]
            return G
    print("  no nowhere-zero kernel vector found in random tries"); return None

def verify(F, G):
    n = len(G[0]); cols = [tuple(G[r][i] for r in range(3)) for i in range(n)]
    gram = [[0]*3 for _ in range(3)]
    for a in range(3):
        for b in range(3):
            s = 0
            for i in range(n): s ^= F.mul(G[a][i], G[b][i])
            gram[a][b] = s
    return gram == [[0]*3]*3, is_arc(F, cols)

if __name__ == "__main__":
    out = {}
    # q = 4, 8: regular hyperoval (the only one)
    for m, poly in [(2, 0b111), (3, 0b1011), (4, 0b10011), (5, 0b100101), (6, 0b1000011)]:
        F = GF2m(m, poly)
        reg = [(1, t, F.pw(t, 2)) for t in range(F.q)] + [(0,1,0), (0,0,1)]
        attempt(F, reg, f"regular hyperoval")
    # q = 16: Lunelli-Sce hyperoval, o-polynomial with eta^4 = eta + 1
    F = GF2m(4, 0b10011); e = 2
    def ls(x):
        p = F.pw
        return p(x,12) ^ p(x,10) ^ F.mul(p(e,11), p(x,8)) ^ p(x,6) ^ F.mul(p(e,2), p(x,4)) ^ F.mul(p(e,9), p(x,2))
    LS = [(1, t, ls(t)) for t in range(16)] + [(0,1,0), (0,0,1)]
    if is_arc(F, LS):
        G = attempt(F, LS, "Lunelli-Sce hyperoval")
        if G: print("  verify (self-orthogonal, MDS):", verify(F, G)); out["q16_lunelli_sce"] = {"field_poly": "x^4+x+1", "G": G}
    else: print("LS formula as typed is not a hyperoval")
    # q = 32: translation hyperoval D(4), and q = 128: D(4)
    for m, poly in [(5, 0b100101), (7, 0b10000011)]:
        F = GF2m(m, poly)
        T = [(1, t, F.pw(t, 4)) for t in range(F.q)] + [(0,1,0), (0,0,1)]
        G = attempt(F, T, "translation hyperoval D(4)")
        if G:
            print("  verify (self-orthogonal, MDS):", verify(F, G))
            out[f"q{F.q}_translation_D4"] = {"field_poly_bits": bin(poly), "G": G}
    json.dump(out, open("certificates.json", "w"))
