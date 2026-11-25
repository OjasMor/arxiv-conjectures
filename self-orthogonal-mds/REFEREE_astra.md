# Referee report, gpt-6.2-astra (xhigh)

status: completed  cost: $3.0416  incomplete: None

| Result | Verdict | Reason |
|---|---|---|
| Theorem A | **CORRECT WITH FIXES** | The criterion holds for each individual hyperoval, and the cutoff \(q=16\) is correct. Clarify the singular-conic case and replace the provisional citation. |
| Proposition B | **CORRECT** | The moment calculation and the quadratic obstruction work for every odd prime power, including \(q=3\). |
| Theorem B | **CORRECT WITH FIXES** | The corrected arc classification applies for primes \(p\ge5\). It does not apply at \(p=3\), which has a one-line direct proof. |

### Numbered findings

1. **The actual gap in Theorem B is \(p=3\), not the middle-dimension exception.** When \(k=1\), four generator columns over \(\mathbb F_3\) do not give a four-point arc in \(\mathrm{PG}(0,3)\). Instead, every entry of a generator of an MDS \([4,1]\) code is nonzero, so its self-dot-product is \(4\cdot1=1\) in \(\mathbb F_3\). At \(p=5\), the six columns represent the entire projective line, so the extended-GRS description is immediate. For \(p\ge7\), \(k=(p-1)/2<p\) and \(k\ne(p+1)/2\). Ball’s Theorem 1.8 is quoted accurately **as printed**, but Chowdhury’s Theorem 1.13 explicitly identifies the missing exception; cite the corrected statement. The resulting \(A N D\) factorization, up to column order, is sufficient: Proposition B tests **every** diagonal \(D\), rather than assuming diagonal scaling preserves orthogonality. ([web.mat.upc.edu](https://web.mat.upc.edu/simeon.michael.ball/jems-mds-conj-revised.pdf))

2. **Theorem A’s reduction and regular obstruction are sound.** Three-column independence is precisely the hyperoval condition. The six distinct Gram entries are precisely \(Mw\), where \(w_i=v_i^2\); every nonzero \(w_i\) has the unique square root \(w_i^{q/2}\). Changing representative \(P_i\) to \(\lambda_iP_i\) changes the required \(w_i\) to \(\lambda_i^{-2}w_i\), so existence is independent of representatives. Qualify the draft’s statement about the code itself: an unordered hyperoval determines a monomial-equivalence class, not a particular labeled row space. For a regular hyperoval, evaluating \(y^2+xz\) gives a row-space vector supported **only** at the nucleus, forcing \(w_N=0\) for every kernel vector. This rules out every scaling. ([arxiv.org](https://arxiv.org/abs/1804.06003))

3. **Claim 1 needs “nonsingular,” or an explicit treatment of nonsplit singular conics.** Two rational lines meet the arc in at most four points; two conjugate nonrational lines have only their intersection as a rational point. For a nonsingular conic and \(X\notin\mathcal C\cup\{N\}\), \(XN\) is the unique tangent. The other \(q\) conic points pair on \(q/2\) secants, leaving \(q/2\) external lines. Removing at most two conic points spoils at most two secants. Equivalently, the arc can contain at most \(1+q/2\) conic points if it contains such an \(X\). At \(X=N\) **all** lines are tangents; the draft correctly does not use its secant count there. If the nucleus is the only possible off-conic point, cardinality forces \(H=\mathcal C\cup\{N\}\). The argument works conditionally already at \(q=8\); nonexistence at \(8\) follows because all hyperovals there are regular, not from the counting argument alone. The same classification handles \(4\), where \(4<q-1\) would be false. ([combinatorics.org](https://www.combinatorics.org/ojs/index.php/eljc/article/download/v21i1p14/pdf/))

4. **Claim 2 and Bonferroni are correct.** Claim 1 gives rank six, hence \(\dim K=q-4\). For a **specified** triple \(T\), dependence of its coordinate functionals is equivalent to a nonzero vector in \(K^\perp=\operatorname{row}M\) supported in \(T\): the corresponding quadratic must vanish on the complement of *that* triple. Claim 1 rules this out. Thus each intersection of \(t\le3\) coordinate-zero conditions has probability \(q^{-t}\) for uniform \(w\in K\). Third-order Bonferroni is a **lower** bound for the probability of avoiding them all. Its value simplifies to
   \[
   -\frac2q+\frac{(q+2)(q+1)}{3q^2}
   =\frac{(q-1)(q-2)}{3q^2}>0.
   \]
   No independence of four or more coordinates is assumed.

5. **Proposition B has no power-sum or endpoint error.** The zeroth power sum is \(q=0\) in the field. For positive exponents the sum is \(-1\) at multiples of \(q-1\), zero otherwise. Since \(m+j\le2q-4<2(q-1)\), the \(m\)-th moment is exactly \(-c_{q-1-m}\). This gives the stated vanishing and \(c_2=v_\infty^2\), including at \(q=3\), where the lower range of moments is empty. At \(q=5\) the lower moments are \(m=0,1\) and the final one is \(m=2\). The difference-of-squares count is valid: \((y-s)(y+s)=d\ne0\) gives \(q-1\) ordered solutions, and each successful **nonzero** square uses two of them. A shorter ending is that \(w(X)^{(q-1)/2}-1\) would have degree exactly \(q-1\) and vanish at all \(q\) field elements. ([arxiv.org](https://arxiv.org/abs/1906.00380))

### Independent computation

I implemented multiplication by shifts and XOR with reduction modulo `0b10011` (\(a^4+a+1\)), and evaluated all six determinant terms for every column triple. The displayed matrix gives:

| Check | Result |
|---|---:|
| \(GG^{\mathsf T}\) | \(0_{3\times3}\) |
| Column triples tested | 816 |
| Singular minors | **0** |
| Weights of all \(16^3\) words | \(0:1,\quad16:2295,\quad18:1800\) |

Thus the displayed matrix alone refutes Liu’s Conjecture 1. I also normalized its columns and checked that they match the published Lunelli–Sce \(o\)-polynomial in the stated field representation. I did not verify the unprovided \(q=32,128\) certificate files. [Download the standalone Python verifier](sandbox:/mnt/data/check_hyperoval16.py). ([arxiv.org](https://arxiv.org/html/2611.30048v1))

### Literature findings

- **Existence for every \(h\ge4\): yes.** Cherowitzo, Penttila, Pinneri and Royle, *Flocks and ovals*, **Geom. Dedicata 60** (1996), 17–37, is the correct all-exponent **construction** citation. For **irregularity**, also cite Payne–Penttila–Pinneri, *Isomorphisms between Subiaco \(q\)-clan geometries* (1995), and O’Keefe–Thas, *Collineations of Subiaco and Cherowitzo hyperovals* (1996): their stabilizer results distinguish these from regular hyperovals. The two Subiaco classes when \(h\equiv2\bmod4\) are not an exception to existence. There is also an independent historical route: Segre’s translation examples cover \(h=5\) and \(h\ge7\); Lunelli–Sce cover \(h=4\), and Penttila–Pinneri cover \(h=6\). ([link.springer.com](https://link.springer.com/article/10.1007/BF00150865))
- **Proposition B is an elementary corollary of prior work.** Fang–Liu–Luo, *New MDS Euclidean Self-Orthogonal Codes*, **IEEE Trans. Inform. Theory 67** (2021), 130–137, Lemma 2.3, already give the necessary-and-sufficient multiplier-polynomial criterion. On the full affine field their denominator is \((X^q-X)'=-1\); after normalizing \(v_\infty=1\), their criterion is exactly the monic-quadratic condition above. Thus Theorem B combines existing classification with an elementary specialization. The same reasoning also settles **\(q=9\)**: every 10-arc in \(\mathrm{PG}(3,9)\) is a twisted cubic by Segre. Failure of Ball’s hypothesis for nonprime \(q\) does not imply every such case is open. ([arxiv.org](https://arxiv.org/abs/1906.00380))
- **For Theorem A, the ingredients have precedents, but I did not find the combined criterion.** Heng–Ding give the hyperoval-code correspondence; Wan–Zhu, Lemma 7, give the diagonal-scaling criterion using coordinatewise products; Jin–Xing use full-weight dual words, inclusion–exclusion and square roots for Euclidean self-orthogonal AG codes. Coolsaet–Sticker record the stronger \(q/2+1\) conic-intersection bound underlying Claim 1. None of these results identifies the scalable hyperovals as exactly the irregular ones. ([arxiv.org](https://arxiv.org/abs/1804.06003))
- **Two close search hits do not settle A.** Ezerman–Jitman–Kiah–Ling’s length-\(q+2\) CSS construction proves \(GH^{\mathsf T}=0\) for **two different matrices**, not \(GG^{\mathsf T}=0\). Carlet–Mesnager–Tang–Qi construct \([q+2,3]\) Euclidean **LCD** codes, whose hull has dimension zero, not three. Searching the exact parameters, hyperoval codes, Euclidean hulls, dual-containing/CSS codes, puncture codes and extended-GRS nonexistence, I found no earlier explicit statement of Theorem A or the all-prime Theorem B, and no general resolution of Conjecture 2. That is a search result, not a priority guarantee. ([personal.ntu.edu.sg](https://personal.ntu.edu.sg/hmkiah/docs/papers/aqmds.pdf))