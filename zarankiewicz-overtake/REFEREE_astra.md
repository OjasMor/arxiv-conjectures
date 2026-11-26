# Referee report for 2610.22875__2

status: completed cost: $0.993

REFEREE VERDICT: CORRECT

STATEMENT MATCH: yes. Conjecture **Threshold** (`conj:threshold`) states: “For \(\min(m,n)\ge3\), an overtake occurs if and only if \(H_{\mathrm{limited}}(m,n)\ge5\).” At \((6,5)\) I verified
\[
z_{2A}=21>20=z_2,\qquad H_{\mathrm{limited}}=4.
\]
This refutes the **only-if** direction. It also contradicts the paper’s Proposition `prop:n5-cases`, Theorem `thm:n5-cases`, and the \((6,5)\) entry in Table `tab:range`, all of which assert no overtake there.

DEGENERATE OR ALREADY KNOWN IN PAPER: no. Both one-edge graphs are connected and \(C_4\)-free, and each configuration has disjoint supports. The paper expressly allows the two cells of a 2-edge to “share a row or a column.” This is not the excluded width-two case. The **limited** value \(20\) is already in the paper; the rank-\(21\) **augmented** witness is what its enumeration claims to exclude.

DETAILS:

**Definitions checked.** The paper defines an overtake as “a strict inequality \(z_{2A}(m,n)>z_2(m,n)\).” SOS rank is “the least rank of a positive semidefinite matrix \(Q\) with \(v^{\mathsf T}Qv=P\),” and \(G\) is irreducible if that rank equals \(R(G)\). A limited configuration “satisfies simplicity and the bipartite graph \(G_0\) is \(C_4\)-free with \(|E_1|=z(m,n)\)”; it is limited extremal if it is also irreducible and \(R(G)=z_2(m,n)\). Thus \(H_{\mathrm{limited}}\) counts holes in the limited **extremizer**, not in the overtaking witness. No recursive-line criterion is required for \(z_{2A}\).

**Independent reconstruction.** I wrote and ran new code from the coefficient identities. The claim’s linked C++ file was not present in the sandbox. My outputs were:

| Configuration | \((|E_1|,|E_2|,H,R)\) | One-edge \(C_4\) count | Newly forced pairs per pass | Exact rank of product matrix |
|---|---:|---:|---:|---:|
| Limited | \((14,6,4,20)\) | 0 | \(6\) | \(210/210\) |
| Overtaking | \((13,8,1,21)\) | 0 | \(4,2,2\) | \(231/231\) |

For irreducibility, I compared an arbitrary feasible Gram matrix with the displayed one. Their difference \(D\) vanishes on line pairs and has opposite entries on the two diagonals of each rectangle. Hole rows vanish. On a displayed pair, \(D_{ab}\le0\); equality forces the two unit Gram vectors to coincide, permitting their indices to be interchanged. Propagating these constraints gave the passes in the table. In particular, the critical last relation really is \(D_{4,6}=-D_{3,17}\), with **both** entries nonpositive. Once all pairs were forced, there were zero free Gram-deviation components. Independently, expansion of the products of the resulting forms gave the full column ranks above over both \(\mathbb Q\) and \(\mathbb F_2\). Thus the displayed Grams are unique, not merely feasible, and the SOS ranks are exactly \(20\) and \(21\).

As controls, a row-subset dynamic program forbidding repeated column pairs returned \(z(4,3)=7,\ z(4,4)=9,\ z(5,5)=12,\ z(6,5)=14\), reproducing in particular the width-five table’s classical values. The Gram checker also certified a separate \((4,4)\) configuration with eight singletons, three pairs, two holes and SOS rank \(11\), reproducing the paper’s known overtake witness length.

**Limited upper bound.** The paper’s six-column formula (`eq:n6-exact`) gives \(z_2(5,6)=4\cdot5=20\), hence \(z_2(6,5)=20\) by transposition, despite the width-five proof describing this value as left open by the cited reference. I also checked the upper bound without that citation. At 14 singletons the ten-column-pair budget forces row degrees \(3,3,2,2,2,2\); the triples meet once and the four doubletons are determined. Thus there is one base up to relabeling. It suffices to exclude seven added pairs: any shortening still works after deleted squares are restored.

My independent enumeration on that base returned:
```text
single pairs surviving local reductions:       58
seven-pair matchings surviving local tests: 112904
reduced by exact product dependence:         84340
reduced by a shorter signed-coordinate SOS:  28556
remaining:                                       8
```
The eight remaining matchings were exactly the relabeling orbit of the stated special case. For its proposed replacement Gram, symbolic expansion gave polynomial residual zero. The four nontrivial blocks had orders \(3,3,4,2\) and final Schur pivots \(0,0,0,2-\sqrt3\), respectively. The Gram is PSD of rank \(20\). This completes the limited upper bound.

It follows that \(H_{\mathrm{limited}}=30+14-2(20)=4\). Any irreducible configuration exceeding \(20\) must have at most \(13\) singletons, so the cell identity gives \(2R\le30+13\), proving \(z_{2A}\le21\). The witness attains it.

**First failure in the paper:** Table `tab:n5-candidates` correctly includes \((d,H)=(1,1)\) with 13 singletons and eight pairs. It is the subsequent assertion, “In every case the computed rank is strictly less than \(R(G)\),” that fails. The example does **not** violate the separate sharp hole budget: its excess is \(1=\lfloor4/3\rfloor\).

[Download the independent verification code and replay instructions](sandbox:/mnt/data/referee_6x5_checks.zip)

WHAT A HUMAN EXPERT SHOULD STILL CHECK:
- Trace the paper’s width-five enumeration on this exact witness to distinguish an omitted configuration from an incorrect rank determination.
- Audit other exclusions using the same rank-minimization procedure; this counterexample identifies a failure at \((6,5)\), not which other entries, if any, are wrong.