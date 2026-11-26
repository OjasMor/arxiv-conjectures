# arXiv:2611.20344 [q:ratio]

status: completed cost: $1.5742 incomplete: None

TARGET: \label{q:ratio}
Does every cycle satisfy $2^\ell<3^{a+1}$, that is, $a=\floor{\ell\log_32}$? This holds for
cycles with a single run of steps up (\cref{thm:G}(d)), for all cycles of length $\ell\le30$, and
for all $1{,}133{,}265{,}572$ cycles whose elements are all at most $160$; among the latter, the
largest ratio $2^\ell/3^a$ is $2.398$, for $\ell=71$. If the answer is negative, what is the
supremum of $2^\ell/3^a$?

---

VERDICT: DISPROVED

STATEMENT: “Does every cycle satisfy \(2^\ell<3^{a+1}\), that is, \(a=\lfloor\ell\log_32\rfloor\)?” No. “If the answer is negative, what is the supremum of \(2^\ell/3^a\)?” The ratios are unbounded: the supremum is \(+\infty\).

DEGENERATE: no — the certificate is a simple directed cycle of 149 distinct positive integers, with least element \(2\) and largest element \(458\).

CERTIFICATE:
```json
{
  "start": 2,
  "runs_U_first": [12,1,2,1,2,1,2,1,1,1,2,3,1,3,9,1,2,1,1,2,4,4,6,1,2,2,1,1,4,2,3,2,2,2,1,2,2,1,6,1,1,5,6,1,3,2,6,2,3,2,1,1,2,1,1,1,4,1,1,7]
}
```

ARGUMENT:

**Verification of the counterexample.** The entries are lengths of alternating runs \(U,D,U,D,\ldots\). As a calibration, I first enumerated small cycles by depth-first search from their least vertex, using the paper’s bound \(2^\ell/3^a\le(1+1/m)^\ell\) on the least vertex \(m\). For \(\ell=2,5,8,10\), I obtained respectively \(3,12,140,18\) cycles, with largest vertices \(5,26,242,41\), matching the census. For the larger search I used binary edge variables on a finite vertex interval, with equal in- and out-degree at each vertex and degree at most one in each direction, and inspected the resulting cycles.

Here is the independent verifier, taking the certificate as JSON on standard input:

```python
import json, sys
c = json.load(sys.stdin)
x = c["start"]
seen = set()
a = 0
for i, n in enumerate(c["runs_U_first"]):
    for _ in range(n):
        assert x > 0 and x not in seen
        seen.add(x)
        if i % 2 == 0:
            x = (3*x + 1)//2
            a += 1
        else:
            x = (x + 1)//2
assert x == c["start"] == min(seen)
L = len(seen)
print(L, a, max(seen), 2**L > 3**(a+1))
print(2**L, 3**(a+1))
```

Observed output:
```text
149 93 458 True
713623846352979940529142984724747568191373312 706965049015104706497203195837614914543357369
```

Thus \(2^{149}/3^{93}=3.028256548\ldots\). Simplicity is important here: it ensures that taking \(S\) to consist of the up-vertices gives a single map \(T_S\) that follows the entire cycle.

**Proof that the supremum is infinite.** I will show that any finite list of distinct integers congruent to \(7\bmod 12\), of size at least two, can be visited **in the specified order on a simple cycle**. The point of this stronger statement is that the rounding factors contributed by these odd integers alone have unbounded product.

Write \(g=3/2\), \(\alpha=\log_2 g\), and use the paper’s step lemma in the form
\[
U^j(z)=\lfloor K_z g^j\rfloor,\qquad z<K_z<z+1,\qquad K_{U^j(z)}=g^jK_z.
\]
The last equality also follows by taking the limit of \(g^{-n}U^{n+j}(z)\).

First we need a separation estimate:
\[
|K_z-2K_w|\ \gg\ (w+1)^{-7}\qquad(z,w\ge1), \tag{1}
\]
with an absolute implied constant. Indeed, if the left side is \(<g^{-h}\), then, by taking floors,
\[
d_j=U^j(z)-2U^j(w)\in\{-1,0,1,2\}\qquad(0\le j\le h).
\]
With \(e_j=U^j(w)\bmod2\), the exact update is \(d_{j+1}=\lceil3d_j/2\rceil-e_j\). State \(-1\) requires \(e_j=0\) and stays at \(-1\); state \(2\) requires \(e_j=1\) and stays at \(2\). State \(0\) stays there on \(0\) or moves to \(-1\) on \(1\); state \(1\) stays there on \(1\) or moves to \(2\) on \(0\). Thus the first \(h\) parities of the \(U\)-orbit of \(w\) have at most three constant runs. A run starting at \(u\) has length at most \(\log_2(u+1)\): a run of \(k\) evens requires \(2^k\mid u\), and a run of \(k\) odds requires \(2^k\mid(u+1)\). Since \(U^j(w)+1\le 2^j(w+1)\), each run that starts after \(j\) steps ends by step \(2j+\log_2(w+1)\). Three runs therefore give \(h\le 7\log_2(w+1)\). Taking \(h=\lfloor7\log_2(w+1)\rfloor+1\) proves (1).

Call the integers in our finite list *anchors*. Each anchor \(b\) has two paths:
\[
P_b=\{U^j(b):j\ge0\},\qquad H_b=\{2^j(b-1)+1:j\ge0\}.
\]
The first goes out from \(b\) by up-edges; the second leads in to \(b\) by down-edges. The \(P_b\) are disjoint since \(U\) is injective and \(b\equiv1\bmod3\) is not in its image. All vertices of every \(H_b\) are also \(1\bmod3\). The \(H_b\) are disjoint because the \(b-1\) have distinct odd parts (each is exactly twice an odd integer). Thus among these paths the only intersections are \(P_b\cap H_b=\{b\}\).

We now construct a **link** from one anchor \(x\) to the next anchor \(y\). Let \(F\) be the finite set of vertices used in links already constructed. Assume \(P_x\) and \(H_y\) are free of \(F\) except possibly at \(x,y\), respectively. We will avoid \(F\) except at the endpoints. We will also avoid all \(P_b\) with \(b\ne x\) and all \(H_b\) with \(b\ne y\), except at the endpoints. This last requirement preserves the paths needed for subsequent links.

**Choosing the entrance to \(y\).** Let \(m\) be the number of protected up-paths \(P_b\) (\(b\ne x\)), and choose \(2^J>20000(m+1)\). We can take \(v=2^h(y-1)+1\) arbitrarily high on \(H_y\) such that its down-preimage layers
\[
C_k=((v-1)2^k,v2^k]\qquad(k\ge0)
\]
have these properties:

1. All layers avoid \(F\) and all \(H_b\) with \(b\ne y\).
2. The first \(J\) layers, \(0\le k<J\), also avoid all protected \(P_b\).

For the first property take \(v>\max(F\cup\{x,y\})\). Membership of \(2^p(b-1)+1\) in \(C_k\) would require \((b-1)2^{p-k-h}\in[y-1,y-1+2^{-h})\), impossible for large \(h\) since \(b-1\) and \(y-1\) have distinct odd parts. For the second property, membership of \(U^d(b)\) in \(C_k\) requires \(K_bg^d\) to differ from \((y-1)2^{h+k}\) by at most \(2^k+1\). Taking logs to base \(g\), this requires \(h\log_g2\bmod1\) to be within \(O_y(2^{-h})\) of one of finitely many points (indexed by \(b,k<J\)). Since \(\log_g2\) is irrational, arbitrarily large \(h\) stay a fixed positive distance from those points.

Fix such a \(v\ge4\). Each \(C_k\) contains at most one vertex from each protected \(P_b\), because the up-path grows by factors at least \(3/2>v/(v-1)\). So the set \(Z\) of protected up-path vertices in all these layers satisfies
\[
\sum_{z\in Z}\frac1z\ \le\ \frac{2m}{(v-1)2^J}. \tag{2}
\]

**Choosing the departure from \(x\).** We use paths of the form
\[
x\xrightarrow{U^r}u\xrightarrow{D}w\xrightarrow{U^{t-r}}p,
\]
then go down from \(p\) to \(v\), and from \(v\) to \(y\). The single \(D\) at \(u\) permits several slightly different choices of the height of \(p\). This is used to avoid protected up-paths even at very large heights.

Take arbitrarily large denominators \(Q\) of reduced approximations \(|\alpha-P/Q|<Q^{-2}\), which exist by continued fractions. Writing \(\|\cdot\|\) for distance to the nearest integer, we have
\[
\|k\alpha\|\ge 1/(4Q)\qquad(0<|k|\le3Q/4), \tag{3}
\]
by comparison with \(kP/Q\).

For \(u=U^r(x)\), \(w=D(u)\), put
\[
\epsilon_r=\log_2\!\left(\frac{2K_w}{K_xg^r}\right).
\]
The numerator and denominator inside this logarithm differ by \(O(1)\), and by at least a constant times \((w+1)^{-7}\) by (1). Thus for large \(r\),
\[
w^{-8}\ll|\epsilon_r|\ll w^{-1}. \tag{4}
\]
Moreover \(w\) is on none of the protected \(P_b\) for all sufficiently large \(r\). Otherwise, along a subsequence \(w=U^d(b)\) for a fixed \(b\), and \(K_bg^{d-r}\to K_x/2\). The integer \(d-r\) must then stabilize, giving \(K_x=2K_bg^{d-r}\), contrary to (1) after shifting both up-path indices to be nonnegative.

Use \(m+1\) departure choices, with \(A_i=3\cdot10^{i-1}\), \(1\le i\le m+1\). Choose integers
\[
r_i=A_i\log_g Q+O(1)
\]
such that \(w_i=D(U^{r_i}(x))\) is on none of the \(H_b\). To see that a bounded adjustment suffices, \(\log_2 w_i=\log_2(K_x/2)+r_i\alpha+o(1)\), whereas the fractional parts of the log-heights on any \(H_b\) approach \(\log_2(b-1)\bmod1\). An irrational rotation visits an open interval separated from all these finitely many points with bounded gaps (by density and compactness). For large \(Q\), \(w_i>\max(F\cup\{x,y\})\). The up-run after \(w_i\) cannot hit a protected \(P_b\), by injectivity and the fact that \(b\) has no up-preimage; nor can an up-edge enter any \(H_b\).

Write \(\epsilon_i=\epsilon_{r_i}\). All are \(O(Q^{-3})\). By (4), their absolute values are between constant multiples of \(Q^{-8A_i}\) and \(Q^{-A_i}\), respectively. Since \(A_{i+1}>8A_i\), for fixed \(B=10A_{m+1}+10\) and all sufficiently large \(Q\) they are pairwise separated by more than \(10Q^{-B}\).

**Avoiding obstacles on the descent.** Take integer \(Q/4\le t\le Q/2\). For choice \(i\), the peak is \(p=\lfloor T\rfloor\) where
\[
T=K_{w_i}g^{t-r_i}=(K_x/2)g^t2^{\epsilon_i}.
\]
Suppose some down-iterate of \(p\) is \(z=U^d(b)>Q^B\) on a protected \(P_b\). Then for some \(j\ge0\),
\[
z-1<T/2^j<z+1,\qquad z<K_bg^d<z+1.
\]
Taking logs gives, with \(\beta_b=\log_2(K_x/(2K_b))\),
\[
\|(t-d)\alpha+\beta_b+\epsilon_i\|\le 4Q^{-B}. \tag{5}
\]
Here \(-C\le t-d\le Q/2\) for a fixed \(C\), since \(z\le p\) implies \(K_bg^d<T+1\). For a given \(b\), (3) shows there is **at most one** integer \(t-d\) in this range that can satisfy (5) for any choice \(i\): without \(\epsilon_i\) the distance must already be \(O(Q^{-3})\). For that integer, at most one \(i\) satisfies (5), by the separation of the \(\epsilon_i\). Consequently the \(m\) protected up-paths rule out at most \(m\) choices. Fix a remaining choice \(i\); its descent avoids all protected up-path vertices above \(Q^B\), for every candidate \(t\).

There remain enough \(t\)'s to reach \(v\) while avoiding the smaller obstacles. Indeed, by equidistribution of \(t\alpha\bmod1\), at least \(Q/(100v)\) candidate integers \(t\), for large \(Q\), place \(\log_2(K_x/2)+t\alpha\) in
\[
\big(\log_2(v-1+1/3),\,\log_2(v-1+2/3)\big)\pmod1.
\]
Here \(v\) was fixed before taking \(Q\) large; the interval has length at least \(1/(3v\ln2)\). Adding \(\epsilon_i=o(1)\) leaves \(T/2^s\) between \(v-1+1/4\) and \(v-1+3/4\) for some integer \(s\) tending to infinity. Hence \(D^s(\lfloor T\rfloor)=v\). Every intermediate down-iterate belongs to one of the \(C_k\).

For any particular \(z\in Z\) with \(z\le Q^B\), hitting \(z\) requires \(\log_2 T\bmod1\) to be in the arc from \(\log_2(z-1)\) to \(\log_2(z+1)\) modulo one. Its length is at most \(4/z\); by (3) it costs at most \(1+16Q/z\) candidate integers \(t\). There are \(O(\log Q)\) such \(z\), since the finitely many protected up-paths grow geometrically and \(B\) is fixed. Summing and using (2), the total cost is at most
\[
O(\log Q)+\frac{32m Q}{(v-1)2^J}<\frac{Q}{100v}
\]
for large \(Q\). Some candidate therefore succeeds.

This finishes the link: go down to \(v\) and then follow \(H_y\) to \(y\). It avoids the required paths and previously used vertices apart from the allowed endpoints. Any self-intersections *within* the link can be erased to make it a simple path with the same endpoints.

Now link the anchors consecutively, including the last to the first. At each stage the next unused departure path and the next unused entrance path have been protected, so their required freedom from \(F\) holds inductively. The concatenated links form a simple cycle.

Finally, use the anchors \(7,19,\ldots,7+12(n-1)\). Multiplying the edge ratios around their cycle gives the paper’s exact product
\[
\frac{2^\ell}{3^a}=\prod_{z\text{ on cycle}}\left(1+\frac{z\bmod2}{c_z z}\right),
\qquad c_z\in\{1,3\}.
\]
Every factor is at least one, and each anchor \(b\) contributes at least \(1+1/(3b)\). The product of these lower bounds tends to infinity, since the sum of the reciprocals of the anchors diverges. This proves the claimed supremum.

CONFIDENCE: greater than \(99.99\%\) for the disproof by certificate; \(99\%\) for the unboundedness proof. The most delicate step is avoiding protected up-paths on the descent: the separation argument (5) handles heights above \(Q^B\), while the reciprocal-sum estimate handles heights below it.