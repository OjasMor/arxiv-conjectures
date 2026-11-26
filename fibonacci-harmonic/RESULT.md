# Conjecture 1.19 of arXiv:2611.32519 is true: harmonic means of powers of Fibonacci numbers

Status as of 2026-11-25: a short elementary proof, found by GPT-6.2 Astra in one attempt and read line by line
by Claude. Checked numerically with separate code. No human mathematician has reviewed it.

## Source

Sagar Mandal and Mohan, "Integral Means of Fibonacci Numbers: Divisibility, Density, and Arithmetic
Progressions", arXiv:2611.32519 (math.NT, 24 Nov 2026, v1). With F_1 = F_2 = 1:

> Conjecture 1.19. Let k ≥ 3. Then n^k / (1/F_1^k + 1/F_2^k + ... + 1/F_n^k) is an integer if and only if
> n = 1, 2.

The authors prove the cases k = 1 and k = 2 (their Theorem 1.18) by a 2-adic argument, say that this method
"does not extend to higher powers", and report a computer check for k = 3, 4, 5 and n ≤ 10^4.

## Proof

Write S = 1/F_1^k + ... + 1/F_n^k = U/V in lowest terms, so the quantity is H = n^k V / U.

**Step 0.** For n = 1, H = 1. For n = 2, H = 2^k / 2 = 2^(k-1). Both are integers.

**Step 1 (reduction).** Let n ≥ 2. If H is an integer then U divides n^k V, and gcd(U, V) = 1, so U divides
n^k. Since S ≥ 2 > 1 we have U > V. So it is enough to show V ≥ n^k: then U > n^k and U cannot divide n^k.

**Step 2 (lemma).** If F_r is coprime to F_i for every i ≤ n with i ≠ r, then F_r^k divides V.
Proof: write the sum without the r-th term as A/B in lowest terms. B divides a product of powers of the
other F_i, so gcd(B, F_r) = 1. Then S = (A F_r^k + B) / (B F_r^k), and the numerator is ≡ B mod every prime
factor of F_r, hence coprime to F_r. Nothing cancels against F_r^k.

**Step 3 (n ≥ 7).** Let p be the largest prime ≤ n. By Bertrand's postulate p > n/2, so p is the only
multiple of p in {1, ..., n}, and p ≥ 7. From gcd(F_a, F_b) = F_gcd(a,b), F_p is coprime to every other F_i
with i ≤ n. Also F_j ≥ 2j − 1 for all j ≥ 7 (F_7 = 13 and F_(j+1) − F_j = F_(j−1) ≥ 2), so
F_p ≥ 2p − 1 ≥ n. By the lemma V ≥ F_p^k ≥ n^k.

**Step 4 (n = 4, 5, 6).** For n = 4 the numbers are 1, 1, 2, 3: both 2 and 3 are coprime to the rest, so
6^k divides V and 6^k ≥ 4^k. For n = 5, 6 the numbers are 1, 1, 2, 3, 5, (8): both 3 and 5 are coprime to
the rest, so 15^k divides V and 15^k ≥ 6^k.

**Step 5 (n = 3).** S = 2 + 2^(−k), so H = 6^k / (2^(k+1) + 1). The denominator is odd, so it would have to
divide 3^k, i.e. 2^(k+1) + 1 = 3^a. For k ≥ 3 the left side is ≡ 1 mod 8, so a is even, and
(3^(a/2) − 1)(3^(a/2) + 1) = 2^(k+1). Two powers of 2 that differ by 2 are 2 and 4, giving k = 2. So there
is no solution with k ≥ 3. (For k = 2 it gives H = 4, which is the exceptional case n = 3 in the authors'
Theorem 1.18.) ∎

Steps 1 to 4 do not use k ≥ 3, so they also give a second proof of the n ≥ 4 part of the authors' theorem
for k = 1, 2.

## Verification

- `check.py` (our code, exact rationals): the only integral cases with k ≤ 12 and n ≤ 300 are the stated
  ones; the lemma's conclusion (F_p^k divides V, F_p ≥ n) holds for 7 ≤ n ≤ 120, k ≤ 6; the paper's values
  for k = 1, 2 are reproduced, which confirms the indexing.
- `ASTRA_ATTEMPT.md`: the model's output ($0.49 of OpenAI spend).
- `REFEREE_astra.md`: a fresh-context referee pass.
- Not formalized in Lean.

## Prior work (checked 2026-11-25)

The paper is v1, one day old. No arXiv paper cites it. Nothing on it in github.com/1337isnot1337/solved-conjectures
(files, issue and PR titles). The authors have not been asked.

Checked on GitHub by repository search (name, description, README) for the arXiv id and keywords, and inside the collection repositories we know of (1337isnot1337/solved-conjectures, s66lem/conjectures, the-omega-institute/trureturing, AmirMakir/broken-conjectures and others); on X by arXiv id; and by web search. Nothing found. This is a search, not a guarantee: several people are working through the same papers this week.
