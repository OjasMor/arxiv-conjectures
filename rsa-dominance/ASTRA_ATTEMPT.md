# arXiv:2611.14718 — Conjecture conj:grado3: on every graph of maximum degree at most 3 the sequential model stochastically dominates the static model (verified by the authors for all connected such graphs up to 12 vertices)

status: completed cost: $0.6004 incomplete: None

VERDICT: DISPROVED

STATEMENT: There is a tree \(G\) on 15 vertices with maximum degree 3 for which
\[
\mathbb P(N_G^{\mathrm{stat}}\le 6)=\frac1{55}
\;<\;
\frac{64}{3375}=\mathbb P(N_G^{\mathrm{seq}}\le 6).
\]
This is the reverse of the conjectured inequality at \(k=6\).

ARGUMENT: Start with the path \(0-1-2-3-4-5-6\). Attach the three pendant paths \(0-7-8\), \(3-9-10\), and \(6-11-12\), and attach a leaf \(13\) to \(0\) and a leaf \(14\) to \(6\). These are all the edges.

**Static probability.** Split the maximal independent sets according to whether they contain vertex \(3\).

- If \(3\) is occupied, then \(2,4,9\) are blocked and \(10\) is forced. Each of the two remaining components is a fork: a center with two leaves and one arm of length two. A fork has one maximal independent set of size 2 (the center and the tip of the long arm) and two of size 3 (both leaves and either vertex of the long arm). Thus this case gives \(3^2=9\) sets, exactly one of size 6 and the others larger.
- If \(3\) is unoccupied, deleting it leaves the edge \(9-10\) and two isomorphic components. Each component has a center with one leaf and two arms of length two. It has five maximal independent sets, all of size 3: one containing the center, and four containing the leaf and one vertex from each arm. Thus there are initially \(2\cdot5^2=50\) choices, all of size 7. We must discard those leaving \(3\) undominated, i.e. those omitting all of \(2,4,9\). This forces \(10\) on the edge; on the left there are two choices omitting \(2\), and on the right two omitting \(4\). Hence \(50-4=46\) choices remain.

There are therefore \(9+46=55\) maximal independent sets, and the unique one of size at most 6 is
\[
I=\{0,3,6,8,10,12\}.
\]

**Sequential probability.** Use a uniform random ordering of the vertices, accepting each vertex if still available. This gives the paper’s sequential law: after the first vertex and its neighbors are removed, the relative order of the survivors is again uniform. The output is \(I\) exactly when every vertex outside \(I\) has an earlier neighbor in \(I\). Necessity follows because every rejected vertex was blocked by an earlier accepted one; sufficiency follows by induction along the ordering, since \(I\) is independent.

Consequently, deleting the edges \(1-2\) and \(4-5\) does not change the event that the output is \(I\): neither edge has an endpoint in \(I\). The deletions leave three disjoint five-vertex forks. In each fork the target is its center and the tip of its long arm. If the center comes first, success is certain. If the tip comes first, it blocks its neighbor, and success requires the center to precede its two remaining leaves, with probability \(1/3\). Every other first vertex gives failure. The success probability per fork is therefore \(1/5+(1/5)(1/3)=4/15\). The three relative orders are independent, so
\[
\mathbb P(N_G^{\mathrm{seq}}\le6)=\mathbb P(\text{output}=I)
=\left(\frac4{15}\right)^3=\frac{64}{3375}>\frac1{55}.
\]

**Exact verification code.** This independently computes the sequential CDF by conditioning on the next uniformly chosen available vertex.

```python
from collections import Counter
from fractions import Fraction
from functools import lru_cache

n = 15
E = [(i, i+1) for i in range(6)] + [
    (0,7), (7,8), (3,9), (9,10), (6,11), (11,12), (0,13), (6,14)]
B = [1 << v for v in range(n)]          # closed neighborhoods
for u, v in E:
    B[u] |= 1 << v
    B[v] |= 1 << u
V = (1 << n) - 1

counts = Counter()
for I in range(V + 1):
    covered = 0
    for v in range(n):
        if I & (1 << v):
            if covered & (1 << v):       # adjacent to an earlier member of I
                break
            covered |= B[v]
    else:
        if covered == V:                # independent and dominating
            counts[I.bit_count()] += 1

@lru_cache(None)
def F(S, k):                            # P(at most k more vertices occupied)
    if S == 0:
        return Fraction(1)
    if k == 0:
        return Fraction(0)
    return sum(F(S & ~B[v], k-1) for v in range(n) if S & (1 << v)) / S.bit_count()

static = Fraction(sum(c for k, c in counts.items() if k <= 6), sum(counts.values()))
seq = F(V, 6)
print("MIS counts:", sorted(counts.items()))
print("CDFs at 6 (static, sequential):", static, seq)
print("sequential minus static:", seq - static)
```

Observed output:
```text
MIS counts: [(6, 1), (7, 50), (8, 4)]
CDFs at 6 (static, sequential): 1/55 64/3375
sequential minus static: 29/37125
```

CONFIDENCE: \(>99.99\%\). The subtlest step is deleting the two edges: it preserves the probability of the **specific output \(I\)**, not the full occupancy law. The exact recursion checks the inequality on the original graph without deleting either edge.