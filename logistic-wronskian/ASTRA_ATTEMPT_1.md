# arXiv:2611.32270 [conj:wronskian]

status: completed cost: $0.6373 incomplete: None

TARGET: [Pure-monomial identity for general \(K\)]
\label{conj:wronskian}
    The identity of \cref{thm:wronskian} holds for every \(K \ge 2\).

---

VERDICT: PROVED

STATEMENT: “The identity of \(\cref{thm:wronskian}\) holds for every \(K \ge 2\).” This includes the sign and the full coefficient \(c_K(s)\) displayed in the appendix.

DEGENERATE: no — the proof applies to every ordered scale vector \(0<s_1<\cdots<s_K\).

CERTIFICATE: Not applicable (proof).

ARGUMENT: The key is that \(z\phi(sz)=\partial_s\Phi(sz)\). Thus the desired determinant can be obtained by coalescing pairs of scales in an ordinary Vandermonde determinant.

I use “reduced cofactor” in the polynomial normalization of the appendix: take the determinant of the surviving matrix in the stated row and column order, removing a common factor \(\phi(s_i z)\) from each column belonging to scale \(s_i\). The unreduced minor therefore equals \(Q(z;s)\,\phi(s_Kz)\prod_{i<K}\phi(s_i z)^2\).

**Exact checks.** In Python I formed the reduced columns starting with \(p=s_i\) for a \(\Phi\)-column and \(p=1-s_i^2z^2\) for a \(z\phi\)-column. Each successive row replaces \(p\) by \(p'-s_i^2zp\). At \(s_i=i,\ z=1\), the exact determinants were \(36\) and \(-12\,441\,600\) for \(K=2,3\); for \(K=8,12\) they matched the formula and had the reported \(140\) and \(412\) digits in absolute value. At \(z=2\) the determinant-to-formula ratio was exactly \(1\) for both \(s=(1,2,4,5,7,11)\) and the \(K=13\) vector \(s=(1,3,\ldots,25)\).

**Proof.** Write \(n=2K-1\). First take \(n\) distinct positive scales \(u_1,\ldots,u_n\) and form the unreduced determinant
\[
D(u;z)=\det_{\substack{0\le r<n\\1\le j\le n}}
             \bigl[\partial_z^{r+1}\Phi(u_jz)\bigr].
\]
With \(t=z^2/2\), the first derivative is \(u_j\phi(u_jz)=u_j(2\pi)^{-1/2}e^{-u_j^2t}\). By the chain rule, converting rows of \(t\)-derivatives of orders \(0,\ldots,n-1\) to rows of \(z\)-derivatives is a lower triangular transformation with diagonal \(1,z,\ldots,z^{n-1}\): the coefficient of the highest derivative in row \(r\) is \((dt/dz)^r=z^r\). Factoring \(u_j\phi(u_jz)\) from the \(j\)-th column of the \(t\)-derivative matrix leaves the column \(\bigl((-u_j^2)^r\bigr)_{r=0}^{n-1}\). The ordinary Vandermonde formula gives
\[
D(u;z)=z^{\binom n2}\prod_{j=1}^n u_j\phi(u_jz)
                 \prod_{p<q}(u_p^2-u_q^2). \tag{1}
\]

Now take the scales in interleaved order
\[
u=(s_1,s_1+h,\ldots,s_{K-1},s_{K-1}+h,s_K)
\]
for sufficiently small \(h>0\). In each pair subtract the first column from the second and divide the latter by \(h\). The resulting determinant is \(D(u;z)/h^{K-1}\). As \(h\to0\), the second column of each pair becomes precisely the column of \(z\)-derivatives of \(z\phi(s_i z)\), since the scale and \(z\)-derivatives commute.

Set \(m_i=2\) for \(i<K\) and \(m_K=1\). In (1), the within-pair factors give
\[
\frac{s_i^2-(s_i+h)^2}{h}\longrightarrow -2s_i,
\]
while the factors between blocks \(i<j\) give \((s_i^2-s_j^2)^{m_i m_j}\). The column prefactors tend to \(\prod_i(s_i\phi(s_i z))^{m_i}\). Finally, moving the interleaved \(z\phi\)-columns to the paper’s trailing block crosses \(\sum_{i<K}(K-i)=\binom K2\) columns. Including the \(K-1\) negative within-pair factors, the sign is
\[
(-1)^{\binom K2+K-1}
 =(-1)^{\binom{K-1}{2}}
 =(-1)^{\lfloor(K-1)/2\rfloor}.
\]
Removing the Gaussian factors and using \(\binom n2=(2K-1)(K-1)\) now yields
\[
\boxed{\displaystyle
Q(z;s)=(-1)^{\lfloor(K-1)/2\rfloor}\,2^{K-1}s_K
 \prod_{i<K}s_i^3
 \prod_{1\le i<j<K}(s_i^2-s_j^2)^4
 \prod_{i<K}(s_i^2-s_K^2)^2\,
 z^{(2K-1)(K-1)}.}
\]
This is the asserted identity. Its coefficient is nonzero for all allowed scales, so the reduced minor does not vanish on \(z>0\).

CONFIDENCE: \(>99.99\%\). The only interpretive point is the distinction between the raw minor and the reduced polynomial; the proof gives both, with the column order and sign fixed explicitly.