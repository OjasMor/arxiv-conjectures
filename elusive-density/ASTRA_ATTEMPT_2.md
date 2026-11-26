# arXiv:2611.21894 [que:elusive_density]

status: completed cost: $1.7961 incomplete: None

TARGET: \label{que:elusive_density}
Does the set 
\[
\{ n \in \Nat \mid \text{there exists an elusive group of degree $n$} \}
\] 
have density zero in $\Nat$?

---

VERDICT: PROVED

STATEMENT: “Does the set \(\{n\in\mathbb N\mid \text{there exists an elusive group of degree }n\}\) have density zero in \(\mathbb N\)?” **Yes**, for natural density.

DEGENERATE: no — the argument concerns faithful transitive permutation groups of degree \(n>1\), as in the paper.

CERTIFICATE: Not applicable; this is a density proof.

ARGUMENT:

I used a **gap in the prime factors of the degree**, together with the Cameron–Neumann–Teague theorem on degrees of primitive groups. The role of the gap is to identify several primes at once such that, as one passes through systems of blocks, either a derangement of one of those prime orders can be constructed, or one can pass to a smaller degree without losing the ability to lift it.

**Computational checks.** I first tested the paper’s \(\mathrm{AGL}_1(p^2)\) example by acting on the affine lines of \(\mathbb F_p^2\): these form a transitive set and the stabiliser of the subfield line is \(\mathrm{AGL}_1(p)\). Enumerating the permutations in Python gave degree \(12\) for \(p=3\), with exactly \(18\) derangements of order \(4\) and \(36\) of order \(8\), and no others. For \(p=7\) I got degree \(56\) and no prime-order derangements; for \(p=5\), which is not Mersenne, I got degree \(30\) and \(50\) derangements of order \(3\).

I also tested the subfield actions \(\mathrm{AGL}_1(t^f)/\mathrm{AGL}_1(t)\) for prime powers \(t\le 20000\) and \(2\le f\le4\). Here all nonidentity translations are conjugate, and every nontranslation is conjugate to its scalar part, whose multiplier is conjugacy-invariant. Thus the test is whether every prime factor of \(t^f-1\) divides \(t-1\). The action is faithful: its kernel intersects the translations trivially, so centralises them and is itself trivial. Of the \(6984\) parameter pairs, the ones passing the test gave \((t,f,\text{degree})\)
\[
(3,2,12),\ (7,2,56),\ (31,2,992),\ (127,2,16256),\ (8191,2,67100672).
\]
None of the computations is needed for the proof.

### 1. A sufficient condition on a degree

Suppose that
\[
n=a\prod_{r\in R}r,
\]
where \(R\) is a nonempty set of primes, \(\min R>\max(a,6)\), and \(r\nmid s-1\) for distinct \(r,s\in R\). In particular, each \(r\in R\) occurs just once in \(n\). Impose the following further condition:

* For each divisor \(d\mid n\) divisible by some member of \(R\), every primitive group of degree \(d\) contains \(A_d\), with the allowed exception of subgroups of \(\mathrm{AGL}_1(d)\) in prime degree \(d\) (up to relabelling).

**Claim.** Every transitive group of degree \(n\) has a derangement of order in \(R\).

In fact, we prove this for every divisor \(D\mid n\) divisible by a member of \(R\), by induction on \(D\). Take a transitive \(G\) of degree \(D\). Choose a block of smallest size \(d>1\), allowing the whole point set as a block. Its translates give a system of \(m=D/d\) blocks. The set stabiliser of a block induces a primitive group on it: a smaller nontrivial block for this induced group would also be a block for \(G\). Write \(K\) for the kernel of the action on the \(m\) blocks.

We use the following lifting fact: if the group on blocks has a derangement of prime order \(s\) and \(s\nmid |K|\), then \(G\) has a derangement of order \(s\). Indeed, for a lift \(g\), the order \(v\) of \(g^s\in K\) is coprime to \(s\), so \(g^v\) has order \(s\) and still moves every block.

* If \(d\) has no prime factor in \(R\), then \(d\mid a\), and \(K\) embeds in \(S_d^m\). Its order is therefore coprime to every member of \(R\). Since \(m\) still has a prime factor in \(R\), induction and lifting apply.
* If \(K=1\), we can again use induction when \(m\) has a prime factor in \(R\). Otherwise \(m\le a\) and \(G\) embeds in \(S_m\), which is impossible: a prime \(r\in R\) dividing \(D\) must divide \(|G|\), but \(r>m\).

We are left with \(K\ne1\) and \(r\mid d\) for some \(r\in R\).

First suppose the local primitive group contains \(A_d\). The images of \(K\) on the blocks are nontrivial, by transitivity on blocks and faithfulness, and normal in the respective local groups. Since \(d\ge7\), each image contains \(A_d\). Consequently the commutator subgroup \(K'\) is a subdirect subgroup of \(A_d^m\): every projection is exactly \(A_d\).

Recall why such a subdirect subgroup is a direct product of diagonal copies of \(A_d\), with possible automorphisms on its coordinates. Project away the last coordinate and use induction. The kernel in the last coordinate is normal in \(A_d\), hence is either \(A_d\) or trivial. In the first case the last factor splits off; in the second case the last coordinate is a surjective homomorphism from the preceding product of simple factors to \(A_d\), so it is an isomorphism on one factor and kills the others. This proves the description.

Now \(A_d\) contains a product of \(d/r\) disjoint \(r\)-cycles, since \(r\) is odd. Every automorphism of \(A_d\) for \(d\ge7\) is induced by \(S_d\), so preserves the property of having this cycle type. Choosing such an element in **each** diagonal factor gives an element of \(K'\) of order \(r\) that is fixed-point-free on **every** block.

The remaining possibility is \(d=r\) with affine local group. Here \(|K|\) divides \((r(r-1))^m\). If \(m\) has a prime factor in \(R\), induction gives a derangement on blocks of some order \(s\in R\) dividing \(m\). Then \(s\ne r\) by squarefreeness at \(r\), and \(s\nmid r-1\) by hypothesis, so the derangement lifts.

Finally, if \(m\) has no prime factor in \(R\), then \(m\le a<r\) and \(D=mr<r^2\). A Sylow \(r\)-subgroup \(P\) of \(G\) cannot have a common fixed point, because every point stabiliser has index divisible by \(r\). Its orbits therefore all have length \(r\). On each of the \(m\) orbits its image is cyclic of order \(r\), acting regularly. The \(m<r\) kernels of these actions, each of index \(r\) in \(P\), cannot cover \(P\). An element outside their union has order \(r\) and moves every point. This completes the induction.

### 2. Primitive groups on large divisors of a typical integer

Fix \(0<\delta<1\). I claim that, for all but \(o(x)\) integers \(n\le x\), **every divisor \(d>x^\delta\) of \(n\)** satisfies the primitive-group condition in part 1.

Here we use the quantitative Cameron–Neumann–Teague theorem (*On the degrees of primitive permutation groups*, Math. Z. **180** (1982), 141–149). In the form needed here, the number of degrees \(d\le t\) admitting a primitive group not containing \(A_d\) is
\[
(2+o(1))\frac{t}{\log t}.
\]
All sufficiently large primes \(p\) and all \(p+1\) for sufficiently large primes \(p\) are such degrees, by the regular cyclic action and the projective-line action, respectively. These two sets are disjoint apart from a finite exception. By the prime number theorem, the set \(E\) of **remaining** such degrees has counting function \(o(t/\log t)\). Thus for fixed \(\delta\), partial summation gives
\[
\sum_{\substack{x^\delta<d\le x\\d\in E}}\frac1d=o(1),
\]
since \(\int_{x^\delta}^x dt/(t\log t)=\log(1/\delta)\). Hence only \(o(x)\) integers under consideration have a divisor in this range belonging to \(E\).

For **prime** degrees we use the classification of primitive groups with a regular cyclic subgroup (G. A. Jones, *Cyclic regular subgroups of primitive permutation groups*, J. Group Theory **5** (2002), 403–407). It applies since a transitive group of prime degree \(d\) contains a \(d\)-cycle. Apart from finitely many exceptions, a group in prime degree neither containing \(A_d\) nor contained in \(\mathrm{AGL}_1(d)\) requires
\[
d=(q^k-1)/(q-1)
\]
for a prime power \(q\) and \(k\ge2\). For \(k=2\), primality forces \(q\) even, so there are \(O(\log t)\) choices up to \(t\). For \(k\ge3\), we have \(q\le\sqrt t\) and \(k\le1+\log_2 t\). These exceptional primes thus have counting function \(O(\sqrt t\log t)\), more than sufficient for the same reciprocal-sum argument.

It remains to handle **shifted primes**. Their reciprocal sum in the range in question does *not* tend to zero. Instead, we show
\[
\#\{n\le x:\ p+1\mid n\text{ for some prime }p,\ x^\delta<p+1\le x\}=o(x). \tag{1}
\]
Here is a proof to make the divisor-density step explicit. Fix \(w\), put \(Q=\prod_{\ell\le w,\ \ell\ {\rm prime}}\ell\), and let \(F(n)\) count the distinct prime divisors of \(n\) dividing \(Q\). Put \(M=\sum_{\ell\mid Q}1/\ell\). For uniform \(n\le x\), the limiting mean of \(F\) is \(M\) and its limiting variance is at most \(M\), by uniformity modulo \(Q\). The limiting proportion with \(F(n)>3M/2\) is at most \(4/M\).

Now count incidences \(n=k(p+1)\le x\) with \(p+1>x^\delta\), giving each incidence weight \(1/x\). For fixed residues \(p\equiv h\bmod Q,\ k\equiv j\bmod Q\), with \(h\) a unit, the total weight tends to
\[
\frac{\log(1/\delta)}{\varphi(Q)Q}.
\]
Indeed, the count of \(k\)'s per prime is \(x/((p+1)Q)+O(1)\), the total floor error is \(o(x)\), and the prime number theorem in fixed arithmetic progressions gives the limit by partial summation. Thus the limiting distribution for incidences, after normalisation, is uniform on the independent residues \(h\in(\mathbb Z/Q)^\times,\ j\in\mathbb Z/Q\). For each \(\ell\mid Q\) the probability that \(\ell\mid j(h+1)\) is
\[
\frac1\ell+\left(1-\frac1\ell\right)\frac1{\ell-1}=\frac2\ell,
\]
independently across \(\ell\). Hence the incidence distribution of \(F\) has mean \(2M\) and variance at most \(2M\). Its proportion with \(F\le3M/2\) is at most \(8/M\). Counting integers by the ordinary bound when \(F>3M/2\) and by incidences otherwise gives a limsup in (1), after division by \(x\), of at most
\[
\frac{4+8\log(1/\delta)}{M}.
\]
Let \(w\to\infty\). This proves (1), and finishes the claim about all divisors \(d>x^\delta\).

### 3. Finding the gap

We show that for each \(\epsilon>0\) one can choose a **fixed** \(\delta>0\) such that, apart from at most \((\epsilon+o(1))x\) integers \(n\le x\), there is a factorisation as in part 1 with \(\min R>x^\delta\).

Use uniform \(n\in\{1,\ldots,x\}\) for integral \(x\). Write \(a_y=\prod_{p\le y}p^{v_p(n)}\). We first need the uniform bound, for \(y\) large,
\[
\Pr(a_y>y^u)\le C e^{-u}. \tag{2}
\]
In fact for \(t=1/\log y\),
\[
\mathbb E[a_y^t]\le
\prod_{p\le y}\left(1+\frac{p^t-1}{p(1-p^{t-1})}\right)=O(1).
\]
The inequality follows by expanding \(p^{t v_p(n)}\) using the nonnegative increments \(p^{kt}-p^{(k-1)t}\) on multiples of \(p^k\), and bounding the probability of divisibility by \(h\) by \(1/h\). The product bound follows from \(p^t-1\ll t\log p\) for \(p\le y\) and \(\sum_{p\le y}(\log p)/p=O(\log y)\). Markov's inequality proves (2).

Take a large integer \(u\) and \(J=u^2\). Try the \(J\) disjoint intervals of primes
\[
(y_j,y_j^u],\qquad y_j=x^{\delta u^j},\qquad 0\le j<J.
\]
For sufficiently small fixed \(\delta>0\), the limsup probability that **every** interval contains a divisor prime of \(n\) is at most
\[
(1-1/u)^J+1/u. \tag{3}
\]
To verify this, for any subset \(S\) of the intervals consider the event that none of the primes in their union divides \(n\). In the independent model assigning probability \(1/p\) to divisibility by \(p\), its probability tends to \(u^{-|S|}\) by Mertens' theorem. For the actual probability, apply the Bonferroni bounds at orders \(K-1,K\). Up through order \(K\), the actual sums differ from the independent sums by \(o(1)\) if \(K\delta u^J<1\): there is an error of at most \(1/x\) per product of distinct primes, and at most \(O(x^{K\delta u^J})\) terms. The width of the bounds in the independent model is at most
\[
\frac{(J\log u+1)^K}{K!}
\]
for large \(x\), by Mertens' bound on the reciprocal sum of the primes in the union. Choose \(K\) so this is less than \(1/(u2^J)\), then choose \(\delta\) with \(K\delta u^J<1\). Inclusion–exclusion over the \(J\) empty-interval events gives (3).

By (2) the probability that **any** \(a_{y_j}>y_j^u\) is at most \(JC e^{-u}\). Thus, except for a proportion with limsup at most
\[
(1-1/u)^J+1/u+JC e^{-u},
\]
there is an empty interval \((y,y^u]\) with \(a_y\le y^u\). Set \(a=a_y\); every prime dividing \(n/a\) exceeds \(y^u\), hence exceeds \(a\) and \(x^\delta\). We may discard \(n\le x^{\delta u^J}\), only \(o(x)\) integers, so \(n/a>1\).

Two more exceptions cost \(o(x)\) for this fixed \(\delta\). First, the proportion having a squared prime factor \(r^2\) with \(r>x^\delta\) is at most \(\sum_{r>x^\delta}1/r^2=o(1)\). Second, the proportion having distinct prime factors \(r,s>x^\delta\) with \(r\mid s-1\) is at most
\[
\sum_{r>x^\delta}\frac1r\sum_{\substack{s\le x\\s\equiv1\bmod r\\s>1}}\frac1s
\ \ll\ (\log x)\sum_{r>x^\delta}\frac1{r^2}=o(1).
\]
The estimates even allow sums over integers in place of primes. Taking \(R\) to be the prime divisors of \(n/a\) now gives the arithmetic conditions in part 1. Since \(J=u^2\), the displayed limsup bound can be made smaller than \(\epsilon\) by the choice of \(u\).

**Conclusion.** For the fixed \(\delta\) furnished by part 3, every divisor of \(n\) divisible by a member of \(R\) exceeds \(x^\delta\). Part 2 therefore gives the remaining primitive-group condition after discarding only \(o(x)\) more integers. By part 1, none of the resulting degrees admits an elusive group. The upper natural density of degrees admitting one is at most \(\epsilon\) for every \(\epsilon>0\), and hence their natural density is zero.

CONFIDENCE: 0.97. The most delicate step is passing from scarcity of exceptional *primitive degrees* to scarcity of integers having one as a *divisor*. Qualitative density zero for primitive degrees would not suffice. The proof uses the quantitative Cameron–Neumann–Teague theorem, removes shifted primes by the separate incidence estimate (1), and keeps \(\delta\) fixed when taking each \(x\to\infty\) limit.