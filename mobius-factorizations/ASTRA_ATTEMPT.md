# arXiv:2611.18194 [conjecture#1]

status: completed cost: $0.2103 incomplete: None

TARGET: The Möbius function between the prime factorization of $n$ and $n$ is either $0$ or has the sign $(-1)^{\Omega(n)+1}$, and it vanishes for $n=p^k$ with $k\ge3$.

---

VERDICT: DISPROVED

STATEMENT: “The Möbius function between the prime factorization of \(n\) and \(n\) is either \(0\) or has the sign \((-1)^{\Omega(n)+1}\), and it vanishes for \(n=p^k\) with \(k\ge3\).”

DEGENERATE: no — \(n=2^7 3^6=93312\) has two distinct prime divisors and \(\Omega(n)=13\), beyond the paper’s stated checked range.

CERTIFICATE:
```json
{
  "n": 93312,
  "bottom": [2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3],
  "top": [93312],
  "interval_size": 1752,
  "mobius": -57
}
```

ARGUMENT: For \(n=2^7 3^6\), the conjectured sign is \((-1)^{13+1}=+1\), but the Möbius value is \(-57\).

The following verifier represents an unordered factorization by its sorted tuple of factors. `refinements(f)` computes the entire lower interval of `f`: each binary split is a refinement, and any refinement can be reached by binary splits, by splitting off one desired subfactor at a time. Set union counts each resulting factorization once, regardless of how it was reached. Thus `mob(f)` applies exactly the recurrence \(\mu(\hat0,f)=-\sum_{g<f}\mu(\hat0,g)\), with value \(1\) at the prime factorization.

```python
from functools import cache
from math import isqrt

@cache
def refinements(f):
    result = {f}
    for i, a in enumerate(f):
        for b in range(2, isqrt(a) + 1):
            if a % b == 0:
                g = tuple(sorted(f[:i] + f[i+1:] + (b, a//b)))
                result.update(refinements(g))
    return result

@cache
def mob(f):
    lo = refinements(f)
    if len(lo) == 1:
        return 1
    return -sum(mob(g) for g in lo if g != f)

for n in (16, 36, 72, 2**4 * 3**4, 2**7 * 3**6):
    print(n, len(refinements((n,))), mob((n,)))
```

Observed output (columns: \(n\), interval size, Möbius value):
```text
16 5 0
36 9 -1
72 16 2
1296 109 -8
93312 1752 -57
```
The first four rows reproduce the paper’s values for exponent patterns \((4)\), \((2,2)\), \((3,2)\), and \((4,4)\).

The **prime-power clause is true**. For \(n=p^k\), \(k\ge3\), the bottom has a unique atom \(a\), obtained by merging two copies of \(p\). Every nonbottom factorization lies above \(a\): it contains a factor \(p^j\) with \(j\ge2\), so it can be formed by grouping the factors of \(a\). Now \(\mu(\hat0,a)=-1\), and induction in the Möbius recurrence gives \(\mu(\hat0,z)=0\) for every \(z>a\): the only nonzero terms below \(z\) are \(1\) at \(\hat0\) and \(-1\) at \(a\). Since the top is strictly above \(a\) for \(k\ge3\), its value vanishes.

CONFIDENCE: \(>99.99\%\). The only computational step is the finite interval enumeration; I also obtained \(-57\) independently by enumerating upward from the prime factorization using pairwise merges.