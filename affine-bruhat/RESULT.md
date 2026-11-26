# Conjectures 4.46 and 4.69 of arXiv:2611.19137 fail in type Ã_2 outside the QBG-regular range

Status as of 2026-11-25: two explicit examples found by GPT-6.2 Astra (one attempt each, $1.53 and $1.24),
rebuilt by a separate AI agent with its own implementation of the affine Weyl group, and passed by AI referees.
No human has reviewed them. The paper's conventions are intricate; the code reproduces the paper's tables and
proved corollaries before testing the conjectures, but an expert check is still needed.

## Source

Elizabeth Milićević, Petra Schwer, Anne Thomas, "Intervals in affine Bruhat order", arXiv:2611.19137 (math.CO,
14 Nov 2026). Corollaries 4.45 and 4.68 show that shortest paths in the quantum Bruhat graph give chains of
covers (in Bruhat order, and of the translation parts in the "Iwahori" order) when λ is lower, respectively
upper, QBG-regular. The paper then says "We conjecture that the restriction of Corollary 4.45 to lower
QBG-regular elements of Q^∨ can be dropped" (Conjecture 4.46) and that Corollary 4.68 "can be strengthened"
in the same way (Conjecture 4.69). Both conjectures are stated for all λ in Q^∨.

## Counterexamples (type Ã_2, coordinates in the standard hyperplane model)

**Conjecture 4.46, part (2).** λ' = (2, −3, 1), which is regular but not lower QBG-regular; u' = s_2. Along the
shortest path w_0 → s_2 s_1 → s_2 the elements x'_u have lengths 9, 10, 11, so part (1) holds, but the lower
corners are (−2,1,1), (2,−3,1), (2,−3,1) and (−2,1,1) < (2,1,−3) < (2,−3,1) strictly in the Iwahori order: the
first step is not a cover. Part (1) of the conjecture held in every case tested.

**Conjecture 4.69, parts (1) and (2).** λ = (0, 1, −1), regular but not upper QBG-regular; u = s_1 and the
gate element is x = t^λ s_2 s_1 of length 2. The path s_1 → id is a single down edge, and x^(id) has length 5:
the length jumps by 3, so it is not a Bruhat cover, and the translation parts are not an Iwahori cover either.

## How far the failures go

In a search over all λ in the coweight lattice with coordinates of absolute value at most 6 (2,944 path
instances): Conjecture 4.46 fails in 100 instances and Conjecture 4.69 in 140, for regular and non-regular λ
alike; neither fails in any lower (respectively upper) QBG-regular instance, so the paper's proved corollaries
are not contradicted. Every failure has dominant representative λ_+ within one step of a wall (a simple-root
pairing 0 or 1); the pattern continues in a larger box (coordinates up to 12).

## Verification

- `aff.py`, `check_paper.py` (separate agent): exact implementation of Ã_2; reproduces the paper's weight table
  (36 entries), its table of edge reflections (15 edges), its worked examples, its length formula on 3,000
  elements, and Corollaries 4.45 and 4.68 on thousands of paths with no failure.
- `counterexamples.py`, `search.py`, `extent.py`: the two examples and the search above. Output in `log.txt`.
- Conventions the conclusion depends on: Q^∨ is the coweight lattice; x = t^λ w acts by z ↦ λ + wz; Iwahori
  covers are covers in the order on the full type class.
- `REFEREE_astra_corner.md`, `REFEREE_astra_upper.md`: fresh-context referees, both CORRECT.

## Prior work (checked 2026-11-25)

GitHub repository search, the collection repositories we know of, and X by arXiv id: nothing found. The authors
have not been asked; they are the right people to confirm or correct this.
