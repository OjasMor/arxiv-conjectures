# Conjecture 8 of arXiv:2611.18194 is false: the Möbius function of the factorization poset of 2^7 · 3^6

Status as of 2026-11-25: a counterexample found by GPT-6.2 Astra in one attempt ($0.21) and re-computed by
separate code with two independent recursions. A finite computation anyone can repeat. Not reviewed by a human.

## Source

Madjid Mirzavaziri, Daniel Yaqubi, "The Möbius function of factorizations with a simple prime factor",
arXiv:2611.18194 (math.CO, 13 Nov 2026). The factorizations of n into integers greater than 1 (order ignored)
are ordered by refinement, with the prime factorization at the bottom and n itself at the top.

> Conjecture 8. The Möbius function between the prime factorization of n and n is either 0 or has the sign
> (−1)^(Ω(n)+1), and it vanishes for n = p^k with k ≥ 3.

The paper proves the sign statement when n has a prime factor of exponent 1, and reports that it holds in every
case computed, "which includes all n with Ω(n) ≤ 8".

## Counterexample

n = 2^7 · 3^6 = 93312. Here Ω(n) = 13, so the predicted sign is +. The poset has 1,752 elements and

    μ(prime factorization, n) = −57.

It is the only violation among all prime signatures with every exponent ≥ 2 and Ω ≤ 13 (the neighbours behave:
(6,6) gives −4, (8,5) gives 50, (7,5) gives −31), so 93312 is the smallest counterexample of this kind that we
know. The second half of the conjecture (prime powers) holds in every case computed, up to p^13.

## Verification

- `mob.py` (separate agent, from the paper's definitions): builds the poset as multiset partitions of the prime
  factors and computes μ by an upward and a downward recursion, cross-checked against a brute-force comparison
  on labelled primes for Ω ≤ 7.
- `run1.py`: reproduces the paper's Table 1 in full (20 entries), its Example 2.2 (value 92), its values for
  n = 16, and its formula for integers with a simple prime factor.
- `run3.py`, `run4.py`: the value −57 for signature (7,6) and the scan up to Ω = 13. Output in `log.txt`.
- `REFEREE_astra.md`: fresh-context referee, verdict CORRECT.

## Prior work (checked 2026-11-25)

GitHub repository search and the collection repositories we know of: nothing on this conjecture (a benchmark
repository cites the paper but does not contain this case). X by arXiv id: nothing. The authors have not been
asked.
