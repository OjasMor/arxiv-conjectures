import sys
from collections import Counter, defaultdict
from aff import *

BOX = int(sys.argv[1]) if len(sys.argv) > 1 else 6   # max |coordinate| of lam (any type in Q^v)


def fmt(z):
    return "(" + ",".join(str(x) for x in z) + ")"


def lattice_box(B):
    pts = []
    for t in range(3):
        for k0 in range(-B - 1, B + 2):
            for k1 in range(-B - 1, B + 2):
                k2 = -t - k0 - k1
                z = tuple(F(k) + F(t, 3) for k in (k0, k1, k2))
                if max(abs(c) for c in z) <= B:
                    pts.append(z)
    return pts


def lower_qbg_regular(mu):
    up = oppC(mu)
    mp = dominant(mu)
    return all(pair(0, 1, vsub(mp, wt(u, up))) >= 1 and pair(1, 2, vsub(mp, wt(u, up))) >= 1 for u in W)


def upper_qbg_regular(mu):
    ug = gateC(mu)
    mp = dominant(mu)
    return all(pair(0, 1, vadd(mp, wt(ug, v))) >= 1 and pair(1, 2, vadd(mp, wt(ug, v))) >= 1 for v in W)


def classes(mu, qbgreg):
    return ("QBGreg" if qbgreg else "notQBGreg") + "/" + ("regular" if regular(mu) else "nonregular")


pts = lattice_box(BOX)
print(f"box: all lam in Q^v (coweight lattice, 3 types) with max|coord|<={BOX}: {len(pts)} points; "
      f"coroot-lattice ones: {sum(1 for p in pts if p[0] % 1 == 0)}")

for conj in (1, 2):
    name_ = "conj:CornerCovers" if conj == 1 else "conj:UpperCovers"
    print("\n" + "=" * 70 + f"\n{name_}\n" + "=" * 70)
    inst = Counter(); fail1 = Counter(); fail2 = Counter(); failany = Counter()
    lam_tot = Counter(); lam_fail = Counter()
    firstfail1 = defaultdict(list); firstfail2 = defaultdict(list)
    for mu in pts:
        if conj == 1:
            tgt = oppC(mu)
            qr = lower_qbg_regular(mu)
            xp = (mu, tgt)
        else:
            src = gateC(mu)
            qr = upper_qbg_regular(mu)
            x = gate_elt(mu)
        cls = classes(mu, qr)
        lam_tot[cls] += 1
        lam_has_fail = False
        for other in W:
            paths = shortest_paths(other, tgt) if conj == 1 else shortest_paths(src, other)
            for verts, es in paths:
                k = len(verts) - 1
                if k == 0:
                    continue          # empty chain: vacuous
                if conj == 1:
                    xs = [amul(path_pr(verts[j:], es[j:]), xp) for j in range(k + 1)]
                else:
                    xs = [amul(ainv(path_pr(verts[:j + 1], es[:j])), x) for j in range(k + 1)]
                f1 = any(length(xs[j + 1]) - length(xs[j]) != 1 for j in range(k))
                f2 = False
                for j in range(k):
                    a, c = xs[j][0], xs[j + 1][0]
                    if a != c and not iw_cover(a, c):
                        f2 = True
                        break
                inst[cls] += 1
                if f1:
                    fail1[cls] += 1
                    if len(firstfail1[cls]) < 3:
                        firstfail1[cls].append((mu, [name(v) for v in verts], [length(q) for q in xs]))
                if f2:
                    fail2[cls] += 1
                    if len(firstfail2[cls]) < 3:
                        firstfail2[cls].append((mu, [name(v) for v in verts], [fmt(q[0]) for q in xs]))
                if f1 or f2:
                    failany[cls] += 1
                    lam_has_fail = True
        if lam_has_fail:
            lam_fail[cls] += 1
    print(f"{'class':28s} {'#lam':>6s} {'#lam w/ fail':>12s} {'instances':>10s} {'fail(1)':>8s} {'fail(2)':>8s} {'fail any':>9s}")
    for cls in sorted(lam_tot):
        print(f"{cls:28s} {lam_tot[cls]:6d} {lam_fail[cls]:12d} {inst[cls]:10d} {fail1[cls]:8d} {fail2[cls]:8d} {failany[cls]:9d}")
    tot_i = sum(inst.values()); tot_f = sum(failany.values())
    print(f"{'TOTAL':28s} {sum(lam_tot.values()):6d} {sum(lam_fail.values()):12d} {tot_i:10d} {sum(fail1.values()):8d} {sum(fail2.values()):8d} {tot_f:9d}")
    # regular (any) / nonregular aggregated, and hypothesis aggregates
    for label, sel in (("regular lam (all <alpha,lam> != 0)", lambda c: c.endswith("/regular")),
                       ("non-regular lam", lambda c: c.endswith("/nonregular")),
                       ("QBG-regular lam (authors' hypothesis for the Corollary)", lambda c: c.startswith("QBGreg")),
                       ("NOT QBG-regular lam", lambda c: c.startswith("notQBGreg"))):
        i = sum(v for c, v in inst.items() if sel(c)); f1 = sum(v for c, v in fail1.items() if sel(c))
        f2 = sum(v for c, v in fail2.items() if sel(c)); fa = sum(v for c, v in failany.items() if sel(c))
        print(f"  {label}: instances {i}, fail(1) {f1}, fail(2) {f2}, fail either {fa}, satisfy conjecture {i - fa}")
    print("  sample failures of part (1) [lam, path, lengths along chain]:")
    for cls, L in firstfail1.items():
        for t in L[:2]:
            print("    ", cls, fmt(t[0]), t[1], t[2])
    print("  sample failures of part (2) [lam, path, translation parts along chain]:")
    for cls, L in firstfail2.items():
        for t in L[:2]:
            print("    ", cls, fmt(t[0]), t[1], t[2])
