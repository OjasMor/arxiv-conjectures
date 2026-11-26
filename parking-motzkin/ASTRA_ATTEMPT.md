# arXiv:2611.29890 [question#2]

status: completed cost: $0.8806 incomplete: None

TARGET: For fixed $k\in\mathbb{N}$, can $|\Out_{B}^{-1}(12\cdots(k-1)(k)(n)(n-1)\cdots(k+2)(k+1))|$ for $n>k$ be expressed as a sum involving Motzkin numbers whose indices depend on $n$?

---

VERDICT: PROVED

STATEMENT: “For fixed \(k\in\mathbb{N}\), can \(|\Out_{B}^{-1}(12\cdots(k-1)(k)(n)(n-1)\cdots(k+2)(k+1))|\) for \(n>k\) be expressed as a sum involving Motzkin numbers whose indices depend on \(n\)?”

DEGENERATE: no — the formula holds for every \(k\ge1\) and \(n>k\), including a decreasing suffix of length one.

CERTIFICATE: Not applicable (proof).

ARGUMENT:

**Yes.** Write \(A_k(m)\) for the requested count with a decreasing suffix of length \(m\), so \(n=k+m\). Let \(C_j=\frac1{j+1}\binom{2j}{j}\) be the Catalan numbers. Define integer polynomials, independently of \(n\), by
\[
P_0(z)=1,\qquad
P_{k+1}(z)=z^2P_k(z)-z\sum_{j=0}^k C_jP_{k-j}(z).
\]
Then the answer is the finite linear combination
\[
\boxed{\displaystyle
A_k(n-k)=\sum_{h=0}^{2k}[z^h]P_k(z)\,M_{n-k+h}.}
\]
For example, the first case beyond the paper’s formulas is
\[
A_3(n-3)=M_{n+3}-3M_{n+2}+3M_{n+1}-3M_n+2M_{n-1}-2M_{n-2}.
\]

**1. Inserting a car that finishes in the first spot.** For a preference list \(\beta=(b_1,\dots,b_\ell)\), let \(s(\beta)\) be the length of its longest initial segment of distinct preferences. Suppose its outcome is \(\rho\). To obtain an outcome consisting of car \(1\) followed by \(\rho\) with all labels increased by one, shift every \(b_i\) up by one and prepend a preference \(p\). The choices corresponding to \(\beta\) are exactly
\[
p=1,\qquad\text{or}\qquad p=1+b_j\quad(1\le j\le s(\beta)).
\]

Indeed, if \(p=1\), car \(1\) stays there and the remaining process is a shifted copy of \(\beta\). If \(p=1+b_j\), the first \(j-1\) later cars park without a collision, and the next car bumps car \(1\) into the still-vacant spot \(1\). At that point the other cars are parked exactly as in the shifted process for \(\beta\).

Conversely, in any list producing this outcome, no later car can prefer spot \(1\): the last car to prefer that spot would stay there. If car \(1\) does not start there, spot \(1\) must remain empty until car \(1\) is bumped into it. Thus the **first bump** must displace car \(1\), since otherwise a different car would fill spot \(1\). This forces precisely one of the stated choices \(1+b_j\), with \(b_1,\ldots,b_j\) distinct. Deleting the first preference and shifting the others down uniquely recovers \(\beta\).

The resulting initial distinct-run lengths are \(s(\beta)+1\) for \(p=1\), and \(j\) for \(p=1+b_j\). Thus a list with statistic \(s\) has exactly one extension of each statistic \(1,\ldots,s+1\).

Let \(E_k(s)\) count its extensions after \(k\) such insertions. Then
\[
E_0(s)=1,\qquad E_{k+1}(s)=\sum_{j=1}^{s+1}E_k(j).
\]
Writing \(C(u)=\sum_{j\ge0}C_ju^j\), we have
\[
\sum_{k\ge0}E_k(s)u^k=C(u)^{s+1}.
\]
Indeed, \(C=1+uC^2\) gives \(C^{s+1}=1+u\sum_{j=1}^{s+1}C^{j+1}\) by telescoping, which is exactly the recurrence and initial condition. Multiplying by \(C(u)\) now gives
\[
E_k(s+1)=\sum_{j=0}^k C_jE_{k-j}(s). \tag{1}
\]

**2. Splitting lists with decreasing outcome.** Let \(D_h\) be the set of lists with decreasing outcome of length \(h\), taking \(D_0\) to consist of the empty list with statistic zero. For \(h\ge2\), car \(1\) finishes in spot \(h\). There are two possibilities.

* **Car \(1\) prefers \(h\).** It is never bumped: once it left \(h\), it could not return, because that spot would remain occupied. Deleting car \(1\) and spot \(h\) therefore leaves an arbitrary list in \(D_{h-1}\). Conversely, prepending \(h\) to such a list works and increases its statistic by one.
* **Car \(1\) does not prefer \(h\).** It must be bumped into \(h\) on the last arrival, since \(h\) can be the first vacant spot only when all other spots are occupied. The last car prefers spot \(1\), so immediately beforehand the first \(h-1\) spots have outcome \(1,(h-1),(h-2),\ldots,2\), and spot \(h\) is empty. The earlier list is therefore exactly a one-step extension from \(D_{h-2}\) as in step 1. Conversely, appending preference \(1\) to any such extension produces the decreasing outcome. Appending this preference does not change the statistic: if the preceding \(h-1\) preferences were all distinct, they already included \(1\), and otherwise the first repetition already occurred.

This split also gives a short verification of the base count \(|D_h|=M_h\). Refine Motzkin paths by their number of components, meaning the segments between consecutive visits to height zero. Appending a horizontal step to a path of length \(h-1\) increases its component count by one, matching the first case. Every path of length \(h\) ending in a down-step is obtained uniquely from a path of length \(h-2\) with \(s\) components: choose \(1\le j\le s+1\), keep its first \(j-1\) components, and enclose the remaining suffix in an up-step and a down-step. The result has \(j\) components, matching exactly the choices in the second case. The length-zero and length-one counts and statistics agree, so induction proves the refined equality and hence the base count.

**3. The recurrence for the requested family.** Repeated first-spot insertion gives
\[
A_k(m)=\sum_{\beta\in D_m}E_k(s(\beta)).
\]
Apply the split in step 2 to \(D_{m+2}\) and weight each list by \(E_k\) of its statistic. The first case contributes
\(\sum_{j=0}^k C_j A_{k-j}(m+1)\) by (1). The second case contributes \(A_{k+1}(m)\): it performs one extension from \(D_m\), appends a preference without changing the statistic, and then counts \(k\) further extensions. Consequently,
\[
A_{k+1}(m)=A_k(m+2)-\sum_{j=0}^k C_j A_{k-j}(m+1).
\]
Since \(A_0(m)=M_m\), interpreting \(z\) as the forward shift in \(m\) gives exactly the polynomial recurrence stated above. Its degree is at most \(2k\) for \(P_k\), proving the boxed formula.

**Computational checks.** Direct simulation reproduced the paper’s example \((1,4,4,3,2,2)\mapsto164325\). Exhausting all \(6^6\) preference lists gave the counts
\[
(51,76,99,118,132,132)\qquad(k=0,1,\ldots,5),
\]
so the first three entries agree with the paper’s Motzkin formulas and the fourth with the new \(k=3\) formula. An independent reverse-parking enumeration also agreed for every \(0\le k<n\le12\), including \(A_3(9)=55862\) at \(n=12\).

CONFIDENCE: 99.9%. The most delicate step is exhaustiveness of the first-spot insertion rule; it rests on the fact that the first bump into a vacant spot \(1\) must put car \(1\) there, since an occupied spot never becomes vacant again.