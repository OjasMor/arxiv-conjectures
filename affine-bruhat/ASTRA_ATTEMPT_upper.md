# arXiv:2611.19137 [conj:UpperCovers]

status: completed cost: $1.2387 incomplete: None

TARGET: \label{conj:UpperCovers} Let $\lambda \in Q^\vee$, let $u = \gateC(\lambda)$, and let $x \in \eW$ be such that the alcove $x\fa$ is in the gate position at $\lambda$. For all $u' \in \sW$, define \[x^{u'} = \pr(u \to u')^{-1}x,\] and put $u_0 = u$ and $u_k = u'$, where $k = d_\Phi(u \to u')$. Then for all shortest paths $(u_0, \dots, u_k)$ from $u$ to $u'$ in the QBG, we have:
\begin{enumerate}
\item covering relations in Bruhat order
\[
x^{u_0} \lessdot x^{u_1} \lessdot \cdots \lessdot x^{u_k};
\]
and
\item in Iwahori order, relations
\[
\lambda^{u_0} \Ileq \lambda^{u_1} \Ileq \cdots \Ileq \lambda^{u_k}
\]
such that for all $0 \leq j < k$, either $\lambda^{u_j} \lessdot_I \lambda^{u_{j+1}}$ or $\lambda^{u_j} = \lambda^{u_{j+1}}$.
\end{enumerate}

---

VERDICT: DISPROVED

STATEMENT: Conjecture `conj:UpperCovers`:
> Let \(\lambda \in Q^\vee\), let \(u = \operatorname{gateC}(\lambda)\), and let \(x \in \widetilde W\) be such that the alcove \(x\mathfrak a\) is in the gate position at \(\lambda\). For all \(u' \in W\), define \(x^{u'} = \operatorname{pr}(u \to u')^{-1}x\), and put \(u_0 = u\) and \(u_k = u'\), where \(k = d_\Phi(u \to u')\). Then for all shortest paths \((u_0, \dots, u_k)\) from \(u\) to \(u'\) in the QBG, we have:
> 1. covering relations in Bruhat order \(x^{u_0} \lessdot x^{u_1} \lessdot \cdots \lessdot x^{u_k}\); and
> 2. in Iwahori order, relations \(\lambda^{u_0} \leq_I \lambda^{u_1} \leq_I \cdots \leq_I \lambda^{u_k}\) such that for all \(0 \leq j < k\), either \(\lambda^{u_j} \lessdot_I \lambda^{u_{j+1}}\) or \(\lambda^{u_j} = \lambda^{u_{j+1}}\).

Both assertions fail on the **same single quantum edge** \(s_1\to\mathrm{id}\) in type \(A_2\).

DEGENERATE: no — the starting coweight is regular and nonzero, and \(x\) lies in the affine Coxeter group itself. The coweight is not upper QBG-regular, so the example does not contradict the paper’s proved corollary.

CERTIFICATE:
```json
{
  "affine_type": "A2~",
  "coordinates": "triples of sum zero; alpha_1=e_1-e_2, alpha_2=e_2-e_3",
  "multiplication": "rightmost factor acts first",
  "lambda": [0, 1, -1],
  "u": "s1",
  "x": "t^lambda s2 s1 = s1 s0",
  "shortest_QBG_path": ["s1", "id"],
  "edge_reflection": "s_{alpha_1,1} = s2 s0 s2",
  "affine_Bruhat_chain": ["x", "s2 x", "s0 s2 x", "s2 s0 s2 x"],
  "affine_lengths": [2, 3, 4, 5],
  "strict_Iwahori_chain": [[0, 1, -1], [0, -1, 1], [2, -1, -1]]
}
```

ARGUMENT: Take \(\lambda=\alpha_2^\vee=(0,1,-1)\). Its dominant representative is \(\lambda_+=(1,0,-1)\), with \(\lambda=s_1\lambda_+\). Since \(\lambda\) is regular, \(u=\operatorname{gateC}(\lambda)=s_1\). The gate representative is
\[
x=t^\lambda u w_0=t^\lambda s_2s_1=s_1s_0.
\]
This also follows by minimizing length over \(t^\lambda W\), as checked below.

The edge \(s_1\to\mathrm{id}\) is quantum of weight \(\alpha_1^\vee\): the finite length change is \(-1=1-\langle 2\rho,\alpha_1^\vee\rangle\). Being a single edge between distinct vertices, it is shortest. Its assigned reflection is
\[
r=s_{-s_1\alpha_1,1}=s_{\alpha_1,1}=s_2s_0s_2,
\]
where the last equality holds because \(s_0=s_{\alpha_1+\alpha_2,1}\) and \(s_2(\alpha_1+\alpha_2)=\alpha_1\). Thus \(x^{s_1}=x\) and \(x^{\mathrm{id}}=rx\). For the upper corner I use \(\lambda^{\mathrm{id}}=r\lambda\), as in the paper’s unpacking of its definition (the definition’s displayed \(\lambda'\) is unbound).

Here is what happens when the three simple factors of \(r\) act on \(x\). The lengths are given by the paper’s Iwahori–Matsumoto formula.

| Element | Translation vector | Spherical direction | Length |
|---|---|---|---:|
| \(x\) | \((0,1,-1)\) | \(s_2s_1\) | 2 |
| \(s_2x\) | \((0,-1,1)\) | \(s_1\) | 3 |
| \(s_0s_2x\) | \((2,-1,-1)\) | \(s_1s_2\) | 4 |
| \(s_2s_0s_2x=rx\) | \((2,-1,-1)\) | \(w_0\) | 5 |

Each row after the first is obtained by left multiplication by a simple reflection increasing length. The table therefore gives **three** successive Bruhat covers from \(x\) to \(rx\), not one. This disproves (1).

For (2), Bruhat inequalities imply Iwahori inequalities between translation vectors, by the paper’s Proposition `prop:BruhatImpliesIwahori`. Applying this to the first three rows gives
\[
\lambda^{s_1}=(0,1,-1)
\;<_{I}\; (0,-1,1)
\;<_{I}\; (2,-1,-1)=\lambda^{\mathrm{id}}.
\]
Both inequalities are strict because the vectors are distinct. Thus the proposed step is neither equality nor an Iwahori cover.

**Verification code.** The first three outputs reproduce entries of the paper’s \(A_2\) weight and edge-reflection tables. A reflection label \((a,b,k)\) denotes \(s_{e_a-e_b,k}\). The last two columns of the step-by-step output give the affine length and the minimum length in the translation vector’s coset.

```python
from itertools import permutations, combinations

E = (0,1,2)
W = list(permutations(E))
P = list(combinations(E,2))
S1, S2, W0 = (1,0,2), (0,2,1), (2,1,0)

def mul(p,q): return tuple(p[i] for i in q)
def act(p,z): return tuple(z[p.index(i)] for i in E)
def finlen(p): return sum(p[i] > p[j] for i,j in P)

def edge(p,q):
    for i,j in P:
        h = list(E)
        h[i],h[j] = h[j],h[i]
        if mul(p,h) != q: continue
        d = finlen(q)-finlen(p)
        if d not in (1, 1-2*(j-i)): continue
        k = int(d != 1)
        weight = tuple(k*((n==i)-(n==j)) for n in E)
        a,b = sorted((p[i]+1,p[j]+1))
        return weight, (a,b,k)

def afflen(z,p):
    return sum(abs(z[i]-z[j]-(p.index(i)>p.index(j))) for i,j in P)

for p,q in [(S1,E),(S1,mul(S1,S2)),(W0,E)]:
    print(edge(p,q))

z = (0,1,-1)
u = min((p for p in W if act(p,(1,0,-1)) == z), key=finlen)
p = min(W, key=lambda h: afflen(z,h))
assert u == S1 and p == mul(S2,S1)
assert edge(u,E) == ((1,-1,0),(1,2,1))
print("initial coset lengths:", sorted(afflen(z,h) for h in W))
for step in ("start","s2","s0","s2"):
    if step == "s2":
        z,p = act(S2,z),mul(S2,p)
    elif step == "s0":
        z,p = (z[2]+1,z[1],z[0]-1),mul(W0,p)
    print(step,z,afflen(z,p),min(afflen(z,h) for h in W))
```

Observed output:
```text
((1, -1, 0), (1, 2, 1))
((0, 0, 0), (1, 3, 0))
((1, 0, -1), (1, 3, 1))
initial coset lengths: [2, 3, 3, 4, 4, 5]
start (0, 1, -1) 2 2
s2 (0, -1, 1) 3 3
s0 (2, -1, -1) 4 4
s2 (2, -1, -1) 5 4
```

CONFIDENCE: \(>99.99\%\). The most convention-sensitive step is the choice of gate representative; it agrees both with the paper’s regular-gate formula and with direct minimization over all six representatives.