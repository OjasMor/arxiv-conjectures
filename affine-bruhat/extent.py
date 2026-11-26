"""Where do failures live? Box 12: summarize failing lam by dominant rep pairings (m1,m2)=(<a1,lam+>,<a2,lam+>) and chamber."""
import sys
from collections import defaultdict
sys.argv = ["x", "12"]
exec(open("search.py").read().split("for conj in (1, 2):")[0])
for conj in (1, 2):
    fails = defaultdict(set); qbgreg_fail = 0; tot = 0
    for mu in pts:
        mp = dominant(mu); m = (int(pair(0,1,mp)), int(pair(1,2,mp)))
        if conj == 1:
            tgt = oppC(mu); qr = lower_qbg_regular(mu); xp = (mu, tgt); ch = tgt
        else:
            src = gateC(mu); qr = upper_qbg_regular(mu); x = gate_elt(mu); ch = src
        for other in W:
            paths = shortest_paths(other, tgt) if conj == 1 else shortest_paths(src, other)
            for verts, es in paths:
                k = len(verts) - 1
                if k == 0: continue
                xs = ([amul(path_pr(verts[j:], es[j:]), xp) for j in range(k + 1)] if conj == 1
                      else [amul(ainv(path_pr(verts[:j + 1], es[:j])), x) for j in range(k + 1)])
                f1 = any(length(xs[j+1]) - length(xs[j]) != 1 for j in range(k))
                f2 = any(xs[j][0] != xs[j+1][0] and not iw_cover(xs[j][0], xs[j+1][0]) for j in range(k))
                tot += 1
                if f1 or f2:
                    fails[(name(ch), m)].add((f1, f2))
                    if qr: qbgreg_fail += 1
    print(f"conj {conj}: box 12, {len(pts)} lam, {tot} instances; failures inside QBG-regular: {qbgreg_fail}")
    print("   failing (chamber of oppC/gateC, (<a1,lam+>,<a2,lam+>)) -> {(fail1,fail2)}:")
    mx = max(min(m) for (_, m) in fails) if fails else None
    print("   max over failing lam of min(<a1,lam+>,<a2,lam+>) =", mx)
    mx2 = max(max(m) for (_, m) in fails if min(m) >= 1) if any(min(m) >= 1 for (_, m) in fails) else None
    print("   failing lam are all within distance 2 of a wall of the dominant chamber (after conjugation):", all(min(m) <= 2 for (_, m) in fails))
    print("   max over failing lam of max(m1,m2) =", max(max(m) for (_, m) in fails), " (so failures occur at arbitrarily large lam along a wall, not only near 0)")
    for key in sorted(fails, key=lambda k: (k[1], k[0]))[:24]:
        print("     ", key, sorted(fails[key]))
