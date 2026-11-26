from aff import *

A1 = lam(1, -1, 0)
A2 = lam(0, 1, -1)
def fmt(z):
    return "(" + ",".join(str(x) for x in z) + ")"
def comb(c1, c2):
    return vadd(vscale(c1, A1), vscale(c2, A2))

print("=== Attempt 1: conj:CornerCovers, lam' = (2,-3,1) ===")
mu = lam(2, -3, 1)
up = oppC(mu)
print("lam'=", fmt(mu), " <a1,.>,<a2,.>,<theta,.> =", pair(0,1,mu), pair(1,2,mu), pair(0,2,mu), "regular:", regular(mu))
print("lam'_+ =", fmt(dominant(mu)), " u'=oppC =", name(up), " opp-gate elt = t^lam' u' length", length((mu, up)))
xp = (mu, up)
for u in W:
    d = dPhi(u, up)
    for verts, es in shortest_paths(u, up):
        if d < 2 and u != W0:
            continue
        xs = [amul(path_pr(verts[j:], es[j:]), xp) for j in range(len(verts))]
        lams = [x[0] for x in xs]
        print(f"u={name(u)} path={[name(v) for v in verts]}")
        print("   x'_u:", [(fmt(x[0]), name(x[1])) for x in xs])
        print("   lengths:", [length(x) for x in xs], "cover steps:", [length(xs[j+1]) - length(xs[j]) == 1 for j in range(len(xs)-1)])
        for j in range(len(xs) - 1):
            a, c = lams[j], lams[j+1]
            if a != c:
                between = [m for m in iwahori_lower(c) if m not in (a, c) and iw_leq(a, m)]
                print(f"   step {j}: lam'_u {fmt(a)} <=_I {fmt(c)}: {iw_leq(a,c)}; Iwahori cover: {iw_cover(a,c)}; strictly between: {[fmt(m) for m in between]}")
        if d == 2 and u == W0:
            pass

print()
print("--- the specific intermediate b=(2,1,-3), witnessed by Bruhat chain z0<z1<z2 (attempt 1) ---")
a = lam(-2, 1, 1); b = lam(2, 1, -3); c = lam(2, -3, 1)
z0 = (a, ID)                    # t^a
z1 = amul(S0, z0)
z2 = amul(((F(0),)*3, S2), z1)
print("lengths", [length(z) for z in (z0, z1, z2)], "translation parts", [fmt(z[0]) for z in (z0, z1, z2)], "dirs", [name(z[1]) for z in (z0, z1, z2)])
print("a<=_I b:", iw_leq(a, b), " b<=_I c:", iw_leq(b, c), " a<=_I c:", iw_leq(a, c), "distinct:", len({a, b, c}) == 3)

print()
print("=== Attempt 2: conj:UpperCovers, lam = (0,1,-1) ===")
mu = lam(0, 1, -1)
ug = gateC(mu)
print("lam=", fmt(mu), "pairings", pair(0,1,mu), pair(1,2,mu), pair(0,2,mu), "regular:", regular(mu), " lam_+ =", fmt(dominant(mu)), " u=gateC =", name(ug))
x = gate_elt(mu)
print("gate element x = t^lam w, w =", name(x[1]), " length", length(x), " coset lengths", sorted(length((mu, w)) for w in W))
y = (mu, pmul(ug, W0))
print("t^lam u w0 == gate elt:", y == x)
for v in W:
    for verts, es in shortest_paths(ug, v):
        if v == ID:
            print("path", [name(q) for q in verts], "weights", fmt(path_wt(verts, es)), "pr =", [(fmt(r[0]), name(r[1])) for r in [path_pr(verts, es)]])
            xs = [amul(ainv(path_pr(verts[:j+1], es[:j])), x) for j in range(len(verts))]
            print("  x^{u_j}:", [(fmt(q[0]), name(q[1])) for q in xs], "lengths", [length(q) for q in xs])
            for j in range(len(xs)-1):
                a, c = xs[j][0], xs[j+1][0]
                between = [m for m in iwahori_lower(c) if m not in (a, c) and iw_leq(a, m)]
                print(f"  step {j}: lam^u {fmt(a)} <=_I {fmt(c)}: {iw_leq(a,c)}; Iwahori cover {iw_cover(a,c)}; between {[fmt(m) for m in between]}")
            r = path_pr(verts, es)
            print("  r = pr is an affine reflection s_{a1,1}?:", r == refl(0, 1, 1))
            # explicit Bruhat chain x < s2 x < s0 s2 x < s2 s0 s2 x
            ch = [x]
            for i in (2, 0, 2):
                ch.append(amul(SIMPLE[i], ch[-1]))
            print("  left-mult chain x, s2x, s0s2x, s2s0s2x lengths:", [length(q) for q in ch], " last == r x:", ch[-1] == amul(r, x))
