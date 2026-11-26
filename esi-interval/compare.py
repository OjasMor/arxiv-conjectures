import random, itertools
from brute import esi_brute, interval_adj, components, from_edges
from algo import esi_algo
random.seed(1)
stats = {"conn":[0,0], "disc":[0,0]}
mis = []
def test(iv, tag=""):
    adj = interval_adj(iv); n = len(iv)
    b = esi_brute(n, adj); a = esi_algo(iv)
    k = "conn" if components(n, adj) == 1 else "disc"
    stats[k][0] += 1
    if a != b:
        stats[k][1] += 1; mis.append((n, iv, a, b, k, tag))
N = 30000
for _ in range(N):
    n = random.randint(1, 12); m = random.choice([3,4,5,6,8,12])
    iv = []
    for _ in range(n):
        x, y = random.randint(0, m), random.randint(0, m)
        iv.append((min(x,y), max(x,y)))
    test(iv, "rand")
# structured
for n in range(1, 13):
    test([(0,0)]*n, "identical-point"); test([(0,5)]*n, "identical")
    test([(2*i,2*i) for i in range(n)], "indep"); test([(0,i) for i in range(n)], "clique-nested-left")
    test([(i, 2*n-i) for i in range(n)], "nested"); test([(i,i+1) for i in range(n)], "touch-path")
    test([(i,i+2) for i in range(n)], "overlap-path2"); test([(i,i+3) for i in range(n)], "path3")
    test([(0,2*n)]+[(2*i+1,2*i+1) for i in range(n-1)], "star-ish")
    test([(0, 2*n)]+[(2*i,2*i+1) for i in range(n-1)], "caterpillar")
    test([(2*i, 2*i+2) for i in range(n)], "touch2")
    # caterpillar: spine path + legs
    k = max(1, n//2); iv = [(2*i, 2*i+2) for i in range(k)] + [(2*i+1, 2*i+1) for i in range(n-k)]
    test(iv[:n], "caterpillar2")
# exhaustive over all families of n<=5 intervals in range 0..4 (multiset-ish: all ordered)
cnt = 0
ints = [(a,b) for a in range(5) for b in range(a,5)]
for n in range(1, 5):
    for iv in itertools.product(ints, repeat=n): test(list(iv), "exh"); cnt += 1
print("exhaustive extra:", cnt)
for k,(t,m) in stats.items(): print(k, "instances", t, "mismatches", m)
print("total", sum(t for t,m in stats.values()), "mismatches", len(mis))
if mis:
    mis.sort(key=lambda x:(x[0], sum(b-a for a,b in x[1])))
    print("smallest:", mis[0]); print(mis[:5])
