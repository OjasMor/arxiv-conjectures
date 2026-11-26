# Conjecture 1.3 of arXiv:2611.26570 is true: R_k(k) = R_(k−1)(k) for critical percolation on the cylinder

Status as of 2026-11-25: a short structural proof from the paper's own entry formulas, found by GPT-6.2 Astra in
one attempt ($0.63). A separate AI agent checked every step and confirmed the identity in exact arithmetic for
2 ≤ k ≤ 12 (the paper reports k ≤ 8). An AI referee passed it. No human mathematician has reviewed it.

## Source

Melda Akyazi-Zavadski, Nathanaël Berestycki, Sunil Chhita, "On Romik's rationality conjectures for critical
percolation", arXiv:2611.26570 (math.PR, 19 Nov 2026). Their Theorem 1.2 gives, for each k, a rational function
R_k with P_(C_N)(F_k) = R_k(N) for all N > k (nested-arch connectivity events on a cylinder of width N). They
show R_(k−1)(k) = 1/A_k and verify with Mathematica that R_k(k) = R_(k−1)(k) for 2 ≤ k ≤ 8.

> Conjecture 1.3. For every k ≥ 2, the rational function R_k from Theorem 1.2 satisfies R_k(k) = R_(k−1)(k).

The paper notes this would extend the rational-function identity to N = k, as predicted by Romik's conjecture.

## Proof

R_k(N) is the Pfaffian of a 2k × 2k matrix whose 2 × 2 blocks (r, s) are given by the paper's lemma on final
entries as finite sums of H_N(c_1, c_2) and of a term p, with c_1 running over r+2, ..., 2r+2, plus an explicit
term 1 when r = s. The paper's rational forms of H_N and p contain the factor
∏_(a=1..c−1) (N² − a²)/(4N² − a²), which is regular at N = k and vanishes there as soon as c > k.

For the last block row r = k − 1 the index c_1 runs over k+1, ..., 2k, so at N = k every H-term and p-term in
that row vanishes. The row of the last white vertex is then zero except for a single entry 1, in the column of
its own black vertex. Expanding the Pfaffian along that row removes the last block and leaves exactly the
matrix for k − 1 evaluated at N = k (entries depend only on N, r, s, not on k). Hence R_k(k) = R_(k−1)(k). ∎

Both sides are evaluations of rational functions that agree with the Pfaffians at all integers N > k, so no
probabilistic meaning at N = k is needed.

## Verification

- `rk.py`, `check2.py` (separate agent, exact fractions): the entry formulas reproduce all eight half-plane
  probabilities printed in the paper's table and agree with the direct definitions for small N; R_k(k) and
  R_(k−1)(k) agree and equal 1/A_k for every k from 2 to 12 (1/2, 1/7, 1/42, 1/429, 1/7436, ...); the last
  white row has the single entry 1 in each case. Output in `log.txt`.
- The proof relies on the paper's lemma on final entries and its proposition giving H_N in rational form, as
  printed. Those were tested numerically here, not re-derived.
- `REFEREE_astra.md`: fresh-context referee, verdict CORRECT.

## Prior work (checked 2026-11-25)

**Earlier independent result.** github.com/the-omega-institute/trureturing recorded a proof of this conjecture, with a Lean formalization, on 26 Nov 2026 at 00:55 UTC, about 40 minutes before this folder was published. Credit for the first proof goes there. What is here is an independent proof found the same afternoon.

Paper is 6 days old and proves only k = 1. GitHub repository search (arXiv id, "Romik rationality percolation"),
the collection repositories we know of, and X by arXiv id: nothing found. The authors have not been asked.
