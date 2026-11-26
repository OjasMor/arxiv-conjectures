# arXiv:2611.32519 [conj:harm]

status: completed cost: $0.4859 incomplete: None

TARGET: \label{conj:harm}
Let $k\geq 3$. Then
    $\dfrac{n^k}{\displaystyle{\frac{1}{F_1^{k}}+\frac{1}{F_2^{k}}+\cdots+\frac{1}{F_n^{k}}}} \in \mathbb{N}$ if and only if  $n=1,2$.

---

VERDICT: PROVED

STATEMENT: “Let \(k\geq 3\). Then \(\dfrac{n^k}{\displaystyle{\frac{1}{F_1^{k}}+\frac{1}{F_2^{k}}+\cdots+\frac{1}{F_n^{k}}}} \in \mathbb{N}\) if and only if \(n=1,2\).”

DEGENERATE: no — the proof covers all positive integers \(n\) and all integers \(k\ge 3\), as in the paper.

CERTIFICATE: Not applicable (proof).

ARGUMENT: Write \(S_{n,k}=\sum_{i=1}^n F_i^{-k}\) and \(H_{n,k}=n^k/S_{n,k}\). As a check on the indexing, exact Python arithmetic with \(F_1=F_2=1\) reproduced the paper’s values \(H_{3,1}=6/5\), \(H_{4,1}=24/17\), \(H_{3,2}=4\), and \(H_{4,2}=576/85\). An exact search found no integral \(H_{n,k}\) for \(3\le n\le40\) and \(3\le k\le100\). The proof does not rely on this search.

Write \(S_{n,k}=U/V\) in lowest terms. If \(H_{n,k}=n^kV/U\) is an integer, then \(U\mid n^k\). Thus, for \(n\ge2\), it suffices to show \(V\ge n^k\): then \(U=S_{n,k}V>n^k\), since \(S_{n,k}>1\).

The key observation is that **if \(F_r\) is coprime to every other \(F_i\) with \(1\le i\le n\), then \(F_r^k\mid V\)**. Indeed, write the sum omitting index \(r\) as \(A/B\) in lowest terms. Then \(\gcd(B,F_r)=1\), and
\[
S_{n,k}=\frac{AF_r^k+B}{BF_r^k}.
\]
The numerator is coprime to \(F_r\), so none of the factor \(F_r^k\) cancels.

**For \(n\ge7\)**, let \(p\) be the largest prime at most \(n\). By Bertrand’s postulate, \(p>n/2\), and \(p\ge7\). Hence \(p\) is the only multiple of \(p\) among the indices \(1,\ldots,n\). By the Fibonacci identity \(\gcd(F_p,F_i)=F_{\gcd(p,i)}\), every \(i\ne p\) in that range satisfies \(\gcd(F_p,F_i)=F_1=1\). Moreover,
\[
F_p\ge 2p-1\ge n:
\]
the first inequality holds for every index \(p\ge7\), since \(F_7=13\) and \(F_{j+1}-F_j=F_{j-1}\ge2\) for \(j\ge7\). The observation therefore gives \(V\ge F_p^k\ge n^k\), ruling out integrality.

**For \(4\le n\le6\)**, the same observation suffices. At \(n=4\), the terms \(F_3=2\) and \(F_4=3\) are each coprime to all the others, so \(6^k\mid V\). At \(n=5,6\), use \(F_4=3\) and \(F_5=5\) instead: each is coprime to all the others (including \(F_6=8\) when present), so \(15^k\mid V\). In each case \(V\ge n^k\).

**For \(n=3\)**, the quotient is
\[
H_{3,k}=\frac{6^k}{2^{k+1}+1}.
\]
If this were integral, its odd denominator would have to be a power \(3^a\). Since \(k\ge3\), we have \(3^a=2^{k+1}+1\equiv1\pmod8\), so \(a\) is even. Thus
\[
(3^{a/2}-1)(3^{a/2}+1)=2^{k+1}.
\]
The factors are positive even powers of two differing by \(2\). The smaller divides the larger and hence divides their difference, so the factors must be \(2\) and \(4\). Their product is \(8\), forcing \(k=2\), a contradiction.

Finally, \(H_{1,k}=1\) and \(H_{2,k}=2^{k-1}\) are integers. This proves both directions.

CONFIDENCE: \(>99.99\%\). The principal external ingredients are Bertrand’s postulate and the standard Fibonacci gcd identity recalled in the paper; the denominator noncancellation is explicit above.