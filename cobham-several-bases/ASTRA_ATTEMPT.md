# arXiv:2611.27882 [q:severalbases]

status: completed cost: $1.2722 incomplete: None

TARGET: \label{q:severalbases}
Let $d\ge2$, and let $\alpha_1,\dots,\alpha_t\in R$ be expansive, with $\Q(\alpha_1^{n_1},\dots,\alpha_t^{n_t})=K$ for all $n_i\ge1$ and $\alpha_i^rR\ne\alpha_j^sR$ for all $i\ne j$ and $r,s\ge1$. Is every function $f:R\to\Omega$ automatic in all the bases $\alpha_i$ eventually periodic, even when no pair $(\alpha_i,\alpha_j)$ satisfies \textup{(H)}?

---

VERDICT: PROVED

STATEMENT: “Let \(d\ge2\), and let \(\alpha_1,\dots,\alpha_t\in R\) be expansive, with \(\mathbb Q(\alpha_1^{n_1},\dots,\alpha_t^{n_t})=K\) for all \(n_i\ge1\) and \(\alpha_i^rR\ne\alpha_j^sR\) for all \(i\ne j\) and \(r,s\ge1\). Is every function \(f:R\to\Omega\) automatic in all the bases \(\alpha_i\) eventually periodic, even when no pair \((\alpha_i,\alpha_j)\) satisfies \(\textup{(H)}\)?”

The answer is **yes**, with \(t\ge2\) as specified in the preceding paragraph of the paper, \(R=\mathcal O_K\), and \(\Omega\) finite.

DEGENERATE: no — the proof covers the case where every original pair fails (H).

ARGUMENT:

**Sanity checks.** In the paper’s base-\(7\) example in \(\mathbb Z[\sqrt2]\), I enumerated the length-\(k\) word values \(a+b\sqrt2\), \(0\le a,b<7^k\). Testing divisibility by \((3+\sqrt2)^k\) by repeated exact division gave counts \(7,49,343\) for \(k=1,2,3\), as stated. For the paper’s three bases \(4+\sqrt2,4+\sqrt3,4+\sqrt5\), exact minimal-polynomial computations gave degree \(4\) for each pairwise product, but degree \(8\) for the product of all three and for its second and third powers. The proof below handles all powers without extrapolating from these checks.

**1. Automaticity passes to product bases.** Suppose \(f\) is automatic in two expansive bases \(a,b\), and put \(\lambda=ab\). Fix a window set \(D\) for \(\lambda\). By the paper’s size bound, every \(c\in D^{(n)}\) satisfies
\[
|\sigma c|\le C_D|\sigma\lambda|^n
\]
at every archimedean place. Thus every \(\lambda\)-kernel \(y\mapsto f(c+\lambda^ny)\) belongs to the finite family in the mixed-kernels proposition for \(a,b\): take the mixed scale \(a^nb^n\). The window-set kernel criterion gives \(\lambda\)-automaticity. This uses neither (H) nor (Ind). By iteration and passage to powers, \(f\) is automatic in every base \(\prod_i\alpha_i^{e_i}\) with positive integer exponents.

**2. Choose one product base every power of which generates \(K\).** For each positive integer \(m\), put
\[
b_m=\prod_{i=1}^t\alpha_i^{m^{i-1}}.
\]
Fix a proper intermediate field \(\mathbb Q\subseteq F\subsetneq K\). I claim that for at most \(t-1\) distinct \(m\) does **any** positive power of \(b_m\) belong to \(F\).

Indeed, suppose \(b_{m_j}^{s_j}\in F\) for \(t\) distinct \(m_j\) and positive \(s_j\). The integer matrix
\[
A_{ji}=s_jm_j^{i-1}
\]
has nonzero determinant by the Vandermonde formula. Its row lattice therefore contains \(D_0\mathbf e_i\) for every standard basis vector \(\mathbf e_i\), where \(D_0=|\det A|\), by the adjugate identity. The homomorphism
\[
\mathbb Z^t\longrightarrow K^\times,\qquad (v_i)\longmapsto\prod_i\alpha_i^{v_i}
\]
sends every row of \(A\) into \(F^\times\), hence sends its whole row lattice into \(F^\times\). In particular \(\alpha_i^{D_0}\in F\) for every \(i\), contradicting the joint field-generation hypothesis. This proves the claim.

There are only finitely many intermediate fields, by Galois correspondence in a finite normal closure of \(K/\mathbb Q\). Choose \(m\) outside the finite union of their bad choices, taking the union over proper fields only. Then \(b=b_m\) satisfies \(\mathbb Q(b^s)=K\) for **every** \(s\ge1\): otherwise \(\mathbb Q(b^s)\) itself would be a proper field witnessing a bad choice. Thus \((b,\alpha_j)\) satisfies (H) for every \(j\).

**3. Choose the second base among the original ones.** At most one \(\alpha_iR\) can have a positive power equal to a positive power of \(bR\). Indeed, if \(b^{u_i}R=\alpha_i^{v_i}R\) and \(b^{u_j}R=\alpha_j^{v_j}R\) for distinct \(i,j\), then raising the equalities to \(u_j\) and \(u_i\), respectively, gives
\[
\alpha_i^{v_i u_j}R=\alpha_j^{v_j u_i}R,
\]
contrary to the hypothesis. Since \(t\ge2\), choose \(j\) for which \((b,\alpha_j)\) satisfies (Ind).

Both bases are expansive, both compute \(f\) by Step 1 and the original assumption, and they satisfy (H) and (Ind). The paper’s two-base main theorem now says exactly that \(f\) agrees outside a finite set with a function periodic for a subgroup of \(R\) of rank \(d\). This is the required eventual periodicity.

CONFIDENCE: 99.9%. The substantive dependency is the supplied two-base main theorem, used as stated; the reduction to a pair satisfying its hypotheses is independent of the numerical checks.