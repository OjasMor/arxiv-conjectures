# Referee report for 2611.27882__1

status: completed cost: $1.3767

REFEREE VERDICT: CORRECT

STATEMENT MATCH: yes. Question 10.3 (`q:severalbases`) asks:

> Let \(d\ge2\), and let \(\alpha_1,\dots,\alpha_t\in R\) be expansive, with \(\mathbb Q(\alpha_1^{n_1},\dots,\alpha_t^{n_t})=K\) for all \(n_i\ge1\) and \(\alpha_i^rR\ne\alpha_j^sR\) for all \(i\ne j\) and \(r,s\ge1\). Is every function \(f:R\to\Omega\) automatic in all the bases \(\alpha_i\) eventually periodic, even when no pair \((\alpha_i,\alpha_j)\) satisfies (H)?

The preceding paragraph specifies \(t\ge2\); the standing assumptions are \(R=\mathcal O_K\) and \(\Omega\) finite. The relevant definitions are:

- “\(\gamma\in R\) is *expansive* if \(|\sigma\gamma|>1\) for every \(\sigma\in\Sigma_\infty\).”
- “\(f\) is \(\gamma\)-automatic when it has finitely many \(\gamma\)-kernels with respect to one, equivalently every, window set for \(\gamma\).” These kernels are \(y\mapsto f(c+\gamma^ny)\), with \(c\) a word value of length \(n\); a window set requires that “every class of \(R/\gamma^nR\) meets \(D^{(n)}\).”
- “The function \(f\) is *eventually periodic* if it agrees, outside a finite subset of \(R\), with a function whose group of periods has rank \(d\).”

DEGENERATE OR ALREADY KNOWN IN PAPER: no. The paper proves that, under joint field generation, **one far period suffices**. It explicitly says, “What the methods of this paper do not give is the first far period.” The claim does not assume such a period or an original pair satisfying (H). It constructs a new pair to which the paper’s theorem applies.

DETAILS:

1. **Product automaticity holds.** For a window set \(D\) of \(ab\), the size bound gives \(|\sigma c|\le C_D|\sigma(ab)^n|\) at *each* place for every \(c\in D^{(n)}\). Thus every \(ab\)-kernel belongs to the finite family in Proposition `prop:mixed`, taking \(k=l=n\) and, for instance, \(A=1+C_D\). That proposition assumes neither (H) nor (Ind). The window criterion gives \(ab\)-automaticity. Iteration is valid because products of expansive elements remain expansive; no uniform bound across different product bases is needed.

2. **The field-selection argument handles every positive power, not just the first.** Fix a proper intermediate field \(F\), including the possibility \(F=\mathbb Q\). If \(t\) distinct \(m_j\) had \(b_{m_j}^{s_j}\in F\), the exponent matrix would have determinant
   \[
   \det A=\Bigl(\prod_j s_j\Bigr)\prod_{j<k}(m_k-m_j)\ne0.
   \]
   The identity \(\operatorname{adj}(A)A=(\det A)I\) puts \(|\det A|\mathbf e_i\) in the **row** lattice for every \(i\). Negative coefficients in a row combination cause no problem: its multiplicative image is taken in \(F^\times\). Thus \(F\) contains every \(\alpha_i^{|\det A|}\), contradicting the joint hypothesis at this common positive exponent. Each \(F\) therefore rules out at most \(t-1\) choices of \(m\), even allowing \(s_j\) to vary. There are finitely many intermediate fields by passage to the finite Galois closure. For any remaining \(m\), a failure at any \(s\ge1\) would make \(\mathbb Q(b_m^s)\) itself a forbidden proper field.

3. **The ideal argument uses only pairwise independence.** If two distinct original bases had ideal powers equal to powers \(u_i,u_j\) of \(bR\), raising to \(u_j,u_i\) respectively would equate positive powers of their own ideals. Hence at most one original base is disqualified. For any other \(\alpha_j\), (Ind) holds, and (H) holds because \(\mathbb Q(b^r)=K\) for every \(r\ge1\). Theorem 8.1 (`thm:main`) now gives exactly the required eventual periodicity. **No step fails.**

**Independent exact Python checks:**

- In the paper’s base-\(7\) example, I used \(M=\left(\begin{smallmatrix}3&2\\1&3\end{smallmatrix}\right)\), multiplication by \(3+\sqrt2\). Testing \(\operatorname{adj}(M^k)(a,b)^T\equiv0\bmod 7^k\) over the word-value box gave counts **`[7, 49, 343]`** for \(k=1,2,3\).
- For the paper’s half-space \(f(x+y\sqrt2)=\mathbf1_{x>0}\), I enumerated the kernel thresholds on the first coordinate using the standard coordinate-box windows. In bases \(2,3\), and their product \(6\), the threshold sets at depths \(0,1,2,3\) were all **`{1}, {0,1}, {0,1}, {0,1}`**. This tests product closure where (H) fails.
- For \(4+\sqrt2,4+\sqrt3,4+\sqrt5\), I computed degrees as the square-free characteristic-polynomial degrees of multiplication matrices in the eight-dimensional multiquadratic field. The pairwise products gave **`[4,4,4]`**; for each \(m=1,2,3\), the degrees of \(b_m,b_m^2,b_m^3\) were **`[8,8,8]`**. The original absolute norms had prime supports **`{2,7}, {13}, {11}`**, confirming pairwise (Ind). Every original pair lies in a proper biquadratic field, so this is genuinely the case the question singles out.
- Two boundary tests matter. In \(\mathbb Z[i]\), with bases \(2+i,1+2i\), the first candidate \(b_1=5i\) gave power degrees **`[2,1,2,1]`**: checking only the degree of \(b_1\) would be wrong. With bases \(2+i,3,3(2+i)\), the product is exactly the **square of the third base**, while its norm \(2025\) excludes power dependence with either of the first two, of norms \(5\) and \(9\). Thus Step 3 really can have one disqualified index.

WHAT A HUMAN EXPERT SHOULD STILL CHECK: For a standalone certification, independently audit the supplied paper’s two-base main theorem. It is used as a theorem here, not reproved. I found no outstanding issue in the reduction from several bases to two.