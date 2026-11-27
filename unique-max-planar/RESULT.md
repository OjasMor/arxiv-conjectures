# Part (ii) of the Fabrici–Lužar–Rindošová–Soták conjecture is false: a planar graph needs 6 colours

Status as of 2026-11-26: an explicit counterexample, found by GPT-6.2 Astra and re-checked by independent code.

## The conjecture

A colouring of the vertices by positive integers is *unique-maximum with respect to open neighbourhoods* if for
every vertex v the largest colour in N(v) appears exactly once in N(v). iUMo(G) is the least number of colours
(the colouring need not be proper; graphs with isolated vertices are excluded). Fabrici, Lužar, Rindošová and
Soták (Discrete Appl. Math. 2023) conjectured for the class P of planar graphs: (i) iUMc(P) = 4,
(ii) iUMo(P) = 5, (iii) pUMc(P) = 6, (iv) pUMo(P) ≤ 7. Sedlar and Škrekovski (arXiv:2611.23478, 17 Nov 2026)
prove (i), disprove (iii), and write that (ii) and (iv) remain open: "for part (ii), we do not even know whether
iUMo(P) ≤ 6".

## Result: (ii) is false

There is a connected planar graph W on 781 vertices and 1926 edges, minimum degree 2, with iUMo(W) = 6.
A smaller one has 322 vertices and 678 edges. With the paper's upper bound this gives 6 ≤ iUMo(P) ≤ 8.

## Files

- `W781.json`, `W781_iUMo6_colouring.json`: the graph and a valid 6-colouring.
- `smallest_unsat5.json` (322 vertices), `smallest_unsat5.cnf`: the smaller graph and its 5-colour CNF.
- `A1111_n322.json`, `A1111_n322_k5.cnf`, `A1111_n322_k5.drup`: the unreduced 322-vertex graph, its CNF and a
  DRUP proof from glucose4 (the proof file has not been run through a proof checker).
- `um.py`, `main.py`, `crosscheck.py`, `verify_plain.py`, `test_encoding.py`, `mk322.py`, `shrink2.py`, `log.txt`.
- `ASTRA_ATTEMPT.md`: the construction and a human-readable argument for the 781-vertex graph.

## What was checked

- W was rebuilt from the construction text alone; vertex and edge counts match; planarity by networkx.
- No unique-maximum colouring with 5 colours: UNSAT with two different SAT encodings on four solvers
  (cadical, glucose4, minisat22, maplechrono). A 6-colouring exists and passes a plain-Python checker.
- The encoding agrees with brute force on 2832 small cases and reproduces three values from the paper
  (pUMc of its 21-vertex graph = 5; pUMc and pUMo of its 151-vertex graph = 7).
- The human-readable argument was read step by step for the 781-vertex graph; no gap found. The 322-vertex
  graph rests on the solver only. It is locally minimal, not proved smallest.

## Prior work (checked 2026-11-26)

The paper of 17 Nov lists (ii) as open. GitHub repository search and the AI-results collections we track:
nothing found. This is a search, not a guarantee. No author has been contacted yet.
