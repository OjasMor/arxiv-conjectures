"""Numerical checks for the proof of Conjecture 1.19 of arXiv:2611.32519 (exact rational arithmetic).

1. H(n,k) = n^k / (1/F_1^k + ... + 1/F_n^k) is an integer only for n = 1, 2 when 3 <= k <= 12, n <= 300.
2. The key lemma: with S(n,k) = U/V in lowest terms and p the largest prime <= n (n >= 7), F_p^k divides V
   and F_p >= n. Checked for 7 <= n <= 120, 1 <= k <= 6.
3. The paper's own values for k = 1, 2 (its Theorem 1.18) are reproduced, to confirm the indexing F_1 = F_2 = 1.
"""
from fractions import Fraction

F = [0, 1, 1]
while len(F) < 400:
    F.append(F[-1] + F[-2])


def is_prime(m):
    return m > 1 and all(m % q for q in range(2, int(m ** 0.5) + 1))


# 1
integral = []
for k in range(1, 13):
    S = Fraction(0)
    for n in range(1, 301):
        S += Fraction(1, F[n] ** k)
        if (Fraction(n ** k) / S).denominator == 1:
            integral.append((k, n))
assert [x for x in integral if x[0] >= 3] == [(k, n) for k in range(3, 13) for n in (1, 2)]
assert [x for x in integral if x[0] == 1] == [(1, 1), (1, 2)] and [x for x in integral if x[0] == 2] == [(2, 1), (2, 2), (2, 3)]
print("1. integral cases for k <= 12, n <= 300:", integral)

# 2
for k in range(1, 7):
    S = sum(Fraction(1, F[i] ** k) for i in range(1, 7))
    for n in range(7, 121):
        S += Fraction(1, F[n] ** k)
        p = max(q for q in range(2, n + 1) if is_prime(q))
        assert 2 * p > n and F[p] >= 2 * p - 1 >= n
        assert S.denominator % (F[p] ** k) == 0 and S.denominator >= n ** k and S.numerator > n ** k
print("2. key lemma holds for 7 <= n <= 120, k <= 6")

# 3
vals1 = [Fraction(n) / sum(Fraction(1, F[i]) for i in range(1, n + 1)) for n in range(1, 6)]
vals2 = [Fraction(n * n) / sum(Fraction(1, F[i] ** 2) for i in range(1, n + 1)) for n in range(1, 6)]
assert vals1 == [1, 1, Fraction(6, 5), Fraction(24, 17), Fraction(150, 91)]
assert vals2 == [1, 2, 4, Fraction(576, 85), Fraction(22500, 2161)]
print("3. paper's values for k = 1, 2 and n <= 5 reproduced")
