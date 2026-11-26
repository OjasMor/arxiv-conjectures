# arXiv:2611.32928 [conj:rateBound]

status: completed cost: $0.4783 incomplete: None

TARGET: \label{conj:rateBound}
The quantity $esr(\bar{Q})$ is an upper bound for the exponential convergence rate $R$, i.e.,
$$
R \leq esr(\bar{Q}) 
$$

---

VERDICT: DISPROVED

STATEMENT: “The quantity \(esr(\bar{Q})\) is an upper bound for the exponential convergence rate \(R\), i.e., \(R \leq esr(\bar{Q})\).” On \(K_4\) with uniform i.i.d. broadcasts and the paper’s regular-graph weights, **\(R\geq 2/3>5/8=esr(\bar Q)\)**.

DEGENERATE: no — \(K_4\) is connected and simple, the step size is strictly inside the allowed interval, and the initial memories agree with the initial estimates.

CERTIFICATE:
```json
{
  "vertices": [1, 2, 3, 4],
  "communication_graph": "K4",
  "measurement_arcs": "one ordered arc (i,j) for every pair i != j",
  "noise_covariance_matrix": "12-by-12 identity",
  "epsilon": "1/8",
  "broadcast_law": "independent at each iteration",
  "beta": ["1/4", "1/4", "1/4", "1/4"],
  "xi_initial_current": [1, 0, 0, 0],
  "xi_initial_memory": [1, 0, 0, 0]
}
```

ARGUMENT: The measurement values do not enter the homogeneous recursion for \(\xi\). Here \(d_{\max}=3\), \(R_{\min}=1\), and \(0<\epsilon=1/8<1/6\). Since both measurement directions are present, every off-diagonal weight is \(2\epsilon=1/4\); the diagonal weights are also \(1/4\).

**Mean-matrix check.** As checks against the paper, the program below reproduces \(esr(P)=0\) for complete graphs and the eigenvalue \(s_2^{(1)}=1-(\nu^2+1)/(N(\nu+1))\) of \(\bar Q\): it gives \(4/9\) on \(K_3\) and \(3/8\) on \(K_4\). This eigenvalue need not be the second-largest in modulus. On \(K_4\), direct construction from the broadcast updates gives
\[
\det(tI-\bar Q)=(t-1)(t-3/8)(t-5/8)^3(t-1/2)^3.
\]
Thus \(esr(\bar Q)=5/8\), using the paper’s definition rather than its separate complete-graph corollary.

**Mean-square lower bound.** The key is that a broadcast changes only **one** of the \(N\) memory coordinates. Write \(\xi=(x,y)\), with \(y\) the memory-error vector, and let
\[
V(y)=\min_c\sum_j(y_j-c)^2=\frac1N\sum_{j<\ell}(y_j-y_\ell)^2.
\]
When node \(i\) broadcasts, \(y_i\) is replaced by \(x_i\) and every other memory is retained. Whatever \(x_i\) is, the new variance is at least the minimum sum of squares on the retained coordinates alone:
\[
V(y^+)\ \geq\ \min_c\sum_{j\ne i}(y_j-c)^2
=\frac1{N-1}\sum_{\substack{j<\ell\\j,\ell\ne i}}(y_j-y_\ell)^2.
\]
Under a uniform independent broadcast, each pair is retained with probability \((N-2)/N\). Consequently
\[
\mathbb E[V(y^+)\mid \xi]\ \geq\ \frac{N-2}{N-1}V(y).
\]
For \(N=4\) the factor is \(2/3\). Moreover, \(\|\Omega\xi\|^2\) minimizes the sum of squares over **all** eight coordinates about one constant, so it is at least \(V(y)\). Iterating from the certified initialization, for which \(V(y(0))=3/4\), gives
\[
\mathbb E\|\Omega\xi(k)\|^2\ \geq\ \frac34(2/3)^k .
\]
Taking \(k\)-th roots and the limsup proves \(R\geq 2/3\) from this one initial condition. The strict gap is at least \(1/24\).

**Exact verification code** (Python/SymPy). The squares identity also checks the one-step variance inequality directly on the update matrices.
```python
import sympy as s

t = s.symbols('t')

def complete(n):
    P = s.ones(n)/n
    E = s.eye(2*n)
    qs = []
    for i in range(n):
        Q = E.copy()
        Q[n+i, :] = E[i, :]                 # refresh memory i
        for j in range(n):
            if j != i:
                Q[j, :] = (E[j, :] + E[i, :] +
                           sum((E[n+h, :] for h in range(n) if h not in (i,j)),
                               s.zeros(1, 2*n)))/n
        qs.append(Q)
    return P, qs

for n in (3, 4):
    P, qs = complete(n)
    avg = sum(qs, s.zeros(2*n))/n
    print(n, s.factor(P.charpoly(t).as_expr()),
          s.factor(avg.charpoly(t).as_expr()))

# Now qs is for K4. The quadratic form of D is V(y).
H = s.eye(n) - s.ones(n)/n
D = s.diag(s.zeros(n), H)
B = s.eye(n).row_join(-(s.ones(n) - s.eye(n))/(n-1))
LD = sum((Q.T*D*Q for Q in qs), s.zeros(2*n))/n
print("squares identity:", LD - s.Rational(2,3)*D == s.Rational(3,16)*B.T*B)
print("gap at least:", s.Rational(2,3) - s.Rational(5,8))
```

Observed output:
```text
3 t**2*(t - 1) (t - 1)*(9*t - 4)*(9*t**2 - 10*t + 3)**2/729
4 t**3*(t - 1) (t - 1)*(2*t - 1)**3*(8*t - 5)**3*(8*t - 3)/32768
squares identity: True
gap at least: 1/24
```

CONFIDENCE: \(>99.99\%\). The point most sensitive to interpretation is that the paper defines \(R\) using \(\Omega\) on the full \(2N\)-coordinate state, including the memories. The variance lower bound uses exactly that definition; it does not assume that a computed second-moment eigenmode is attained.