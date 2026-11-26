# Referee report for 2611.26653__1

status: completed cost: $0.5948

REFEREE VERDICT: CORRECT

STATEMENT MATCH: yes. Conjecture 4.1 (`conj:ham`) states: “If \(G\) is Hamiltonian of order \(n\ge5\), then \(\mathrm{DD}_D(G)\le\max\{2,\lfloor n/3\rfloor\}\); equality holds for the cycles \(C_{3k}\).” The claim proves this upper bound and this equality statement, without asserting that cycles are the only equality cases.

The relevant definitions match. The paper says “All graphs are finite, simple and connected” and defines \(D(u,v)\) as “the length of a longest \(u,v\)-path in \(G\), with \(D(u,u)=0\).” Definition 1.1 requires “\(\emptyset\ne S\ne V(G)\)” and “\(D(w,u)\ne D(w,v)\) for every \(w\notin S\) and all distinct \(u,v\in S\).” The upper number is “the maximum order of a maximal DDD set,” and “maximal is meant with respect to inclusion.” A largest proper DDD set is necessarily inclusion-maximal; the proof does not assume that subsets of DDD sets are DDD sets.

DEGENERATE OR ALREADY KNOWN IN PAPER: no for the general bound; **yes for the cycle equality alone**. Theorem `thm:ham` gives only \(\lfloor n/2\rfloor\) in general. The paper explicitly notes that \(\mathrm{DD}_D(C_{3k})=k\), from `thm:agree` and the cited cycle theorem `pre:cycles`. No standing assumption excludes the Hamiltonian graphs treated here.

DETAILS: I found no failing step.

1. **Gap count.** The complementary cycle arc gives \(1\le h(w,x)=n-D(w,x)\le d\) for either arc length \(d\), so \(s\le\lfloor n/2\rfloor\). If \(g<a+b\), choosing \(\ell=\min(g,b)\) makes the first cap at most \(a+b-1\) and the second cap \(\max(g,b)\le a+b-1\). This contradicts injectivity at that single outside vertex. With at least two runs, the runs on either side of each gap are disjoint, and each run is counted twice, **including when there are exactly two runs**. Thus \(n-s\ge2s\).

2. **Chords in the one-run case.** At each end of the outside run, the ordered \(h\)-values are distinct positive integers bounded successively by \(1,\ldots,s\), forcing (1). An internal chord \(x_jx_k\), \(k>j+1\), gives the stated path of length \(t+k-1>t+j=D(y_1,x_{j+1})\). A chord \(y_1x_j\), \(j<s\), gives length \(t+s-j>t=D(y_t,x_s)\); reversal handles \(y_t\).

   For the delicate mixed chord \(y_ix_j\), the proposed path to \(x_r\), \(r<j\), uses disjoint \(y\)-segments \([1,\ell]\), \([i,t]\) and disjoint \(x\)-segments \([j,s]\), \([1,r]\). It therefore really is simple. The number omitted is \((i-\ell-1)+(j-r-1)\); adding **one** converts this to the upper bound on \(h\), as claimed. The gap count gives \(i-1\ge s\) for \(j\ge2\), and reversal gives \(t-i\ge s\) for \(j\le s-1\). For \(j=1\), the additional path inequality \(t-i+s\le t\) supplies \(i\ge s\); \(j=s\) is symmetric. Thus every chord meeting \(S\) is excluded under \(t<2s\).

3. **Two attachments.** Equation (3) is exact: a path ending in the induced run has only two ways to enter, cannot leave and re-enter, and either longest prefix in \(H\) can be extended to \(x_j\). This includes a zero-length prefix at an attachment. If \(|A-B|\le s-2\), the crossing of the two affine terms gives equal maxima at the flanking indices for a half-integer crossing, or at the two neighboring indices for an integer crossing. Those indices lie in \([1,s]\). Hence (4) follows.

   The rest of the contradiction also holds at the boundary cases. For \(t=s\), an internal \(y\)-vertex has both distances positive. For \(t>s\), the lower bound \(B(y_i)\ge t-i\) forces (5) for \(i<p\), and also for \(i=p\) unless \(p=s\); in that case reversal fixes the middle vertex and exchanges its two distances. Consequently \(A(y_p)=p-1\), and (4) forces \(B(y_p)\ge t-1\). But any edge from \(y_i\), \(i<p\), into \(R\) yields a simple path from \(y_1\) to \(y_{i+1}\) visiting all \(p\) prefix vertices and at least one more, contradicting (5). Thus a path from \(y_t\) to \(y_p\) first enters the prefix at its endpoint and has length at most \(t-p<t-1\).

4. **Equality.** Equal cycle distances from \(w\) to distinct \(x,x'\) imply \(x+x'\equiv2w\pmod{3k}\). If both are multiples of three, then so is \(w\), so no outside vertex witnesses a tie. Since \(D=3k-d\) off the diagonal and \(k\ge2\) in the stated range, the set attains the bound.

**Independent Python checks.** I computed longest simple paths by subset dynamic programming: for each source and visited-vertex mask, I stored all achievable endpoints and extended only to unvisited neighbors. I then tested injectivity on nonempty proper subsets. Outputs included:

| Test | Output |
|---|---|
| Paw, using the paper’s vertex labels | Maximal sets \(\{1,2\},\{1,3\},\{1,4\}\), reproducing Example `ex:paw` |
| Upper numbers for \(C_5,C_6,C_9,C_{12}\) | \(1,2,3,4\) |
| All 512 chord subsets of a fixed labelled \(C_6\) | 498 graphs with upper number 1; 14 with upper number 2 |
| Cycles of orders 6–12 with zero or one added chord | 3,108 multi-run gap inequalities checked; none failed |
| One chord meeting the specified run, \(s=3,4\), \(s\le t<2s\) | 125 graphs; all 936 tested mixed-chord \(h\)-bounds held |
| Two-attachment construction, every chord subset inside \(H\), \(s=3,4\), \(s\le t<2s,\ t\le6\) | 1,170 graphs; (3) and the distinctness test agreed on all 6,854 outside-vertex rows. In all 60 orientations satisfying the tested prefix condition (5) with \(p\ge2\), \(B(y_p)\le t-p\). |

WHAT A HUMAN EXPERT SHOULD STILL CHECK: No mathematical gap remains in this review. If publication priority matters, check the literature beyond the supplied paper for the **general bound**, distinguishing it from the already known cycle equality.