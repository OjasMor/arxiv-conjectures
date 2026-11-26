# Self-orthogonal MDS codes of length q+2: Conjecture 1 of arXiv:2611.30048 is false for every even q ≥ 16

Status as of 2026-11-25:
- Explicit counterexample: checked by three independent programs (Python, PARI/GP, and GPT-6.2 Astra's own
  sandbox code) and proved in Lean 4 (`../lean/SelfOrthogonalMDS.lean`, axioms: propext,
  Classical.choice, Quot.sound).
- Written proofs: one adversarial referee pass by GPT-6.2 Astra (`REFEREE_astra.md`), verdict correct with
  the fixes now applied below. No human mathematician has reviewed them.
- Prior work: no earlier statement of Theorem A found (see "Prior work" at the end). Not a priority guarantee.

## Source

Shu Liu, "On Self-orthogonal MDS Codes", arXiv:2611.30048 (cs.IT, 23 Nov 2026).

> Conjecture 1. For an even q ≥ 4, there do not exist q-ary [q+2,3] self-orthogonal MDS codes.

> Conjecture 2. For odd q, there do not exist any [n,k] = [q+1,(q−1)/2] self-orthogonal MDS codes.

"Self-orthogonal" is with respect to the Euclidean inner product (C ⊆ C^⊥, i.e. G Gᵀ = 0 for a generator
matrix G). The paper proves Conjecture 1 for q = 4 and Conjecture 2 for q = 3, 5.

## Result A (Conjecture 1)

**Theorem A.** Let q = 2^h ≥ 4. A q-ary [q+2,3] Euclidean self-orthogonal MDS code exists if and only if
PG(2,q) contains an irregular hyperoval (one that is not a conic plus its nucleus).
Consequently such codes do not exist for q = 4 and q = 8, and do exist for every q = 2^h ≥ 16.
So Conjecture 1 holds exactly for q ∈ {4, 8} and fails for every even q ≥ 16.

**Explicit counterexample (q = 16).** F_16 = F_2[a]/(a^4+a+1); write an element as the integer whose bit i
is the coefficient of a^i. The matrix

    G = [14 12  3 12 10  1 11  2  2  7  1 11  5  5 11 11  0  0]
        [ 0 12  6  7 14  5 15 14  3 10 10  9  9 12  8  3  3  0]
        [ 0 12 15  5  9  7  5  6  5  3 12  6 11 14  3  8  0  9]

satisfies G Gᵀ = 0, and all 816 of its 3×3 column minors are nonzero. So its row space is an
[18,3,16] self-orthogonal MDS code over F_16. Its columns are multiples of the points of the
Lunelli–Sce hyperoval. Further explicit examples: q = 32 and q = 128 (translation hyperoval
{(1,t,t^4)} ∪ {(0,1,0),(0,0,1)}); see `certificates.json`.

### Proof of Theorem A

Let C be a [q+2,3] MDS code over F_q, q even, with generator matrix G whose columns are g_1,…,g_n, n = q+2.
MDS means every 3 columns are independent, so writing g_i = v_i P_i with v_i ∈ F_q^* and P_i a representative
of a projective point, H = {P_1,…,P_n} is a (q+2)-arc of PG(2,q), i.e. a hyperoval. Conversely every hyperoval
and every choice of nonzero v_i gives a [q+2,3] MDS code. Row operations on G do not change C, so C depends
only on H up to PGL(3,q) and on the scalars v_i.

G Gᵀ = Σ_i v_i² P_i P_iᵀ. Since squaring is a bijection of F_q (q even), putting w_i = v_i² gives:

  (★) C self-orthogonal for some choice of scalars ⇔ there is w ∈ (F_q^*)^n with Σ_i w_i P_i P_iᵀ = 0.

Let ν(P) = (x², y², z², xy, xz, yz) for P = (x,y,z), and let M be the 6 × n matrix with columns ν(P_i).
(★) says: ker M contains a vector with no zero coordinate. A row vector c with cM = 0 is a conic
(quadratic form) vanishing on all of H; more generally the support conditions below are about conics
through subsets of H.

*Regular hyperovals fail.* If H is regular we may take H = {(1,t,t²) : t ∈ F_q} ∪ {(0,0,1)} ∪ {N}, N = (0,1,0).
The form y² + xz vanishes on every point of H except N, where it equals 1. Hence every w ∈ ker M has
w_N = 0. No nowhere-zero w exists. For q = 4 and q = 8 every hyperoval is regular, so no code exists.

*Irregular hyperovals work, q ≥ 16.* Let H be irregular.

Claim 1: no conic contains q−1 or more points of H. A singular conic is a pair of lines over F_q, a repeated
line, or a pair of conjugate lines over F_{q²} (whose only rational point is their intersection); it meets
an arc in at most 4 points, and 4 < q−1. Let 𝒞 be a nonsingular conic with |𝒞 ∩ H| ≥ q−1, and let X ∈ H
with X ∉ 𝒞 and X not the nucleus of 𝒞. Through X there pass exactly one tangent, q/2 secants and q/2 external
lines of 𝒞. At most 2 points of 𝒞 lie outside H, so at least q/2 − 2 ≥ 1 secants through X (as q ≥ 8) meet 𝒞
in two points of H, giving three collinear points of H, a contradiction. So H ⊆ 𝒞 ∪ {nucleus}, and counting
points, H = 𝒞 ∪ {nucleus} is regular. Contradiction.

Claim 2: rank M = 6 and any three coordinate functionals are linearly independent on K = ker M.
Rank M < 6 would give a conic through all of H, impossible by Claim 1. So dim K = n − 6 = q − 4.
Three coordinates i,j,l are dependent on K iff some nonzero vector of the row space of M is supported in
{i,j,l}, i.e. iff some conic contains H minus at most three points, i.e. at least q−1 points. Impossible by
Claim 1. (Same argument for one or two coordinates.)

Counting: let A_i = {w ∈ K : w_i = 0}. By Claim 2, any intersection of t ≤ 3 distinct A_i has size
q^{k−t}, k = q−4. The Bonferroni inequality truncated after the third term gives

  #{w ∈ K nowhere zero} ≥ q^k [ 1 − n/q + C(n,2)/q² − C(n,3)/q³ ]  with n = q+2
                        = q^k · (q−1)(q−2) / (3q²)  > 0.

So a nowhere-zero w exists, and with v_i = w_i^{q/2} (the square root) the code is self-orthogonal and MDS.

*Existence of irregular hyperovals for every h ≥ 4.* Lunelli–Sce for h = 4; Segre's translation hyperovals
for h = 5 and h ≥ 7; Penttila–Pinneri for h = 6. Alternatively the Subiaco hyperovals for all h ≥ 4
(Cherowitzo, Penttila, Pinneri, Royle, "Flocks and ovals", Geom. Dedicata 60 (1996) 17–37; irregularity via
Payne–Penttila–Pinneri 1995 and O'Keefe–Thas 1996). These citations come from the Astra referee report and
have NOT been read at the source by us; machine-checked here are q = 16, 32, 128.  ∎

Remark. The count in Claim 1 works for any q ≥ 8; nonexistence at q = 4, 8 comes from the classical fact
that all hyperovals of PG(2,4) and PG(2,8) are regular.

## Result B (Conjecture 2), partial

**Proposition B.** For every odd prime power q, no doubly-extended generalised Reed–Solomon code with
parameters [q+1,(q−1)/2] is self-orthogonal. Hence Conjecture 2 holds for every q for which all
(q+1)-arcs of PG((q−3)/2, q) are normal rational curves.

Proof. Take columns v_t(1,t,…,t^{k−1})ᵀ for t ∈ F_q and v_∞(0,…,0,1)ᵀ, k = (q−1)/2, w_t = v_t².
G Gᵀ = 0 reads Σ_t w_t t^m = 0 for 0 ≤ m ≤ q−4 and Σ_t w_t t^{q−3} = −v_∞². Write w as a polynomial
function Σ_{j ≤ q−1} c_j t^j. As Σ_t t^e = −1 if (q−1) | e, e > 0, and 0 otherwise, the conditions say
c_{q−1} = … = c_3 = 0 and c_2 = v_∞² ≠ 0. So w(t) = c_2 t² + c_1 t + c_0 must be a nonzero square for
all q values of t, with c_2 a square. Dividing by c_2 and completing the square, s² + d must be a nonzero
square for every s ∈ F_q. If d = 0, s = 0 fails. If d ≠ 0, y² − s² = d has exactly q−1 solutions (s,y),
so at most (q−1)/2 values of s work. Contradiction. ∎

**Theorem B.** Conjecture 2 holds for every odd prime q (and for q = 9).

Proof. q = 3: k = 1, a generator of a [4,1] MDS code has four nonzero entries, each of square 1, so its
self-product is 4 = 1 ≠ 0. q = 5: k = 2, the six columns are all points of PG(1,5), so the code is a
doubly-extended GRS code and Proposition B applies. q = p ≥ 7: S. Ball, "On sets of vectors of a finite vector space in which every subset of basis size is a
basis", J. Eur. Math. Soc. 14 (2012) 733–748, Theorem 1.8 (read in the published PDF on 2026-11-25):
"If p ≥ k then a set S of q+1 vectors of F_q^k such that every subset of S of size k is a basis, is
equivalent to Example 1.1", Example 1.1 being {(1,t,…,t^{k−1})} ∪ {(0,…,0,1)}. For q = p prime and
k = (p−1)/2 ≤ p, every [p+1,(p−1)/2] MDS code therefore has a generator matrix A·N·D with A invertible,
N the matrix of Example 1.1 (columns in some order) and D a nonzero diagonal matrix. Row operations do not
change the code, so it is a doubly-extended GRS code and Proposition B applies. ∎

(The corrected form of Ball's classification excludes k = (q+1)/2; see the revised version on Ball's page and
Chowdhury's Theorem 1.13, as reported by the referee. Our k = (q−1)/2 is not that value.)
q = 9: every 10-arc of PG(3,9) is a twisted cubic (Segre), so Proposition B applies.

Note on novelty: Proposition B is an elementary specialisation of a known criterion for self-orthogonal GRS
codes (Fang–Liu–Luo, IEEE Trans. Inform. Theory 67 (2021) 130–137, Lemma 2.3, per the referee). Theorem B
is that criterion plus the known arc classification. It is a short observation, not a deep result.

For odd prime powers q = p^h, h ≥ 2, Conjecture 2 remains open in general: k = (q−1)/2 > p, so Ball's
classification does not apply.

## Verification done

- `search.py`: builds the hyperovals, checks the arc property directly, solves the kernel, verifies
  G Gᵀ = 0 and all 3×3 minors nonzero, for q = 16, 32, 128. Also confirms the nucleus coordinate is forced
  to zero for the regular hyperoval at q = 4, 8, 16, 32, 64.
- `verify_q16.gp`: independent PARI/GP check of the q = 16 matrix (own field arithmetic): Gram matrix zero,
  0 of 816 minors singular, minimum weight over all 4095 nonzero codewords = 16.
- `verify_q32.gp`, `verify_q128.gp`: PARI/GP re-check of the q = 32 and q = 128 matrices: Gram matrix zero,
  0 of 5,984 and 0 of 357,760 minors singular.
- q = 64 has no machine-checked example; it is covered only by the written proof plus the cited existence
  of an irregular hyperoval.

## Prior work (checked 2026-11-25)

- arXiv:2611.30048 is still v1; nothing on arXiv cites or answers it; no arXiv abstract links hyperovals to
  self-orthogonal/self-dual codes or hulls.
- Nothing in github.com/1337isnot1337/solved-conjectures (main, research, history, 688 issues/PRs), on GitHub
  at large, or on X.
- Neighbouring literatures searched by consequence and by the Hermitian twin: the quantum MDS literature
  (a Euclidean self-orthogonal [q+2,3] code gives a CSS quantum MDS code [[q+2,q−4,4]]_q) and Hermitian
  self-orthogonal hyperoval codes. Read at the source: S. Ball, "Some constructions of quantum MDS codes"
  (arXiv:1907.04391) discusses the [18,3,16]_16 codes from the regular and Lunelli–Sce hyperovals, but only
  for the Hermitian inner product; Grassl–Rötteler (arXiv:1502.05267) Theorem 14 gives [[4^m+2,4^m−4,4]]
  codes, Hermitian; Ball–Vilar, "The geometry of Hermitian self-orthogonal codes", has no mention of
  hyperovals or the Euclidean case. None states the Euclidean result.
- Astra referee search (references below are per the referee and unread by us): ingredients have precedents (Heng–Ding: hyperoval codes; Wan–Zhu Lemma 7: scaling
  criterion; Jin–Xing: full-weight dual words; Coolsaet–Sticker: conic-intersection bound) but no earlier
  statement that the scalable hyperovals are exactly the irregular ones. Close but different: Ezerman–
  Jitman–Kiah–Ling (two different matrices, G Hᵀ = 0); Carlet–Mesnager–Tang–Qi ([q+2,3] LCD codes).
- This is a search result, not a guarantee. The paper's author was told on 25 Nov 2026 and replied the next day that an update to the preprint is planned. Since the paper never
  mentions arcs or hyperovals the author may not know this literature. A finite-geometry reader (someone who
  works on arcs and hyperovals) is the decisive check.

## Not done yet

- Review by a human mathematician.
- Reading the hyperoval-existence citations at the source.
- Lean proof of the general Theorem A (only the q = 16 example is formalized).
