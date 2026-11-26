# Question 10.3 of arXiv:2611.27882: yes, the several-bases Cobham statement follows from the two-base theorem

Status as of 2026-11-25: a short reduction to the paper's own main theorem, found by GPT-6.2 Astra in one
attempt ($1.27). Claude checked each step; a fresh AI referee passed it. No human mathematician has reviewed
it, and it rests on the paper's main theorem (Theorem 8.1), which is itself a new preprint.

## Source

Francesco Chiera, Taoufik Safer, "Cobham theorem for expansive bases in orders of number fields",
arXiv:2611.27882 (20 Nov 2026). K is a number field of degree d ≥ 2 with ring of integers R. For expansive
α, β in R the paper's main theorem says: if (H) Q(α^r, β^s) = K for all r, s ≥ 1 and (Ind) α^r R ≠ β^s R for
all r, s ≥ 1, then a function on R that is automatic in both bases is eventually periodic.

> Question 10.3. Let d ≥ 2, and let α_1, ..., α_t in R be expansive, with Q(α_1^(n_1), ..., α_t^(n_t)) = K
> for all n_i ≥ 1 and α_i^r R ≠ α_j^s R for all i ≠ j and r, s ≥ 1. Is every function f : R → Ω automatic in
> all the bases α_i eventually periodic, even when no pair (α_i, α_j) satisfies (H)?

The paper notes that its methods "do not give the first far period" in this situation.

## Answer: yes

**Step 1. Products of bases are bases.** If f is automatic in expansive bases a and b, it is automatic in ab.
A kernel of f in base ab has the form y ↦ f(c + (ab)^n y) with |σc| ≤ C·|σ(ab)^n| at every place, and these
all lie in the finite family of mixed kernels of the paper's Proposition on mixed kernels (take the scale
a^n b^n). So f is automatic in every product α_1^(e_1) ... α_t^(e_t) with positive exponents, and such
products are expansive.

**Step 2. One product base whose every power generates K.** For m ≥ 1 put b_m = α_1 · α_2^m · α_3^(m²) ···
α_t^(m^(t−1)). Fix a proper subfield F of K. If some positive power b_m^(s) lay in F for t different values
of m, the exponent matrix (s_j m_j^(i−1)) would have non-zero (Vandermonde) determinant D, so its row lattice
would contain D·e_i for each i, and F would contain α_i^|D| for every i. That contradicts the hypothesis
Q(α_1^(n_1), ..., α_t^(n_t)) = K. So each F excludes at most t − 1 values of m. K has finitely many
subfields, so some m works for all of them: b = b_m has Q(b^s) = K for every s ≥ 1.

**Step 3. Apply the two-base theorem.** The pair (b, α_j) satisfies (H) for every j, because Q(b^r) = K
already. It satisfies (Ind) for all but at most one j: if b^u R = α_i^v R and b^u' R = α_j^v' R with i ≠ j,
then α_i^(v u') R = α_j^(v' u) R, which the hypothesis forbids. Since t ≥ 2 there is a j with both (H) and
(Ind), f is automatic in b and in α_j, and the paper's main theorem gives that f is eventually periodic. ∎

## Verification

- Steps 2 and 3 are elementary and were checked by hand. Step 1 uses the paper's mixed-kernel proposition and
  its window-set criterion for automaticity exactly as stated there.
- `ASTRA_ATTEMPT.md`: the model output, including exact checks of two examples from the paper.
- `REFEREE_astra.md`: fresh-context referee, verdict CORRECT, "no step fails".
- There is no finite certificate here: this is a proof, and it is only as good as the paper's Theorem 8.1.

## Prior work (checked 2026-11-25)

The paper is 5 days old and poses this as an open question. Checked on GitHub by repository search for the arXiv
id and keywords and inside the collection repositories we know of; on X by arXiv id; and by web search.
Nothing found. This is a search, not a guarantee. The authors have not been asked.
