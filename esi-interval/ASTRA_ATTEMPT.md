# arXiv:2611.28073 [question#1]

status: completed cost: $0.4855 incomplete: None

TARGET: Is the \textsc{ESI Set} problem solvable in polynomial time on interval graphs?

---

VERDICT: PROVED

STATEMENT: “Is the \textsc{ESI Set} problem solvable in polynomial time on interval graphs?” **Yes.** The maximum ESI-set cardinality can be computed in \(O(n^2)\) time.

DEGENERATE: no — the algorithm applies to every nonempty connected interval graph, with arbitrary interval containments.

CERTIFICATE: Not applicable (algorithmic proof).

ARGUMENT:

The key is to choose the **supporting set** rather than the independent set. For any graph \(G\),
\[
\alpha_{\rm es}(G)=
\max_{\substack{S\subseteq V(G)\\ V(G)\setminus N[S]\text{ independent}}}
|V(G)\setminus N[S]|.
\]
Indeed, if \(B\) is an ESI-set, take \(S=V(G)\setminus N[B]\). No vertex of \(B\) is in \(N[S]\), and every vertex of \(N(B)\) has a neighbor in \(S\), so \(V(G)\setminus N[S]=B\). Conversely, if \(B=V(G)\setminus N[S]\) is independent, then \(S\subseteq V(G)\setminus N[B]\). Every vertex of \(N(B)\) lies in \(N[S]\setminus S\), so it has a neighbor in \(S\), as required.

**Gap decomposition.** Use a closed interval model \(I_v=[L_v,R_v]\). If only the graph is given, such a model can be obtained in \(O(n+m)\) time by the classical Booth–Lueker interval graph algorithm. Now \(N[S]\) consists exactly of the vertices whose intervals meet \(\bigcup_{v\in S} I_v\). Thus, if one interval of \(S\) is contained in another, we may remove the smaller one without changing \(N[S]\); for equal intervals we keep just one. After these removals, sorting \(S\) by left endpoint puts its **right endpoints in strictly increasing order as well**.

Adjoin sentinels \(s,t\) with \(L_s=R_s=-\infty\) and \(L_t=R_t=+\infty\). For consecutive members \(i,j\) of the resulting sequence, define
\[
F(i,j)=\{v\in V(G): R_i<L_v\ \text{and}\ R_v<L_j\}.
\]
Then \(V(G)\setminus N[S]\) is the disjoint union of these \(F(i,j)\). To see this, an interval avoiding \(S\) has a prefix of the selected intervals strictly to its left and the remaining selected intervals strictly to its right. The break uniquely determines its pair \(i,j\), including at either sentinel. Conversely, an interval in \(F(i,j)\) misses the entire prefix because its right endpoints are at most \(R_i\), and misses the entire suffix because its left endpoints are at least \(L_j\). Intervals in *different* gaps cannot intersect, since a selected interval separates them. Hence the remainder is independent exactly when the intervals in *each* \(F(i,j)\) are pairwise disjoint. Overlapping consecutive supporters cause no problem: their gap is empty.

**Algorithm.** Build a directed graph on the input intervals and the two sentinels. Insert an arc \(i\to j\) precisely when
\[
L_i<L_j,\qquad R_i<R_j,\qquad
\{I_v:v\in F(i,j)\}\ \text{is pairwise disjoint}.
\]
Give that arc weight \(|F(i,j)|\). The graph is acyclic by the left-endpoint order. Every \(s\)-\(t\) path specifies a supporting set \(S\) whose remainder is independent, and its weight is exactly the size of that remainder. Conversely, a supporting set attaining the displayed maximum, after the containment removals, gives an \(s\)-\(t\) path of that weight. Thus the longest path weight is \(\alpha_{\rm es}(G)\); compare it with the given positive threshold \(\ell\).

**Running time.** For a fixed tail \(i\), visit heads \(j\) in nondecreasing \(L_j\). Scan the vertices once in nondecreasing \(R_v\), consuming them as soon as \(R_v<L_j\) and retaining only those with \(L_v>R_i\). The vertices retained so far are exactly \(F(i,j)\). Maintain their count, their largest right endpoint \(M\), and a flag recording whether an intersection has occurred. When adding \(v\) to a nonempty retained set, it intersects an earlier interval exactly when \(L_v\le M\): the interval ending at \(M\) then contains the point \(M\in I_v\), since \(M\le R_v\) by scan order. Once set, the conflict flag stays set. This computes all outgoing arcs and weights in \(O(n)\) time per tail after sorting. Arc construction and the longest-path computation therefore take \(O(n^2)\) time in total.

**Sandbox checks.** I first enumerated subsets using the paper’s ESI definition directly, obtaining, for example, \(\alpha_{\rm es}(P_5)=2\), \(\alpha_{\rm es}(P_9)=3\), \(\alpha_{\rm es}(C_8)=2\), and \(\alpha_{\rm es}(C_{12})=3\), matching the stated values. The gap algorithm then agreed with direct enumeration on every pairing of \(2n\) distinct ordered endpoints for \(1\le n\le6\) (10,395 models at \(n=6\)), and on 750 further random models with tied endpoints allowed, at orders \(7,10,14\).

CONFIDENCE: 99.9%. The most sensitive step is decomposing the remainder when selected intervals overlap; the strict gap inequalities and the increasing order of both endpoints handle that case without assuming the supporters are independent.