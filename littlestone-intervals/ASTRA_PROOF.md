# arXiv:2611.28727 — the conjecture that the closed-form greedy-adversary bound for the randomized Littlestone dimension of intervals is exact

status: completed cost: $0.8285 incomplete: None

VERDICT: PROVED

STATEMENT: For every segment position \(J_S\), the paper’s greedy schedule attains \(\mathrm{RL}(J_S)\). In particular, for every \(m\ge 0\),
\[
\mathrm{RL}(\mathrm{Int}_m)=R(m+1),
\]
where \(R\) is the paper’s closed-form greedy-adversary bound.

ARGUMENT:

Write a position as a vector \(X\) of **piece measures** \(n=g+1\), not block lengths \(g\). We allow entries \(0\) and \(1\) as bookkeeping; both are ignored. Write \(T(n)=\tilde\lambda(n)\) for \(n\ge1\), and let \(F(X)\) be the discounted value of the paper’s greedy schedule. By the exact cutting recursion, it suffices to prove that for every cut \(p=a+b\), \(a,b\ge1\), taking \(X\) to \(Y\),
\[
2F(X)-F(Y)\ \ge\ 1+\tfrac12\bigl(T(a)+T(b)\bigr). \tag{1}
\]

The key is that the greedy value has a halving recurrence for **every vector of pieces**, not just a single rod. The recurrence rounds all pieces down together or up together. When a cut requires different rounding directions for its two children, concavity gives the comparison in the needed direction.

### 1. A counting formula for the greedy value

When greedy cuts \(p\), let \(D\) be the largest power of two at most \(p\). The two children lie in \([D/2,D]\), and at least one is a power of two. Since \(T\) is affine on that interval, the cut reward, before discounting, is
\[
1+\tfrac12\bigl(T(a)+T(b)\bigr)=1+T(p/2)=T(p).
\]
Greedy cuts pieces in nonincreasing order of measure, since it selects a largest piece and both children are smaller.

Fix a power of two \(d\ge1\) and \(1\le r\le d\). The number of greedy cuts of pieces of size at least \(d+r\) descending from one initial piece \(n\), counting the cut of \(n\) itself if applicable, is
\[
C_{d,r}(n)=\max\left(0,\left\lfloor\frac{n-r}{d}\right\rfloor\right). \tag{2}
\]
Indeed, for \(n<d+r\) the count is zero. For \(d+r\le n<2d\), only the root qualifies, since its children are at most \(d\). For \(n\ge2d\), both children \(u,v\) are at least \(d\), and one, say \(u\), is a power of two divisible by \(d\). By induction the count is then
\[
1+\left(\frac ud-1\right)+\left\lfloor\frac{v-r}{d}\right\rfloor
=\left\lfloor\frac{n-r}{d}\right\rfloor.
\]
This proves (2), also for the ignored entries.

Set \(H(s)=1-2^{-s}\). For integer \(p\ge1\), the increments of the interpolated logarithm give
\[
T(p)=\sum_{d=1,2,4,\ldots}\frac1d\sum_{r=1}^d \mathbf 1[p\ge d+r].
\]
For each threshold \(d+r\), the cuts meeting it form an initial segment of the greedy schedule. If there are \(s\) such cuts, their discount weights sum to \(\sum_{i=1}^s2^{-i}=H(s)\). Therefore
\[
F(X)=\sum_{d=1,2,4,\ldots}\frac1d\sum_{r=1}^d
H\left(\sum_{n\in X}C_{d,r}(n)\right). \tag{3}
\]
Only finitely many terms are nonzero.

### 2. Two consequences: halving and a rounding inequality

Let \(X^-\) and \(X^+\) be obtained by replacing every \(n\) by \(\lfloor n/2\rfloor\) and \(\lceil n/2\rceil\), respectively. Let \(M(X)=\sum_{n\in X}(n-1)_+\), the number of cuts remaining.

The \(d=1\) term in (3) is \(H(M(X))\). For \(d=2e\), formula (2) gives
\[
C_{2e,2s}(n)=C_{e,s}(\lfloor n/2\rfloor),\qquad
C_{2e,2s-1}(n)=C_{e,s}(\lceil n/2\rceil).
\]
Grouping even and odd \(r\) in (3) thus proves the vector recurrence
\[
F(X)=H(M(X))+\tfrac12\bigl(F(X^-)+F(X^+)\bigr). \tag{4}
\]

Now suppose \(Z_1,Z_2\) are two roundings of a vector \(Z\): in each coordinate they receive its lower and upper half, in either order. Then
\[
F(Z_1)+F(Z_2)\ \ge\ F(Z^-)+F(Z^+). \tag{5}
\]
To see this, fix \(d,r\) in (3), and let \(A,B\) be the sums of \(C_{d,r}\) on \(Z^-,Z^+\), respectively. By monotonicity of \(C_{d,r}\), the corresponding sums on \(Z_1,Z_2\) both lie in \([A,B]\); together they sum to \(A+B\). By concavity of \(H\), their two \(H\)-values sum to at least \(H(A)+H(B)\). Summing proves (5).

### 3. Proof of the cut inequality

For this step only, set \(T(0)=-2\). This is not a dimension; it makes the identity
\[
T(n)=1+\tfrac12\bigl(T(\lfloor n/2\rfloor)+T(\lceil n/2\rceil)\bigr) \tag{6}
\]
valid also at \(n=1\). For \(n\ge2\), (6) follows from dyadic scaling and linear interpolation.

With this convention, (1) holds for a *formal* split \(p=0+p\), \(p\ge1\). In fact \(F(Y)=F(X)\), and the right side of (1) is \(T(p)/2\). If \(p\ge2\), the first greedy cut alone earns at least \(T(p)/2\), since it cuts a largest piece; if \(p=1\), the required bound is zero.

We now prove (1) for genuine cuts by induction on \(M=M(X)\), with \(M=0\) vacuous. Fix \(p=a+b\) in \(X\), giving \(Y\). Construct two rounded cuts
\[
p_\sigma=a_\sigma+b_\sigma,\qquad \sigma\in\{-,+\},
\]
where \(p_-=\lfloor p/2\rfloor\), \(p_+=\lceil p/2\rceil\), and each child gets its lower and upper half once. If \(a,b\) are not both odd, round both down in the minus cut and up in the plus cut. If both are odd, round \(a\) down and \(b\) up in the minus cut, and reverse the choices in the plus cut. These choices give the asserted sums in both cases.

Perform these cuts in \(X^-,X^+\), calling the resulting vectors \(\widehat Y_-,\widehat Y_+\). Each genuine rounded cut satisfies (1) by induction: the selected piece \(p\ge2\) has strictly decreased in measure, and no other piece has grown, so both coarse positions have fewer than \(M\) cuts remaining. A rounded cut with a zero child satisfies the formal-split bound above. Hence
\[
2F(X^\sigma)-F(\widehat Y_\sigma)
\ \ge\ 1+\tfrac12\bigl(T(a_\sigma)+T(b_\sigma)\bigr). \tag{7}
\]

The vectors \(\widehat Y_-,\widehat Y_+\) are complementary roundings of \(Y\) in the sense of (5). Also \(M(Y)=M-1\), and \(2H(M)-H(M-1)=1\). Applying (4), then (5), gives
\[
\begin{aligned}
2F(X)-F(Y)
&=1+\tfrac12\sum_{\sigma\in\{-,+\}}
       \bigl(2F(X^\sigma)-F(Y^\sigma)\bigr)\\
&\ge 1+\tfrac12\sum_{\sigma\in\{-,+\}}
       \bigl(2F(X^\sigma)-F(\widehat Y_\sigma)\bigr).
\end{aligned}
\]
By (7) and (6), the average in the last line is at least
\[
1+\tfrac12\bigl((T(a)-1)+(T(b)-1)\bigr)
=\tfrac12\bigl(T(a)+T(b)\bigr).
\]
This proves (1).

Thus \(F\) is a supersolution of the exact cutting recursion. It vanishes on terminal positions, so induction on the number of remaining cuts gives \(\mathrm{RL}(J_S)\le F(X)\). The reverse inequality holds because greedy is a feasible schedule. For a single piece \(n\), (4) has initial value \(F((1))=0\) and toll \(H(n-1)=1-2^{1-n}\), exactly the defining recurrence of \(R(n)\). Taking \(n=m+1\) proves the claimed closed form.

**Computational check.** I also ran the exact cutting DP against greedy on all **14,882** nonempty multisets of pieces of measure at least \(2\) and total measure at most \(35\), with **0 mismatches**. For every single rod \(2\le n\le128\), I tested every unordered first cut followed by greedy: **4,096 cuts, 0 improvements**. These checks used integer-scaled dyadic rewards and are independent of the induction.

CONFIDENCE: 99.9%. The most delicate step is the direction of (5) when both children of a cut are odd: synchronized rounding minimizes the sum of the two greedy values. Formula (3) establishes that direction term by term by concavity.