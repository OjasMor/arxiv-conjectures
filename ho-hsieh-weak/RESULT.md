# The weak Ho–Hsieh conjecture is true: the Ising ground state on a ring of L qubits can be prepared with L/2 layers

Status as of 2026-11-26: a written constructive proof, found by GPT-6.2 Astra (two separate runs; both give a
proof by the same route, written in different variables). The construction was turned into code and checked end
to end on the full 2^L state vector for L = 2, 4, ..., 14, and mode by mode for L = 20 and 40. **No physicist or mathematician has checked the written proof.**

## The conjecture

Ho and Hsieh, "Efficient variational simulation of non-trivial quantum states" (SciPost Phys. 2019,
arXiv:1803.00026), study the alternating circuit

    |Ψ(γ, β)> = Π_{k=1..p} exp(−i β_k H_X) exp(−i γ_k H_ZZ) |+ ... +>

on a ring of L qubits, with H_ZZ = −Σ Z_i Z_{i+1} (periodic) and H_X = −Σ X_i. They conjectured that for even L
and every field strength g, the ground state of the transverse-field Ising model H_ZZ + g H_X can be prepared
exactly with p = L/2 layers. Edward Jiang (arXiv:2611.31308, 22 Nov 2026) calls this the weak form, disproves a
stronger form, and writes: "The weak form of the conjecture concerning the preparation of the ground state
remains open."

## Result: the weak form is true

For every even L ≥ 2 and every real g ≠ 0, the ground state is prepared exactly (up to a global phase) by
L/2 layers; angles are computed by `angles.py`. For g = 0 the same holds for the even cat state, by a limit
argument. The proof is in `ASTRA_ATTEMPT_1.md` (a second, independent run is `ASTRA_ATTEMPT_2.md`). Outline:

1. Free-fermion reduction to n = L/2 two-level pair modes, at the points x_j = −cos((2j−1)π/L), the roots of the
   Chebyshev polynomial T_n. The target on mode j is the ground state of a 2×2 Hamiltonian with energy
   r(x) = sqrt(1 + g² + 2gx).
2. A Hermite interpolant of r at the nodes, with sign bounds on [−1, 1] proved by a concavity argument.
3. A factorisation into polynomials A, B with |A|² + (1 − x²)|B|² = 1 of degrees ≤ n and ≤ n − 1 that match the
   target on every node.
4. A layer-peeling lemma (of quantum-signal-processing type): every such normalised polynomial pair is produced
   by exactly n layers of the circuit, with no extra rotations.

## What was checked independently (a separate agent, from the paper's definitions)

- `check.py`: for each (L, g) it computes the L/2 angle pairs, runs the circuit on the full 2^L state vector with
  the paper's conventions, and compares with the ground state from exact diagonalisation. Worst infidelity over
  g ∈ {−3, −1.2, −1, −0.5, −0.01, 0.01, 0.3, 1, 1.5, 4}:

  | L | 2 | 4 | 6 | 8 | 10 | 12 | 14 |
  |---|---|---|---|---|---|---|---|
  | worst 1 − fidelity | 6.7e-16 | 1.3e-15 | 1.6e-15 | 2.2e-15 | 3.3e-15 | 6.2e-15 | 1.4e-14 |

  25 further random g per L (|g| from 1e-3 to 50, both signs): worst 1.2e-14 (`extra_tests.py`).
- `verify_steps.py`: each intermediate claim of the proof at 120 digits (roots of T_n, the Hermite error
  identity, concavity and the sign bounds at 12,173 grid points, identity |A|² + (1 − x²)|B|² = 1, layer
  peeling). No failing step. One printed FAIL is an absolute-tolerance artifact (relative remainder 1.8e-116).
- The algebra of the layer-peeling step was re-derived by hand by the checking agent. No gap found.
- `large_L_modes.py` (written separately by Claude): applies the L/2 layers to each pair mode and compares with
  the mode's ground spinor, with no 2^L vector. L = 20 (g = 1, −0.999) and L = 40 (g = 1.001, −1, 0.3), at
  300 digits: worst mode infidelity below 2e-300.
- Claude read and re-derived by hand, in the second write-up, the layer-removal lemma (its Section 2) and the
  bounded interpolant (its Section 3: the integral formula for the Hermite error, convexity of E, concavity of
  E + 2√t/C, the bounds inside and at the ends of the interval). No gap found. The spectral-factorisation step
  was checked numerically only.
- Numerics confirm the statement for the tested sizes; for all L the claim rests on the written proof.

## Prior work (checked 2026-11-26)

Read (abstract and full text, the relevant sections verbatim):
- Ho and Hsieh (arXiv:1803.00026), Section 4.3: stated as a conjecture, "support with numerical data".
- Jiang (arXiv:2611.31308, 22 Nov 2026): weak form "remains open".
- Dreyer, Bejan, Granet (arXiv:2104.01168): reduce the conjecture to a system of L/2 equations; no solution shown.
- Mbeng, Fazio, Santoro (arXiv:1906.08948): lower bound for 2P < N; exact preparation for the zero-field target.
- Marwaha (arXiv:2606.29562) and Kol, Ben-Shahar, Sulimany, Englund (arXiv:2606.29687): prove the
  Farhi–Goldstone–Gutmann conjecture for the ring of disagrees (zero field); no transverse-field statement.
- Arezzo et al. (arXiv:2509.17754): controllability; depth N/2 for the uniform ring is a dimension-count
  prediction. Partly read.
- Matos et al. (arXiv:2206.06400): reachability at some depth by a Lie-algebra argument; depth L/2 is a
  numerical finding. Partly read.

Named but not read: Rabinovich, Kardashin, Adhikary (arXiv:2508.10086; reported to cover the zero-field case).

Also searched: titles of the papers citing Ho–Hsieh and Dreyer et al. on Semantic Scholar (2024–2026), GitHub
repositories, and the AI-results collections we track. Nothing found that proves the statement.

This is a search, not a guarantee. No author has been contacted yet.
