# arXiv:2611.20344 [q:forcing]

status: completed cost: $0.6811 incomplete: None

TARGET: \label{q:forcing}
Does every force-divergent set, that is, every $A$ such that $T_S$ is unbounded for all $S\supseteq A$,
contain a tail of a chain?

---

VERDICT: DISPROVED

STATEMENT: “Does every force-divergent set, that is, every \(A\) such that \(T_S\) is unbounded for all \(S\supseteq A\), contain a tail of a chain?”

DEGENERATE: no — both \(A\) and its complement are infinite. In fact, every orbit diverges for every \(S\supseteq A\).

CERTIFICATE:
```json
{
  "domain": "N = {1,2,3,...}",
  "A": "N minus {w(n) : n in N}",
  "w(n)": {
    "initial_value_of_x": "n",
    "update": "x = (3*x + 1)//2",
    "number_of_updates": "2*n + 2",
    "return": "x"
  }
}
```

ARGUMENT: With the paper’s \(U(x)=\lceil 3x/2\rceil\) and \(D(x)=\lceil x/2\rceil\), the omitted numbers are
\[
w_n=U^{2n+2}(n),\qquad n\ge1.
\]
For **every** starting integer \(x\), its chain tail \(\{U^j(x):j\ge0\}\) contains the omitted number \(w_x\). Thus \(A\) contains no chain tail.

The key is that the omissions are more than a factor of two apart. Indeed, \(w_1=8\), and monotonicity of \(U\) gives
\[
w_{n+1}=U^{2n+4}(n+1)\ \ge\ U^{2n+4}(n)
=U^2(w_n)\ \ge\ \tfrac94 w_n>2w_n.
\]
Put \(w_0=0\) for notation only. For \(z=w_n\), we have \(z\ge8\), so
\[
w_{n-1}<\frac z2\le D(z)<U(D(z))
\le\frac{3z+5}{4}<z=w_n.
\]
The upper bound uses \(D(z)\le(z+1)/2\) and \(U(y)\le(3y+1)/2\). Thus **both \(D(w_n)\) and \(U(D(w_n))\) belong to \(A\)**: they lie strictly between consecutive omissions, or below the first omission when \(n=1\).

Now fix any \(S\supseteq A\). A down step can occur only at an omission \(w_n\), and the next two steps are then forced up. Hence every three consecutive steps include at least two ups. Since an up step multiplies by at least \(3/2\) and a down step by at least \(1/2\),
\[
T_S^3(x)\ge \tfrac98 x\qquad\text{for every }x\ge1.
\]
For each \(r=0,1,2\), it follows that \(T_S^{3k+r}(x)\ge(9/8)^kT_S^r(x)\to\infty\). This proves force-divergence without any assumption on the choices made outside \(A\).

**Verification code.** The first check reproduces the paper’s chain of \(1\) and its counts through \(10^{60}\): \(340\) terms, \(173\) even. The four-residue checks verify the local inequalities using the indicated translation identities. The final enumeration is an additional finite check of all allowed three-step paths, not an extrapolation to infinite orbits.

```python
def U(x): return (3*x + 1)//2
def D(x): return (x + 1)//2

def w(n):
    x = n
    for _ in range(2*n + 2):
        x = U(x)
    return x

chain = []
x = 1
while x <= 10**60:
    chain.append(x)
    x = U(x)
print("chain:", chain[:8], len(chain), sum(x % 2 == 0 for x in chain))

holes = [w(n) for n in range(1, 65)]
print("first omissions:", holes[:8])
assert holes[0] == 8
# Under x -> x+4, U(U(x)), D(x), U(D(x)) increase by 9, 2, 3.
assert all(U(U(x)) > 2*x for x in range(1, 5))
assert all(D(x) < U(D(x)) < x for x in range(8, 12))
assert all(2*a < b for a, b in zip(holes, holes[1:]))

B = 10000
assert holes[-1] > U(U(B))  # covers every possible source of the third step
W = set(holes)
for x in range(1, B+1):
    p = {x}
    for _ in range(3):
        p = {U(y) for y in p} | {D(y) for y in p if y in W}
    assert 8*min(p) >= 9*x
print("three-step bound verified for starts 1 through", B)
```

Observed output:
```text
chain: [1, 2, 3, 5, 8, 12, 18, 27] 340 173
first omissions: [8, 27, 93, 243, 710, 1850, 5165, 12137]
three-step bound verified for starts 1 through 10000
```

CONFIDENCE: 99.99%. The step most sensitive to rounding is \(U(D(w_n))<w_n\); the explicit bound \((3w_n+5)/4<w_n\) holds from the first omission onward.