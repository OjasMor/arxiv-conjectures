# A 15-vertex tree disproves the degree-3 dominance conjecture of arXiv:2611.14718

Status as of 2026-11-25: counterexample re-checked by our own exact code and a
simulation. No human has reviewed it.

## Source

R. Higuita-Díaz, L. López, A. Roldán-Correa, "Random Sequential Adsorption versus the Uniform Ensemble of
Jammed Configurations: Stochastic Dominance on Graphs", arXiv:2611.14718 (math.PR, v2 of 18 Nov 2026).

Two ways to fill a graph until no more vertices fit (a maximal independent set):
- sequential: keep picking a uniformly random still-available vertex, occupy it, block its neighbours;
- static: pick a maximal independent set uniformly at random.
N_seq and N_stat are the numbers of occupied vertices. "Sequential dominates static" means
P[N_stat ≤ k] ≥ P[N_seq ≤ k] for every k.

> Conjecture (label conj:grado3). For every finite simple graph G with maximum degree Δ(G) ≤ 3, the
> sequential model dominates the static model.

The authors checked all 27,525 connected graphs with maximum degree ≤ 3 on at most 12 vertices.

## Result

The conjecture is false. Take the path 0–1–2–3–4–5–6, attach the paths 0–7–8, 3–9–10 and 6–11–12, and
attach a leaf 13 to 0 and a leaf 14 to 6. This is a tree on 15 vertices with maximum degree 3, and

    P[N_stat ≤ 6] = 1/55  ≈ 0.018182   <   P[N_seq ≤ 6] = 64/3375 ≈ 0.018963.

It has 55 maximal independent sets (1 of size 6, 50 of size 7, 4 of size 8). At k = 7 the inequality goes
the other way (51/55 vs 8185211/10135125), so on this tree the two models are not comparable at all.

Among trees of maximum degree ≤ 3 this is the smallest counterexample and the only one on 15 vertices:
`search_trees.py` checks all 135, 265, 552 and 1,132 such trees on 12, 13, 14 and 15 vertices.
Graphs with cycles on 13 and 14 vertices were not searched, so a smaller non-tree counterexample is possible.

## Verification

- Found by GPT-6.2 Astra in one attempt ($0.60): `ASTRA_ATTEMPT.md`, with its own hand count and code.
- `verify.py` (our own code): maximal independent sets by brute force over all 2^15 subsets; the sequential
  law by exact rational dynamic programming over available-vertex sets; and 3,000,000 simulated runs
  straight from the verbal definition, giving 0.018869 ± 0.000079, which is 8.7 standard errors above the
  static value 0.018182 and consistent with 64/3375.
- Definitions and the direction of the inequality were read from the paper's TeX source (its dominance
  definition and its description of the process).

## Prior work (checked 2026-11-25)

arXiv:2611.14718 is at v2 (18 Nov), conjecture still stated. No arXiv paper cites or answers it; a web search
found only the paper. The authors' repository (github.com/lykoslopezrivera-blip/Stochastic_Dominance_DPP_Graphs)
was last pushed 17 Nov and has nothing beyond 12 vertices. Nothing in the teen's repo or in GitHub issues.
No X search was run. The authors were told on 25 Nov 2026 through an issue on their repository
(https://github.com/lykoslopezrivera-blip/Stochastic_Dominance_DPP_Graphs/issues/1); no reply yet.

## Not done

- Lean formalization (a finite computation; feasible).
- Search of non-tree graphs on 13–14 vertices for a smaller counterexample.
