# Conjecture 2.8 of arXiv:2611.32270 is true: the pure-monomial Wronskian identity holds for every K

Status as of 2026-11-25: a proof by confluent Vandermonde limits, found by GPT-6.2 Astra (two attempts on the
two statements of the same identity, $0.64 and $0.62). A separate AI agent checked the steps and confirmed the
identity in exact integer arithmetic for every K up to 20 (the paper proves K ≤ 5 by computer algebra and
tests integer scales up to K = 12). An AI referee passed it. No human mathematician has reviewed it.

## Source

Ruijie Li, "Certified minimax normal-scale mixtures for the logistic-normal integral", arXiv:2611.32270
(math.ST, 24 Nov 2026). For scales 0 < s_1 < ... < s_K take the functions Φ(s_i z) and z φ(s_i z) (normal
distribution function and density), form their Wronskian-type matrix of derivatives of orders 1 to 2K − 1 with
the column z φ(s_K z) removed, and strip the Gaussian factors. The paper's Theorem 2.7 says that for 2 ≤ K ≤ 5
the resulting determinant is a pure monomial, Q(z; s) = c_K(s) z^((2K−1)(K−1)), with

    c_K(s) = (−1)^⌊(K−1)/2⌋ 2^(K−1) s_K ∏_(i<K) s_i³ ∏_(i<j≤K−1) (s_i² − s_j²)⁴ ∏_(i<K) (s_i² − s_K²)².

> Conjecture 2.8 (Pure-monomial identity for general K). The identity of Theorem 2.7 holds for every K ≥ 2.

(The appendix restates it with the closed form for c_K(s); the two statements are the same identity.)

## Proof idea

z φ(sz) is the derivative of Φ(sz) with respect to s. For 2K − 1 distinct scales u_j the matrix of derivatives
of the Φ(u_j z) is, after a triangular change from d/dz to d/d(z²/2), a Vandermonde matrix in the u_j², which
gives the power z^((2K−1)(K−1)) and the product of differences. Letting the scales merge in pairs
(s_i, s_i + h → s_i) turns pairs of columns into Φ and z φ columns and the Vandermonde product into the
confluent one with block sizes 2, ..., 2, 1; that is exactly c_K(s), including the sign. Full text in
`ASTRA_ATTEMPT_1.md` and `ASTRA_ATTEMPT_2.md`.

## Verification

- `wr.py`, `big.py`, `raw.py` (separate agent): symbolic check for K = 2, 3; exact rational checks at random
  points for K ≤ 8; the paper's own integer values (36 for K = 2, −12441600 for K = 3, 140 digits at K = 8,
  412 digits at K = 12) are reproduced; exact integer determinants against the closed form at random integer
  scales for every K from 6 to 20, all equal. Output in `log.txt`.
- The paper does not define "reduced" explicitly; the reading used (divide each column by its Gaussian factor)
  is the only one under which the paper's stated values come out, and it reproduces them.
- The limit h → 0 in the proof is routine but only sketched.
- `REFEREE_astra.md`: fresh-context referee, verdict CORRECT.

## Prior work (checked 2026-11-25)

Paper is 1 day old. GitHub repository search, the collection repositories we know of, and X by arXiv id:
nothing found. The author has not been asked.
