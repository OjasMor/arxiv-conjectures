# arXiv:2611.26653 [conj:ham]

status: completed cost: $1.3609 incomplete: None

TARGET: \label{conj:ham}
If $G$ is Hamiltonian of order $n\ge5$, then $\DDD(G)\le\max\{2,\lfloor n/3\rfloor\}$; equality holds for the cycles $C_{3k}$.

---

VERDICT: PROVED

STATEMENT: “If \(G\) is Hamiltonian of order \(n\ge5\), then \(\mathrm{DD}_{D}(G)\le\max\{2,\lfloor n/3\rfloor\}\); equality holds for the cycles \(C_{3k}\).”

DEGENERATE: no — the proof covers all finite simple Hamiltonian graphs in the stated range, with DDD sets required to be nonempty and proper.

CERTIFICATE: not applicable.

ARGUMENT:

As a definition check, I enumerated simple paths by depth-first search, measuring length in edges, and tested every nonempty proper vertex subset. This reproduced the upper numbers \(2,1,2,3\) for the paw, \(C_5,C_6,C_9\), respectively. On all \(512\) ways to add chords to a fixed labelled \(C_6\), the upper number was \(1\) in \(498\) cases and \(2\) in \(14\). The proof below does not rely on the computation.

It suffices to prove that **every DDD set \(S\) of size \(s\ge3\) satisfies \(n\ge3s\)**. Indeed, the largest size of a DDD set equals the largest size of an inclusion-maximal one, by finiteness.

Fix a Hamiltonian cycle and write
\[
h(w,x)=n-D_G(w,x)\qquad(w\ne x).
\]
For every \(w\notin S\), the \(h(w,x)\), \(x\in S\), are distinct positive integers. If a cycle arc from \(w\) to \(x\) has length \(d\), the complementary arc gives \(h(w,x)\le d\). In particular \(h(w,x)\le\lfloor n/2\rfloor\), so \(s\le\lfloor n/2\rfloor\).

**1. Counting across a gap.** Suppose \(w_1,\dots,w_g\) are outside \(S\), with \(g\ge1\), and \(A,B\subseteq S\) are disjoint nonempty sets of sizes \(a,b\). If for each \(\ell\),
\[
h(w_\ell,x)\le \ell+a-1\quad(x\in A),\qquad
h(w_\ell,x)\le g-\ell+b\quad(x\in B),
\]
then \(g\ge a+b\). Otherwise take \(\ell=\min(g,b)\): both upper bounds are at most \(a+b-1\), which cannot accommodate \(a+b\) distinct positive integers.

If \(S\) has at least two runs of consecutive vertices on the Hamiltonian cycle, apply this observation to each gap between successive runs. With \(A,B\) the runs on its two sides, the required inequalities follow by taking the cycle arcs from \(w_\ell\) toward the respective runs. Summing over gaps counts each run twice, so \(n-s\ge2s\), as desired.

Henceforth suppose, for contradiction, that \(n<3s\). There must be just one run, so the cyclic order is
\[
x_1,\ldots,x_s,\ y_1,\ldots,y_t,\qquad
S=\{x_1,\ldots,x_s\},\qquad s\le t<2s.
\]

**2. No chord can meet \(S\).** At \(y_1\), the values \(h(y_1,x_s),h(y_1,x_{s-1}),\ldots,h(y_1,x_1)\) are bounded above by \(1,2,\ldots,s\), respectively. Distinctness forces equality term by term. The same argument at \(y_t\) gives
\[
D_G(y_1,x_j)=t+j-1,\qquad D_G(y_t,x_j)=n-j. \tag{1}
\]
A chord \(x_jx_k\) with \(k>j+1\) would give the path
\[
y_1\cdots y_t\,x_1\cdots x_j\,x_kx_{k-1}\cdots x_{j+1}
\]
of length \(t+k-1>D_G(y_1,x_{j+1})\). Also, an edge \(y_1x_j\) with \(j<s\) would give the path \(y_t\cdots y_1\,x_j\cdots x_s\) of length greater than \(D_G(y_t,x_s)=t\). Symmetrically, \(y_t\) has no neighbor in \(S\) other than \(x_1\).

It remains to rule out a chord \(y_ix_j\) with \(1<i<t\). We claim
\[
j\ge2\ \Longrightarrow\ i-1\ge s,\qquad
j\le s-1\ \Longrightarrow\ t-i\ge s. \tag{2}
\]
For the first implication, apply the gap count to \(w_\ell=y_\ell\), \(1\le\ell\le i-1\), with
\[
A=\{x_j,\ldots,x_s\},\qquad B=\{x_1,\ldots,x_{j-1}\}.
\]
For \(x_r\in A\), the arc through \(y_1\) gives \(h(y_\ell,x_r)\le\ell+s-r\le\ell+|A|-1\). For \(x_r\in B\), use the simple path
\[
y_\ell\cdots y_1\,x_s\cdots x_j\,y_i\cdots y_t\,x_1\cdots x_r.
\]
It omits exactly \(i-\ell-1\) vertices of the \(y\)-run and \(j-r-1\) of the \(x\)-run. Thus
\[
h(y_\ell,x_r)\le 1+(i-\ell-1)+(j-r-1)
\le (i-1)-\ell+|B|.
\]
The gap count gives \(i-1\ge |A|+|B|=s\). Reversing both runs proves the second implication in (2).

For \(1<j<s\), (2) contradicts \(t<2s\). For \(j=1\), it gives \(t-i\ge s\); moreover the path \(y_t\cdots y_i\,x_1\cdots x_s\) has length \(t-i+s\le D_G(y_t,x_s)=t\), so \(i\ge s\), again impossible. The case \(j=s\) follows by reversal. This proves that the \(x\)-run is an induced path attached to its complement only by \(y_1x_s\) and \(y_tx_1\).

**3. The two attachments cannot distinguish the whole run when \(t<2s\).** Let \(H=G[\{y_1,\ldots,y_t\}]\), and put
\[
A(w)=D_H(w,y_1),\qquad B(w)=D_H(w,y_t).
\]
A simple path from \(w\in V(H)\) ending at \(x_j\) must enter the \(x\)-run at one end and follow it to \(x_j\). Both choices are attainable, so
\[
D_G(w,x_j)=\max\{A(w)+s+1-j,\ B(w)+j\}. \tag{3}
\]
For these \(s\) values to be distinct, we must have
\[
|A(w)-B(w)|\ge s-1. \tag{4}
\]
Indeed, otherwise the two affine functions in (3) cross at an integer or half-integer in \([3/2,s-1/2]\). At a half-integer crossing the two flanking indices give equal maxima; at an integer crossing its two neighbors do.

Since \(A,B\le t-1\), (4) gives \(\min(A(w),B(w))\le t-s\) everywhere. In particular \(t=s\) is impossible, since at an internal vertex of \(y_1\cdots y_t\) both distances are positive. Set
\[
p=t-s+1,\qquad 2\le p\le s.
\]
We may orient the \(y\)-path so that
\[
A(y_i)\le p-1\quad\text{for all }1\le i\le p. \tag{5}
\]
In fact, for \(i<p\) we have \(B(y_i)\ge t-i\ge s>p-1\), forcing (5). At \(i=p\) we have \(B(y_p)\ge s-1\), which likewise suffices if \(p<s\). If \(p=s\), then \(t=2s-1\) and \(y_p\) is the middle vertex, so we can reverse the path to put its smaller distance on the \(A\) side.

Now \(A(y_p)=p-1\) by (5) and the path from \(y_1\). Since \(B(y_p)\ge s-1\ge A(y_p)\), (4) forces
\[
B(y_p)\ge (p-1)+(s-1)=t-1. \tag{6}
\]
But (5) makes this impossible. To see why, split the path into \(L=\{y_1,\ldots,y_p\}\) and \(R=\{y_{p+1},\ldots,y_t\}\). If any \(y_i\) with \(i<p\) has a neighbor in \(R\), start at \(y_1\), follow the path to \(y_i\), cross to that neighbor, travel within \(R\) to \(y_{p+1}\), then follow \(y_p,\ldots,y_{i+1}\). This simple path visits all \(p\) vertices of \(L\) and at least one of \(R\), yet ends in \(L\), contradicting (5). Hence \(y_p\) is the only vertex of \(L\) adjacent to \(R\). A simple \(y_t,y_p\)-path therefore stays in \(R\) until its final vertex, giving \(B(y_p)\le t-p<t-1\), contrary to (6).

This contradiction proves the upper bound.

**Equality.** On \(C_{3k}\) in the stated range, label vertices modulo \(3k\) and take \(S\) to be the multiples of \(3\). For distinct vertices \(D(w,x)=3k-d(w,x)\). Two distinct vertices \(x,x'\) at the same cycle distance from \(w\) satisfy \(x+x'\equiv2w\pmod{3k}\). If \(x,x'\in S\), reduction modulo \(3\) forces \(w\in S\). Thus \(S\) is a DDD set of size \(k\), attaining the bound.

CONFIDENCE: 99.9%. The most delicate step is (2), where a chord creates a second gap constraint; the explicit simple path and omitted-vertex count verify it directly.