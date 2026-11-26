# arXiv:2611.20820 [conj:skew]

status: completed cost: $0.4918 incomplete: None

TARGET: \label{conj:skew}
Let $n>r\ge 1$, and let $v_1,\ldots,v_k\in\F^n$ satisfy
$d_H(v_i,v_j)\le r$ for all $i$ and $j$. If there exist
$w_1,\ldots,w_k\in\F^n$ such that $d_H(w_i,v_i)\ge r+1$ for every $i$
and $d_H(w_i,v_j)\le r$ whenever $j<i$, then $k\le 2^r$.

---

VERDICT: PROVED

STATEMENT: “Let \(n>r\ge 1\), and let \(v_1,\ldots,v_k\in\mathbb F_2^n\) satisfy \(d_H(v_i,v_j)\le r\) for all \(i\) and \(j\). If there exist \(w_1,\ldots,w_k\in\mathbb F_2^n\) such that \(d_H(w_i,v_i)\ge r+1\) for every \(i\) and \(d_H(w_i,v_j)\le r\) whenever \(j<i\), then \(k\le 2^r\).”

DEGENERATE: no — the proof covers every \(n>r\ge1\), and the bound is attained for every such pair.

CERTIFICATE: Not applicable (proof).

ARGUMENT: **Append the swapped pairs in reverse order.** Consider the following list of \(2k\) ordered pairs:
\[
(v_1,w_1),\ldots,(v_k,w_k),\quad
(w_k,v_k),\ldots,(w_1,v_1).
\]
Each pair has distance at least \(r+1\). We claim that the first entry of every earlier pair is within distance \(r\) of the second entry of every later pair. There are three cases:

- Within the first half, this is \(d_H(v_i,w_j)\le r\) for \(i<j\).
- From the first half to the second, this is \(d_H(v_i,v_j)\le r\) for arbitrary \(i,j\).
- Within the second half, the earlier pair has the larger original index, so this is \(d_H(w_i,v_j)\le r\) for \(i>j\).

Thus the doubled list is an ordinary skew Hamming set-pair system. The Gao–Zhao bound quoted in the paper gives \(2k\le 2^{r+1}\), hence \(k\le 2^r\).

**Self-contained verification of the binary skew bound.** To remove any dependence on the cited preprint, put \(m=r+1\). Over the rational function field \(K=\mathbb F_2(t_{sh}:1\le s\le n,\ 1\le h\le m)\), form the \(2^m\)-dimensional algebra
\[
R=K[X_1,\ldots,X_m]/(X_1^2,\ldots,X_m^2).
\]
Let \(\lambda\) extract the coefficient of \(X_1\cdots X_m\). For each coordinate \(s\), put \(L_s=\sum_{h=1}^m t_{sh}X_h\), and encode a binary word \(x\) by
\[
P(x)=\prod_{s:x_s=1}(1+L_s).
\]
In characteristic two, \(L_s^2=0\), so \((1+L_s)^2=1\). Consequently
\[
P(x)P(y)=\prod_{s:x_s\ne y_s}(1+L_s).
\]
If \(d_H(x,y)<m\), this product has degree less than \(m\), so \(\lambda(P(x)P(y))=0\). If \(d_H(x,y)\ge m\), choose \(m\) differing coordinates \(s_1,\ldots,s_m\). Specializing the coefficients so that \(L_{s_h}=X_h\) and all other \(L_s=0\) gives top coefficient \(1\). Hence the top coefficient before specialization is a nonzero polynomial.

For any skew list \((a_i,b_i)_{i=1}^{q}\), the matrix \(\bigl[\lambda(P(a_i)P(b_j))\bigr]_{i,j}\) is therefore lower triangular with nonzero diagonal. Its rank is \(q\). But its columns evaluate the linear functionals \(u\mapsto\lambda(uP(b_j))\) on elements of \(R\), so its rank is at most \(\dim_K R=2^m\). This proves exactly the bound used above.

**Small-case checks.** I also computed the exact maximum \(k\) in Python. After a prefix, let \(C\) be the intersection of the radius-\(r\) balls about its chosen \(v_j\), initially the whole cube. A candidate \(v\in C\) is legal exactly when \(C\setminus B(v,r)\ne\varnothing\): any point of that difference is a witness. Memoizing the longest chain of legal updates \(C\gets C\cap B(v,r)\) gave
\[
\begin{array}{c|rrrrrr}
(n,r)&(3,1)&(4,2)&(5,2)&(4,3)&(5,3)&(6,3)\\ \hline
\max k&2&4&4&8&8&8 .
\end{array}
\]
The first four reproduce cases stated in the paper; the last two go beyond its stated exact range for the close-skew invariant. In general, sharpness follows by taking the \(v_i\) in an \(r\)-dimensional coordinate subcube and their witnesses to be their respective antipodes in a containing \((r+1)\)-dimensional coordinate subcube.

CONFIDENCE: \(>99.99\%\). The key indexing step is the reversal of the second half: it ensures that no distance \(d_H(w_i,w_j)\), which the hypotheses do not control, is ever required.