# arXiv:2611.31308 [conjecture#2]

status: completed cost: $0.9861 incomplete: None

TARGET: [Weak form]
For even $L$ and any field strength $g$, the ground state of the TFIM can be prepared by a VQCS circuit with $L/2$ layers.

---

VERDICT: PROVED

STATEMENT: “For even \(L\) and any field strength \(g\), the ground state of the TFIM can be prepared by a VQCS circuit with \(L/2\) layers.”

DEGENERATE: no — the proof works for every positive even \(L\) and every real \(g\). At \(g=0\), I read preparation as preparation of **a** ground state; the one obtained is the spin-flip-even ground state.

CERTIFICATE: Not applicable.

ARGUMENT:

I used a **signed-energy polynomial reduction**, rather than trying to prove saturation of the set of reachable states. The special property of the TFIM ground-state target is that the squared one-mode energy is *affine* in the mode coordinate \(x\). This makes it possible to construct a single nonnegative polynomial whose spectral factor specifies the circuit.

As initial convention checks, I evaluated the paper’s \(L=4\) isometry on its four stated basis states. The maximum absolute entry discrepancies from its displayed \(\tilde H_X,\tilde H_{ZZ}\) were \(2.23\times10^{-15}\) and \(3.56\times10^{-15}\), respectively, rounded up. Applying its three-layer parameters directly in the 16-dimensional spin space gave squared overlap \(0.9999999999999989\) with \(\Psi_T\). The proof below does not use reachability of \(\Psi_T\).

### 1. Mode coordinates and the preparation problem

Write \(L=2n\). The \(n\) mode coordinates, in a convenient order, are
\[
x_j=\cos\frac{(2j-1)\pi}{2n},\qquad 1\le j\le n.
\]
Write \(s=\sqrt{1-x^2}\). In the paired two-dimensional mode spaces the initial spinor is \((1,0)^t\), and the contributions to \(H_X,H_{ZZ}\) are respectively
\[
-2\sigma_z,\qquad -2(x\sigma_z+s\sigma_x).
\tag{1}
\]

Here are details of the sector and sign conventions. For \(g>0\), Perron–Frobenius in the \(Z\) basis gives a unique strictly positive ground state: the negative off-diagonal entries connect the whole hypercube. Hence it is even under \(\prod_i X_i\). For \(g<0\), conjugation by \(\prod_i Z_i\) changes the sign of \(g\) and preserves this parity because \(L\) is even. In the even sector, take \(\tau^z=X,\ \tau^x=Z\) and Jordan–Wigner operators \(c_j=(\prod_{\ell<j}\tau_\ell^z)\tau_j^+\). The bond operator is \((c_j^\dagger-c_j)(c_{j+1}^\dagger+c_{j+1})\), using \(c_{L+1}=-c_1\) for the boundary bond. Fourier transformation \(c_j=L^{-1/2}\sum_k e^{ikj}c_k\) thus gives antiperiodic momenta. For each \(0<k<\pi\), the field contribution is \(2(n_k+n_{-k}-1)\), and the bond-Hamiltonian contribution is
\[
-2\cos k\,(n_k+n_{-k}-1)
+\big(-2i\sin k\,c_k^\dagger c_{-k}^\dagger+\mathrm{h.c.}\big).
\]
The constants \(2\cos k\) sum to zero. In the basis of the pair vacuum and \(i c_k^\dagger c_{-k}^\dagger\) applied to that vacuum, these are (1) with \(x=-\cos k\). These \(x\)'s are exactly the listed \(x_j\)'s. The initial spin state is the fermion vacuum. This calculation uses the paper’s periodic sum also for \(L=2\), where it counts the bond twice.

Put
\[
m=g+x,\qquad d=\sqrt{m^2+s^2}=\sqrt{1+g^2+2gx}.
\tag{2}
\]
At a mode node \(s>0\). The local ground spinor is the \(+d\) eigenvector of \(m\sigma_z+s\sigma_x\), and its energy is \(-2d<0\); the two singly occupied states have energy zero. Thus the product of these local ground spinors is a ground state in the even sector and, by the parity argument, a ground state of the spin Hamiltonian for \(g\ne0\).

We will construct complex polynomials \(P,Q\) of degrees at most \(n,n-1\) such that
\[
\begin{split}
 |P(x)|^2+(1-x^2)|Q(x)|^2&=1 \qquad(-1\le x\le1),\\
 P(x_j)&=(g+x_j+d_j)Q(x_j),\qquad d_j=\sqrt{1+g^2+2gx_j}.
\end{split}
\tag{3}
\]
The second line means exactly that \((P(x_j),s_jQ(x_j))^t\) is the required ground spinor: it is proportional to \((m_j+d_j,s_j)^t\).

### 2. Why the polynomial degrees in (3) suffice for \(n\) layers

More generally, any pair satisfying the normalization in (3) with degrees at most \(p,p-1\) is synthesizable, up to overall phase, in \(p\) layers. Here is a layer-removal proof.

For \(p\ge1\), comparing the coefficient of \(x^{2p}\) in the normalization identity gives \(|P_p|=|Q_{p-1}|\), where subscripts denote coefficients. If both vanish, reduce \(p\) by one and pad with an identity layer. Otherwise undo a field rotation, setting
\[
F=e^{-ib}P,\qquad G=e^{ib}Q,
\]
choosing real \(b\) so that \(F_p=G_{p-1}=C\ne0\). Then \(R=F-xG\) has degree at most \(p-1\). The normalization becomes
\[
|R|^2+2x\operatorname{Re}(R\overline G)+|G|^2=1.
\]
Its coefficient of \(x^{2p-1}\) gives \(\operatorname{Re}(R_{p-1}\overline C)=0\). Consequently there exists real \(\alpha\) such that
\[
(\cos\alpha) C-i(\sin\alpha)R_{p-1}=0.
\]
Applying the inverse interaction rotation \(\exp[-i\alpha(x\sigma_z+s\sigma_x)]\) to the spinor \((F,sG)^t\) gives a new polynomial pair
\[
\big( (\cos\alpha)F-i(\sin\alpha)(xR+G),\
       (\cos\alpha)G-i(\sin\alpha)R\big).
\]
The displayed choice of \(\alpha\) kills the leading coefficient in **both** polynomials, so the degrees are at most \(p-1,p-2\). Normalization is preserved. At \(p=0\) the spinor is \((\text{constant phase},0)^t\). Reversing the removals gives precisely the layers in the question, with \(\gamma=\alpha/2\) and \(\beta=b/2\) by (1).

It remains to prove existence in (3), not merely count parameters.

### 3. A bounded interpolant for the mode energies

First suppose \(g\notin\{0,1,-1\}\). Use the squared-energy variable
\[
t=1+g^2+2gx,\qquad t_j=1+g^2+2gx_j.
\]
Let \(a<b\) be \((g-1)^2,(g+1)^2\) in increasing order. For \(v=a,b\), let \(e_v\) be the corresponding **signed** number \(g-1\) or \(g+1\), so \(e_v^2=v\). In particular \(a>0\).

We construct a real polynomial \(A\) of degree at most \(2n+1\) with the following properties:
* \(A(t_j)=\sqrt{t_j}\) and \(A(v)=e_v\) for \(v=a,b\).
* On \([a,b]\), \(-\sqrt t\le A(t)\le\sqrt t\).
* On each exterior interval \(0\le t<a\) or \(t>b\), use its adjacent endpoint \(v=a\) or \(b\). If \(e_v>0\), then \(A(t)\ge\sqrt t\); if \(e_v<0\), then \(A(t)\le-\sqrt t\).

The exterior inequalities are important: we will need a polynomial nonnegative on the **whole real line**, not just on the physical modes.

Set \(W(t)=\prod_j(t-t_j)^2\). The nodes \(x_j\) being the zeros of the Chebyshev polynomial \(T_n\), we have
\[
W(t)=C\, T_n\!\left(\frac{t-1-g^2}{2g}\right)^2,\qquad C=W(a)=W(b)>0.
\]
Thus \(W\le C\) inside \([a,b]\) and \(W\ge C\) outside it.

Let \(B\) be the degree-\(\le 2n-1\) Hermite interpolant to \(f(t)=\sqrt t\) at the \(t_j\), matching values and first derivatives. Its error admits the identity, for \(t>0\),
\[
B(t)=\sqrt t+W(t)E(t),\qquad
E(t)=\frac1\pi\int_0^\infty
            \frac{\sqrt u}{W(-u)(t+u)}\,du .
\tag{4}
\]
Indeed, use \(\sqrt t=\pi^{-1}\int_0^\infty [t/(t+u)]\,du/\sqrt u\). The Hermite interpolant of \(1/(t+u)\) is
\[
\frac{1-W(t)/W(-u)}{t+u},
\]
which is a polynomial of the right degree and matches to first order at every node. Applying this to \(t/(t+u)=1-u/(t+u)\) gives (4) by linearity. Interpolation commutes with the integral because it is a finite linear combination of the convergent node-value and node-derivative integrals.

The function \(E\) is convex, whereas
\[
F(t):=E(t)+2\sqrt t/C
\]
is concave. In fact differentiating (4)'s integral twice and using \(W(-u)\ge C\) gives
\[
0\le E''(t)\le \frac{2}{\pi C}\int_0^\infty\frac{\sqrt u}{(t+u)^3}\,du
=-\frac{f''(t)}{C}.
\]
The differentiations are valid locally on \(t>0\) by integrable domination.

Let \(\ell\) be the affine function specified at \(a,b\) by
\[
\ell(v)=
\begin{cases}
E(v),&e_v>0,\\
F(v),&e_v<0.
\end{cases}
\qquad
A=B-W\ell .
\tag{5}
\]
This gives the claimed degree, node values and signed endpoint values. Inside \([a,b]\), convexity and concavity give \(E\le\ell\le F\): compare \(\ell\) with the two endpoint chords. Therefore
\[
A(t)=\sqrt t-W(t)(\ell(t)-E(t))
\]
lies between \(-\sqrt t\) and \(\sqrt t\), since \(W(t)\le C\).

Outside the interval, consider the adjacent endpoint \(v\). If \(\ell(v)=E(v)\), then \(\ell\) is at or below the extended chord of \(E\) on that side (at the opposite endpoint \(\ell\ge E\)). By convexity this extended chord is at or below \(E\). Hence \(A\ge\sqrt t\). If \(\ell(v)=F(v)\), the reversed comparison gives \(\ell\ge F\) on that side, and \(W\ge C\) gives \(A\le-\sqrt t\). Continuity includes \(t=0\). This proves all the interpolation properties.

### 4. Spectral factorization gives exactly the ground spinors

Now allow \(d\) to be a **signed real variable** and write
\[
x=\frac{d^2-1-g^2}{2g},\qquad m=g+x,\qquad
d-m=\frac{1-(d-g)^2}{2g}.
\]
Consider
\[
N(d)=\frac{d-A(d^2)}{d-m}.
\tag{6}
\]
This is a real polynomial of degree at most \(4n\): the two denominator roots \(g-1,g+1\) are distinct and the numerator vanishes at both by the *signed* endpoint values.

We have \(N(d)\ge0\) for all real \(d\). To see this, if \(a<d^2<b\), then \(|x|<1\) and \(d^2-m^2=1-x^2>0\). The denominator has the sign of \(d\), and \(|A(d^2)|\le |d|\) makes the quotient nonnegative. If \(d^2\) is exterior, then \(|m|>|d|\), and the sign of \(m\) is that of \(e_v\) at the adjacent endpoint: \(m\) equals \(e_v\) there and cannot cross zero in this exterior interval. When \(m>0\), the denominator is negative and \(A(d^2)\ge |d|\); when \(m<0\), the denominator is positive and \(A(d^2)\le-|d|\). Again the quotient is nonnegative. The remaining points follow by continuity.

Consequently there is a complex polynomial \(D\), of degree at most \(2n\), with \(N(d)=|D(d)|^2\) on the real line. This is elementary polynomial factorization: take half the multiplicity of each real root, one side of each nonreal conjugate pair, and the square root of the leading coefficient. The polynomial \(N\) is not identically zero since \(A(d^2)\) cannot be identically \(d\).

Split \(D(d)=U(d^2)+dV(d^2)\) into even and odd parts. With \(t=1+g^2+2gx\), define
\[
Q(x)=-V(t),\qquad P(x)=U(t)+(g+x)Q(x).
\]
These have degrees at most \(n-1,n\), respectively, and give the key identity
\[
D(d)=P(x)-(m+d)Q(x).
\tag{7}
\]
By (6), evaluating at \(d\) and \(-d\) gives
\[
(d-m)|D(d)|^2+(d+m)|D(-d)|^2=2d.
\]
For \(x\in[-1,1]\) take the positive \(d=\sqrt t\). Substitute (7) into this last equality. The mixed terms cancel, and division by \(2d\) yields
\[
|P(x)|^2+(d^2-m^2)|Q(x)|^2=1.
\]
This is the first line of (3). At each positive node energy \(d_j\), we have \(A(d_j^2)=d_j\) and \(d_j-m_j>0\). Thus \(N(d_j)=0\), so \(D(d_j)=0\), and (7) is precisely the second line of (3). This completes the construction at all nonexceptional fields.

### 5. Exceptional fields and checks

For fixed \(L\), all depth-\(n\) parameter angles may be taken modulo \(2\pi\) since the original spin Hamiltonians \(H_X,H_{ZZ}\) have integer spectra. The parameter space is compact. For \(g_*\in\{0,1,-1\}\), let nonexceptional \(g\) tend to \(g_*\) and take a convergent subsequence of the constructed parameters. Circuit states, their energies, and the minimum eigenvalue of \(H_{ZZ}+gH_X\) are continuous. Hence the limiting circuit attains the minimum eigenvalue at \(g_*\). At zero field it stays in the even sector, so this gives the even cat state, not a claim that arbitrary members of the degenerate ground space are preparable.

As numerical checks on the construction, I factored (6), removed the layers as in section 2, and reapplied them. The table gives the Euclidean norm of the vector of the \(n\) unwanted excited-spinor amplitudes, using floating-point angles for the final circuit evaluation:

| \(L\) | \(g\) | Excited-amplitude norm |
|---:|---:|---:|
| 8 | \(2\) | \(3.58\times10^{-16}\) |
| 12 | \(0.75\) | \(1.81\times10^{-15}\) |
| 32 | \(-1.5\) | \(7.87\times10^{-15}\) |
| 64 | \(-1.5\) | \(1.93\times10^{-14}\) |
| 128 | \(-1.5\) | \(5.60\times10^{-14}\) |

I also checked a constructed \(L=6,\ g=-2\) circuit against direct spin-space diagonalization, obtaining squared ground-state overlap \(0.9999999999999993\). These checks are not needed for existence: the interpolation and factorization prove (3) exactly, and the layer-removal argument realizes it with \(L/2\) layers.

CONFIDENCE: 99.7%. The most delicate step is global nonnegativity of (6), especially for negative fields where the signed endpoint data need not agree with \(+\sqrt t\). The exterior chord comparisons in (5) are what enforce the required signs there.