"""Reproduce statements/examples from arXiv:2611.19137 to validate conventions."""
import random
from itertools import product
from aff import *

random.seed(1)
ok_all = True


def report(name_, ok, extra=""):
    global ok_all
    ok_all &= bool(ok)
    print(("PASS " if ok else "FAIL ") + name_ + (" " + extra if extra else ""))


NAMES = {"id": ID, "s1": S1, "s2": S2, "s12": pmul(S1, S2), "s21": pmul(S2, S1), "w0": W0}
ORDER = ["id", "s1", "s2", "s12", "s21", "w0"]
A1 = lam(1, -1, 0)      # alpha_1^v
A2 = lam(0, 1, -1)
TH = lam(1, 0, -1)
Z = lam(0, 0, 0)


def comb(c1, c2):
    return vadd(vscale(c1, A1), vscale(c2, A2))

# --- 0. length formula cross-check
bad = 0
for _ in range(500):
    mu = lam(*[random.randint(-6, 6) for _ in range(2)], 0)
    mu = (mu[0], mu[1], -mu[0] - mu[1])
    for w in W:
        if length_geo((mu, w)) != length_im((mu, w)):
            bad += 1
report("0. geometric length == Iwahori-Matsumoto formula (paper eq. (length)), 3000 elts", bad == 0)
# generators have length 1, s0 = s_{theta,1}
report("0b. l(s0)=l(s1)=l(s2)=1", all(length(SIMPLE[i]) == 1 for i in range(3)))

# --- 1. Table A2_wt (weights)
tab_wt = {
 "id": [Z, Z, Z, Z, Z, Z],
 "s1": [A1, Z, A1, Z, Z, Z],
 "s2": [A2, A2, Z, Z, Z, Z],
 "s12": [comb(1, 1), A2, comb(1, 1), Z, A2, Z],
 "s21": [comb(1, 1), comb(1, 1), A1, A1, Z, Z],
 "w0": [comb(1, 1), comb(1, 1), comb(1, 1), A1, A2, Z],
}
ok = True
for r in ORDER:
    for j, c in enumerate(ORDER):
        if wt(NAMES[r], NAMES[c]) != tab_wt[r][j]:
            ok = False
            print("   mismatch wt", r, c, wt(NAMES[r], NAMES[c]), tab_wt[r][j])
report("1. Table A2_wt: all 36 weights wt(u->u')", ok)

# --- 2. Table A2_QBGEdgeReflection (reflection per edge)
TA = (None,)
def sr(root, k):
    return {"a1": refl(0, 1, k), "a2": refl(1, 2, k), "th": refl(0, 2, k)}[root]
tab_r = {
 ("id", "s1"): sr("a1", 0), ("id", "s2"): sr("a2", 0),
 ("s1", "id"): sr("a1", 1), ("s1", "s12"): sr("th", 0), ("s1", "s21"): sr("a2", 0),
 ("s2", "id"): sr("a2", 1), ("s2", "s12"): sr("a1", 0), ("s2", "s21"): sr("th", 0),
 ("s12", "s1"): sr("th", 1), ("s12", "w0"): sr("a2", 0),
 ("s21", "s2"): sr("th", 1), ("s21", "w0"): sr("a1", 0),
 ("w0", "id"): sr("th", 1), ("w0", "s12"): sr("a2", 1), ("w0", "s21"): sr("a1", 1),
}
found = {}
for u in W:
    for v, a, b, dn in qbg_edges(u):
        found[(name(u), name(v))] = edge_reflection(u, a, b, dn is not None)
report("2. Table A2_QBGEdgeReflection: same edge set (15 edges) and same reflections", found == tab_r,
       f"(my edges: {len(found)})")

# --- 3. worked example pr(s21 -> s1) = s_{th,1} s_{a2,1} s_{a1}, path (s21,s2,id,s1)
u, v = NAMES["s21"], NAMES["s1"]
paths = shortest_paths(u, v)
want = (NAMES["s21"], NAMES["s2"], ID, NAMES["s1"])
prod_ = amul(amul(sr("th", 1), sr("a2", 1)), sr("a1", 0))
report("3. Example pr(s21->s1): path (s21,s2,id,s1) is shortest and pr = s_{th,1}s_{a2,1}s_{a1}",
       any(p[0] == want for p in paths) and all(pr_pair(u, v) == prod_ for _ in [0])
       and all(path_pr(*p) == prod_ for p in paths), f"(#shortest paths={len(paths)})")

# --- 4. Lemma 4.? Lower corner = u(lam'_+ - wt(u->u')) for random lam' ; Table A2_lower; also Lemma upper corner
bad = 0
n = 0
for _ in range(300):
    m = [random.randint(-9, 9) for _ in range(2)]
    mu = comb(m[0], m[1])
    up = oppC(mu)
    mp = dominant(mu)
    for u in W:
        n += 1
        lc = aact(pr_pair(u, up), mu)
        if lc != pact(u, vsub(mp, wt(u, up))):
            bad += 1
        # x'_u = pr(u->u') x' = t^{lc} u
        xp = (mu, up)
        xu = amul(pr_pair(u, up), xp)
        if xu != (lc, u):
            bad += 1
report("4. Lemma lowerCornerWeight and Lemma x'_u = pr x' = t^{lam'_u} u (%d cases)" % n, bad == 0)
bad = 0
for _ in range(300):
    m = [random.randint(-9, 9) for _ in range(2)]
    mu = comb(m[0], m[1])
    ug = gateC(mu)
    mp = dominant(mu)
    for v in W:
        uc = aact(ainv(pr_pair(ug, v)), mu)
        if uc != pact(v, vadd(mp, wt(ug, v))):
            bad += 1
report("4b. Lemma upperCornerWeight: pr(u->u')^{-1} lam = u'(lam_+ + wt)", bad == 0)

# --- 5. paper statement: dominant lam' is lower QBG-regular iff <alpha_i,lam'> >= 3 (type A~2)
def lower_qbg_regular(mu):
    up = oppC(mu)
    mp = dominant(mu)
    for u in W:
        z = vsub(mp, wt(u, up))
        if not (pair(0, 1, z) >= 1 and pair(1, 2, z) >= 1):
            return False
    return True

def upper_qbg_regular(mu):
    ug = gateC(mu)
    mp = dominant(mu)
    for v in W:
        z = vadd(mp, wt(ug, v))
        if not (pair(0, 1, z) >= 1 and pair(1, 2, z) >= 1):
            return False
    return True

ok = True
for m1 in range(0, 8):
    for m2 in range(0, 8):
        # dominant lam' with <a1,.>=m1, <a2,.>=m2 : need integrality in coweight lattice: z0-z1=m1, z1-z2=m2
        z1 = F(m2 - m1, 3)
        z = (z1 + m1, z1, z1 - m2)
        got = lower_qbg_regular(z)
        exp = (m1 >= 3 and m2 >= 3)
        if got != exp:
            ok = False
            print("   mismatch", m1, m2, got, exp)
report("5. dominant lam' lower QBG-regular <=> <a_i,lam'> >= 3 (i=1,2) (range 0..7)", ok)

# --- 6. Example: lam' = 2a1+2a2: oppC=id, not lower QBG-regular, 6 pairwise distinct lower corners
mu = comb(2, 2)
up = oppC(mu)
cs = {aact(pr_pair(u, up), mu) for u in W}
report("6. Example lam'=2a1+2a2: oppC=id, not lower QBG-regular, six distinct lower corners",
       up == ID and not lower_qbg_regular(mu) and len(cs) == 6)

# --- 7. Example upper: lam = -a1-a2: gateC = w0, not upper QBG-regular, corners pairwise distinct
mu = comb(-1, -1)
ug = gateC(mu)
cs = {aact(ainv(pr_pair(ug, v)), mu) for v in W}
report("7. Example lam=-a1-a2: gateC=w0, not upper QBG-regular, six distinct upper corners",
       ug == W0 and not upper_qbg_regular(mu) and len(cs) == 6)

# --- 8. gates: lam dominant regular -> gate = t^lam w0; lam in H_{a1} nonzero dominant -> gate t^lam s21 ; H_{a2} -> s12
reg = comb(3, 3)  # <a1,>=3
gl = gate_elt(reg)
report("8a. dominant regular lam: gate = t^lam w0", gl == (reg, W0))
lam1 = (F(2, 3), F(2, 3), F(-4, 3))   # <a1,lam>=0, <a2,lam>=2 : dominant in H_{a1}
lam1 = comb(1, 2)  # a1+2a2: <a1,>=2-2=0, <a2,>=-1+4=3
assert pair(0, 1, lam1) == 0 and pair(1, 2, lam1) == 3
lam2 = comb(2, 1)  # <a1,>=3, <a2,>=0
assert pair(1, 2, lam2) == 0
report("8b. nonzero dominant lam in H_{a1}: gate = t^lam s21; in H_{a2}: t^lam s12",
       gate_elt(lam1)[1] == pmul(S2, S1) and gate_elt(lam2)[1] == pmul(S1, S2),
       f"(got {name(gate_elt(lam1)[1])},{name(gate_elt(lam2)[1])})")
report("8c. gate(0) = base alcove (identity)", gate_elt(Z) == (Z, ID))

# --- 9. Prop BruhatImpliesIwahori: x<=y (Bruhat) => lam_x <=_I lam_y.  Bruhat via subword sets
def bruhat_down(x):
    word, g0 = reduced_decomp(x)
    D = {(Z, ID)}
    for i in word:
        D = D | {amul(y, SIMPLE[i]) for y in D}
    return {amul(y, g0) for y in D}

bad = 0
cnt = 0
for _ in range(60):
    m = [random.randint(-4, 4) for _ in range(2)]
    mu = comb(m[0], m[1])
    y = (mu, random.choice(W))
    for x in bruhat_down(y):
        cnt += 1
        if not iw_leq(x[0], y[0]):
            bad += 1
report("9. Prop BruhatImpliesIwahori on random elements (%d pairs)" % cnt, bad == 0)

# --- 10. Thm lowerIwahoriPolytope: [0_w, lam']_I = P_{lam'} cap lattice, P = conv(lower corners)
def hull_contains(points, q):
    # 2D via coordinates (z0,z1); exact; convex hull by monotone chain
    P = sorted({(p[0], p[1]) for p in points})
    def cross(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
    if len(P) == 1:
        return (q[0], q[1]) == P[0]
    lower, upper = [], []
    for p in P:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    for p in reversed(P):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    H = lower[:-1] + upper[:-1]
    qq = (q[0], q[1])
    if len(H) == 1:
        return qq == H[0]
    if len(H) == 2:
        a, b = H
        return cross(a, b, qq) == 0 and min(a[0], b[0]) <= qq[0] <= max(a[0], b[0]) and min(a[1], b[1]) <= qq[1] <= max(a[1], b[1])
    for i in range(len(H)):
        if cross(H[i], H[(i + 1) % len(H)], qq) < 0:
            return False
    return True

bad = 0
tested = 0
for _ in range(25):
    m = [random.randint(-5, 5) for _ in range(2)]
    mu = comb(m[0], m[1])
    up = oppC(mu)
    corners = [aact(pr_pair(u, up), mu) for u in W]
    L = iwahori_lower(mu)
    tp = mu[0] % 1
    R = 8
    # simpler: all q = mu + comb(a,b) (same type)
    for a in range(-R, R + 1):
        for b in range(-R, R + 1):
            q = vadd(mu, comb(a, b))
            inP = hull_contains(corners, q)
            tested += 1
            if inP != (q in L):
                bad += 1
report("10. Thm lowerIwahoriPolytope: [0,lam']_I == conv(lower corners) cap lattice (%d pts)" % tested, bad == 0)

# --- 11. Corollary LowerCovers on lower-QBG-regular lam' (Bruhat covers AND Iwahori covers)
bad1 = bad2 = n = 0
for m1 in range(-9, 10):
    for m2 in range(-9, 10):
        mu = comb(m1, m2)
        if not lower_qbg_regular(mu):
            continue
        up = oppC(mu)
        xp = (mu, up)
        for u in W:
            for verts, es in shortest_paths(u, up):
                n += 1
                xs = [amul(path_pr(verts[j:], es[j:]), xp) for j in range(len(verts))]
                if any(length(xs[j + 1]) - length(xs[j]) != 1 for j in range(len(xs) - 1)):
                    bad1 += 1
                if any(not iw_cover(xs[j][0], xs[j + 1][0]) for j in range(len(xs) - 1)):
                    bad2 += 1
report("11. Cor LowerCovers (lower-QBG-regular): Bruhat covers & Iwahori covers (%d paths)" % n, bad1 == 0 and bad2 == 0, f"[bruhat fails {bad1}, iwahori fails {bad2}]")

# --- 12. Corollary UpperCovers on upper-QBG-regular lam (y^{u'} = t^{lam^{u'}} u' w0)
bad1 = bad2 = n = 0
for m1 in range(-9, 10):
    for m2 in range(-9, 10):
        mu = comb(m1, m2)
        if not upper_qbg_regular(mu):
            continue
        ug = gateC(mu)
        y = (mu, pmul(ug, W0))
        for v in W:
            for verts, es in shortest_paths(ug, v):
                n += 1
                ys = [amul(ainv(path_pr(verts[:j + 1], es[:j])), y) for j in range(len(verts))]
                if any(length(ys[j + 1]) - length(ys[j]) != 1 for j in range(len(ys) - 1)):
                    bad1 += 1
                if any(not iw_cover(ys[j][0], ys[j + 1][0]) for j in range(len(ys) - 1)):
                    bad2 += 1
report("12. Cor UpperCovers (upper-QBG-regular): Bruhat covers & Iwahori covers (%d paths)" % n, bad1 == 0 and bad2 == 0, f"[bruhat fails {bad1}, iwahori fails {bad2}]")

# --- 13. Lemma: oppC / gateC maximal/minimal length u with lam in C_u; gate = t^lam u w0, opp = t^lam u (shrunken) etc.
bad = 0
for m1 in range(-6, 7):
    for m2 in range(-6, 7):
        mu = comb(m1, m2)
        ups = [u for u in W if all(pair(a, b, pact(pinv(u), mu)) >= 0 for a, b in PAIRS)]  # lam in C_u: u^{-1}lam dominant
        if oppC(mu) != max(ups, key=ell_w) or gateC(mu) != min(ups, key=ell_w):
            bad += 1
        if opp_elt(mu) != (mu, oppC(mu)):
            bad += 1
report("13. Def/Lemma formula: oppC=max-length u with lam in C_u, gateC=min; opp gate = t^lam oppC(lam)", bad == 0)

print("\nALL PAPER CHECKS PASS" if ok_all else "\nSOME PAPER CHECKS FAILED")
