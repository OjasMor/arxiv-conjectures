# Conjecture 14 (Threshold) of arXiv:2610.22875 is false: an overtake at (6, 5)

Status as of 2026-11-25: an explicit 6 × 5 configuration, found by GPT-6.2 Astra in one attempt ($1.85). Its key
property was re-derived in exact rational arithmetic by separate code and by a fresh AI referee. No human
mathematician has reviewed it. It contradicts a computed claim in the paper itself, so an error on our side in
reading the definitions is the main risk; the definitions we used are quoted below.

## Source

Chen Ouyang, Liqun Qi, "Overtake and the recursive-line equality for second-order Zarankiewicz numbers",
arXiv:2610.22875 (math.CO, 16 Oct 2026). A configuration G on an m × n grid has 1-edges E_1 (single cells) and
2-edges E_2 (pairs of distinct cells, which "may share a row or a column"), no two edges sharing a cell. Its
polynomial is P_G = Σ_(E_1) x_i² y_j² + Σ_(E_2) (x_i y_j + x_k y_l)², R(G) = |E_1| + |E_2|, the SOS rank is the
least rank of a positive semidefinite Gram matrix of P_G in the monomials x_i y_j, and G is irreducible if the
SOS rank equals R(G). z_2(m,n) is the largest R(G) over irreducible configurations with C_4-free E_1 and
|E_1| = z(m,n) ("limited"); z_2A(m,n) drops the condition |E_1| = z(m,n). An overtake is z_2A > z_2.
H_limited is the number of empty cells in a limited extremal configuration.

> Conjecture 14 (Threshold). For min(m, n) ≥ 3, an overtake occurs if and only if H_limited(m, n) ≥ 5.

The paper states z_2(6,5) = 20 (so H_limited(6,5) = 30 + 14 − 2·20 = 4) and, in its Proposition and Theorem on
width 5 and its range table, that z_2A(6,5) = 20: no overtake at (6,5).

## Counterexample

Number the cells 5i + j (0 ≤ i < 6, 0 ≤ j < 5).

    E_1 = {0, 1, 2, 5, 8, 11, 13, 15, 19, 22, 24, 28, 29}                                  (13 single cells)
    E_2 = {6,4}, {14,10}, {16,21}, {7,12}, {26,18}, {27,9}, {17,3}, {20,23}                (8 pairs)
    empty cell: 25

E_1 is C_4-free, the supports are disjoint, and R(G) = 21. The Gram matrix of P_G is unique, so its SOS rank is
exactly 21 and G is irreducible. Hence z_2A(6,5) ≥ 21 > 20 = z_2(6,5): an overtake with H_limited = 4. The "only
if" direction of Conjecture 14 fails, and the paper's statement that there is no overtake at (6,5) is wrong.
(Its own candidate table for m = 6 lists the type (|E_1|, |E_2|) = (13, 8); the assertion that every such
candidate has rank below R(G) is what fails.) The example does not contradict the paper's Conjecture 13: its
excess is 1 = ⌊4/3⌋.

## Why the Gram matrix is unique

Let Q_0 be the displayed Gram matrix and Q any feasible positive semidefinite one, D = Q − Q_0. Comparing
coefficients: D vanishes on the diagonal and on pairs of cells in a common row or column, the two diagonals of
each rectangle have opposite entries, and the row of the empty cell is zero. For a displayed pair {a,b},
D_ab ≤ 0, and D_ab = 0 forces the two Gram vectors to coincide. Propagating these relations forces all eight
pairs (the last step is D_(6,4) = −D_(17,3) with both ≤ 0). Then Q is a Gram matrix on the 21 displayed forms,
and their 231 pairwise products are linearly independent, so Q = Q_0.

## Verification

- `exact_forcing.py` (separate agent, exact rationals, runs in under a second; re-run by us): forces 8/8 pairs,
  finds rank 231 for the products, concludes SOS rank 21. The same test gives rank exactly 20 for a limited
  configuration with 14 single cells and 6 pairs, and certifies a (4,4) configuration of rank 11, matching the
  paper's known overtake there; it certified none of 2,100 other random configurations.
- `zaran.py`: z(6,5) = 14 and other classical values by dynamic programming.
- `REFEREE_astra.md`: fresh-context referee with its own code, verdict CORRECT; it also re-derived the limited
  upper bound 20.
- A numerical semidefinite-programming check was attempted and was inconclusive (the feasible set is a single
  point, which solvers handle badly). The claim rests on the exact argument, not on it. See `log.txt`.
- Taken from the paper, not re-derived by us: z_2(6,5) = 20 (via its six-column formula).

## Prior work (checked 2026-11-25)

No repository found for this paper or this example (GitHub repository search, the collection repositories we
know of, X by arXiv id, web). A different result on the m × 3 limited numbers exists in
TommyMaHaoKun/Quod-Erat-Demonstrandum-ex-Machina. The authors have not been asked.
