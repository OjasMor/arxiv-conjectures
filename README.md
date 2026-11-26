# Three conjectures from this month's arXiv, settled with AI

Three open conjectures from arXiv preprints posted in November 2026, each settled with AI models and then
re-checked with separate code. **Correction, 25 Nov:** two of the three (the tree and the Littlestone proof) turned out to have been
published by other people shortly before us; they are credited in the table and in each folder. As far as we know
the self-orthogonal MDS result is new. None of this has been reviewed by a human mathematician. If you find an error,
or know that any of it is already in the literature, please open an issue.

| Paper | Conjecture | Outcome | Found by | Evidence |
|---|---|---|---|---|
| [arXiv:2611.14718](https://arxiv.org/abs/2611.14718) Higuita-Díaz, López, Roldán-Correa | On every graph of maximum degree ≤ 3, random sequential adsorption stochastically dominates the uniform jammed ensemble | **False.** A tree on 15 vertices. Not first: [AmirMakir/broken-conjectures](https://github.com/AmirMakir/broken-conjectures) published the same tree about eight hours earlier, with a Lean proof. | GPT-6.2 Astra, one attempt | Exact rational computation and simulation: [`rsa-dominance/`](rsa-dominance/) |
| [arXiv:2611.30048](https://arxiv.org/abs/2611.30048) Shu Liu | Conjecture 1: no q-ary [q+2,3] self-orthogonal MDS codes for even q ≥ 4 | **False.** An explicit [18,3,16] code over F_16. | Claude | Three independent programs and a Lean 4 proof: [`self-orthogonal-mds/`](self-orthogonal-mds/), [`lean/`](lean/) |
| [arXiv:2611.28727](https://arxiv.org/abs/2611.28727) Daga, Ramu | Conjecture 31: the randomised Littlestone dimension of intervals equals the greedy closed form | **True** (written proof). Not first: [s66lem/conjectures](https://github.com/s66lem/conjectures) published a Lean-verified proof on 24 Nov, a day earlier. | GPT-6.2 Astra, one attempt | Proof, AI referee report, exact numerical checks: [`littlestone-intervals/`](littlestone-intervals/) |

## How sure is each one

- The tree and the F_16 matrix are finite objects. Run the scripts and check them yourself in seconds.
- For arXiv:2611.30048 there is also a written proof that such codes exist exactly for even q ≥ 16 (so the
  conjecture holds only for q = 4 and 8), and that Conjecture 2 holds for odd primes. These proofs have been
  checked by an AI referee only. Machine-checked field sizes: 16, 32, 128.
- The Littlestone proof has been checked by an AI referee, by exact computation on small cases, and by one
  careful read. It starts from a reduction proved in the paper itself.

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

## How these were found

Conjectures were taken from the TeX source of recent arXiv papers. Each got one capped attempt by
GPT-6.2 Astra with a Python sandbox, or was worked on directly by Claude. Every claimed result was then
re-derived with separately written code, sent to a fresh model session for adversarial review, and checked
against arXiv, GitHub and the authors' own repositories for prior work.

Not everything worked: of five single attempts, two produced the results above, two produced partial results
that are not claimed here, and one request failed.

## Credit

The conjectures and all of the surrounding theory are the work of the papers' authors. The idea of sweeping
recent arXiv conjectures with an AI agent follows Cinna Davis's
[solved-conjectures](https://github.com/1337isnot1337/solved-conjectures).
