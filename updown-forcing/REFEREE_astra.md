# Referee report for 2611.20344__1

status: completed cost: $0.6811

REFEREE VERDICT: CORRECT

STATEMENT MATCH: yes — Question 7.7 (`q:forcing`), under “Families,” asks: “Does every force-divergent set, that is, every \(A\) such that \(T_S\) is unbounded for all \(S\supseteq A\), contain a tail of a chain?” The counterexample answers **no** in exactly that direction.

The definitions that matter are:

- Definition 1.1 takes \(\mathbb N=\{1,2,3,\dots\}\), with “\(U(x)=\lceil 3x/2\rceil\) and \(D(x)=\lceil x/2\rceil\),” and sets \(T_S(x)=U(x)\) for \(x\in S\), \(D(x)\) for \(x\notin S\).
- Section 1.1: “We call \(T_S\) bounded if all its orbits are eventually periodic, and unbounded otherwise.” Section 2.3 requires unboundedness “for every \(S\supseteq A\), whatever happens outside \(A\).”
- Section 3.2: “For any \(x\), the set \(\{x,U(x),U^2(x),\dots\}\) is the part of the chain of \(x\) from \(x\) on; we call it a tail of the chain.”

There is no periodicity, density, or parity restriction on \(A\).

DEGENERATE OR ALREADY KNOWN IN PAPER: no — both \(A\) and its complement are infinite. The paper already uses the fact that two forced ups after every down imply divergence, for \(\mathbb N\setminus(8\mathbb N-1)\) in §6.5. It does **not** establish that this periodic set misses every chain tail. Conversely, the Runs proposition (`prop:runs`(c)) constructs a divergent orbit for one map without a chain tail, not for every superset. The certificate supplies the missing combination.

DETAILS:

1. **Every tail is hit.** For each positive integer \(x\), the omission \(w_x=U^{2x+2}(x)\) belongs to the tail starting at \(x\). This checks every possible starting vertex, not just the root of each chain. Thus no tail is contained in \(A\).
2. **A down step forces two ups.** Direct iteration gives \(w_1=8\). Monotonicity of \(U\) and \(U(y)\ge 3y/2\) give \(w_{n+1}\ge U^2(w_n)\ge 9w_n/4>2w_n\). With \(w_0=0\) and \(z=w_n\),
   \[
   w_{n-1}<z/2\le D(z)<U(D(z))\le (3z+5)/4<z.
   \]
   The upper bound uses the integer ceiling errors \(D(z)\le(z+1)/2\) and \(U(y)\le(3y+1)/2\); the final strict inequality holds for \(z>5\), including the first omission. Consequently the **sources** of the next two steps, \(D(z)\) and \(U(D(z))\), are in \(A\). They remain forced up for every \(S\supseteq A\).
3. **Every orbit tends to infinity.** No three-step window can contain two downs. Multiplying the lower bounds for its three steps gives \(T_S^3(x)\ge 9x/8\), regardless of the position of the down. Applying this to each of the three subsequences gives \(T_S^{3k+r}(x)\ge(9/8)^k T_S^r(x)\) for \(r=0,1,2\). Thus every orbit diverges, which is stronger than required. No proof step fails.

**Independent Python check.** I tested omission membership backward, independently of the forward list used to construct the \(w_n\). A vertex \(v\equiv1\pmod3\) has no \(U\)-parent; otherwise its unique parent is \(\lfloor2v/3\rfloor\), since \(U(2k)=3k\) and \(U(2k-1)=3k-1\). Reaching \(n\) after exactly \(2n+2\) backward steps certifies that the original vertex is \(w_n\). This lets the path test recognize omissions without a truncation cutoff.

```python
from itertools import islice, takewhile
from fractions import Fraction

def D(v):
    q, r = divmod(v, 2)
    return q + r

def U(v): return v + D(v)

def chain(v):
    while True:
        yield v
        v = U(v)

def hole(v):
    j = 0
    while v % 3 != 1:
        v = 2*v // 3
        j += 1
        if j == 2*v + 2: return True
    return False

C = list(takewhile(lambda v: v <= 10**60, chain(1)))
W = [next(islice(chain(n), 2*n+2, None)) for n in range(1, 129)]
print(C[:8], len(C), sum(v % 2 == 0 for v in C))
for a, b in zip([0]+W, W):
    assert hole(b) and 2*a < b and a < D(b) < U(D(b)) < b
    assert 4*U(D(b)) <= 3*b+5
    assert not hole(D(b)) and not hole(U(D(b)))
    if a: assert b >= U(U(a)) and 4*U(U(a)) >= 9*a
print(W[:8], len(W))

def paths(v, k, d=0):
    if k == 0:
        yield v, d
    else:
        yield from paths(U(v), k-1, d)
        if hole(v): yield from paths(D(v), k-1, d+1)

counts = [0]*4
best = Fraction(4)
for x in range(1, 50_001):
    for y, d in paths(x, 3):
        counts[d] += 1
        if Fraction(y, x) < best:
            best, witness = Fraction(y, x), (x, y)
print(counts, best, witness)
```

Output:
```text
[1, 2, 3, 5, 8, 12, 18, 27] 340 173
[8, 27, 93, 243, 710, 1850, 5165, 12137] 128
[50000, 28, 0, 0] 9/8 (8, 9)
```

The first line reproduces the paper’s 340 chain elements through \(10^{60}\), of which 173 are even. Among all allowed three-step paths from starts through 50,000, none had two or three downs. The lower bound is attained: \(8\to4\to6\to9\).

WHAT A HUMAN EXPERT SHOULD STILL CHECK: Only priority outside the supplied paper, if novelty is at issue. No further computation is needed for correctness.