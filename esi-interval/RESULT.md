# Question 1 of arXiv:2611.28073: yes, ESI Set is polynomial on interval graphs

Status as of 2026-11-25: an O(n²) algorithm with proof, found by GPT-6.2 Astra in one attempt ($0.49). Claude
checked the proof step by step; separate code compared it with brute force on 84,384 interval graphs
(0 mismatches). No human mathematician has reviewed it.

## Source

Dragana Božović, Tanja Dravec, Aleksander Kelenc, "Externally supported independence in split and proper
interval graphs", arXiv:2611.28073 (math.CO, 13 Nov 2026). A set B is an ESI-set if it is independent and
every vertex of N(B) has a neighbour in V ∖ N[B]; α_es(G) is the largest size of one. The paper shows the
decision problem is NP-complete on split graphs, gives a linear algorithm on proper interval graphs, and asks:

> Question 1. Is the ESI Set problem solvable in polynomial time on interval graphs?

## Answer: yes

**Reformulation (any graph).** α_es(G) = max |V ∖ N[S]| over sets S for which V ∖ N[S] is independent.
(If B is an ESI-set take S = V ∖ N[B]; then V ∖ N[S] = B. Conversely if B = V ∖ N[S] is independent, then
S ⊆ V ∖ N[B] and every vertex of N(B) lies in N[S] ∖ S, so it has a neighbour in S.)

**Interval graphs.** Take a closed-interval model I_v = [L_v, R_v]. N[S] is the set of intervals meeting the
union of S, so intervals of S contained in others can be dropped; then S sorted by left endpoint also has
increasing right endpoints. For consecutive i, j in S (with sentinels at −∞ and +∞) let
F(i,j) = {v : R_i < L_v and R_v < L_j}. Then V ∖ N[S] is the disjoint union of the F(i,j), intervals in
different gaps never meet, and so V ∖ N[S] is independent exactly when each F(i,j) is pairwise disjoint.

**Algorithm.** Build a DAG on the intervals plus two sentinels with an arc i → j when L_i < L_j, R_i < R_j
and F(i,j) is pairwise disjoint, with weight |F(i,j)|. The longest sentinel-to-sentinel path has weight
α_es(G). With sorted endpoints all arcs out of one vertex are found in one scan, O(n²) in total.

The full argument is in `ASTRA_ATTEMPT.md`.

## Verification

- `brute.py` computes α_es from the paper's definition by exhaustive search and reproduces the paper's values
  for paths (⌈n/4⌉), cycles (⌊n/4⌋) and complete graphs (0).
- `algo.py` implements the algorithm; `compare.py` compares the two on 84,384 interval models with up to 12
  intervals (random with many ties, nestings and equal intervals; every family of up to 4 intervals with
  endpoints in 0..4; structured families). 0 mismatches. `reform.py` checks the reformulation on 6,000 random
  general graphs. 0 mismatches. Output in `log.txt`.
- These scripts were written by a separate agent given the paper's definitions.
- A fresh-context AI referee pass was still running when this was committed.

## Prior work (checked 2026-11-25)

The paper's only polynomial algorithm is for proper interval graphs; it cites NP-completeness in general and a
linear algorithm on trees. Nothing in the teen's repository or on GitHub. The authors have not been asked.

Checked on GitHub by repository search (name, description, README) for the arXiv id and keywords, and inside the collection repositories we know of (1337isnot1337/solved-conjectures, s66lem/conjectures, the-omega-institute/trureturing, AmirMakir/broken-conjectures and others); on X by arXiv id; and by web search. Nothing found. This is a search, not a guarantee: several people are working through the same papers this week.
