# Referee report for 2611.19137__2

status: completed cost: $1.3474

REFEREE VERDICT: **CORRECT**

STATEMENT MATCH: **yes** — Conjecture `conj:UpperCovers` in `sec:upperSaturated` states:

> Let \(\lambda\in Q^\vee\), let \(u=\operatorname{gateC}(\lambda)\), and let \(x\in\widetilde W\) be such that the alcove \(x\mathfrak a\) is in the gate position at \(\lambda\). For all \(u'\in W\), define \(x^{u'}=\operatorname{pr}(u\to u')^{-1}x\), and put \(u_0=u\) and \(u_k=u'\), where \(k=d_\Phi(u\to u')\). Then for all shortest paths \((u_0,\dots,u_k)\) from \(u\) to \(u'\) in the QBG, we have:
> 1. covering relations in Bruhat order \(x^{u_0}\lessdot x^{u_1}\lessdot\cdots\lessdot x^{u_k}\); and
> 2. in Iwahori order, relations \(\lambda^{u_0}\le_I\lambda^{u_1}\le_I\cdots\le_I\lambda^{u_k}\) such that for all \(0\le j<k\), either \(\lambda^{u_j}\lessdot_I\lambda^{u_{j+1}}\) or \(\lambda^{u_j}=\lambda^{u_{j+1}}\).

The path is directed **away from** the gate chamber. Only the starting alcove must be a gate. The preceding Corollary `cor:UpperCovers` assumes upper QBG-regularity; the conjecture does not. Proposition `prop:CornerLocationUpper` already gives the weak Iwahori inequalities without that assumption. It is the **cover-or-equality** assertion that fails.

DEGENERATE OR ALREADY KNOWN IN PAPER: **no** — The starting coweight is regular and nonzero. It lies in the coroot lattice \(R^\vee\subset Q^\vee\), and all affine elements used are in the irreducible affine Coxeter group of type \(\widetilde A_2\). The endpoint is singular, but this is not excluded. The supplied paper does not state the counterexample; its tables do allow one to deduce the failure once this coweight is chosen.

DETAILS:

I [rebuilt the certificate in Python](sandbox:/mnt/data/verify_upper_covers_A2.py) using integer affine matrices in the simple-coroot basis. I computed lengths by breadth-first search in the simple generators, independently of the claim’s permutation code and length formula. I also tested Iwahori order directly by folding galleries.

**1. Starting gate.** Definition `defn:gate` calls the gate “the unique alcove in \(\operatorname{St}(\lambda)\) which is at minimum distance from \(\mathfrak a\).” Definition `defn:gateC` takes \(u\) such that this alcove “lies in the Weyl chamber \(\mathcal C_u\).” For \(\lambda=(0,1,-1)\), the computation gave
```text
dominant representative:       (1, 0, -1)
gate chamber:                  s1
lengths in the starting coset: [2, 3, 3, 4, 4, 5]
unique shortest word:          s1 s0
```
This also checks the convention in `lem:formula`: the formula generally uses \(\operatorname{oppC}(\lambda)\), but at this regular \(\lambda\) it equals \(\operatorname{gateC}(\lambda)=s_1\). Thus \(x=s_1s_0=t^\lambda s_2s_1\) is the required element.

**2. Edge and upper corner.** The paper assigns weight \(\alpha^\vee\) when \(\ell(us_\alpha)=\ell(u)-\langle2\rho,\alpha^\vee\rangle+1\), and `defn:QBGEdgeReflection` assigns that edge the reflection \(s_{-u\alpha,1}\). My code reproduced these entries of `table:A2_wt` and `table:A2_QBGEdgeReflection`, with \(\theta=\alpha_1+\alpha_2\):

| Directed edge | Computed weight | Computed reflection |
|---|---|---|
| \(s_1\to\mathrm{id}\) | \(\alpha_1^\vee\) | \(s_{\alpha_1,1}\) |
| \(s_1\to s_{12}\) | \(0\) | \(s_\theta\) |
| \(w_0\to\mathrm{id}\) | \(\theta^\vee\) | \(s_{\theta,1}\) |

The first edge is shortest because its endpoints are distinct. By `defn:QBGPairReflections` its product is the single reflection \(r=s_{\alpha_1,1}=s_2s_0s_2=r^{-1}\).

The unbound \(\lambda'\) in the display of `defn:CornerUpper` is a genuine typo, not a choice on which the counterexample depends. The next display explicitly says “\(\lambda^{u'}=(r_1\cdots r_k)^{-1}\lambda=r_k\cdots r_1\lambda\).” Both this action and the independent formula in `table:A2_upper` give
\[
\lambda^{\mathrm{id}}=r\lambda=\lambda_++\alpha_1^\vee=(2,-1,-1).
\]
Its simple-root pairings are \((3,0)\). Thus \(\lambda\) fails `defn:upper-QBG`, which requires \(\lambda_++\operatorname{wt}(u\to u')\) to be “dominant and regular” for **all** \(u'\). The proved corollary is unaffected.

**3. Bruhat and Iwahori checks.** The independent word search returned:

| Element | Translation vector | Spherical direction | Length | Minimum length in its coset |
|---|---|---|---:|---:|
| \(x\) | \((0,1,-1)\) | \(s_2s_1\) | 2 | 2 |
| \(s_2x\) | \((0,-1,1)\) | \(s_1\) | 3 | 3 |
| \(s_0s_2x\) | \((2,-1,-1)\) | \(s_1s_2\) | 4 | 4 |
| \(rx=s_2s_0s_2x\) | \((2,-1,-1)\) | \(w_0\) | 5 | 4 |

Each row is obtained from the preceding one by a simple left multiplication increasing length by one. Hence there are **three Bruhat covers** from \(x^{s_1}=x\) to \(x^{\mathrm{id}}=rx\) along this chain. In particular the endpoints do not form a cover, disproving (1).

For (2), Definition `def:IwahoriOrder` says \(\lambda\le_I\lambda'\) exactly when “\(\lambda\in\operatorname{Sh}(\lambda')\),” the end-vertices obtained by folding a minimal gallery to \(\lambda'\). I enumerated the fold-or-cross choices along reduced words for the gates. Writing \(L,M,H\) for the first three translation vectors in the table, the output was:
```text
L in Sh(M), M in Sh(H):  True  True
M in Sh(L), H in Sh(M):  False False
```
Thus \(\lambda^{s_1}=L<_I M<_I H=\lambda^{\mathrm{id}}\). The last Bruhat step fixes \(H\), but the **first two** steps strictly change the vertex. This verifies the claim’s use of `prop:BruhatImpliesIwahori` and disproves (2) directly from shadows.

**Separate paper-text issue.** As printed, `cor:CornerLocationUpper`(2) also has a problem on this input. Taking its \(u'=u=s_1\) and \(i=1\), its weight hypothesis holds, but its conclusion would require \(\langle s_1\alpha_1,\lambda\rangle\le-1\); the pairing is \(+1\). This is not a hypothesis of the conjecture, and neither the certificate nor my check uses that corollary.

WHAT A HUMAN EXPERT SHOULD STILL CHECK:
- Check the current manuscript or errata for revisions to `conj:UpperCovers`, the stray prime in `defn:CornerUpper`, and the sign or corner index in `cor:CornerLocationUpper`(2). No mathematical step of the counterexample remains unresolved for the supplied text.