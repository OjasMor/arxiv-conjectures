# Conjecture 21 of arXiv:2611.26110 is true: the volume of Koz(n; 0, d) increases with d

Status as of 2026-11-25: a four-line proof from a formula the paper itself proves. Found by GPT-6.2 Astra in one
attempt ($0.77), checked line by line by Claude. No human mathematician has reviewed it.

## Source

Jan Snellman, "Hilbert functions over the exterior algebra and f-vectors in higher rank III: Lattice points of
the Kozlov polytope", arXiv:2611.26110 (math.CO, 19 Nov 2026).

> Conjecture 21. NV(Koz(n; 0, d)) is weakly increasing in d. (Verified for n ≤ 7 and 0 ≤ d ≤ n − 1; for
> d ≥ n − 1 the value is constant.)

## Proof

Write c_k = C(n, k) and B = c_2 c_3 ... c_n. The paper's rank-two volume corollary gives, for 0 ≤ d ≤ n − 1,

    NV(Koz(n; 0, d)) / B = A(d,1) + ... + A(d, n−d),    A(d,j) = C(n−1+d, d+j−1) · c_(j+1) c_(j+2) ... c_(j+d).

For 0 ≤ d ≤ n − 2 and 1 ≤ j ≤ n − d − 1, Pascal's rule C(n−1+d, d+j−1) + C(n−1+d, d+j) = C(n+d, d+j) gives

    A(d+1, j) = c_(j+d+1) · A(d, j) + c_(j+1) · A(d, j+1).

Every c_k here has 1 ≤ k ≤ n, so c_k ≥ 1. Summing over j = 1, ..., n − d − 1:

    NV(d+1)/B  ≥  Σ_j (A(d,j) + A(d,j+1))  ≥  A(d,1) + ... + A(d,n−d)  =  NV(d)/B,

because each A(d, j) with 1 ≤ j ≤ n − d appears at least once in the middle sum. For d ≥ n − 1 the paper proves
the value is constant. ∎

For n ≥ 3 the increase is strict up to d = n − 1 (the term A(d,2) is multiplied by c_2 = C(n,2) > 1).

## Verification

- `check.py` (our code): reproduces the paper's table of normalised volumes for n = 3, 4, 5 from the formula
  above (so the formula is read correctly), and checks the identity and the monotonicity for all n ≤ 80.
- `ASTRA_ATTEMPT.md`, `REFEREE_astra.md`: the model output and a fresh-context referee pass.
- The proof uses the paper's own Corollary (rank-two volume formula) and Proposition (constant for d ≥ n − 1).

## Prior work (checked 2026-11-25)

Paper is 6 days old; nothing on it in the teen's repository or on GitHub. The author has not been asked.

Checked on GitHub by repository search (name, description, README) for the arXiv id and keywords, and inside the collection repositories we know of (1337isnot1337/solved-conjectures, s66lem/conjectures, the-omega-institute/trureturing, AmirMakir/broken-conjectures and others); on X by arXiv id; and by web search. Nothing found. This is a search, not a guarantee: several people are working through the same papers this week.
