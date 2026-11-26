"""Verify the counterexample to Question 7.1 of arXiv:2611.20344 (our own code).
Up-down graph: x -> ceil(3x/2) (up) and x -> ceil(x/2) (down). A cycle of a map T_S is a simple directed cycle:
all vertices distinct, so each vertex has one chosen direction. Question 7.1 asks whether every cycle with
l steps, a of them up, satisfies 2^l < 3^(a+1)."""
from math import ceil
from fractions import Fraction

RUNS = [12,1,2,1,2,1,2,1,1,1,2,3,1,3,9,1,2,1,1,2,4,4,6,1,2,2,1,1,4,2,3,2,2,2,1,2,2,1,6,1,1,5,6,1,3,2,6,2,3,2,1,1,2,1,1,1,4,1,1,7]
word = "".join(("U" if i % 2 == 0 else "D") * n for i, n in enumerate(RUNS))
x, cycle = 2, []
for step in word:
    cycle.append(x)
    x = ceil(Fraction(3 * x, 2)) if step == "U" else ceil(Fraction(x, 2))
assert x == 2, "does not close"
assert len(set(cycle)) == len(cycle), "repeats a vertex"
S = sorted(v for v, s in zip(cycle, word) if s == "U")          # the set S on the cycle: where the map goes up
# replay as the map T_S restricted to the cycle
y = 2
for _ in range(len(cycle)):
    y = ceil(Fraction(3 * y, 2)) if y in set(S) else ceil(Fraction(y, 2))
assert y == 2
l, a = len(cycle), word.count("U")
print("length l =", l, " ups a =", a, " min =", min(cycle), " max =", max(cycle))
print("2^l      =", 2 ** l)
print("3^(a+1)  =", 3 ** (a + 1))
print("2^l < 3^(a+1)?", 2 ** l < 3 ** (a + 1), "  ratio 2^l/3^a =", float(Fraction(2 ** l, 3 ** a)))
print("cycle:", cycle)
