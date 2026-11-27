# arXiv:2611.31308 [conjecture#2]

status: completed cost: $0.6708 incomplete: None

TARGET: [Weak form]
For even $L$ and any field strength $g$, the ground state of the TFIM can be prepared by a VQCS circuit with $L/2$ layers.

---

VERDICT: PROVED

STATEMENT: “For even \(L\) and any field strength \(g\), the ground state of the TFIM can be prepared by a VQCS circuit with \(L/2\) layers.”

DEGENERATE: no — the proof covers every positive even \(L\) and every real \(g\). At \(g=0\), where the ground state is not unique, the circuit prepares the spin-flip-even ground state. Preparation is up to global phase.

CERTIFICATE: Not applicable (proof).

ARGUMENT:

The key is to interpolate the **energy** of each free-fermion mode, rather than interpolate its rotation angle. The energy polynomial must touch a square root at the \(L/2\) mode locations. I show that its Hermite interpolant satisfies a global sign condition; this allows it to be factored into two amplitude polynomials, from which the \(L/2\) circuit layers can be extracted.

**Convention and numerical checks.** Using the paper’s periodic bond sum and its four-qubit isometry, I obtained \(\widetilde H_X=\operatorname{diag}(-4,0,0,4)\) in the pseudospin \(X\)-basis and \(\langle+-|\widetilde H_{ZZ}|+-\rangle=-2\sqrt2\). Applying the paper’s three-layer angles in the physical four-qubit space gave
\[
\langle\Psi_T|\Psi;3,\vec\gamma,\vec\beta\rangle
=0.7071067811865477+0.7071067811865475i.
\]
I also tested the construction below. For \((L,g)=(2,-2),(4,1),(6,-0.5),(8,0.4)\), the squared overlaps with direct spin-Hamiltonian ground states were within \(10^{-15}\) of one. For \((34,-1.2)\) and \((40,0.7)\), the largest unwanted excited-state amplitude over the modes was \(1.46\times10^{-14}\) and \(2.92\times10^{-15}\), respectively. These checks are not needed for the proof.

### 1. The simultaneous state-preparation problem

Write \(n=L/2\). For \(g>0\), the full spin Hamiltonian has a unique positive ground vector in the computational basis, by Perron–Frobenius: its off-diagonal single-spin flips have coefficient \(-g\) and connect the basis. The vector is even under \(\prod_j X_j\), since this symmetry permutes the basis. For \(g<0\), conjugation by \(\prod_j Z_j\) changes the sign of \(g\) and preserves the spin-flip parity because \(L\) is even. Thus it suffices for now to find the even-sector ground state for \(g\ne0\).

Here are the mode conventions explicitly. Use local Pauli axes \(\sigma^z=X,\ \sigma^x=Z\), and Jordan–Wigner operators \(c_j=(\prod_{l<j}\sigma_l^z)\sigma_j^+\). The initial state is the vacuum. In the even sector the bond sum becomes
\[
H_{ZZ}=-\sum_j(c_j^\dagger-c_j)(c_{j+1}^\dagger+c_{j+1}),
\qquad c_{L+1}=-c_1,
\]
and \(H_X=-L+2\sum_j c_j^\dagger c_j\). With \(c_j=L^{-1/2}\sum_k e^{ikj}c_k\), the positive momenta are \(k=(2j-1)\pi/L,\ j=1,\ldots,n\). For a pair \(k,-k\), the bond term has number part \(-2\cos k\,(n_k+n_{-k})\) and creation part \(-2i\sin k\,c_k^\dagger c_{-k}^\dagger\) plus its adjoint. Thus on the pair basis consisting of the vacuum and \(i c_k^\dagger c_{-k}^\dagger|\mathrm{vac}\rangle\), the two generators are
\[
H_X^{(k)}=-2Z,\qquad H_{ZZ}^{(k)}=-2(xZ+sX),
\qquad x=-\cos k,\quad s=\sqrt{1-x^2}.
\]
Here we dropped a scalar \(-2\cos k\) from the bond term on each pair; these scalars sum to zero. With this shift both generators are zero on the singly occupied states of the pair.

In particular the \(x\)'s are exactly the roots of the Chebyshev polynomial \(T_n\). Put
\[
a(x)=g+x,\qquad \lambda(x)=1+g^2+2gx,\qquad r(x)=\sqrt{\lambda(x)}.
\]
At each mode, \(r^2=a^2+s^2\) and \(r>0\). The lowest pair energy is \(-2r\), attained by the positive-eigenvalue spinor of \(aZ+sX\), proportional to \((r+a,s)^{\mathsf T}\). The product of these pair ground states is even and minimizes the sum.

We will construct complex polynomials \(A,B\), of degrees at most \(n,n-1\), with
\[
|A(x)|^2+(1-x^2)|B(x)|^2=1,                                      \tag{1}
\]
such that the spinor \((A(x),sB(x))^{\mathsf T}\) is the desired one at every root of \(T_n\). Section 4 below verifies directly that every such normalized polynomial spinor is implementable with \(n\) layers.

### 2. The energy interpolant and its bounds

Let \(J=\{x\in\mathbb R:\lambda(x)\ge0\}\), which contains \([-1,1]\). Let \(H_0\) be the polynomial of degree at most \(2n-1\) interpolating both \(r\) and \(r'\) at the \(n\) roots of \(T_n\). Define
\[
h(x)=H_0(x)+T_n(x)^2\ell(x),
\]
where \(\ell\) is the affine polynomial chosen so that \(h(\pm1)=a(\pm1)\). This is possible since \(T_n(\pm1)^2=1\). We claim that
\[
\begin{array}{ll}
-r\le h\le r & (|x|\le1),\\[2mm]
h\ge r\ \text{if }a>0,\qquad h\le-r\ \text{if }a<0
    &(x\in J,\ |x|>1).
\end{array}                                                       \tag{2}
\]
The exterior bounds are important: they will give a polynomial nonnegative on the **whole real line**, not just at the physical momenta.

To prove (2), define
\[
D=\frac{r-h}{T_n^2},\qquad E=2r-D,
\]
using continuous values at the interpolation nodes. **Both \(D\) and \(E\) are concave on \(J\).** Indeed, use
\[
\sqrt{\lambda}=\frac1\pi\int_0^\infty
            \frac{\lambda}{u+\lambda}\frac{du}{\sqrt u},
\qquad
\xi_u=-\frac{1+g^2+u}{2g}.
\]
The error of Hermite interpolation of \(1/(u+\lambda(x))\) at our nodes is exactly
\[
\frac{T_n(x)^2}{(u+\lambda(x))T_n(\xi_u)^2}.
\]
In fact, subtracting this expression from \(1/(u+\lambda(x))\) gives a polynomial of degree at most \(2n-1\), because its numerator vanishes at the pole \(\xi_u\); the subtracted expression has double zeros at all nodes. Applying this identity to \(\lambda/(u+\lambda)=1-u/(u+\lambda)\) gives
\[
D(x)=-\ell(x)-\frac1\pi\int_0^\infty
           \frac{\sqrt u\,du}{(u+\lambda(x))T_n(\xi_u)^2}.        \tag{3}
\]
Interpolation commutes with this integration since it is linear in the finitely many node values and derivatives, whose integrals converge (\(\lambda>0\) at the nodes).

For \(\lambda(x)>0\), differentiating twice, \(D''\) and \(r''\) are respectively the integrals of the same negative weight
\[
-\frac{2(2g)^2}{\pi}\frac{\sqrt u\,du}{(u+\lambda(x))^3}
\]
multiplied by \(T_n(\xi_u)^{-2}\) and by \(1\). These differentiated integrals converge locally uniformly. Since \(|\xi_u|\ge1\), we have \(0<T_n(\xi_u)^{-2}\le1\). Consequently \(D''\le0\) and \(E''=2r''-D''\le0\), proving concavity, including the finite endpoint of \(J\) by continuity.

At \(x=\pm1\), \(r=|a|\), and
\[
D=r-a\ge0,\qquad E=r+a\ge0.
\]
By concavity, \(0\le D\le2r\) on \([-1,1]\). There \(T_n^2\le1\), so \(h=r-T_n^2D\) lies between \(-r\) and \(r\).

For the exterior, consider the endpoint \(e\in\{-1,1\}\) on the side in question. If \(a(e)>0\), then \(D(e)=0\), and concavity together with nonnegativity on \([-1,1]\) gives \(D\le0\) beyond \(e\). Thus \(h\ge r\). If \(a(e)<0\), the same argument gives \(E\le0\) beyond \(e\), so \(D\ge2r\); now \(T_n^2\ge1\) yields \(h\le-r\). The sign of \(a\) does not change on the exterior portion of \(J\), since \(a^2-r^2=x^2-1>0\) there. If \(a(e)=0\), then \(\lambda(e)=0\) and there is no portion of \(J\) beyond that endpoint. This proves (2).

### 3. Factoring the interpolant into amplitudes

Introduce a real variable \(t\) for the **signed** square root and put
\[
x(t)=\frac{t^2-1-g^2}{2g},\qquad
P(t)=\frac{t-h(x(t))}{t-a(x(t))}.                               \tag{4}
\]
This quotient is a real polynomial of degree at most \(4n\): the denominator is \([1-(t-g)^2]/(2g)\), and at both its distinct zeros \(t=g\pm1\) we have \(x(t)=\pm1\) and \(h=a=t\).

Moreover \(P(t)\ge0\) for every real \(t\). Indeed \(x(t)\in J\) and \(t=\pm r(x(t))\). For \(|x|<1\), \(a\) lies strictly between \(-r\) and \(r\), and \(h\) lies between them by (2). Hence the quotient is nonnegative at both choices of sign. For \(|x|>1\), either \(a>r\) and \(h\ge r\), or \(a<-r\) and \(h\le-r\), again giving nonnegativity. The remaining points follow by continuity.

Factor \(P(t)=|F(t)|^2\) on the real line, with \(F\) a complex polynomial of degree at most \(2n\). This is ordinary polynomial factorization: real roots have even multiplicity, and nonreal roots come in conjugate pairs. Separating the even and odd powers of \(t\), write
\[
F(t)=A(x(t))-\bigl(a(x(t))+t\bigr)B(x(t)).
\]
Specifically, the odd part gives \(-tB\), with \(\deg B\le n-1\); the even part gives \(A-aB\), with \(\deg A\le n\), since \(t^2\) is affine in \(x\).

For \(-1<x<1\), formula (4) gives
\[
\frac{r-a}{2r}|F(r)|^2+\frac{r+a}{2r}|F(-r)|^2
=\frac{r-h}{2r}+\frac{r+h}{2r}=1.
\]
Expanding the left side cancels the cross terms and gives \(|A|^2+(r^2-a^2)|B|^2\). Since \(r^2-a^2=1-x^2\), this proves (1), also as a polynomial identity in real \(x\).

Finally, at every root of \(T_n\) we have \(h=r\) and \(r-a>0\). Thus \(F(r)=0\), or
\[
A=(r+a)B .
\]
By (1) the spinor is nonzero, so it is proportional to \((r+a,s)^{\mathsf T}\), exactly as required.

### 4. Extracting the circuit layers

For completeness, suppose \(A,B\) satisfy (1) with degree bounds \(m,m-1\), where \(m\ge1\). We can remove one layer and reduce both bounds by one. Write \(A_j,B_j\) for coefficients, taking missing coefficients as zero. The \(x^{2m}\) coefficient of (1) gives \(|A_m|=|B_{m-1}|\). If both vanish, the bounds are already reduced. Otherwise choose \(b\) so that
\[
U=e^{-ib}A,\qquad W=e^{ib}B,\qquad U_m=W_{m-1}=d\ne0 .
\]
This applies \(e^{-ibZ}\) to the spinor. The \(x^{2m-1}\) coefficient of (1) gives
\(\operatorname{Re}(\bar d(U_{m-1}-W_{m-2}))=0\). Therefore one can choose a real \(v\) with
\[
(\cos v)d-i(\sin v)(U_{m-1}-W_{m-2})=0,
\]
because \((U_{m-1}-W_{m-2})/d\) is purely imaginary.

Next apply \(e^{-iv(xZ+sX)}\). With \(c=\cos v,\ q=\sin v\), the new polynomials are
\[
A'=(c-iqx)U-iq(1-x^2)W,\qquad
B'=-iqU+(c+iqx)W .
\]
In \(A'\) the \(x^{m+1}\) coefficient vanishes because \(U_m=W_{m-1}\); the \(x^m\) coefficient vanishes by the choice of \(v\). The same two cancellations remove the \(x^m\) and \(x^{m-1}\) coefficients of \(B'\). The new spinor remains normalized by unitarity. Induction therefore reduces the spinor to \((\text{constant phase},0)^{\mathsf T}\).

Reversing the reductions prepares the desired spinor with at most \(n\) layers of the form
\[
e^{ibZ}e^{iv(xZ+sX)}.
\]
Crucially, \(b,v\) were chosen from polynomial coefficients, **not separately for each \(x\)**. These are precisely the paper’s common-angle layers with \(\beta=b/2,\ \gamma=v/2\). Identity layers may pad the count to \(n\). Thus the product of pair ground states is prepared for every \(g\ne0\).

At \(g=0\), take a sequence \(g\downarrow0\). The \(2n\) angles may be taken modulo \(2\pi\), since the physical generators have integer spectra. A convergent subsequence on this compact torus gives a limiting \(n\)-layer circuit. By continuity its output minimizes \(H_{ZZ}\) and is spin-flip even, so it is the even ferromagnetic cat state up to phase. This completes the proof.

CONFIDENCE: 0.998. The most delicate step is the exterior sign bound in (2); it is needed for spectral factorization and does not follow from boundedness on the physical interval alone. Equation (3) and the two concavity inequalities establish it on the full required domain.