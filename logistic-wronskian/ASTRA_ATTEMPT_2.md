# arXiv:2611.32270 [conj:S-wronskian]

status: completed cost: $0.6198 incomplete: None

TARGET: [Pure-monomial identity for general \(K\)]
\label{conj:S-wronskian}
    The factorisation of \cref{thm:S-wronskian} holds, with the same closed form
    for \(c_K(s)\), for every \(K \ge 2\).

---

VERDICT: PROVED

STATEMENT: “The factorisation of \(\verb|\cref{thm:S-wronskian}|\) holds, with the same closed form for \(c_K(s)\), for every \(K \ge 2\).”

DEGENERATE: no — the proof applies to every \(K\ge 2\) and every \(0<s_1<\cdots<s_K<\infty\).

CERTIFICATE: Not applicable (proof).

ARGUMENT: The key is that \(z\phi(sz)=\partial_s\Phi(sz)\). Thus the second block of columns can be obtained by letting pairs of scales coalesce in an ordinary Vandermonde determinant.

**Convention and checks.** I read the paper’s *reduced cofactor* as the determinant of the surviving matrix in its specified row and column order, with the common Gaussian factor \(\phi(s_i z)\) removed from each column of scale \(s_i\). Thus the unreduced minor is \(Q(z;s)\,\phi(s_Kz)\prod_{i<K}\phi(s_i z)^2\). As a check, I evaluated the reduced derivative matrix directly in Python using exact integers. At \(z=1,\ s_i=i\), I obtained \(36\) and \(-12{,}441{,}600\) for \(K=2,3\); at \(K=8,12\) the absolute determinants had respectively \(140\) and \(412\) digits, reproducing the paper’s counts. Beyond its checked range, at \(K=13,\ s_i=i^2+1,\ z=2\), the determinant and the conjectured formula agreed as \(1195\)-digit integers.

**Proof.** Put \(n=2K-1\), \(D=\binom n2=(2K-1)(K-1)\), and define the unreduced column
\[
U(a)=\bigl(\partial_z^r\Phi(az)\bigr)_{r=1}^{n}.
\]
First take \(n\) distinct positive scales \(a_1,\ldots,a_n\). I claim that
\[
\det[U(a_1),\ldots,U(a_n)]
=(-z)^D\prod_{j=1}^n a_j\phi(a_jz)
          \prod_{p<q}(a_q^2-a_p^2). \tag{1}
\]
Indeed, the first derivative is \(a\phi(az)\). Write \(x=-z^2/2\), so \(\phi(az)=(2\pi)^{-1/2}e^{a^2x}\). By the chain rule, for any smooth \(F\),
\[
\partial_z^h F(x(z))=\sum_{\ell=0}^h L_{h\ell}(z)F^{(\ell)}(x(z)),
\qquad L_{hh}(z)=(-z)^h.
\]
The coefficients are independent of \(F\): each differentiation multiplies the new highest-derivative coefficient by \(x'(z)=-z\). Consequently, after extracting \(a_j\phi(a_jz)\) from column \(j\), the matrix on the left of (1) is the product of the lower triangular matrix \(L\), indexed by \(0\le h,\ell<n\), and the Vandermonde matrix \(\bigl((a_j^2)^\ell\bigr)_{\ell,j}\). Their determinants give (1).

Now take the scales in the interleaved order
\[
s_1,\ s_1+\varepsilon,\ s_2,\ s_2+\varepsilon,\ \ldots,\
s_{K-1},\ s_{K-1}+\varepsilon,\ s_K
\]
for sufficiently small \(\varepsilon>0\). Subtract the first column of each pair from the second, divide each such second column by \(\varepsilon\), and let \(\varepsilon\downarrow0\). The second column of pair \(i\) becomes
\[
U'(s_i)=\bigl(\partial_z^r[z\phi(s_i z)]\bigr)_{r=1}^n,
\]
by commutation of the scale and argument derivatives. This produces exactly the desired unreduced columns, still interleaved.

On the right of (1), the within-pair Vandermonde factor divided by \(\varepsilon\) tends to \(2s_i\). Between distinct scales \(s_i,s_j\), there are \(m_i m_j\) factors tending to \(s_j^2-s_i^2\), where \(m_i=2\) for \(i<K\) and \(m_K=1\). After removing the Gaussian column factors, the interleaved determinant is therefore
\[
(-z)^D
\left(\prod_{i=1}^{K}s_i^{m_i}\right)
\left(\prod_{i<K}2s_i\right)
\prod_{i<j}(s_j^2-s_i^2)^{m_i m_j}. \tag{2}
\]

Finally, moving \(U'(s_i)\) past the \(K-i\) later undifferentiated columns puts the columns in the paper’s order. This contributes \((-1)^{\binom K2}\). Together with the sign in \((-z)^D\), the sign is
\[
(-1)^{D+\binom K2}=(-1)^{\binom{K-1}{2}}
                  =(-1)^{\lfloor(K-1)/2\rfloor}.
\]
Since all difference exponents in (2) are even, their orientation is immaterial. Hence
\[
\boxed{\displaystyle
Q(z;s)=z^{(2K-1)(K-1)}
(-1)^{\lfloor(K-1)/2\rfloor}\,2^{K-1}s_K
\prod_{i=1}^{K-1}s_i^3
\prod_{1\le i<j\le K-1}(s_i^2-s_j^2)^4
\prod_{i=1}^{K-1}(s_i^2-s_K^2)^2 .}
\]
This is the stated coefficient, and it is nonzero throughout the ordered positive scale cone.

CONFIDENCE: \(>99.99\%\). The only interpretive point is the normalization of “reduced cofactor”; the proof gives the unreduced minor as well, and the stated normalization reproduces the paper’s sign and integer checks.