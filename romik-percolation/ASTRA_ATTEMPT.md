# arXiv:2611.26570 [conj:cylinder-boundary]

status: completed cost: $0.6251 incomplete: None

TARGET: \label{conj:cylinder-boundary} 
For every $k\geq 2$, the rational function $R_k$ from \cref{thm:cylinder-rationality} satisfies 
\begin{equation}     
    R_k(k)=R_{k-1}(k). 
\end{equation}

---

VERDICT: PROVED

STATEMENT: “For every \(k\geq 2\), the rational function \(R_k\) from \(\cref{thm:cylinder-rationality}\) satisfies \(R_k(k)=R_{k-1}(k)\).”

DEGENERATE: no — the proof covers every integer \(k\geq 2\).

CERTIFICATE: Not applicable.

ARGUMENT: At \(N=k\), the last white row of the rationally continued Pfaffian matrix has a single nonzero entry: a \(1\) in the last black column. Expanding along that row gives the conjecture.

As a check on the indexing and signs, I evaluated the paper’s entry formulas and Pfaffian in Python with exact fractions. The first three half-plane values were \(3/8,\ 59/1024,\ 7737/2097152\), agreeing with the paper. At the boundary, the two Pfaffians agreed for every \(2\leq k\leq12\); in particular, at \(k=9\) both were \(1/911835460\).

**Proof.** Fix \(k\geq2\). Write \(M_k(N)\) for the \(2k\times2k\) matrix in the paper’s Pfaffian formula, using the rational expressions for its entries and retaining the paper’s order: white then black for each \(r=0,\ldots,k-1\). Since \(\operatorname{Pf}M_k(N)=R_k(N)\) at every integer \(N>k\), this is an identity of rational functions.

Every index \(c,c_1,c_2\) in the entry formulas is at most \(2k\). The product formula for \((-1)^Np(N-1,N-c,0)\) contains the factor
\[
D_c(N):=\prod_{a=1}^{c-1}\frac{N^2-a^2}{4N^2-a^2}.
\]
Likewise, for \(c_1\ne c_2\), the paper’s rational formula for \(H_N(c_1,c_2)\) contains the factor \(D_{\max(c_1,c_2)}(N)\), using antisymmetry if necessary. All \(N\)-dependent denominators in these formulas are nonzero at \(N=k\): their factors are \(4N^2-a^2\) with \(a\leq2k-1\). Thus the entries are regular there. Moreover, \(D_c(k)=0\) for \(k<c\leq2k\), because the numerator includes the factor indexed by \(a=k\). Consequently, at \(N=k\) the rational \(p\)-term vanishes if \(c>k\), and the rational \(H\)-term vanishes if either index exceeds \(k\) (the diagonal is identically zero).

Now take the white row \(r=k-1\). In both \(f_N^{1,1}(r,s)\) and \(f_N^{1,0}(r,s)\), the first index in **every** \(H\)-term ranges over
\[
r+2\leq c_1\leq2r+2,\qquad\text{that is,}\qquad k+1\leq c_1\leq2k.
\]
The single \(p\)-sum in \(f_N^{1,0}(r,s)\) has exactly the same range. Hence all these sums vanish at \(N=k\). The only surviving term is the explicit \(+\mathbbm{1}_{r=s}\) in \(f_N^{1,0}\). This proves the asserted single-entry property without interpreting the continued row as an actual vertex of the boundary graph.

The last white and black indices are \(2k-1,2k\), so their pairing has positive sign in the Pfaffian expansion. Deleting them leaves exactly \(M_{k-1}(k)\), since the entry for each retained pair \(r,s\) depends only on \(N,r,s\), not on the matrix size. Therefore
\[
R_k(k)=\operatorname{Pf}M_k(k)
=1\cdot\operatorname{Pf}M_{k-1}(k)
=R_{k-1}(k).
\]

CONFIDENCE: \(>99.99\%\). The key dependency is the paper’s rational entry formula for \(H_N\); its explicit product factor and denominator range are sufficient at the specialization, with no limiting cancellation assumed.