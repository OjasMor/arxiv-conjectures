"""Search all trees with max degree <= 3 on n vertices (nauty gentreeg) for violations of
P[N_stat <= k] >= P[N_seq <= k]. Exact rational arithmetic, reusing verify.analyse."""
import subprocess, sys
from fractions import Fraction as Fr
import networkx as nx
from verify import analyse
for n in [int(a) for a in sys.argv[1:]]:
    out = subprocess.run(["gentreeg", "-D3", "-q", str(n)], capture_output=True).stdout.splitlines()
    viol = []
    for line in out:
        G = nx.from_sparse6_bytes(line)
        edges = list(G.edges())
        _, stat, seq = analyse(n, edges)
        tot = sum(stat.values()); a = Fr(0); b = Fr(0)
        for k in range(0, n + 1):
            a += Fr(stat.get(k, 0), tot); b += seq.get(k, Fr(0))
            if a < b:
                viol.append((edges, k, a, b)); break
    print(f"n={n}: {len(out)} trees with max degree <= 3, violations: {len(viol)}", flush=True)
    for e, k, a, b in viol[:6]:
        print("   k=%d static %s < sequential %s  edges %s" % (k, a, b, e), flush=True)
