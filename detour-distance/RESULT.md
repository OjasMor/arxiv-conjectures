# Conjecture 4.1 of arXiv:2611.26653 is true: detour different-distance sets in Hamiltonian graphs

Status as of 2026-11-25: a written proof by GPT-6.2 Astra (one attempt, $1.36), checked step by step by a
separate AI agent and passed by an AI referee, plus an exhaustive computer check of every Hamiltonian graph on
5 to 9 vertices. Claude has not read every step of the proof and no human mathematician has reviewed it.
Treat the proof as unreviewed and the computation as solid.

## Source

Ammar Alsinai, Hanan Ahmed, "Detour different-distance sets in graphs", arXiv:2611.26653 (math.CO, 17 Nov
2026). D(u,v) is the length of a longest u–v path. A proper non-empty vertex set S is a detour
different-distance (DDD) set if for every w outside S the numbers D(w,u), u in S, are distinct; DD_D(G) is the
largest size of a DDD set. The paper proves DD_D(G) ≤ ⌊n/2⌋ for Hamiltonian G and conjectures:

> Conjecture 4.1. If G is Hamiltonian of order n ≥ 5, then DD_D(G) ≤ max{2, ⌊n/3⌋}; equality holds for the
> cycles C_3k.

## Proof idea

Fix a Hamiltonian cycle and put h(w,x) = n − D(w,x). For w outside S the values h(w,x), x in S, are distinct
positive integers, and h(w,x) is at most the length of either cycle arc from w to x. If S (with |S| ≥ 3) has
at least two runs of consecutive vertices on the cycle, counting distinct values across each gap gives
n − |S| ≥ 2|S|. If S is a single run and n < 3|S|, the distinctness forces the detour distances from the two
neighbours of the run, rules out most chords, and leads to a contradiction. Full text in `ASTRA_ATTEMPT.md`.

## Verification

- `ref.py` computes detour distances and DD_D straight from the paper's definitions and reproduces 26 values
  stated in the paper (cycles, wheels, books, the Petersen graph, prisms and others).
- `ham.c`: every graph obtained from a labelled cycle C_n by adding chords, for n = 5, ..., 9 (all 134,217,728
  graphs for n = 9). The largest DD_D found is 1, 2, 2, 2, 3 against the bound 2, 2, 2, 2, 3. No violation.
- `gap.py`: numerical tests of the proof's intermediate claims on all DDD sets for n ≤ 8. No violation.
- The last step of the single-run case could only be checked by hand (the case it treats never occurs).
- These scripts were written by a separate agent given the paper's definitions. `REFEREE_astra.md`: CORRECT.

## Prior work (checked 2026-11-25)

GitHub repository search, the collection repositories we know of, and X by arXiv id: nothing found. This is a
search, not a guarantee. The authors have not been asked.
