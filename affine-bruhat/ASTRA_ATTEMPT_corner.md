# arXiv:2611.19137 [conj:CornerCovers]

status: completed cost: $1.5272 incomplete: None

TARGET: \label{conj:CornerCovers} Let $\lambda' \in Q^\vee$, let $u' = \oppC(\lambda')$, and let $x' = t^{\lambda'}u' \in \eW$.  For all $u \in \sW$, let \[ x'_u = t^{\lambda'_u}u = \pr(u \to u')x' \in \eW \] and put $u_0 = u$ and $u_k = u'$, where $k = d_\Phi(u \to u')$. Then for all shortest paths $(u_0, \dots, u_k)$ from $u$ to $u'$ in the QBG, we have:
\begin{enumerate}
\item covering relations in Bruhat order
\[
x'_{u_0} \lessdot x'_{u_1} \lessdot \cdots \lessdot x'_{u_k};
\]
and
\item in Iwahori order, a sequence
\[
\lambda'_{u_0} \leq_I \lambda'_{u_1} \leq_I \cdots \leq_I \lambda'_{u_k}
\]
where for all $0 \leq j < k$, either $\lambda'_{u_j} \lessdot_I \lambda'_{u_{j+1}}$ or $\lambda'_{u_j} =\lambda'_{u_{j+1}}$.
\end{enumerate}

---

VERDICT: DISPROVED

STATEMENT: Conjecture `conj:CornerCovers` states:

> Let \(\lambda' \in Q^\vee\), let \(u' = \operatorname{oppC}(\lambda')\), and let \(x' = t^{\lambda'}u' \in \widetilde W\). For all \(u \in W\), let
> \[
> x'_u = t^{\lambda'_u}u = \operatorname{pr}(u \to u')x'
> \]
> and put \(u_0 = u\) and \(u_k = u'\), where \(k = d_\Phi(u \to u')\). Then for all shortest paths \((u_0, \dots, u_k)\) from \(u\) to \(u'\) in the QBG, we have:
> 1. covering relations in Bruhat order
> \[
> x'_{u_0} \lessdot x'_{u_1} \lessdot \cdots \lessdot x'_{u_k};
> \]
> 2. in Iwahori order, a sequence
> \[
> \lambda'_{u_0} \leq_I \lambda'_{u_1} \leq_I \cdots \leq_I \lambda'_{u_k}
> \]
> where for all \(0 \leq j < k\), either \(\lambda'_{u_j} \lessdot_I \lambda'_{u_{j+1}}\) or \(\lambda'_{u_j} =\lambda'_{u_{j+1}}\).

Part **(2)** fails: a single step skips a strictly intermediate coweight. Part **(1)** does hold, as shown below using the paper’s lower-polytope theorems.

DEGENERATE: no — the example is in irreducible type \(\widetilde A_2\), with a regular, nonzero \(\lambda'\) in the coroot lattice and a shortest path of length two.

CERTIFICATE:
```json
{
  "affine_type": "A2^(1)",
  "coordinates": "sum-zero triples; alpha_i = alpha_i^vee = e_i - e_(i+1)",
  "permutations": "one-line images of 1,2,3; w(e_i) = e_(w(i))",
  "lambda_prime": [2, -3, 1],
  "u_prime": [1, 3, 2],
  "shortest_path": [[3, 2, 1], [3, 1, 2], [1, 3, 2]],
  "lower_corners_on_path": [[-2, 1, 1], [2, -3, 1], [2, -3, 1]],
  "failed_step_zero_based": 0,
  "strict_Iwahori_intermediate": [2, 1, -3]
}
```

ARGUMENT:

**The counterexample.** Write \(\theta=e_1-e_3\), so \(s_0=s_{\theta,1}\). Take
\[
c=\lambda'=(2,-3,1),\qquad \lambda'_+=(2,1,-3).
\]
Since \(c=s_2\lambda'_+\) is regular, \(u'=\operatorname{oppC}(c)=s_2\). Consider
\[
w_0\longrightarrow s_{21}\longrightarrow s_2.
\]
These are quantum edges given by right multiplication by \(s_2\) and \(s_1\), respectively. The path is shortest: \(w_0^{-1}s_2\) is a three-cycle, not a reflection, so there is no direct edge.

By the paper’s edge-reflection definition, the reflections on this path, in order, are \(s_{\alpha_1,1}\) and \(s_{\theta,1}\): indeed \(w_0\alpha_2=-\alpha_1\) and \(s_{21}\alpha_1=-\theta\). Reading backwards from \(c\), the second reflection fixes \(c\) because \(\langle\theta,c\rangle=1\). The first then gives
\[
s_{\alpha_1,1}c=c-(5-1)\alpha_1^\vee=(-2,1,1)=:a.
\]
Thus the **first** QBG step projects to \(a\leq_I c\).

To see that this is not a cover, put
\[
b=s_0a=(2,1,-3),\qquad s_2b=c.
\]
Consider the three affine Weyl elements
\[
z_0=t^a,\qquad z_1=s_0t^a=t^b w_0,\qquad
z_2=s_2s_0t^a=t^c s_2w_0.
\]
Their lengths by the paper’s Iwahori–Matsumoto formula are \(6,7,8\), respectively. Each step is left multiplication by a simple reflection, so \(z_0\lessdot z_1\lessdot z_2\). By Proposition `prop:BruhatImpliesIwahori`, their translation vectors satisfy \(a\leq_I b\leq_I c\). All three are distinct, hence
\[
\boxed{\lambda'_{w_0}=a<_I b<_I c=\lambda'_{s_{21}}.}
\]
This disproves (2) without assuming that projection preserves covers.

**Why (1) nevertheless holds.** Fix any \(v\in W\), write \(\eta=\lambda'_v\), \(x=x'_v=t^\eta v\), and let \(P=\operatorname{poly}_{\lambda'}\). By the paper’s lower-polytope and pseudo-Weyl theorems, \(\eta\leq_I\lambda'\) and
\[
P\subseteq \eta+vC^-.
\]
Since \(x'\) is the opposite gate representative at \(\lambda'\), Corollary `cor:oppgateBruhatIwahori-eW` gives \(x\leq x'\).

For \(\beta>0\), set \(\gamma=v\beta\) and \(m=\langle\gamma,\eta\rangle\). The key inequality is
\[
m+\mathbf 1_{\gamma<0}\ \geq\ 0. \tag{*}
\]
Indeed, suppose it fails. The \(\gamma\)-coordinates of the interior of \(x\mathfrak a\) lie in \((m,m+1)\), while those of the base alcove interior lie in \((0,1)\) if \(\gamma>0\), and in \((-1,0)\) if \(\gamma<0\). Since \(m\) is integral, \(H_{\gamma,m+1}\) separates these alcoves. Its reflection \(r\) therefore satisfies \(rx<x\): fold a minimal gallery to \(x\mathfrak a\) where it crosses this hyperplane. Thus \(rx\leq x'\), implying \(r\eta\leq_I\lambda'\) and hence \(r\eta\in P\). But
\[
r\eta=\eta+\gamma^\vee=\eta+v\beta^\vee\notin\eta+vC^-.
\]
This contradiction proves \((*)\). In the paper’s terminology, it proves \(\mathrm{id}\in\mathrm{LP}(x'_v)\).

Now reindex the Iwahori–Matsumoto formula by \(\beta>0\) and use \((*)\) to remove the absolute values:
\[
\ell(x'_v)
=\sum_{\beta>0}\left|\langle v\beta,\eta\rangle+\mathbf 1_{v\beta<0}\right|
=\langle 2\rho,v^{-1}\eta\rangle+\ell(v).
\]
By Lemma `lem:lowerCornerWeight`, \(v^{-1}\eta=\lambda'_+-\mathrm{wt}(v\to u')\). Summing the defining QBG length change along a shortest path gives
\[
d_\Phi(v\to u')=\ell(u')-\ell(v)+\langle2\rho,\mathrm{wt}(v\to u')\rangle.
\]
Consequently \(\ell(x'_v)=\ell(x')-d_\Phi(v\to u')\). Along any shortest path to \(u'\), consecutive lifts differ by the prescribed affine reflection and their lengths increase by exactly one. This proves (1). The counterexample shows precisely why this length calculation does not establish (2).

**Python verification.** The first two checks reproduce the paper’s \(A_2\) shortest-path weights for \(s_{12}\to s_1\) and \(s_{21}\to s_1\), and its six distinct lower corners for \(2\alpha_1^\vee+2\alpha_2^\vee\).

```python
from itertools import permutations, combinations
from collections import deque

e, s1, s2, w0 = (1,2,3), (2,1,3), (1,3,2), (3,2,1)
W, pairs = list(permutations(e)), list(combinations(range(3),2))
def mul(u,v): return tuple(u[i-1] for i in v)
def act(u,a): return tuple(a[u.index(i)] for i in e)
def ell(u): return sum(u[i]>u[j] for i,j in pairs)
def aff(a,u):  # length of t^a u
    return sum(abs(a[i]-a[j]-(u.index(i+1)>u.index(j+1))) for i,j in pairs)

def edges(u):
    for i,j in pairs:
        v = list(u); v[i],v[j] = v[j],v[i]; v = tuple(v)
        h = ell(v)-ell(u)
        if h in (1,1-2*(j-i)):
            yield v, tuple((h!=1)*((k==i)-(k==j)) for k in range(3))

def path(u,t):  # BFS: distance and shortest-path weight
    q, seen = deque([(u,0,(0,0,0))]), {u}
    while q:
        v,d,wt = q.popleft()
        if v == t: return d,wt
        for h,b in edges(v):
            if h not in seen:
                seen.add(h)
                q.append((h,d+1,tuple(x+y for x,y in zip(wt,b))))

def corner(u,t,dom):
    return act(u,tuple(x-y for x,y in zip(dom,path(u,t)[1])))

s12,s21 = mul(s1,s2),mul(s2,s1)
print("table:", path(s12,s1), path(s21,s1))
print("distinct:", len({corner(u,e,(2,0,-2)) for u in W}))

c = (2,-3,1)
dom = tuple(sorted(c, reverse=True))
t = max((v for v in W if act(v,dom)==c), key=ell)
p = [w0,s21,t]
assert all(v in dict(edges(u)) for u,v in zip(p,p[1:]))
d = path(w0,t)[0]
assert d == 2
C = [corner(u,t,dom) for u in p]
print("target, distance, corners:", t,d,C)
print("corner lift lengths:", [aff(a,u) for a,u in zip(C,p)])

a = C[0]
b = (a[2]+1,a[1],a[0]-1)  # s_0(a)
assert act(s2,b) == c == C[1] and len({a,b,c}) == 3
L = [aff(a,e),aff(b,w0),aff(c,mul(s2,w0))]
assert L[2] == L[1]+1 == L[0]+2
print("intermediate, witness lengths:", b,L)
```

Observed output:
```text
table: (1, (0, 1, -1)) (3, (1, 0, -1))
distinct: 6
target, distance, corners: (1, 3, 2) 2 [(-2, 1, 1), (2, -3, 1), (2, -3, 1)]
corner lift lengths: [9, 10, 11]
intermediate, witness lengths: (2, 1, -3) [6, 7, 8]
```

CONFIDENCE: \(>99.99\%\) in the disproof. The order-theoretic step in the certificate is the paper’s implication from Bruhat comparison to Iwahori comparison; strictness follows from distinct coordinates. The separate proof of (1) uses the paper’s lower-polytope theorems, which are not needed for the disproof.