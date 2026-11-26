# Referee report for 2611.32519__1

status: completed cost: $0.5506

REFEREE VERDICT: CORRECT

STATEMENT MATCH: yes — Conjecture 1.19 (`conj:harm`) states: “Let \(k\geq 3\). Then \(\dfrac{n^k}{\frac{1}{F_1^{k}}+\frac{1}{F_2^{k}}+\cdots+\frac{1}{F_n^{k}}} \in \mathbb{N}\) if and only if \(n=1,2\).”

The paper defines “\(F_0=0,F_1=1,\) and \(F_{n+2}=F_{n+1}+F_n\) for \(n\geq0\)” and specifies “\(\mathbb N=\{1,2,3,\ldots\}\).” Equation `eq:Snk` begins “For integers \(n,k\geq1\), we write \(S_{n,k}=\sum_{i=1}^{n}\frac{1}{F_i^{k}}=\frac{U_{n,k}}{V_{n,k}}\),” where the numerator and denominator are “coprime positive integers.” The claim uses precisely these conventions and proves both directions.

DEGENERATE OR ALREADY KNOWN IN PAPER: no — Theorem 1.18 (`Theorem 11`) proves the harmonic-mean results for \(k=1,2\) only. The paper reports computations for \(k=3,4,5\) through \(n=10^4\) and explains why its \(2\)-adic estimate is insufficient for \(k\geq3\). That limits the method, not the conjecture. The cited Fibonacci gcd identity is an ingredient, not itself the claimed result.

DETAILS: No proof step fails.

1. **Reduced denominator.** Writing \(S_{n,k}=U/V\) in lowest terms gives \(H_{n,k}\in\mathbb N\) exactly when \(U\mid n^k\). For \(n\geq2\), \(S_{n,k}\geq2\), so \(V\geq n^k\) suffices to rule out integrality. If \(F_r\) is coprime to all the other terms’ bases, the reduced denominator \(B\) of the sum omitting \(r\) is coprime to \(F_r\). On adding \(1/F_r^k\), the numerator is \(AF_r^k+B\equiv B\pmod{F_r}\). Thus the entire factor \(F_r^k\) survives reduction, even when \(F_r\) is composite.
2. **\(n\geq7\).** Bertrand’s postulate applied to \(\lfloor n/2\rfloor\) ensures that the largest prime \(p\leq n\) satisfies \(n<2p\); also \(p\geq7\). No other index up to \(n\) is divisible by \(p\), so the paper’s identity “\(\gcd(F_n,F_m)=F_{\gcd(n,m)}\)” gives \(\gcd(F_p,F_i)=1\) for every \(i\ne p\) in the sum. The growth bound starts at equality \(F_7=13\); each subsequent increment is at least \(2\). Hence \(F_p\geq2p-1\geq n\), giving \(V\geq F_p^k\geq n^k\).
3. **\(4\leq n\leq6\).** At \(n=4\), the isolated coprime bases \(2,3\) give \(6^k\mid V\). At \(n=5,6\), the bases \(3,5\) give \(15^k\mid V\); neither shares a factor with \(F_6=8\). Both bounds suffice.
4. **\(n\leq3\).** At \(n=3\), integrality requires the odd number \(2^{k+1}+1\) to divide \(6^k\), hence to equal \(3^a\) with \(a>0\). Reduction modulo \(8\) forces \(a\) even. Then \(3^{a/2}-1\) and \(3^{a/2}+1\) are even integers whose product is a power of two. Both are powers of two, so the smaller divides their difference \(2\). The pair must be \(2,4\), forcing \(k=2\), outside the conjecture. Finally \(H_{1,k}=1\) and \(H_{2,k}=2^{k-1}\), proving the converse.

**Independent Python check.** I generated the Fibonacci numbers from the recurrence and accumulated `s += Fraction(1, F[n]**k)` before computing `n**k / s`. The first two output rows reproduce the paper’s complete small-\(n\) lists:
```text
H(n,1), n=1..5:  1, 1, 6/5, 24/17, 150/91
H(n,2), n=1..5:  1, 2, 4, 576/85, 22500/2161
V(n,3), n=3..7:  8, 216, 27000, 1728000, 3796416000
Integral hits, 3<=n<=40 and 3<=k<=100:  0 of 3724
Integral exponents at n=3, 1<=k<=100:   [2]
```
On the grid \(1\leq n\leq40,\ 1\leq k\leq100\), I also checked the reduced-numerator criterion, divisibility by \(F_r^k\) for every isolated index, and \(V\geq n^k\) for every \(n\geq4\). None failed.

WHAT A HUMAN EXPERT SHOULD STILL CHECK: Literature priority outside the supplied manuscript, if novelty is claimed. No mathematical gap remains in the submitted argument.