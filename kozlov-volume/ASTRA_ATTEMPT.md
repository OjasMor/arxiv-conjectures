# arXiv:2611.26110 [conj-nv-monotone]

status: completed cost: $0.7747 incomplete: None

TARGET: \(\NV(\Koz(n;0,d))\) is weakly increasing in \(d\). (Verified for \(n\le7\) and
\(0\le d\le n-1\); for \(d\ge n-1\) the value is constant, by Proposition \ref{prop-product-regime}.)
\label{conj-nv-monotone}

---

VERDICT: PROVED

STATEMENT: “\(\operatorname{NV}(\operatorname{Koz}(n;0,d))\) is weakly increasing in \(d\).” In fact, for \(n\ge 3\) it is strictly increasing up to \(d=n-1\), and constant thereafter.

DEGENERATE: no — the proof applies to every \(n\ge1\) and every integer shift \(d\ge0\).

CERTIFICATE: Not applicable.

ARGUMENT: Write \(V_d=\operatorname{NV}(\operatorname{Koz}(n;0,d))\), \(c_k=\binom nk\), and \(B_n=\prod_{k=2}^n c_k\). The paper’s rank-two volume corollary gives, for \(0\le d\le n-1\),
\[
\frac{V_d}{B_n}=\sum_{j=1}^{n-d} A_{d,j},
\qquad
A_{d,j}=\binom{n-1+d}{d+j-1}\prod_{k=j+1}^{j+d}c_k .
\]
As a check on the normalization and indices, exact Python evaluation reproduced the paper’s rows \((12,36,54)\) for \(n=3\) and \((192,1248,6720,11520)\) for \(n=4\). I also checked every consecutive shift through \(d=n-1\) for \(8\le n\le50\), with no decrease.

The key is that **each term at shift \(d+1\) dominates the sum of its two neighbors at shift \(d\)**. Indeed, for \(0\le d\le n-2\) and \(1\le j\le n-d-1\), Pascal’s identity gives exactly
\[
A_{d+1,j}
=c_{j+d+1}A_{d,j}+c_{j+1}A_{d,j+1}.
\]
The two factors on the right extend the respective old products to the same new product \(\prod_{k=j+1}^{j+d+1}c_k\); the two old binomial coefficients then add to \(\binom{n+d}{d+j}\).

Since every \(c_k\ge1\), summing gives
\[
\frac{V_{d+1}}{B_n}
\ge \sum_{j=1}^{n-d-1}(A_{d,j}+A_{d,j+1})
\ge \sum_{j=1}^{n-d} A_{d,j}
=\frac{V_d}{B_n}.
\]
The second inequality holds because every old term occurs at least once. For \(n\ge3\), the first inequality is strict: already at \(j=1\), the positive term \(A_{d,2}\) has multiplier \(c_2=\binom n2>1\).

Finally, for \(d\ge n-1\) the paper’s product-regime proposition identifies every polytope unimodularly with \(\operatorname{Koz}(n)^2\), so \(V_d\) is constant. This also covers \(n=1\), when every polytope is a point.

CONFIDENCE: \(>99.99\%\). The only substantive input is the paper’s proved rank-two volume formula; the consecutive-shift comparison is an exact identity.