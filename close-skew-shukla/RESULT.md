# Conjecture 5.9 of arXiv:2611.20820 follows from the Gao–Zhao theorem, and with it Shukla's conjecture

Status as of 2026-11-25: a three-line reduction, found by GPT-6.2 Astra in one attempt ($0.49) and checked by
hand by Claude. No human mathematician has reviewed it. It is conditional in the same way the paper's own
Theorem D(b) is: it uses the skew Hamming set-pair theorem of Gao and Zhao, which is a preprint.

## Source

S. Selvaraja, "Collapsibility of Vietoris–Rips complexes of hypercube graphs in codimension two",
arXiv:2611.20820 (math.CO, 16 Nov 2026). Distances are Hamming distances in F_2^n.

> Conjecture 5.9. Let n > r ≥ 1, and let v_1, ..., v_k in F_2^n satisfy d(v_i, v_j) ≤ r for all i and j. If
> there exist w_1, ..., w_k in F_2^n such that d(w_i, v_i) ≥ r + 1 for every i and d(w_i, v_j) ≤ r whenever
> j < i, then k ≤ 2^r.

The paper recalls the theorem of Gao and Zhao (its Theorem 5.2, Hypothesis (S_r)): if pairs (a_1, b_1), ...,
(a_m, b_m) in F_2^n, n > r, satisfy d(a_i, b_i) ≥ r + 1 for all i and d(a_i, b_j) ≤ r whenever i < j, then
m ≤ 2^(r+1). It notes that the extremal example for that bound does not have pairwise close first points, and
conjectures that this extra condition halves the bound.

## Proof of Conjecture 5.9 (given the Gao–Zhao theorem)

Take v_1, ..., v_k and w_1, ..., w_k as in the conjecture and form the list of 2k pairs

    (v_1, w_1), (v_2, w_2), ..., (v_k, w_k), (w_k, v_k), (w_(k−1), v_(k−1)), ..., (w_1, v_1).

Each pair has distance ≥ r + 1. For an earlier pair (a, b) and a later pair (a', b') we need d(a, b') ≤ r:

- both in the first half, (v_i, w_i) before (v_j, w_j) with i < j: d(v_i, w_j) ≤ r, by the hypothesis on w_j;
- first half then second half, (v_i, w_i) before (w_j, v_j): d(v_i, v_j) ≤ r, because the v's are pairwise
  close (this is where the extra condition is used; i = j is allowed);
- both in the second half, (w_i, v_i) before (w_j, v_j), which means i > j: d(w_i, v_j) ≤ r, by the hypothesis
  on w_i.

So the list is a skew system of 2k pairs, and the Gao–Zhao theorem gives 2k ≤ 2^(r+1), that is k ≤ 2^r. ∎

## What follows, by the paper's own statements

After Conjecture 5.9 the paper says it is equivalent to d'(VR(I_n; r)) = 2^r and that, "together with Theorem B,
this would imply ly(VR(I_n; r)) = coll(VR(I_n; r)) = θ(VR(I_n; r)) = 2^r, and hence Conjectures 3.6 and 1.1".
Conjecture 1.1 is Shukla's conjecture: the collapsibility number of the Vietoris–Rips complex of the
n-dimensional hypercube graph at scale r equals 2^r for all n ≥ r + 1. The paper itself proves it for n = r + 2.

So, assuming the Gao–Zhao theorem and the paper's Lemma 5.1 and Theorem B, Shukla's conjecture holds in full.
We have checked the three-line reduction above. We have not checked the paper's lemmas or the Gao–Zhao proof.

## Verification

- `lean/CloseSkew.lean` (Lean 4 with Mathlib): the reduction is formally verified. The theorem `closeSkew_of_skew` takes the Gao–Zhao
  bound as a hypothesis and proves the bound of Conjecture 5.9. No `sorry`; axioms: propext, Classical.choice, Quot.sound.
- `check.py` (our code): exhaustive search over F_2^n for n ≤ 4 finds that the largest k is exactly 2^r in every
  case; and on 20,000 random close-skew systems (n ≤ 7) the doubled list satisfies the skew conditions.
- `ASTRA_ATTEMPT.md`: the model output. It also contains a self-contained algebraic proof of the binary skew
  bound; we did not check that part and do not rely on it.
- `REFEREE_astra.md`: fresh-context referee, verdict CORRECT.

## Prior work (checked 2026-11-25)

The paper is 9 days old and states this as a conjecture, proved there only for r ≤ 2 and n = r + 1. A web search
for Shukla's conjecture finds the paper itself and earlier partial results only. GitHub repository search (arXiv
id, "Shukla conjecture", "skew Hamming set-pair"), the collection repositories we know of, and X: nothing found.
This is a search, not a guarantee. The author has not been asked.
