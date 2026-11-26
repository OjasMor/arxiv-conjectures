# Conjectures and open questions from recent arXiv preprints, settled with AI

Open conjectures and questions stated in arXiv preprints from October and November 2026, each settled with AI
models and then re-checked with separate code. None of this has been reviewed by a human mathematician. If you
find an error, or know that any of it is already in the literature, please open an issue.

Several people are working through the same papers this week, so every entry says whether we know of an earlier
solution. Two of our first three results turned out to have been published by others shortly before us; they
are marked below and credited in their folders.

## New as far as we know

| Paper | Statement | Outcome | Found by | Evidence |
|---|---|---|---|---|
| [arXiv:2611.20820](https://arxiv.org/abs/2611.20820) Selvaraja (16 Nov) | Conjecture 5.9 (close-skew set-pair bound k ≤ 2^r). The paper notes it would imply Shukla's conjecture that the collapsibility number of the Vietoris–Rips complex of the hypercube at scale r is 2^r | **True, given the Gao–Zhao skew set-pair theorem** (a preprint the paper already relies on). A three-line reduction. | GPT-6.2 Astra, one attempt | Checked by hand, AI referee, exhaustive check for n ≤ 4: [`close-skew-shukla/`](close-skew-shukla/) |
| [arXiv:2611.30048](https://arxiv.org/abs/2611.30048) Shu Liu (23 Nov) | Conjecture 1: no q-ary [q+2,3] self-orthogonal MDS codes for even q ≥ 4 | **False.** An explicit [18,3,16] code over F_16. | Claude | Three independent programs and a Lean 4 proof: [`self-orthogonal-mds/`](self-orthogonal-mds/), [`lean/`](lean/) |
| [arXiv:2611.32519](https://arxiv.org/abs/2611.32519) Mandal, Mohan (24 Nov) | Conjecture 1.19: for k ≥ 3, n^k / (1/F_1^k + ... + 1/F_n^k) is an integer only for n = 1, 2 | **True.** Short elementary proof. | GPT-6.2 Astra, one attempt | Proof read line by line, AI referee, exact checks: [`fibonacci-harmonic/`](fibonacci-harmonic/) |
| [arXiv:2611.26110](https://arxiv.org/abs/2611.26110) Snellman (19 Nov) | Conjecture 21: the normalised volume of Koz(n; 0, d) is weakly increasing in d | **True.** Four lines from the paper's own volume formula. | GPT-6.2 Astra, one attempt | Proof read line by line, AI referee, exact checks: [`kozlov-volume/`](kozlov-volume/) |
| [arXiv:2611.28073](https://arxiv.org/abs/2611.28073) Božović, Dravec, Kelenc (13 Nov) | Question 1: is ESI Set solvable in polynomial time on interval graphs? | **Yes.** An O(n²) algorithm. | GPT-6.2 Astra, one attempt | Proof read line by line; 84,384 interval graphs against brute force, 0 mismatches: [`esi-interval/`](esi-interval/) |
| [arXiv:2611.29890](https://arxiv.org/abs/2611.29890) Clifton, Harris, Khaqan (23 Nov) | Question 5.2: can the number of backgammon parking functions with outcome 1 2 ... k n ... (k+1) be written with Motzkin numbers? | **Yes.** An explicit formula for every k. | GPT-6.2 Astra, one attempt | AI-written proof; formula matches exhaustive enumeration in all 55 cases with n ≤ 10: [`parking-motzkin/`](parking-motzkin/) |
| [arXiv:2611.27882](https://arxiv.org/abs/2611.27882) Chiera, Safer (20 Nov) | Question 10.3: is a function automatic in several expansive bases of a number field eventually periodic, even when no pair of bases satisfies the paper's hypothesis (H)? | **Yes.** A reduction to the paper's two-base theorem. | GPT-6.2 Astra, one attempt | Proof checked step by step, AI referee; rests on the paper's main theorem: [`cobham-several-bases/`](cobham-several-bases/) |

## Found independently, but others were first

| Paper | Statement | Outcome | Who was first | Our folder |
|---|---|---|---|---|
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
