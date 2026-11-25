# Randomised Littlestone dimension of intervals: Conjecture 31 of arXiv:2611.28727 is true

Status as of 2026-11-25: no human mathematician has reviewed the proof.

## Source

Miit Daga, Swarna Priya Ramu, "How many mistakes does it take to learn an interval? Exact Littlestone
dimensions of intervals and their unions", arXiv:2611.28727 (cs.LG, 21 Nov 2026).

> Conjecture (label conj:rl; numbered 31 in the compiled paper per the referee). For every position J_S,
> RL(J_S) equals the value of the greedy schedule started from S. In particular RL(Int_m) = R(m+1) for all m ≥ 0.

The paper proves RL(Int_m) ≥ R(m+1), an upper bound within 0.64, and checks equality for m ≤ 70. It notes the
conjecture is equivalent to: from every position, one arbitrary cut followed by greedy play is never better
than greedy play.

## Result

The conjecture holds for every position, hence RL(Int_m) = R(m+1) for all m ≥ 0.

Proof: `ASTRA_PROOF.md` (found by GPT-6.2 Astra, xhigh, one attempt, $0.83). Outline:
1. For a power of two d and 1 ≤ r ≤ d, the number of greedy cuts of pieces of size ≥ d+r descending from a
   piece n is max(0, ⌊(n−r)/d⌋).
2. Hence the greedy value of any vector of pieces X is F(X) = Σ_d (1/d) Σ_{r=1..d} H(Σ_{n∈X} C_{d,r}(n)),
   H(s) = 1 − 2^{−s}.
3. This gives a halving recurrence F(X) = H(M(X)) + ½(F(X⁻) + F(X⁺)), all pieces rounded down together or up
   together.
4. A cut of a piece with two odd children forces opposite roundings; concavity of H shows the synchronised
   roundings minimise the sum, which is the direction needed.
5. Induction on the number of remaining cuts gives the supersolution inequality.

## Verification

- `REFEREE_astra.md`: fresh-context adversarial referee (GPT-6.2 Astra, $1.42). Verdict: proof correct;
  statement identical to the conjecture; the cutting recursion it relies on is proved in the paper. Its own
  exact computations: original shattered-tree definition for m ≤ 27; cutting optimum vs greedy on all
  34,262,962 states of total measure ≤ 86 (868,637,629 cuts); the proof's identities on large samples. 0 failures.
- `check_independent.py`: our own exact-rational code written from the paper's definitions. Optimum equals
  greedy on all 5,603 multisets of total measure ≤ 30 (the same count the paper reports); RL = R for rods
  n ≤ 45; one-cut-then-greedy never beats greedy on 26,015 states of total ≤ 38 and on all 40,000 first cuts
  of rods up to 400. 0 violations.
- Claude read the full proof (count formula, value formula, halving recurrence, rounding inequality, the
  formal-split convention, and the final induction) and re-derived each displayed step; no gap found.

Caveats: prover and referee are the same model family, so their errors could be correlated; the independent
numerics and Claude's read are the only cross-family checks. The proof starts from the paper's exact cutting
recursion (its eq. rlcut, derived from its Lemma on RL recursion and its threshold proposition). That paper is
an unrefereed preprint, so the result is conditional on that reduction being right; the referee's brute force
from the original definition (m ≤ 27) supports it but does not prove it.

## Prior work (checked 2026-11-25)

arXiv:2611.28727 is still v1. No arXiv paper cites or answers it. Nothing in
github.com/1337isnot1337/solved-conjectures or in GitHub issues mentions it. The authors' own repository
(github.com/researchbackup27-sudo/exact-littlestone-intervals) has a single commit from 21 Nov and no proof
of the conjecture. No web or X search was run for this one. The authors have not been asked.

## Not done

- Human review. Lean formalization (the authors already have a Lean 4 development for their other formulas,
  so a Lean proof of this would fit their repo).
