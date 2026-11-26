"""Check for the answer to Question 7.7 of arXiv:2611.20344.
T_S(x) = ceil(3x/2) if x in S, ceil(x/2) otherwise. A = N minus {w_n}, w_n = U^(2n+2)(n).
1. Every chain tail {x, U(x), U^2(x), ...} contains w_x, so A contains no tail of a chain.
2. For every S containing A, any three consecutive steps of any orbit multiply by at least 9/8.
   Checked for all starts up to 20000 over all possible choices at the omitted numbers."""
def U(x): return (3 * x + 1) // 2      # ceil(3x/2)
def D(x): return (x + 1) // 2          # ceil(x/2)

assert all(U(x) == -((-3 * x) // 2) and D(x) == -((-x) // 2) for x in range(1, 1000))

def w(n):
    x = n
    for _ in range(2 * n + 2): x = U(x)
    return x

holes = [w(n) for n in range(1, 70)]
assert holes[0] == 8 and all(b > 2 * a for a, b in zip(holes, holes[1:]))
W = set(holes)
# after a down step at a hole z, the next two numbers are not holes
for z in holes:
    assert D(z) not in W and U(D(z)) not in W and D(z) < U(D(z)) < z
B = 20000
assert holes[-1] > U(U(U(B)))
for x in range(1, B + 1):
    level = {x}
    for _ in range(3):
        level = {U(y) for y in level} | {D(y) for y in level if y in W}   # down is possible only at a hole
    assert 8 * min(level) >= 9 * x
# every tail meets a hole
for x in range(1, 400):
    y = x
    for _ in range(2 * x + 2): y = U(y)
    assert y in W or y == w(x)
print("first omitted numbers:", holes[:8])
print("three-step growth >= 9/8 verified for all starts up to", B)
