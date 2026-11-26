# Referee report for 2611.26570__1

status: completed cost: $0.7539

REFEREE VERDICT: CORRECT

STATEMENT MATCH: yes — Conjecture 1.3 (`conj:cylinder-boundary`) states: “For every \(k\geq 2\), the rational function \(R_k\) from [Theorem 1.2] satisfies \(R_k(k)=R_{k-1}(k)\).” The claim proves exactly this equality.

The model is the completely packed \(O(1)\) loop model on the semi-infinite cylinder of circumference \(2N\). The paper defines the event, for “\(k\geq1\) (with \(k\leq N\) on \(\mathcal C_N\)),” by
\[
F_k:=\{\omega:\pi_\omega(i)=2k+1-i\text{ for }i=1,\dots,k\}.
\]
In contrast, Theorem 1.2 specifies \(R_k\in\mathbb Q(N)\) by “\(\mathbb P_{\mathcal C_N}(F_k)=R_k(N),\qquad N>k\).” The strict inequality matters: the paper’s rotational-invariance identity already gives \(\mathbb P_{\mathcal C_k}(F_k)=R_{k-1}(k)=1/A_k\), but it does **not** identify that value with \(R_k(k)\).

DEGENERATE OR ALREADY KNOWN IN PAPER: no — The paper establishes regularity at \(N=k\) and reports checks for \(2\leq k\leq8\), but does not prove the general boundary identity. The claim obtains it as a short consequence of the paper’s entry formulas, without treating the continued matrix as an inverse Kasteleyn submatrix at \(N=k\).

DETAILS:

1. **Continuation.** For fixed \(k\), the Pfaffian of the rational entry formulas agrees with \(R_k\) at every integer \(N>k\), hence in \(\mathbb Q(N)\). It is the combined term \((-1)^Np(N-1,N-c,0)\), not the sign separately, that is replaced by its rational expression.
2. **Vanishing without a pole.** In `eq:p-rational` the product is \(D_c(N)\); in Proposition 5.1 (`prop:H_N-rational`) the outer product is \(D_{\max(c_1,c_2)}(N)\) off the diagonal. The additional denominators inside that proposition include \(4N^2-j^2\), but \(j\leq\min(c_1,c_2)-1\). Thus every \(N\)-dependent denominator index is at most \(2k-1\), even when a summation index equals \(2k\). None vanishes at \(N=k\). For \(k<c\leq2k\), the factor with \(a=k\) therefore gives a genuine zero of \(D_c(k)\). The diagonal \(H\)-term is identically zero.
3. **Row and sign.** In both white-row formulas of `lem:final-entries`, setting \(r=k-1\) gives \(k+1\leq c_1\leq2k\). This kills every \(H\)-term and the entire signed \(p\)-sum. The mixed entry retains exactly \(+\mathbbm1_{r=s}\). The paper specifies that “the white endpoint is listed first and the black endpoint second,” so the forced pair is \((2k-1,2k)\) with Pfaffian sign \(+1\). Deleting it leaves \(M_{k-1}(k)\) entry for entry: the retained formulas depend on \(r,s,N\), not on the number of blocks. **No proof step fails.**

I independently implemented the formulas in Python with exact fractions and evaluated the Pfaffians by elimination, without using the claimed last-row reduction. The checks gave:

- For \(2\leq N\leq12\) and all indices from \(1\) through \(2N\), the rational signed \(p\) and \(H_N\) formulas had **zero mismatches** against the factorial definition of \(p\) and the defining sum for \(H_N\), including the zero-extended cases.
- For every \(2\leq k\leq12\), the last white row had its sole nonzero entry \(+1\) in column \(2k\); the retained minor matched; and both Pfaffians equalled \(1/A_k\). Outputs included \(1/2,\ 1/7,\ 1/42\) for \(k=2,3,4\), and **\(1/911835460\)** for \(k=9\).
- The first three half-plane Pfaffians were **\(3/8,\ 59/1024,\ 7737/2097152\)**, reproducing the paper’s table. As a separate check in the physical range \(N>k\), direct enumeration of perfect matchings on the paper’s graph agreed with every Pfaffian for \(2\leq N\leq6\).

WHAT A HUMAN EXPERT SHOULD STILL CHECK: For priority, check the forthcoming work `[ABCR]` mentioned in the paper. A full proof of Romik’s cylindrical conjecture including \(N=k\), as announced there, would also imply this identity by rotational invariance and uniqueness of the rational function. That is separate from the correctness of the submitted proof.