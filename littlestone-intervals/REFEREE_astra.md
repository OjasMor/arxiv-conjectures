# Referee report, gpt-6.2-astra (xhigh), fresh context

status: completed cost: $1.4193 incomplete: None

**VERDICT: PROOF CORRECT**

The proof establishes greedy optimality from **every segment position**, not just from a single interval rod. The decisive comparison is (5): synchronized rounding **minimizes** the sum of the two continuation values. Because those values are subtracted in the induction, this gives exactly the required upper bound on the benefit of deviating from greedy. I found no missing parity case or unproved optimality assumption.

## Numbered findings

### 1. The claimed statement is the same as the conjecture

In the supplied paper, **Conjecture 31** (`conj:rl`) reads:

> For every position \(J_S\), \(\mathrm{RL}(J_S)\) equals the value of the greedy schedule started from \(S\). In particular \(\mathrm{RL}(\mathrm{Int}_m)=R(m+1)\) for all \(m\ge0\).

The relevant definitions are:

- **Definition 11 (Segment classes):** “For a finite multiset \(S\) of positive integers, place disjoint blocks \(B_g\) of consecutive points, one of length \(g\) for each \(g\in S\). Let \(J_S\) consist of \(\emptyset\) together with every set of consecutive points contained in a single block. Up to relabelling, \(J_S\) depends only on \(S\), and \(\mathrm{Int}_m=J_{\{m\}}\).”
- **Measure convention:** “Give each block of length \(g\) the *measure* \(g+1\).” Also: “Pieces of measure \(1\) (empty blocks) cannot be cut.”
- **Randomised dimension:** \(\mathrm{RL}(H)\) is “defined as half the largest expected length of a random root-to-leaf branch (each step left or right with probability \(\tfrac12\)) of a tree shattered by \(H\).”
- **Interpolated logarithm:** “For real \(\ell\ge1\) write \(\tilde\lambda(\ell)=t+(\ell-2^t)/2^t\) with \(t=\lfloor\lg\ell\rfloor\), the piecewise-linear interpolation of \(\lg\) between consecutive powers of two.”
- **Greedy rule:** “A simple rule does reach the optimum in all computed cases: cut a largest piece \(\ell\), with \(t=\lambda(\ell)\), into
  \[
  u=\max(2^{t-1},\,\ell-2^t),\qquad v=\ell-u.
  \]”
  Here \(\lambda(\ell)=\lfloor\lg\ell\rfloor\).
- **Definition of \(R\):** “Let \(R(1)=0\) and \(R(\ell)=1-2^{1-\ell}+\tfrac12\bigl(R(\lfloor\ell/2\rfloor)+R(\lceil\ell/2\rceil)\bigr)\) for \(\ell\ge2\).”

The proof correctly converts the paper’s multiset of **lengths** \(S\) to a vector of **measures** \(X\). Its zero entries are bookkeeping, not extra queries. At \(m=0\), the paper specifies \(\mathrm{Int}_0=\{\emptyset\}\); the empty position and the single inert measure \(1\) both give value zero. There is no domain-size shift or statement mismatch.

### 2. The exact cutting recursion is proved in the paper; greedy optimality is not assumed

Here is the dependency audit. Numbers in this finding refer to the **paper**, not the proposed proof.

| Input | What the paper actually supplies |
|---|---|
| Structure of a query | **Proved in Lemma 12** (`lem:branch`). Part (b) states “\((J_S)^0_x=J_{S'}\), where \(S'=S-\{g\}+\{i-1,\,g-i\}\), with zeros discarded.” The later randomised section accurately refers to the proof of part (a): “the positive branch of a query is the product of two chains of \(u\) and \(v\) functions with \(u+v=\ell\), and part (b) gives the negative branch.” It is this structural decomposition, **not** the deterministic dimension in part (a), that is used. |
| Generic randomised recursion, products, invariance | **Stated and proved in Lemma 27** (`lem:rlrec`). It gives \(\mathrm{RL}(V)=\max(0,\max_x\tfrac12(1+\mathrm{RL}(V_x^0)+\mathrm{RL}(V_x^1)))\) over splitting queries, and “\(\mathrm{RL}(H_1\otimes H_2)=\mathrm{RL}(H_1)+\mathrm{RL}(H_2)\).” Part (c) says “\(\mathrm{RL}\) is invariant under relabelling the domain and under deleting points on which the whole class agrees.” The recursion is credited to Observation 5.5 of Filmus et al., **and** derived locally from the tree definition. The optimal-expected-mistakes characterization used in the paper’s product proof is cited from Filmus et al., not reproved there. |
| Value of the positive branch | **Proved in Proposition 28** (`prop:rlthr`): “A chain of \(c\) threshold functions has \(\mathrm{RL}=\tfrac12\tilde\lambda(c)\).” Its proof uses the availability of every prefix/suffix split and the fact that a balanced split attains the concavity bound. Thus the positive-branch value is \((\tilde\lambda(u)+\tilde\lambda(v))/2\). |
| Exact discounted cutting recursion | **Explicitly stated and derived**, as equation **(2)** of the paper (`eq:rlcut`), not as a conjecture or just a lower bound. The introduction to the display says “With Lemma [27] and Proposition [28] this yields, exactly,” followed by \(\mathrm{RL}(J_S)=\max(0,\max_{\text{cuts }\ell=u+v}\tfrac12(1+\tfrac12\tilde\lambda(u)+\tfrac12\tilde\lambda(v)+\mathrm{RL}(J_{S'})))\). The next display gives the unrolled weights \(2^{-i}\). In particular the **first** reward is discounted by \(1/2\). |
| Greedy children, reward, and order | **Proved in Step 1 of Theorem 30** (`thm:rllower`): “If \(p\le3\cdot2^{t-1}\), then \(u=2^{t-1}\) and \(v\in[2^{t-1},2^t]\); otherwise \(v=2^t\) and \(u\in(2^{t-1},2^t)\).” Also: “Each cut piece is a largest current piece and its children are smaller, so the pieces are cut in non-increasing order of size.” The elementary scaling identity “\(\tilde\lambda(2y)=\tilde\lambda(y)+1\)” is stated with the definition and follows directly from it. |
| Single-rod value and closed form | **Proved**, but not as an optimality theorem. Theorem 30 states “For every \(m\ge0\), \(\mathrm{RL}(\mathrm{Int}_m)\ge R(m+1)\).” Its proof evaluates the greedy schedule. **Lemma 29** (`lem:Rclosed`) proves \(R(\ell)=\sum_{j=0}^{L}(1-2^{1-f_j}+\pi_j2^{-f_j})\). Neither result supplies the missing upper bound. |
| Supersolution criterion | **Stated in prose**, immediately after Conjecture 31: “from every position, one arbitrary cut followed by greedy play is never better than greedy play.” Its equivalence to optimality follows by finite induction from the exact recursion; the paper does **not** assert that the criterion has been proved. |

The proof’s general threshold count (2), all-vector formula (3), synchronized halving (4), mixed-rounding inequality (5), formal zero splits, and rounded-cut induction (7) are **not stated as such in the paper**. The closest count in Theorem 30 is “\(C_q=f_{q-1}-1\)” for thresholds \(2^q\). The paper also gives (6) for ordinary \(n\ge2\) in the proof of Proposition 32, but not the extension \(T(0)=-2\). These are legitimate new steps: the submission proves what it needs. It does not rely on the deterministic cutting lemma, on the \(0.64\) gap bound, or on a Lean verification of the randomised conjecture.

### 3. The greedy count (2), value formula (3), and halving recurrence (4) all check out

Write \(T=\tilde\lambda\), and let \(D=2^{\lfloor\lg p\rfloor}\) for a genuine greedy cut \(p\ge2\). Put \(p=D+h\), \(0\le h<D\). The rule gives

\[
(a,b)=
\begin{cases}
(D/2,D/2+h),&h\le D/2,\\
(h,D),&h>D/2.
\end{cases}
\]

Thus **both** children are in \([D/2,D]\), and **at least one** is a power of two. This includes both boundary cases \(h=0,D/2\), when both children are powers of two. By affinity on this interval and scaling,
\[
1+\tfrac12(T(a)+T(b))=1+T(p/2)=T(p).
\]
After removing a largest piece, neither its children nor any untouched piece is larger than it. The sequence of cut measures is therefore nonincreasing, irrespective of ties.

**Count (2).** Fix \(d=2^k\), \(1\le r\le d\), and count cut nodes of measure at least \(d+r\) in the greedy tree rooted at \(n\).

- If \(n<d+r\), no node qualifies, and \(\max(0,\lfloor(n-r)/d\rfloor)=0\).
- If \(d+r\le n<2d\), the largest power of two at most \(n\) is \(d\); its children are at most \(d\). Exactly the root qualifies, and the floor is \(1\).
- If \(n\ge2d\), both children are at least \(d\). A power-of-two child \(u\) is divisible by \(d\). The other child \(v\) satisfies \(v-r\ge0\), so there is no clipped negative term in applying induction. The root and its two subtrees contribute
  \[
  1+\left(\frac ud-1\right)+\left\lfloor\frac{v-r}{d}\right\rfloor
   =\left\lfloor\frac{u+v-r}{d}\right\rfloor.
  \]
  Here the \(-1\) holds for **every** \(1\le r\le d\), including \(r=d\).

This proves (2), including zero and unit entries.

**Value (3).** For \(d<k\le2d\), \(T(k)-T(k-1)=1/d\). These bands partition the integers \(k\ge2\), and \(T(1)=0\). Hence
\[
T(p)=\sum_d\frac1d\sum_{r=1}^d{\bf1}_{p\ge d+r}.
\]
For any one threshold, the number of qualifying cuts is \(s=\sum_{n\in X}C_{d,r}(n)\): interleaving different pieces does not change their descendant trees. Because the schedule is nonincreasing, these are precisely the **first** \(s\) cuts. Their weights sum to \(1-2^{-s}=H(s)\). Summing the increments gives exactly (3):
\[
F(X)=\sum_d\frac1d\sum_{r=1}^d H\!\left(\sum_{n\in X}C_{d,r}(n)\right).
\]

**Halving (4).** At \(d=r=1\), \(C_{1,1}(n)=(n-1)_+\), giving the toll \(H(M(X))\). For \(d=2e\), taking the floor first after division by two gives
\[
\left\lfloor\frac{n-2s}{2e}\right\rfloor
 =\left\lfloor\frac{\lfloor n/2\rfloor-s}{e}\right\rfloor,\qquad
\left\lfloor\frac{n-2s+1}{2e}\right\rfloor
 =\left\lfloor\frac{\lceil n/2\rceil-s}{e}\right\rfloor.
\]
Clipping at zero preserves both identities. For \(s=1,\ldots,e\), the even thresholds therefore use **all floors**, and the odd thresholds **all ceilings**. Their coefficient is \(1/(2e)\), half the coefficient at scale \(e\). This gives
\[
F(X)=H(M(X))+\tfrac12(F(X^-)+F(X^+)).
\]
It would not justify independently rounding every coordinate at random. The proposed proof does not make that mistake.

### 4. Inequality (5) has the correct direction in every parity case

For a fixed summand of (3), let \(A,B\) be the total counts after synchronous lower and upper rounding. Each coordinate’s count is nondecreasing, so \(A\le B\). A complementary pair of mixed roundings has counts \(A+i,B-i\) for some \(0\le i\le B-A\): it receives each coordinate’s two counts exactly once. The exact difference is
\[
H(A+i)+H(B-i)-H(A)-H(B)
=2^{-A}(1-2^{-i})(1-2^{-(B-A-i)})\ \ge0.
\]
All coefficients in (3) are positive. This proves (5) with the sign shown.

More explicitly, write \(a=2i+\alpha,\ b=2j+\beta\). The rounded child pairs in (7) are:

| \((\alpha,\beta)\) | Minus pair | Plus pair | Comparison with synchronous roundings of \(Y\) |
|---|---|---|---|
| \((0,0)\) | \((i,j)\) | \((i,j)\) | Equal |
| \((0,1)\) | \((i,j)\) | \((i,j+1)\) | Equal |
| \((1,0)\) | \((i,j)\) | \((i+1,j)\) | Equal |
| \((1,1)\) | \((i,j+1)\) | \((i+1,j)\) | Mixed sum **at least** synchronous sum |

The row sums are \(\lfloor p/2\rfloor,\lceil p/2\rceil\) in every row. In the last row both are \(i+j+1\). The inequality can be strict: for \(Y=(3,3)\), the synchronous values sum to \(F(1,1)+F(2,2)=3/4\), whereas the mixed values sum to \(F(1,2)+F(2,1)=1\). Thus the sign is substantive, not a consequence of the two sides always agreeing.

### 5. The zero-child convention, (6), (7), and the final induction are sound

For \(n\ge2\), the two integer halves of \(n\) lie on the same affine interval \([D/2,D]\) of \(T\), where \(D=2^{\lfloor\lg n\rfloor}\). Their mean is \(n/2\); scaling gives
\[
T(n)=1+\tfrac12(T(\lfloor n/2\rfloor)+T(\lceil n/2\rceil)).
\]
For \(n=1\) the right side is \(1+(-2+0)/2=0=T(1)\). This verifies (6). The extension is used only algebraically.

For a formal split \(p=0+p\), the position is unchanged, so (1) reduces to \(F(X)\ge T(p)/2\). If \(p\ge2\), the first greedy cut of a largest piece \(q\ge p\) already earns \(T(q)/2\ge T(p)/2\); all future rewards are nonnegative. If \(p=1\), the bound is zero. No real query with an empty child is being added to the dimension recursion.

For a genuine cut, \(M(Y)=M(X)-1\), since \((p-1)-(a-1)-(b-1)=1\). In either rounded parent vector the selected measure \(p\ge2\) falls to a measure between \(1\) and \(p-1\), and all other measures weakly decrease. Thus both rounded parents have strictly smaller \(M\). Each row of the parity table gives either a genuine cut covered by induction or a formal cut covered above. This proves (7), including \(p=2,\ a=b=1\), when both rounded cuts are formal.

Finally, \(2H(M)-H(M-1)=1\) for \(M\ge1\). Subtracting the two instances of (4) gives
\[
2F(X)-F(Y)
=1+\tfrac12\sum_\sigma(2F(X^\sigma)-F(Y^\sigma)).
\]
By (5), replacing the **subtracted** synchronous sum by the mixed sum can only lower the right side. By (7) the resulting average, excluding the leading \(1\), is at least
\[
1+\tfrac14\sum_\sigma(T(a_\sigma)+T(b_\sigma))
=1+\tfrac14\bigl(2T(a)-2+2T(b)-2\bigr)
=\tfrac12(T(a)+T(b)).
\]
Restoring the leading \(1\) gives precisely (1).

At \(M=0\) there are no genuine cuts and both values are zero. At \(M=1\) the only nontrivial piece is \(2\); \(F=1/2\) and (1) is \(1\ge1\). In general, induction in the **exact** cutting recursion now bounds every candidate first cut by \(F(X)\), hence \(\mathrm{RL}(J_S)\le F(X)\). Feasibility of the greedy schedule gives the reverse inequality. There is no circular use of optimality at the current position.

For a single rod, (4) has base \(F((1))=0\) and toll \(H(n-1)=1-2^{1-n}\), exactly the recurrence for \(R\). One can also recover the paper’s **displayed closed form** directly: at scale \(d=2^j\le n\), write \(n=qd+h\), \(0\le h<d\). The count in (2) is \(q\) for the first \(h\) values of \(r\), and \(q-1\) for the rest. The scale contributes
\[
(h/d)H(q)+(1-h/d)H(q-1)=1-2^{1-q}+(h/d)2^{-q}.
\]
These are exactly the summands of Lemma 29 with \(q=f_j,\ h/d=\pi_j\). This also works at \(n=1\).

### 6. No cited result supplies the conclusion trivially

Filmus et al.’s recursion specifies a **maximum over queries**; it does not identify the maximizing query for interval segment states. Even maximizing immediate reward does not settle the issue: as the paper notes, on rod \(6\), the equally balanced first cut \(3+3\) gives \(61/32\) under balanced play, less than the greedy \(63/32\) from \(2+4\), despite equal immediate rewards. The deterministic interval results do not resolve this discounted comparison either.

No cited result, as described in the supplied paper, proves the all-position optimality theorem. The new ingredient here is the all-vector value formula and the comparison it permits after rounding. I have not independently authenticated the arXiv record or established worldwide publication priority.

## Computations run and observed output

I ran three separate checks, all with **exact dyadic arithmetic**. [Download the source code and observed output logs](sandbox:/mnt/data/referee_checks.zip).

**A. Original shattered-tree definition — no cuts or threshold formulas in the optimizer.** I constructed the empty hypothesis and every interval \([a,b]\) as explicit function tables. At each surviving class \(V\), I tried every point with two nonempty restrictions and maximized the **raw expected branch length** \(1+(E(V_0)+E(V_1))/2\), with a leaf worth zero. I divided by two to obtain \(\mathrm{RL}\). Before any positive answer the cache key was the set of coordinates not yet excluded; after a positive answer it was the full bitset of surviving hypotheses. Fixing the suffix negative recovers each smaller prefix class.

- **Range:** every \(0\le m\le27\). **Closed-form mismatches: 0.**
- Largest run: 379 explicit hypotheses, 134,217,728 pre-positive states and 27,405 positive-history states.
- Observed values began \(0,\ 1/2,\ 1,\ 11/8,\ 27/16,\ 63/32,\ 139/64,\ 303/128\). At \(m=27\): \(559923199/134217728\).

**B. Exact cutting optimization — not restricted to greedy moves.** I enumerated all multisets of non-unit pieces of total measure at most \(86\), padding with inert units for indexing. For every distinct cuttable part I tried **every unordered split**, used the optimal successor value, and separately checked whether the greedy first move attained that maximum.

```text
total measure limit                 86
states, including terminal          34,262,962
candidate cuts evaluated           868,637,629
states where greedy was not best             0
single-rod closed-form mismatches            0
```

The single-rod range is **\(0\le m\le85\)**, not \(m\le86\). At rod \(86\) the observed value was \(224057372476108280151670783/2^{85}\).

**C. Direct tests of the proposed identities.** For these checks I simulated the actual greedy schedule using a priority queue and the two-child reward, independently of (3) and (4). Random seed: `261128727`.

| Check | Exhaustive | Random | Mismatches or violations |
|---|---:|---:|---:|
| (2), actual descendant counts | 524,799 checks: \(0\le n\le512\), every dyadic \(d\le512\), every \(1\le r\le d\) | 32,768 thresholds, sampled rods up to 8,192 | 0 |
| (3), sum versus simulated discounted value | 14,883 positions, total non-unit measure \(\le35\), including terminal | 5,000 vectors | 0 |
| (4), synchronous halving | Same 14,883 positions | 5,000 vectors | 0 |
| (1), actual one-cut deviation | All 150,487 distinct candidate cuts on those positions | 4,994 cuts | 0 |
| (5), general complementary roundings | 56,574 assignments, total non-unit measure \(\le30\) | 5,000 assignments | 0 |
| (7), rounded inequalities, including formal splits | 300,974 rounded cuts | 9,988 rounded cuts | 0 |

Random vectors included explicit \(0,1\) padding and up to 12 sampled entries in \(0,\ldots,128\); the largest observed \(M\) was 1,170. I also tested (6) for every \(1\le n\le65{,}535\), the child-range/power-of-two/reward claims for every \(2\le p\le65{,}535\), and all **4,096** unordered single-rod first cuts for \(2\le n\le128\). There were **zero failures**. The claimed count of **14,882 nonempty** multisets through measure 35 is also correct: the 14,883rd state is terminal.

**Confidence:** Very high in the mathematical verdict for the supplied text. The all-state conclusion follows from the induction; the computations independently check the dimension normalization, the measure convention, and the delicate rounding sign.