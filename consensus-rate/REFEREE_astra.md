# Referee report for 2611.32928__1

status: completed cost: $0.4371

REFEREE VERDICT: CORRECT

STATEMENT MATCH: yes. Conjecture IV.4 (`conj:rateBound`) states: “The quantity \(esr(\bar{Q})\) is an upper bound for the exponential convergence rate \(R\), i.e., \(R\leq esr(\bar{Q})\).” The paper defines
\[
R=\sup_{\xi(0)}\limsup_{k\to\infty}\mathbb E[\|\Omega\xi(k)\|^2]^{1/k},
\qquad \bar Q=\mathbb E[Q_i]=\sum_i\beta_i Q_i.
\]
It specifies that in \(\Omega=I-\mathbf1\mathbf1^T/(2N)\), “\(I\) is the \(2N\)-dimensional identity matrix and the vector \(\mathbf1\) is \(2N\)-dimensional.” Thus the squared norm includes the memories, not just the current estimates. The paper defines essential spectral radius as “the second largest in absolute value eigenvalue.” With these definitions, the certificate gives **\(R\ge 2/3>5/8=esr(\bar Q)\)**.

DEGENERATE OR ALREADY KNOWN IN PAPER: no. The paper expressly considers complete graphs. The bidirected measurement graph is weakly connected, the noise covariance is positive definite, and \(0<1/8<1/6\) is strictly inside the step-size interval. Uniform i.i.d. broadcasts satisfy random persistence and Assumption `ass:1`. The initialization is permitted even if all stored copies must agree initially. The previously cited bound (`eq:rateBounds`) gives only \(25/64\le R\le 3/4\) on this instance; it does not decide the conjecture.

DETAILS:

**Independent reconstruction.** I formed the incidence matrix from the ordered measurement arcs, computed \(P=I-\epsilon A^TA\), and implemented each broadcast as two operations in the paper’s specified order: refresh the sender’s memory, then update the listening nodes using the refreshed memories. My reconstruction code was:

```python
import sympy as s

def rebuild(n):
    I, Z = s.eye(n), s.zeros(n)
    A = s.Matrix([[int(h == a) - int(h == b) for h in range(n)]
                  for a in range(n) for b in range(n) if a != b])
    P = I - A.T*A/(2*n)             # unit covariances, epsilon = 1/(2n)
    D = s.diag(*P.diagonal())
    M = P - D
    Q = []
    for i in range(n):
        F = I[:, i]*I[:, i].T
        L = s.diag(*(int(M[j, i] != 0) for j in range(n)))
        refresh = I.row_join(Z).col_join(F.row_join(I-F))
        update = (I-L+L*D).row_join(L*M).col_join(Z.row_join(I))
        Q.append(update * refresh)
    return P, Q
```

Exact characteristic-polynomial outputs for the uniform mean were
\[
\begin{array}{c|l|l}
 &\det(tI-P)&\det(tI-\bar Q)\\ \hline
 K_3&t^2(t-1)&(t-1)(9t-4)(9t^2-10t+3)^2/729\\
 K_4&t^3(t-1)&(t-1)(t-3/8)(t-5/8)^3(t-1/2)^3 .
\end{array}
\]
These reproduce the paper’s \(esr(P)=0\) and its stated eigenvalue \(s_2^{(1)}=1-(\nu^2+1)/(N(\nu+1))\): respectively \(4/9\) and \(3/8\). On \(K_4\), \(3/8\) is an eigenvalue but **not** the essential spectral radius.

**Mean-square check.** For \(V(y)=\min_c\sum_j(y_j-c)^2\), removing the refreshed coordinate from the sum before minimizing gives a lower bound on \(V(y^+)\). Each old pair of coordinates survives with conditional probability \((N-2)/N\). Applying the pairwise variance identity to the \(N-1\) retained coordinates therefore gives
\[
\mathbb E[V(y^+)\mid \xi]\ \ge\ \frac{N-2}{N-1}V(y).
\]
I also checked this directly on the reconstructed matrices. With \(D_y=\operatorname{diag}(0_N,I-\mathbf1\mathbf1^T/N)\), the exact eigenvalues of
\(\tfrac14\sum_iQ_i^TD_yQ_i-\tfrac23D_y\) on \(K_4\) were **\(0\)** (multiplicity 4), **\(5/24\)** (3), and **\(3/8\)** (1). Thus the inequality holds for every state, not just along a simulated trajectory.

The full-state squared distance to consensus is at least \(V(y)\), and the certified initial memory has \(V(y(0))=3/4\). Iteration gives \(\mathbb E\|\Omega\xi(k)\|^2\ge(3/4)(2/3)^k\) for every \(k\). Taking \(k\)-th roots proves the lower bound for this one initialization, which suffices for the supremum defining \(R\). No step of the counterexample fails.

**Error in the paper, not the certificate.** Corollary `thm:proofComplete` prints \(2(N-1)/N\), which gives \(3/2\) on \(K_4\), impossible for a stochastic matrix. Its appendix instead gives \(2(N-1)/N^2=3/8\). This is not fixed merely by correcting the denominator: the appendix selects the wrong eigenvalue. In fact, substituting \(N=4,\nu=3\) into the finite-\(N\) threshold in Theorem `thm:LowerBoundRate` gives \(\gamma^*=(9-\sqrt{26})/2>1\), so the appendix’s assertion \(1-esr(P)=1>\gamma^*\) fails. The direct spectrum above resolves the discrepancy.

WHAT A HUMAN EXPERT SHOULD STILL CHECK: For publication or priority, check whether a later version or erratum corrects the complete-graph corollary or changes the conjecture. No such correction is needed to decide the claim against the supplied text.