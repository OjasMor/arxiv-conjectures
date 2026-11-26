# arXiv:2610.22875 [conj:threshold]

status: completed cost: $1.854 incomplete: None

TARGET: [Threshold]\label{conj:threshold}
{ For \(\min(m,n)\ge3\), an overtake occurs if and only if \(H_{\mathrm{limited}}(m,n)\ge5\).}

---

VERDICT: DISPROVED

STATEMENT: “For \(\min(m,n)\ge3\), an overtake occurs if and only if \(H_{\mathrm{limited}}(m,n)\ge5\).”

DEGENERATE: no. The counterexample is at \((m,n)=(6,5)\); both one-edge graphs below are connected and \(C_4\)-free, and all displayed supports are disjoint.

CERTIFICATE:
```json
{
  "m": 6,
  "n": 5,
  "cell_numbering": "5*i+j, with 0 <= i < 6 and 0 <= j < 5",
  "limited": {
    "E1": [0,1,2,6,8,12,13,16,19,22,24,25,28,29],
    "E2": [[3,17],[4,11],[5,20],[9,27],[10,15],[23,26]],
    "holes": [7,14,18,21]
  },
  "overtaking": {
    "E1": [0,1,2,5,8,11,13,15,19,22,24,28,29],
    "E2": [[6,4],[14,10],[16,21],[7,12],[26,18],[27,9],[17,3],[20,23]],
    "holes": [25]
  }
}
```

ARGUMENT:

At \((6,5)\) the values are
\[
\boxed{z=14,\qquad z_2=20,\qquad H_{\mathrm{limited}}=4,\qquad z_{2A}=21.}
\]
Thus it is the **only-if** direction that fails. The paper's stated *limited* value \(z_2(6,5)=20\) is correct; it is the claimed exclusion of the *non-limited* length \(21\) that fails.

[Download the complete standalone verification code (C++17)](sandbox:/mnt/data/threshold65.cpp). It checks both witnesses and independently checks the limited upper bound, without using an SOS optimizer. My observed output was:
```text
unique Gram: singles=14 pairs=6 holes=4 rank=20
unique Gram: singles=13 pairs=8 holes=1 rank=21
7-pair matchings passing local tests: 112904
dependent products: 84340; shorter signed SOS: 28556; special orbit: 8
```

### Why the length-21 witness is irreducible

As an initial check, enumerating row masks while prohibiting any repeated column pair gave \(z(4,3)=7,\ z(4,4)=9,\ z(5,5)=12\). Substitution of the paper's respective \(z_2\) values into \(mn+z-2z_2\) reproduced the hole counts \(3,5,3\).

Now use the cell numbering in the certificate. Let \(Q_0\) be the displayed Gram matrix of the overtaking witness, let \(Q\) be **any** feasible PSD Gram matrix for the same polynomial, and put \(D=Q-Q_0\). Comparing polynomial coefficients gives:

* All diagonal deviations are zero. Occupied cells therefore have unit Gram vectors, and the hole has zero Gram vector.
* \(D_{ab}=0\) for two cells on the same row or column.
* For diagonals \((a,b)\) and \((c,d)\) of the same rectangle, \(D_{ab}=-D_{cd}\).

If \((a,b)\) is a displayed pair, then \(D_{ab}=Q_{ab}-1\le0\). If \(D_{ab}=0\), its two unit vectors coincide in **every** feasible representation. Indices \(a,b\) can then be interchanged in \(D\), since their rows coincide in both \(Q\) and \(Q_0\).

The four pairs \((14,10),(16,21),(7,12),(20,23)\) coincide in this sense immediately: each is on one row or column. Using those identifications and the rectangle equations gives
\[
\begin{aligned}
D_{18,26}&=-D_{16,28}=-D_{21,28}
           =D_{23,26}=D_{20,26}=-D_{21,25}=0,\\
D_{9,27}&=-D_{7,29}=-D_{12,29}
           =D_{14,27}=D_{10,27}=-D_{12,25}=0,
\end{aligned}
\]
because cell \(25\) is the hole. Thus \(18\) is identified with \(26\), and \(9\) with \(27\).

The key final step is
\[
D_{4,6}=-D_{1,9}=-D_{1,27}=D_{2,26}=D_{2,18}=-D_{3,17}.
\]
**Both ends are deviations of displayed pairs:** \(D_{4,6}\le0\) and \(D_{3,17}\le0\). Hence both vanish. All eight displayed pairs are now forced.

Consequently any feasible representation is a Gram representation on the list \(w_1,\ldots,w_{21}\) of displayed bilinear forms. Its Gram matrix on that list must be the identity if the \(231\) products \(w_iw_j\), \(i\le j\), are linearly independent. The following short exact check proves independence even modulo \(2\), which suffices over \(\mathbb R\) since the coefficient matrix is integral.

```python
import itertools as it

def product_test(pairs, holes):
    used = set(holes) | {i for p in pairs for i in p}
    w = [(i,) for i in range(30) if i not in used] + pairs
    basis = {}
    for A, B in it.combinations_with_replacement(w, 2):
        s = 0
        for a, b in it.product(A, B):
            r, u = sorted((a//5, b//5))
            c, v = sorted((a%5, b%5))
            s ^= 1 << (((6*r + u)*5 + c)*5 + v)
        while s:
            h = s.bit_length()
            if h not in basis:
                basis[h] = s
                break
            s ^= basis[h]
    return len(w), len(basis)

print(product_test([(6,4),(14,10),(16,21),(7,12),(26,18),(27,9),
                    (17,3),(20,23)], [25]))
print(product_test([(3,17),(4,11),(5,20),(9,27),(10,15),(23,26)],
                   [7,14,18,21]))
```

Observed output:
```text
(21, 231)
(20, 210)
```

This proves SOS rank \(21\) for the overtaking witness. It also checks the product independence for the limited witness: there, each of the six pairs is forced either by sharing a line or by having a hole on the other diagonal of its rectangle. Thus the limited witness has SOS rank \(20\).

### The limited value and the hole count

The paper itself gives \(z_2(6,5)=20\) independently of its augmented enumeration, by its displayed exact six-column formula at \(m=5\), transposed. Taking that value as given, the disproof is already complete: the limited witness has four holes, while the other witness strictly overtakes it.

For an **independent verification** of the upper bound \(z_2\le20\), the downloadable checker uses the following reduction. In a \(C_4\)-free base, the row degrees \(d_i\) satisfy \(\sum_i\binom{d_i}{2}\le10\). Fifteen edges violate this bound even with degrees as balanced as possible. At fourteen edges the degrees must be \(3,3,2,2,2,2\), with all ten column pairs used exactly once. The two triples intersect in one column; the four doubletons are then determined. This gives exactly the limited base in the certificate up to relabeling, and proves \(z=14\).

It suffices to exclude **seven** added pairs on this base: any reduction of a subform remains a reduction after the other displayed squares are added back. The checker enumerates seven-pair matchings on the sixteen available cells. Its tests are:

1. Discard locally reducible pairs. In particular, if multiplying a displayed pair-sum by a singleton gives a sum of two products of singletons via rectangle identities, there is a nontrivial dependence among displayed products. Another test flips a pair to the opposite diagonal when that diagonal consists of two singletons: this preserves the polynomial, and a resulting all-singleton rectangle reduces four squares to two.
2. Test for a dependence among all displayed products. Such a dependence gives a nonzero symmetric Gram direction \(T\) on the displayed forms. Moving from \(I\) along \(I+tT\) to a PSD boundary point reduces rank.
3. Seek a shorter SOS by assigning occupied cells signed coordinate unit vectors. A successful assignment matches all line and rectangle coefficients and uses fewer than \(21\) coordinates.

The eight matchings left by these tests are relabelings of a **single** case:
\[
(3,17),(4,11),(5,18),(7,10),(9,27),(14,20),(23,26).
\]
Here is its explicit rank reduction. Split \((3,17)\) and \((7,10)\) into separate cell monomials, keeping each other pair as one sum labeled by its smaller index. Write \(w_a\) for the resulting \(23\) forms. Their initial Gram has diagonal ones and off-diagonal ones at \((3,17),(7,10)\). The three product identities
\[
\begin{aligned}
w_0w_7-w_2w_5+w_3w_{17}&=0,\\
w_5w_{12}-w_7w_{10}-w_{13}w_{17}&=0,\\
w_{17}w_{24}-w_{19}w_{22}&=0
\end{aligned}
\]
follow by expanding cell monomials. Perturb the corresponding symmetric off-diagonal entries by these three coefficient patterns times \(-\alpha,\beta,\tau\), respectively, where
\[
\alpha=\sqrt3/2,\qquad \beta=1/2,\qquad \tau=\sqrt{\sqrt3-1}.
\]
The polynomial is unchanged. The new Gram has three disjoint star blocks with center-to-leaf weight vectors
\[
(-\alpha,1-\beta),\qquad(\alpha,\beta),\qquad(1-\alpha,-\beta,\tau).
\]
Each vector has norm one, so each unit-diagonal star is PSD of corank one by its Schur complement. The only other nontrivial block has off-diagonal \(-\tau\) and is positive definite. The rank is therefore \(23-3=20\). This closes the independent limited upper-bound check.

Finally,
\[
H_{\mathrm{limited}}=30+14-2(20)=4.
\]
Any irreducible configuration exceeding \(20\) is non-limited, so has at most \(13\) singletons; the cell identity gives \(2R\le30+13\), hence \(R\le21\). The witness attains \(21\). This is an overtake **below** the proposed threshold, inside the paper's reported range.

CONFIDENCE: \(>99.9\%\). The most implementation-dependent step is the independent enumeration for the limited upper bound; it agrees with the separately stated exact six-column formula. The strict lower bound \(z_{2A}(6,5)\ge21\) uses only the explicit Gram equalities and the short integer product-rank check above.