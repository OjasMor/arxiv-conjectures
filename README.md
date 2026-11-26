# Conjectures and open questions from recent arXiv preprints, settled with AI

Open conjectures and questions stated in arXiv preprints from October and November 2026, each settled with AI
models and then re-checked with separate code. None of this has been reviewed by a human mathematician. If you
find an error, or know that any of it is already in the literature, please open an issue.

Several people are working through the same papers this week, so every entry says whether we know of an earlier
solution. Four of our results turned out to have been published by others before us (two of them within hours); they
are listed separately below and credited in their folders.

## New as far as we know

| Paper | Statement | Outcome | Found by | Evidence |
|---|---|---|---|---|
| [arXiv:2611.21894](https://arxiv.org/abs/2611.21894) Scott Harper (16 Nov) | Question 2.19: does every transitive permutation group have a derangement of prime or prime-squared order? (Fein–Kantor–Schacher give one of prime power order.) | **No.** An explicit transitive group of degree 2,239,488 whose derangements all have order divisible by 8 or 27. | GPT-6.2 Astra, one attempt | Every element with g⁴ = 1 or g⁹ = 1 tested by our own code (10 seconds): [`derangement-prime-square/`](derangement-prime-square/) |
| [arXiv:2611.20820](https://arxiv.org/abs/2611.20820) Selvaraja (16 Nov) | Conjecture 5.9 (close-skew set-pair bound k ≤ 2^r). The paper notes it would imply Shukla's conjecture that the collapsibility number of the Vietoris–Rips complex of the hypercube at scale r is 2^r | **True, given the Gao–Zhao skew set-pair theorem** (a preprint the paper already relies on). A three-line reduction. | GPT-6.2 Astra, one attempt | Checked by hand, AI referee, exhaustive check for n ≤ 4: [`close-skew-shukla/`](close-skew-shukla/) |
| [arXiv:2611.30048](https://arxiv.org/abs/2611.30048) Shu Liu (23 Nov) | Conjecture 1: no q-ary [q+2,3] self-orthogonal MDS codes for even q ≥ 4 | **False.** An explicit [18,3,16] code over F_16. | Claude | Three independent programs and a Lean 4 proof: [`self-orthogonal-mds/`](self-orthogonal-mds/), [`lean/`](lean/) |
| [arXiv:2611.32519](https://arxiv.org/abs/2611.32519) Mandal, Mohan (24 Nov) | Conjecture 1.19: for k ≥ 3, n^k / (1/F_1^k + ... + 1/F_n^k) is an integer only for n = 1, 2 | **True.** Short elementary proof. | GPT-6.2 Astra, one attempt | Proof read line by line, AI referee, exact checks: [`fibonacci-harmonic/`](fibonacci-harmonic/) |
| [arXiv:2611.26110](https://arxiv.org/abs/2611.26110) Snellman (19 Nov) | Conjecture 21: the normalised volume of Koz(n; 0, d) is weakly increasing in d | **True.** Four lines from the paper's own volume formula. | GPT-6.2 Astra, one attempt | Proof read line by line, AI referee, exact checks: [`kozlov-volume/`](kozlov-volume/) |
| [arXiv:2611.28073](https://arxiv.org/abs/2611.28073) Božović, Dravec, Kelenc (13 Nov) | Question 1: is ESI Set solvable in polynomial time on interval graphs? | **Yes.** An O(n²) algorithm. | GPT-6.2 Astra, one attempt | Proof read line by line; 84,384 interval graphs against brute force, 0 mismatches: [`esi-interval/`](esi-interval/) |
| [arXiv:2611.29890](https://arxiv.org/abs/2611.29890) Clifton, Harris, Khaqan (23 Nov) | Question 5.2: can the number of backgammon parking functions with outcome 1 2 ... k n ... (k+1) be written with Motzkin numbers? | **Yes.** An explicit formula for every k. | GPT-6.2 Astra, one attempt | AI-written proof; formula matches exhaustive enumeration in all 55 cases with n ≤ 10: [`parking-motzkin/`](parking-motzkin/) |
| [arXiv:2611.27882](https://arxiv.org/abs/2611.27882) Chiera, Safer (20 Nov) | Question 10.3: is a function automatic in several expansive bases of a number field eventually periodic, even when no pair of bases satisfies the paper's hypothesis (H)? | **Yes.** A reduction to the paper's two-base theorem. | GPT-6.2 Astra, one attempt | Proof checked step by step, AI referee; rests on the paper's main theorem: [`cobham-several-bases/`](cobham-several-bases/) |
| [arXiv:2610.22875](https://arxiv.org/abs/2610.22875) Ouyang, Qi (16 Oct) | Conjecture 14 (Threshold): for second-order Zarankiewicz numbers, an overtake occurs if and only if H_limited ≥ 5 | **False.** An explicit 6 × 5 configuration of rank 21, which also contradicts the paper's own no-overtake claim at (6,5). | GPT-6.2 Astra, one attempt | Exact rational certificate from separate code, AI referee: [`zarankiewicz-overtake/`](zarankiewicz-overtake/) |
| [arXiv:2611.20344](https://arxiv.org/abs/2611.20344) Vasilyev (16 Nov) | Question 7.1 (Collatz-type maps): does every cycle with l steps, a of them up, satisfy 2^l < 3^(a+1)? | **No.** An explicit cycle of length 149 with ratio about 3.03. | GPT-6.2 Astra, one attempt | Re-checked with our own code in exact integers: [`updown-cycle-ratio/`](updown-cycle-ratio/) |
| [arXiv:2611.26653](https://arxiv.org/abs/2611.26653) Alsinai, Ahmed (17 Nov) | Conjecture 4.1: DD_D(G) ≤ max{2, ⌊n/3⌋} for Hamiltonian graphs | **True** (AI-written proof, not yet read in full by us). | GPT-6.2 Astra, one attempt | Every Hamiltonian graph on 5 to 9 vertices checked; proof checked by a second AI agent and a referee: [`detour-distance/`](detour-distance/) |
| [arXiv:2611.32928](https://arxiv.org/abs/2611.32928) Carli, Carron, Schenato (24 Nov) | Conjecture IV.4: the convergence rate R of the asynchronous consensus algorithm is at most esr(Q̄) | **False.** On K_4 with the paper's own step size, R = 0.671 > 0.625. | GPT-6.2 Astra, one attempt | Exact characteristic polynomials and a 2,000,000-run simulation from separate code: [`consensus-rate/`](consensus-rate/) |
| [arXiv:2611.32270](https://arxiv.org/abs/2611.32270) Ruijie Li (24 Nov) | Conjecture 2.8: the pure-monomial Wronskian identity holds for every K (paper: K ≤ 5) | **True.** Confluent Vandermonde argument. | GPT-6.2 Astra | Steps checked by a second AI agent and a referee; exact check for every K ≤ 20: [`logistic-wronskian/`](logistic-wronskian/) |
| [arXiv:2611.19137](https://arxiv.org/abs/2611.19137) Milićević, Schwer, Thomas (14 Nov) | Conjectures 4.46 and 4.69: two cover-chain statements for affine Bruhat order hold without the QBG-regularity hypothesis | **False as stated** in type Ã_2, for coweights next to a wall. The proved corollaries are not affected. | GPT-6.2 Astra, one attempt each | Rebuilt with a separate implementation that first reproduces the paper's tables; search statistics: [`affine-bruhat/`](affine-bruhat/) |
| [arXiv:2611.18194](https://arxiv.org/abs/2611.18194) Mirzavaziri, Yaqubi (13 Nov) | Conjecture 8: the Möbius function from the prime factorization of n to n is 0 or has sign (−1)^(Ω(n)+1) | **False.** For n = 2^7 · 3^6 the value is −57. | GPT-6.2 Astra, one attempt | Re-computed by separate code that reproduces the paper's table: [`mobius-factorizations/`](mobius-factorizations/) |

## Found independently, but others were first

| Paper | Statement | Outcome | Who was first | Our folder |
|---|---|---|---|---|
| [arXiv:2611.26570](https://arxiv.org/abs/2611.26570) Akyazi-Zavadski, Berestycki, Chhita | Conjecture 1.3 (critical percolation on the cylinder): R_k(k) = R_(k−1)(k) for every k ≥ 2 | **True.** | [the-omega-institute/trureturing](https://github.com/the-omega-institute/trureturing), about 40 minutes before us, with Lean | [`romik-percolation/`](romik-percolation/) |
| [arXiv:2611.20344](https://arxiv.org/abs/2611.20344) Vasilyev | Question 7.7: does every force-divergent set contain a tail of a chain? | **No.** | [the-omega-institute/trureturing](https://github.com/the-omega-institute/trureturing), on 20 Nov, with Lean | [`updown-forcing/`](updown-forcing/) |
| [arXiv:2611.14718](https://arxiv.org/abs/2611.14718) Higuita-Díaz, López, Roldán-Correa | On every graph of maximum degree ≤ 3, random sequential adsorption stochastically dominates the uniform jammed ensemble | **False.** A tree on 15 vertices. | [AmirMakir/broken-conjectures](https://github.com/AmirMakir/broken-conjectures), about eight hours before us, with a Lean proof | [`rsa-dominance/`](rsa-dominance/) |
| [arXiv:2611.28727](https://arxiv.org/abs/2611.28727) Daga, Ramu | Conjecture 31: the randomised Littlestone dimension of intervals equals the greedy closed form | **True.** | [s66lem/conjectures](https://github.com/s66lem/conjectures), a day before us, Lean-verified | [`littlestone-intervals/`](littlestone-intervals/) |


## How sure is each one

- The tree and the F_16 matrix are finite objects. Run the scripts and check them yourself in seconds.
- For arXiv:2611.30048 there is also a written proof that such codes exist exactly for even q ≥ 16 (so the
  conjecture holds only for q = 4 and 8), and that Conjecture 2 holds for odd primes. These proofs have been
  checked by an AI referee only. Machine-checked field sizes: 16, 32, 128.
- The Littlestone proof has been checked by an AI referee, by exact computation on small cases, and by one
  careful read. It starts from a reduction proved in the paper itself.
- The Fibonacci and Kozlov proofs are short and elementary; each was read line by line and passed a fresh AI
  referee. The Kozlov proof uses a volume formula proved in the paper itself.
- The interval-graph algorithm has a proof that was read line by line and agrees with brute force on every
  instance tried (up to 12 intervals).
- The close-skew bound is three lines on top of the Gao–Zhao theorem, which is a preprint; the step to Shukla's
  conjecture is the paper's own remark, which we did not re-derive.
- The 6 × 5 configuration contradicts a computed claim in its source paper. Its rank is certified in exact
  arithmetic, but it has not been confirmed by the authors.
- The detour-distance proof is the least checked item here: the computation is exhaustive up to 9 vertices, the
  general proof has only been read by AI.
- The parking-function formula is proved by an AI-written argument and agrees with exhaustive enumeration up to
  n = 10. Treat the proof as unreviewed.

## Check it yourself

    # the 15-vertex tree (needs Python 3; search_trees.py also needs networkx and nauty's gentreeg)
    python3 rsa-dominance/verify.py

    # the F_16 code (needs PARI/GP), and the larger fields
    gp -q self-orthogonal-mds/verify_q16.gp
    gp -q self-orthogonal-mds/verify_q32.gp
    gp -q self-orthogonal-mds/verify_q128.gp

    # the Lean proof of the F_16 example (Lean 4 + Mathlib; axioms: propext, Classical.choice, Quot.sound)
    # copy lean/SelfOrthogonalMDS.lean into a Mathlib project and run `lake build`

    # numerical check of the Littlestone conjecture
    python3 littlestone-intervals/check_independent.py

    # the newer results (plain Python 3)
    python3 fibonacci-harmonic/check.py
    python3 kozlov-volume/check.py
    (cd esi-interval && python3 compare.py)
    # parking-motzkin: see its RESULT.md and log.txt

## How these were found

Conjectures were taken from the TeX source of recent arXiv papers. Each got one capped attempt by
GPT-6.2 Astra with a Python sandbox, or was worked on directly by Claude. Every claimed result was then
re-derived with separately written code, sent to a fresh model session for adversarial review, and checked
against arXiv, GitHub and the authors' own repositories for prior work.

Not everything worked, and not everything was new. Many attempts gave nothing, some claimed results were
rejected on our own check (trivial readings of a mistyped statement, counterexamples that only use degenerate
small cases), and several correct results had already been published by other people working through the same
papers. Those are not listed as ours.
