# Question 7.7 of arXiv:2611.20344: no, a force-divergent set need not contain a tail of a chain

Status as of 2026-11-25: an explicit set with a half-page proof, found by GPT-6.2 Astra in one attempt ($0.68)
and checked by hand by Claude. No human mathematician has reviewed it.

## Source

Oleg Vasilyev, "Up or down at every integer: Collatz-type maps of arbitrary sets and the up-down graph",
arXiv:2611.20344 (cs.DM, 16 Nov 2026). For a set S of positive integers, T_S sends x to U(x) = ⌈3x/2⌉ if x is in
S and to D(x) = ⌈x/2⌉ otherwise (the odd numbers give the Collatz map). A tail of a chain is a set
{x, U(x), U²(x), ...}. A set A is force-divergent if T_S has a divergent orbit for every S ⊇ A. Any set
containing a tail of a chain is force-divergent, and the paper asks for the converse:

> Question 7.7. Does every force-divergent set, that is, every A such that T_S is unbounded for all S ⊇ A,
> contain a tail of a chain?

## Answer: no

Let w_n = U^(2n+2)(n) for n ≥ 1 (so w_1 = 8, w_2 = 27, w_3 = 93, ...) and let A be all positive integers
except the w_n.

**A contains no tail of a chain.** The tail starting at x contains U^(2x+2)(x) = w_x, which is not in A.

**A is force-divergent.** U is increasing and U(x) ≥ 3x/2, so w_(n+1) ≥ U^(2n+4)(n) = U²(w_n) ≥ (9/4) w_n > 2 w_n.
Take any S ⊇ A. A step down can happen only at some z = w_n. Then w_(n−1) < z/2 ≤ D(z) < U(D(z)) ≤ (3z+5)/4 < z,
so D(z) and U(D(z)) are not omitted numbers and the next two steps go up. So any three consecutive steps
contain at least two steps up, and T_S³(x) ≥ (3/2)²(1/2) x = (9/8) x for every x. Every orbit of every such
T_S diverges. ∎

## Verification

- `check.py` (our code): the omitted numbers more than double each time; the three-step bound holds for every
  start up to 20,000 under every possible choice at the omitted numbers.
- `ASTRA_ATTEMPT.md`, `REFEREE_astra.md`: model output and a fresh-context referee pass (CORRECT).

## Prior work (checked 2026-11-25)

Paper is 9 days old. GitHub repository search, the collection repositories we know of, and X by arXiv id:
nothing found. This is a search, not a guarantee. The author has not been asked.
