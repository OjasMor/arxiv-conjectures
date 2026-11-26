# Conjecture IV.4 of arXiv:2611.32928 is false: on K_4 the convergence rate exceeds esr(Q̄)

Status as of 2026-11-25: a counterexample found by GPT-6.2 Astra in one attempt ($0.48), re-derived in exact
arithmetic by a separate AI agent and passed by an AI referee. No human has reviewed it.

## Source

Ruggero Carli, Andrea Carron, Luca Schenato, "An exponential-rate consensus-based algorithms for estimation
from relative measurements", arXiv:2611.32928 (math.OC, 24 Nov 2026). In the asynchronous algorithm one random
node broadcasts its estimate at each step; neighbours store it in memory and update. The error obeys
ξ(k+1) = Q_i ξ(k) with i random, Q̄ = E[Q_i], and the rate is defined in mean square,
R = sup over initial conditions of limsup_k E[‖Ωξ(k)‖²]^(1/k). The paper cites esr(Q̄)² ≤ R and conjectures,
on the basis of Monte Carlo runs:

> Conjecture IV.4. The quantity esr(Q̄) is an upper bound for the exponential convergence rate R, i.e. R ≤ esr(Q̄).

## Counterexample

The complete graph K_4, unit weights, uniform broadcast probabilities, step size ε = 1/8. This is the paper's
own Assumption 1 setting (ε = 1/(2(ν+1)) with ν = 3), and 1/8 lies inside the allowed interval (0, 1/6).

- Q̄ has eigenvalues 1, 5/8 (three times), 1/2 (three times), 3/8, so esr(Q̄) = 5/8 = 0.625.
- The second-moment operator M ↦ E[Q_i^T M Q_i], restricted to the disagreement subspace, has characteristic
  polynomial 32768 t⁴ − 40960 t³ + 16320 t² − 2628 t + 147, whose largest root is R = 0.6710905...

So R − esr(Q̄) = 0.046 > 0. The reason: a broadcast refreshes only one memory entry, so the variance of the
memory disagreement shrinks by at most (N−2)/(N−1) = 2/3 per step, which the averaged matrix Q̄ does not see.

The same happens on K_5, K_6 and K_8 at the paper's step size (gaps 0.0076, 0.0026, 0.0006), and on K_4 for all
step sizes above about 0.0775. Paths, cycles and stars tested show no violation.

## Verification

- `acl.py` and `run1.py` ... `run7.py` (separate agent, built from the paper's formulas): exact characteristic
  polynomials with sympy; reproduction of the paper's eigenvalue lemma and of its bounds esr² ≤ R ≤ 0.75 on
  this instance; a Monte Carlo run of 2,000,000 trajectories whose fitted rate is 0.67106. Output in `log.txt`.
- The conclusion uses the paper's definition of R (mean square). Under an almost-sure reading of "rate", which
  the paper does not use, a rough estimate gives no violation.
- `REFEREE_astra.md`: fresh-context referee pass.

## Prior work (checked 2026-11-25)

Paper is 1 day old. GitHub repository search, the collection repositories we know of, and X by arXiv id:
nothing found. The authors have not been asked.
