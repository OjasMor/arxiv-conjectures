# Referee report for 2611.26110__1

status: completed cost: $0.8806

REFEREE VERDICT: CORRECT

STATEMENT MATCH: yes. Conjecture `conj-nv-monotone` states: “\(\operatorname{NV}(\operatorname{Koz}(n;0,d))\) is weakly increasing in \(d\).” It specifies that this was verified for \(n\le 7\) and \(0\le d\le n-1\), and that “for \(d\ge n-1\) the value is constant” by Proposition `prop-product-regime`. The verification range is not a restriction on the conjecture. The claim proves it for every \(n\ge1\) and strengthens it to strict increase before the plateau for \(n\ge3\).

The relevant definitions are: “For an integer \(d\ge0\) the **shift** prepends \(d\) zeros”; \(\operatorname{Koz}(n;\mathbf d)=\sum_i\operatorname{shift}^{d_i}(\operatorname{Koz}(n))\), with \(\operatorname{Koz}(n)=\operatorname{conv}(S_n)\) for complexes “that use every vertex” (`eq:koz`); and “\(\operatorname{NV}=D!\,\operatorname{vol}\)” (`eq:NV`), where \(D\) is the dimension of the polytope being measured. The claim uses this normalisation, not Euclidean volume.

DEGENERATE OR ALREADY KNOWN IN PAPER: no, not as a general theorem. The plateau is already proved. The increase up to the plateau is an elementary consequence of the paper’s own rank-two volume formula, but the paper does not make the consecutive-shift comparison and still lists the conjecture under “Open problems.”

DETAILS: No step fails.

1. **Volume formula.** Proposition `prop-simplex-volume` gives \(B_n=\operatorname{NV}(\operatorname{Koz}(n))>0\). Dividing Corollary `cor-rank2-volume` by \(B_n\) gives precisely the claimed \(A_{d,j}\) and summation range, including the empty product at \(d=0\). The binomial legs satisfy the log-concavity hypothesis of the underlying staircase theorem.
2. **Pascal identity.** Set \(D=n-1+d\). After extending each old product to \(\prod_{k=j+1}^{j+d+1}c_k\), its two coefficients are \(\binom D{d+j-1}\) and \(\binom D{d+j}\). Their sum is \(\binom{D+1}{d+j}\), exactly the new coefficient. The last leg index \(j+d+1\) never exceeds \(n\).
3. **Summation and strictness.** With \(m=n-d\ge2\), the sum of the unweighted adjacent pairs equals the old sum **plus** \(\sum_{j=2}^{m-1}A_{d,j}\): both endpoints occur once and every interior term twice. All multipliers are at least one. For \(n\ge3\), the first pair multiplies \(A_{d,2}>0\) by \(c_2=\binom n2>1\). This proves strictness even on the last transition, when \(m=2\) and there are no interior terms.
4. **Plateau and small cases.** For \(d\ge n-1\), the two free coordinate blocks are disjoint, and `prop-product-regime` gives the same lattice product for every such \(d\). Its normalised volume is \(\binom{2n-2}{n-1}B_n^2\), agreeing with the corollary at \(d=n-1\). For \(n=2\) the volume is always \(2\); for \(n=1\) every polytope is a point of normalised volume \(1\).

**Independent Python checks.** I built the prefix vertices \(\tilde F_j\) of Definition `def-ra`, formed all pairwise shifted vertex sums, and dropped constant coordinates. I computed hull volumes by coning triangulated boundary facets to a vertex and summing absolute integer determinants. This does not use the rank-two volume formula. The outputs, for \(d=0,\ldots,n+1\), were:

```text
n=1: [1, 1, 1]
n=2: [2, 2, 2, 2]
n=3: [12, 36, 54, 54, 54]
n=4: [192, 1248, 6720, 11520, 11520, 11520]
n=5: [8000, 102500, 1287500, 9625000, 17500000, 17500000, 17500000]
```

These reproduce the normalised-volume rows of `tab:volumes`. Separately, exact integer checks for \(1\le n\le50\) passed all **20,825** termwise Pascal identities. Among the **1,225** consecutive-shift comparisons with \(0\le d\le n-2\), there were **1,224 increases, one tie** (\(n=2,d=0\)), **and no decreases**.

WHAT A HUMAN EXPERT SHOULD STILL CHECK: For a review independent of the paper’s proved results, audit the staircase tiling underlying `cor-rank2-volume`. Taking that corollary as proved, no unresolved step remains.