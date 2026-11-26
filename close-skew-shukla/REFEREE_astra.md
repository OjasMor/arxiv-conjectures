# Referee report for 2611.20820__1

status: completed cost: $0.6468

**REFEREE VERDICT: CORRECT**

**STATEMENT MATCH: yes.** Conjecture 5.9 (`conj:skew`) states:

> Let \(n>r\ge 1\), and let \(v_1,\ldots,v_k\in\mathbb F_2^n\) satisfy \(d_H(v_i,v_j)\le r\) for all \(i\) and \(j\). If there exist \(w_1,\ldots,w_k\in\mathbb F_2^n\) such that \(d_H(w_i,v_i)\ge r+1\) for every \(i\) and \(d_H(w_i,v_j)\le r\) whenever \(j<i\), then \(k\le 2^r\).

This is exactly the claimed statement. The paper defines \(d_H(\alpha,\beta)=|\{i\in[n]:\alpha_i\ne\beta_i\}|\), and calls a sequence “\(r\)-separated” if it has witnesses satisfying the two inequalities in `eq:skew`. By `lem:dprime-VR`, \(d'(\mathrm{VR}(Z;r))\) is the “maximum length of an \(r\)-separated sequence” with all points and witnesses in \(Z\) and \(d_H(v_i,v_j)\le r\) for all \(i,j\). Here \(Z=\mathbb F_2^n\). There is no pairwise closeness requirement on the witnesses.

**DEGENERATE OR ALREADY KNOWN IN PAPER: no.** The paper proves the close-skew bound for \(r\le 2\) or \(n=r+1\), but presents the general bound as a conjecture. It **is** an immediate corollary of the cited Gao–Zhao theorem once the reverse-order doubling is observed. The paper uses both orientations of each edge in `thm:im-exact` for *induced matchings*; it does not give the reverse-order argument for close-skew systems.

**DETAILS:**

1. **The doubling has the correct direction.** Hypothesis \((\mathrm S_r)\) requires \(d_H(a_i,b_j)\le r\) “whenever \(i<j\).” Within the original half, the required distance is \(d_H(v_i,w_j)\) for \(i<j\). Across halves it is \(d_H(v_i,v_j)\) for arbitrary \(i,j\), including \(i=j\), when it is zero. Within the swapped half it is \(d_H(w_i,v_j)\) for **\(i>j\)** because of the reversal. All three inequalities follow, and every diagonal distance remains at least \(r+1\). No \(w_i\)-to-\(w_j\) comparison is needed. Thus \((\mathrm S_r)\) applies to \(2k\) pairs and gives \(2k\le 2^{r+1}\).

2. **The independent binary proof is valid.** The squarefree monomials form a basis of \(R\), giving dimension \(2^m\). In characteristic two, \(L_s^2=0\), so common coordinates cancel and \(P(x)P(y)=P(x+y)\). Fewer than \(m\) differing coordinates cannot produce the top monomial. For at least \(m\) differences, the proposed specialization gives top coefficient \(1\). Crucially, the coefficient being specialized is a **polynomial**: this proves it is nonzero in \(K\), without needing one numerical specialization to work for every diagonal entry. The evaluation matrix is therefore lower triangular with nonzero diagonal, yet factors through the \(2^m\)-dimensional space \(R\). Both rank conclusions follow.

3. **Independent numerical checks.** I computed exact maxima in Python by choosing the **last** pair, rather than using the claim’s forward search. If \(F(S)\) allows first points in \(S\) and witnesses anywhere in the cube, then \(F(\varnothing)=0\) and for nonempty \(S\),
   \[
   F(S)=1+\max_{v\in S,\ d_H(v,w)>r}F\bigl(S\cap B(v,r)\cap B(w,r)\bigr).
   \]
   Those two balls impose exactly the restrictions of the last pair on earlier first points; earlier witnesses acquire no restriction. I also implemented multiplication in the squarefree algebra over \(\mathbb F_{256}\) and computed the full-cube matrix rank.

   | \((n,r)\) | \((3,1)\) | \((4,2)\) | \((5,2)\) | \((4,3)\) | \((5,3)\) | \((6,3)\) |
   |---|---:|---:|---:|---:|---:|---:|
   | Exact maximum \(k\) | 2 | 4 | 4 | 8 | 8 | 8 |
   | Specialized matrix rank | 4 | 8 | 8 | 16 | 16 | 16 |

   The first four maxima reproduce the paper’s exact values. In all six algebra tests there were zero product-identity or zero/nonzero threshold mismatches over all word pairs. As a separate direction check, I enumerated all **9,155** nonempty close-skew lists for \((4,2)\) normalized by \(v_1=0\). **Zero** failed reverse-order doubling; **7,500** failed if the swapped half was appended without reversing.

4. **Sharpness is genuine and already illustrated in the paper.** In the stated nested subcubes, \(d_H(w_i,v_j)=r+1-d_H(v_i,v_j)\), so precisely the matched first point is too far from its witness. This attains \(2^r\) for every allowed \(n,r\). Consequently the proof also gives \(d'(\mathrm{VR}(I_n;r))=2^r\) and, by the paper’s inequalities, the asserted implication to Shukla’s conjecture. **No proof step fails.**

**WHAT A HUMAN EXPERT SHOULD STILL CHECK:** Bibliographic priority of the reverse-order doubling argument before claiming novelty. The binary proof does not depend on the publication status of Gao–Zhao.