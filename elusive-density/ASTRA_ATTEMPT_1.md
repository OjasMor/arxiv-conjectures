# arXiv:2611.21894 [que:elusive_density]

status: completed cost: $1.7364 incomplete: None

TARGET: \label{que:elusive_density}
Does the set 
\[
\{ n \in \Nat \mid \text{there exists an elusive group of degree $n$} \}
\] 
have density zero in $\Nat$?

---

VERDICT: PROVED

STATEMENT: “Does the set \(\{ n \in \mathbb N \mid \text{there exists an elusive group of degree }n\}\) have density zero in \(\mathbb N\)?” **Yes**, for natural density.

DEGENERATE: no. The argument concerns faithful transitive permutation groups of degree \(n>1\), with no graph or primitivity assumption.

CERTIFICATE: not applicable.

ARGUMENT:

The key is to find a **set of primes** dividing a typical degree \(n\) such that every transitive group of degree \(n\) has a derangement of order one of those primes. Using a set rather than a prescribed prime allows induction on the orbits of a minimal normal subgroup. The induction only has to lift a prime-order element when the kernel is coprime to its order.

**Computational checks.** I first tested the paper’s \(\operatorname{AGL}_1(p^2)/\operatorname{AGL}_1(p)\) example in Python. The points are the affine \(\mathbb F_p\)-lines in \(\mathbb F_{p^2}\): the stabilizer of the line \(\mathbb F_p\) is exactly \(\operatorname{AGL}_1(p)\). Enumerating the maps \(z\mapsto az+b\) and testing whether they preserve any line gave:

| \(p\) | degree | number of derangements | prime orders among derangements |
|---:|---:|---:|:---|
| 3 | 12 | 54 | none |
| 5 | 30 | 500 | 3 |
| 7 | 56 | 2058 | none |

In this family a map is a derangement exactly when \(a\notin\mathbb F_p^\times\): such a multiplier preserves no line direction, whereas a scalar affine map preserves a line. Thus for odd \(p\) the prime-order test is exactly whether \(p+1\) has an odd prime divisor. Scanning odd primes below \(10^6\) gave elusive examples at \(p=3,7,31,127,8191,131071,524287\). I also checked the covering calculation in the degree-\(225\) example: among the \(81\) and \(625\) sum-zero vectors for \(p=3,5\), respectively, none lacked the required two disjoint pairs. These checks are not used in the density proof.

### 1. A sufficient condition on the degree

Let \(\mathcal D\) be the set of degrees \(d\ge 7\) admitting a **primitive nonabelian simple** permutation group other than \(\operatorname{Alt}(d)\).

Suppose \(y\ge 7\) and \(n=ab\) satisfies:

1. \(b>1\) is square-free, and every prime dividing \(b\) exceeds both \(a\) and \(y\).
2. For distinct primes \(r,s\mid b\), one has \(r\nmid s-1\).
3. No divisor \(d>y\) of \(n\) belongs to \(\mathcal D\).

**Claim.** For every \(m\mid n\) with \(\gcd(m,b)>1\), every transitive permutation group of degree \(m\) has a derangement of prime order dividing \(\gcd(m,b)\).

We induct on \(m\). Take such a group \(G\), a minimal nontrivial normal subgroup \(N\), and let \(c\) be the size of an \(N\)-orbit. The orbits all have the same size, and \(c>1\) by faithfulness. Write \(K\) for the kernel of the action on the \(m/c\) orbits.

We will use the following lifting fact: if the orbit action has a derangement of prime order \(r\nmid |K|\), then so does \(G\). Indeed, the preimage of its cyclic subgroup has order \(r|K|\), so by Cauchy’s theorem it has an element of order \(r\). Its image generates the cyclic subgroup, and hence fixes no orbit.

If \(\gcd(c,b)=1\), then \(c\mid a\). Since \(K\) embeds in a direct product of symmetric groups of degree \(c\), no prime dividing \(b\) divides \(|K|\). Induction on the orbit action and the lifting fact prove the claim.

Now fix a prime \(p\mid\gcd(c,b)\).

* **\(N\) abelian.** A minimal abelian normal subgroup is elementary abelian, so \(c\) is a power of \(p\). Since \(p\) occurs only once in \(n\), we have \(c=p\). On each orbit \(N\) induces a regular cyclic group of order \(p\). The group induced there by \(K\) normalizes this cyclic group, so its order divides \(p(p-1)\). Consequently every prime divisor of \(|K|\) divides \(p(p-1)\).

  If \(\gcd(m/p,b)>1\), induction gives a derangement on the orbits of prime order \(r\mid\gcd(m/p,b)\). Here \(r\ne p\), and condition 2 gives \(r\nmid p-1\), so the lifting fact applies. Otherwise \(m/p\mid a\), so there are at most \(a<p\) orbits. In \(N\) the kernel on each orbit has index \(p\). Fewer than \(p\) such kernels cannot cover \(N\), by counting. An element outside their union has order \(p\) and acts nontrivially, hence fixed-point-freely, on every orbit.

* **\(N\) nonabelian.** Write \(N=T^k\) for a nonabelian simple group \(T\), and put \(U=N_\omega\) for one point \(\omega\). We have \([N:U]=c\), so \(p\mid |T|\). Every proper subgroup of \(T\) has index at least \(p\): its coset action is faithful, and a symmetric group of degree less than \(p\) has order coprime to \(p\).

  Suppose first that some coordinate projection of \(U\) is proper in \(T\). Contain that projection in a maximal subgroup \(M<T\), and put \(d=[T:M]\). Then \(d\mid c\) and \(d\ge p>y\). The action of \(T\) on \(T/M\) is primitive, so condition 3 says its image is \(\operatorname{Alt}(d)\). Identify \(T\) with \(\operatorname{Alt}(d)\) this way, making \(M\) a point stabilizer. Since \(d\mid n\) and \(d>a\), some prime \(s\mid b\) divides \(d\). In particular \(s\) is odd. Take \(t\in T\) to be a product of \(d/s\) disjoint \(s\)-cycles.

  The element \((t,\ldots,t)\in N\) is a derangement. To see this, the \(N\)-stabilizers of points are the \(G\)-conjugates of \(U\). Conjugation permutes the simple factors and applies isomorphisms on them, so every such stabilizer has a coordinate projection contained in an automorphic image of \(M\). Since \(d\ge7\), all automorphisms of \(\operatorname{Alt}(d)\) come from \(\operatorname{Sym}(d)\); thus all these images of \(M\) are point stabilizers in the natural action. None contains \(t\). This gives the required order \(s\).

  Finally, suppose all coordinate projections of \(U\) are surjective. Then \(|U|\) is a power of \(|T|\): project away the last coordinate and induct on \(k\), noting that the kernel in the last factor is normal in \(T\) by surjectivity, hence is \(1\) or \(T\). Since \(U<N\), this implies \(|T|\mid c\). In particular **every** maximal subgroup index of \(T\) divides \(n\) and is at least \(p>y\). Taking one such index \(d\), condition 3 again identifies \(T\) with \(\operatorname{Alt}(d)\). But this same group acts faithfully and primitively on the two-element subsets of its natural \(d\)-point set, of degree \(e=\binom d2>d\). Now \(e\mid |T|\mid n\), and the image is too small to be \(\operatorname{Alt}(e)\). Thus \(e\in\mathcal D\), contradicting condition 3.

This proves the claim. In particular, \(n\) is not an elusive degree whenever conditions 1–3 hold.

### 2. Large exceptional simple degrees rarely divide an integer

We prove that for each **fixed** \(0<\theta<1\),
\[
\#\{n\le x:\text{ some }d\mid n,\ d>x^\theta,\ d\in\mathcal D\}=o_\theta(x).
\tag{1}
\]

Two classical classification results are useful here:

* By the primitive-degrees theorem of Cameron, Neumann and Teague, *On the degrees of primitive permutation groups* (1982), the number of degrees up to \(u\) admitting a primitive group not containing the alternating group is asymptotic to \(2u/\log u\). Primes and primes-plus-one already account for this asymptotic: use a cyclic group in prime degree and \(\operatorname{PSL}_2(q)\) in degree \(q+1\) for large primes \(q\). Consequently the degrees outside these two sets contribute \(o(u/\log u)\).
* By Guralnick’s classification, *Subgroups of prime power index in a simple group* (1983), the prime degrees in \(\mathcal D\), apart from finitely many exceptions, have the form \((q^j-1)/(q-1)\) with \(q\) a prime power and \(j\ge2\). For \(j=2\), primality forces \(q\) to be a power of two. For \(j\ge3\) and degree at most \(u\), we have \(q\le\sqrt u\) and \(j\le 1+\log_2 u\). These contribute only \(O(\sqrt u\log u)\) degrees.

It follows that after removing primes-plus-one, the counting function of \(\mathcal D\) is \(o(u/\log u)\). By partial summation, the sum of reciprocals of these remaining degrees between \(x^\theta\) and \(x\) is \(o_\theta(1)\), since \(\int_{x^\theta}^x dt/(t\log t)=\log(1/\theta)\). Counting their multiples proves this part of (1).

For **primes-plus-one**, summing reciprocals alone does not suffice. Here is the needed argument. Fix a large \(w\), let \(L=\sum_{\ell\le w,\ \ell\ {\rm prime}}1/\ell\), and write \(\omega_w(k)\), \(\Omega_w(k)\) for the number of prime factors at most \(w\) of \(k\), counted without and with multiplicity, respectively.

For integers \(k\), the limiting mean of \(\omega_w(k)\) is \(L\) and the limiting variance is at most \(L\), by the Chinese remainder theorem. For \(q\) ranging over primes, the corresponding mean for \(\omega_w(q+1)\) is \(\sum_{\ell\le w}1/(\ell-1)=L+O(1)\), and the variance is at most this mean: by the prime number theorem in fixed arithmetic progressions the residue is uniform on the reduced classes modulo \(\prod_{\ell\le w}\ell\), whose coordinates are independent. Thus the limiting fraction with count below \(0.8L\) is \(O(1/L)\) in either population. Also the mean of \(\Omega_w(k)-\omega_w(k)\) over integers up to \(x\) is bounded by \(\sum_\ell\sum_{j\ge2}\ell^{-j}=O(1)\). Consequently the upper limiting fraction of integers with \(\Omega_w(k)>1.5L\) is \(O(1/L)\), by Chebyshev’s and Markov’s inequalities.

Consider \(n=(q+1)k\le x\) with \(q\) prime and \(q+1>x^\theta\). If both \(\omega_w(q+1)\) and \(\omega_w(k)\) are at least \(0.8L\), then \(\Omega_w(n)\ge1.6L\), so such \(n\) form an upper limiting fraction \(O(1/L)\). For the other cases:

* The sum of \(1/(q+1)\) over the indicated \(q\) with \(\omega_w(q+1)<0.8L\) is \(O_\theta(1/L)+o_{\theta,w}(1)\), by partial summation from their limiting fraction among primes.
* For the case \(\omega_w(k)<0.8L\), choose \(M=M(w)\) large enough that the fraction of such \(k\) up to any \(X\ge M\) is \(O(1/L)\). Sum over \(q\) with \(x/(q+1)\ge M\), using \(\sum_{x^\theta<q+1\le x}1/(q+1)=O_\theta(1)\). The remaining pairs have \(k\le M\), and there are \(O_M(\pi(x))=o_M(x)\) of them.

Taking \(x\to\infty\) and then \(w\to\infty\) proves that these shifted-prime divisors also contribute \(o_\theta(x)\) integers. This proves (1).

### 3. The factorization and the density bound

Set \(y=x^\theta\). Except for \(o_\theta(x)\) integers \(n\le x\), no prime \(p>y\) has \(p^2\mid n\), by the bound \(x\sum_{p>y}p^{-2}\). Also, except for \(o_\theta(x)\) integers, there are no distinct primes \(p,q\mid n\) with \(p>y\) and \(p\mid q-1\): writing \(q=hp+1\), the count is at most
\[
x\sum_{p>y}\frac1p\sum_{h\le x/p}\frac1{hp+1}
=O\!\left(\frac{x\log x}{y}\right).
\tag{2}
\]

It remains to get a split with all primes of \(b\) greater than \(a\) and \(y\). Use Saias’s dense-divisors bound (*Entiers à diviseurs denses I*, 1997): uniformly for \(2\le y\le x\), the number of \(n\le x\) whose consecutive divisors have ratios all at most \(y\) is
\[
O\!\left(x\frac{\log y}{\log x}\right),
\]
with an absolute implied constant.

Indeed, list the prime factors of \(n\) with multiplicity in increasing order. If every next prime \(p\) satisfies \(p\le ya\), where \(a\) is the product of the preceding primes, then \(n\) has consecutive divisor ratios at most \(y\). To check this, inductively the intervals \([d,yd]\) for divisors of the prefix product \(a\) cover \([1,ya]\); their \(p\)-multiples cover \([p,yap]\), and these intervals of coverage meet. Therefore, outside the set counted by Saias, there is a next prime \(p>ya\). Split just before it. This gives \(n=ab\), \(b>1\), with every prime of \(b\) greater than both \(a\) and \(y\).

Now discard the \(o_\theta(x)\) exceptions from (1), (2), and the prime-square bound. Every integer with the split just obtained satisfies conditions 1–3 and hence is not an elusive degree. Writing \(E\) for the set in the question, we have proved
\[
\limsup_{x\to\infty}\frac{|E\cap[1,x]|}{x}\le C\theta
\]
for an absolute \(C\). Letting \(\theta\downarrow0\) proves natural density zero.

CONFIDENCE: 0.98. The most delicate step is (1): sparsity of primitive degrees does **not** by itself imply sparsity of their multiples. The separate shifted-prime argument and the use of the cutoff \(x^\theta\) before sending \(\theta\) to zero are essential.