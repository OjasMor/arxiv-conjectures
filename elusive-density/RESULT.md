# The degrees of elusive groups have density zero (Problem 6.2 of Cameron, Giudici, Jones, Kantor, Klin, Marušič and Nowitz, 2002)

Status as of 2026-11-26: a written proof, found by GPT-6.2 Astra (two independent attempts reached the same
answer by the same route). Claude has read the first proof line by line and re-derived each step below; an
independent adversarial review by a second AI agent is recorded in `referee_notes.md`. **No human mathematician
has checked it.** It is a proof, not a finite certificate, and it uses three published theorems (two of which
depend on the classification of finite simple groups). Treat it as a claim that needs an expert.

## The problem

A transitive permutation group G ≤ Sym(n), n > 1, is *elusive* if it has no derangement of prime order (the
smallest example is M_11 acting on 12 points). In "Transitive permutation groups without semiregular subgroups"
(J. London Math. Soc. 66 (2002) 325–333), Cameron, Giudici, Jones, Kantor, Klin, Marušič and Nowitz asked:

> Problem 6.2. Does the set of n for which there is an elusive group of degree n have density zero?

It is restated as an open question in Scott Harper's survey "Permutation groups, derangements and connections"
(arXiv:2611.21894, 16 Nov 2026, Question 2.14).

## Answer: yes

Let 𝒟 be the set of integers d ≥ 7 for which there is a primitive nonabelian simple permutation group of degree
d other than Alt(d).

### Step 1. A sufficient condition on the degree

**Proposition.** Let y ≥ 7 and n = ab, where
1. b > 1 is squarefree and every prime dividing b is larger than a and larger than y;
2. there are no distinct primes r, s dividing b with r | s − 1;
3. no divisor d > y of n lies in 𝒟.

Then for every m | n with gcd(m, b) > 1, every transitive group of degree m has a derangement of prime order
dividing gcd(m, b). In particular there is no elusive group of degree n.

*Proof.* Induction on m. Let G be transitive of degree m, N a minimal normal subgroup, c > 1 the common size of
the N-orbits, and K the kernel of G on the set of m/c orbits.

*Lifting.* If G/K, acting on the orbits, has a derangement of prime order r not dividing |K|, then G has a
derangement of order r: the preimage of the cyclic group it generates has order r|K|, so it contains an
element of order r, which is not in K, hence maps to a generator and moves every orbit.

*Case gcd(c, b) = 1.* Then c | a. K embeds in a product of symmetric groups of degree c, so every prime
dividing |K| is at most a, hence smaller than every prime of b. Also gcd(m/c, b) = gcd(m, b) > 1, so by
induction G/K has a derangement on the orbits of prime order r | b, and it lifts.

*Case p | gcd(c, b), N abelian.* N is an elementary abelian p-group and c is a power of p; as p² ∤ n, c = p.
On each orbit N induces a regular group of order p and K induces a subgroup of its normaliser AGL_1(p), so
every prime dividing |K| divides p(p − 1). If gcd(m/p, b) > 1, induction gives a derangement on the orbits of
prime order r | b with r ≠ p; by condition 2, r ∤ p − 1, so r ∤ |K| and it lifts. Otherwise m/p divides a, so
there are fewer than p orbits; the kernels of N on the orbits are fewer than p subgroups of index p, which
cannot cover N, and an element of N outside all of them has order p and no fixed point.

*Case p | gcd(c, b), N = T^k with T nonabelian simple.* Let U be a point stabiliser in N, so |N : U| = c and
p divides |T|. Every proper subgroup of T has index at least p (T embeds in the symmetric group on its cosets).

(A) Some coordinate projection of U is a proper subgroup of T. Put it inside a maximal subgroup M of index d.
Then d | c, d ≥ p > y, and T acts primitively on the d cosets of M, so by condition 3 this action is Alt(d) in
its natural action and M is a point stabiliser. Since d | n and d > a, some prime s | b divides d. Let t be a
product of d/s disjoint s-cycles and g = (t, ..., t) in N. The point stabilisers of N are the G-conjugates of
U; conjugation by G permutes the factors of N and acts on them by automorphisms of T, and every automorphism
of Alt(d) comes from Sym(d) because d ≥ 7. So every point stabiliser of N has a coordinate projection inside
a point stabiliser of Alt(d), which does not contain t. Hence g is a derangement of prime order s, and
s | gcd(m, b).

(B) All coordinate projections of U are onto T. Then U is a product of diagonal subgroups, |U| is a power of
|T|, and |T| divides c. So every maximal subgroup of T has index dividing n and at least p > y; taking one of
index d, condition 3 gives T = Alt(d) again. But Alt(d) also acts primitively on the e = d(d−1)/2 two-element
subsets, e divides |T| and so divides n, e > y, and the image is not Alt(e). So e lies in 𝒟, contradicting
condition 3. ∎

### Step 2. Almost every integer has such a factorisation

Fix 0 < θ < 1, let x be large and y = x^θ. We show that all but (Cθ + o(1))x integers n ≤ x admit a
factorisation as in the Proposition, with C an absolute constant.

*Condition 3.* By the theorem of Cameron, Neumann and Teague (Math. Z. 180 (1982)), the number of degrees up to
u of primitive groups not containing the alternating group is 2π(u) + O(√u). All primes and all numbers q + 1
with q ≥ 5 prime are such degrees, so the other such degrees number O(√u). By Guralnick's classification of
simple groups with a subgroup of prime power index (J. Algebra 81 (1983)), the primes in 𝒟 up to u number
O(√u log u). So 𝒟 is contained in the union of {q + 1 : q prime} and a set R with O(√u log u) elements up to
u. The integers n ≤ x with a divisor in R larger than x^θ number at most x Σ 1/d = o(x). For divisors q + 1
> x^θ, write n = (q + 1)k and let ω_w and Ω_w count prime factors up to w without and with multiplicity, and
L = Σ_{ℓ ≤ w} 1/ℓ. By second-moment estimates (for integers by the Chinese remainder theorem, for shifted
primes by the prime number theorem in progressions), the integers k with ω_w(k) < 0.8L, the primes q with
ω_w(q+1) < 0.8L, and the integers n with Ω_w(n) > 1.5L each have limiting proportion O(1/L). If both
ω_w(q+1) and ω_w(k) are at least 0.8L then Ω_w(n) ≥ 1.6L. Summing the three cases over q, with
Σ_{x^θ < q ≤ x} 1/q = O_θ(1), gives O_θ(x/L) + o(x) such n; letting w → ∞ gives o(x).

*Condition 2 and squarefreeness.* The n ≤ x divisible by p² for a prime p > y number O(x/y). The n ≤ x
divisible by pq with primes p > y and q ≡ 1 (mod p) number O(x log x / y).

*The split.* Write the prime factors of n in increasing order. If each one is at most y times the product of
the previous ones, then consecutive divisors of n have ratio at most y, and by Saias's theorem (J. Number
Theory 62 (1997)) there are O(x log y / log x) = O(θx) such n ≤ x. Otherwise some prime factor exceeds y times
the product a of the earlier ones; put b = n/a. Every prime of b is larger than ya, hence larger than a and y.

Discarding the exceptional sets, every remaining n ≤ x satisfies conditions 1 to 3 and is not the degree of an
elusive group. So the upper density of the set of elusive degrees is at most Cθ for every θ > 0, i.e. zero. ∎

## What has and has not been checked

- Each step of Step 1 was re-derived by hand by Claude (lifting, the three cases, the use of Aut(Alt(d)) =
  Sym(d), the subdirect-product fact, the 2-subset action). No gap found.
- Step 2 was read and its estimates re-derived; the argument for divisors of the form q + 1 is of the same kind
  as the classical Erdős–Wagstaff theorem on divisors of the form p − 1.
- The statements of the three cited theorems are used as recalled above; `referee_notes.md` records an
  independent check of them against the literature.
- The second attempt (`ASTRA_ATTEMPT_2.md`) reaches the same answer by a different route: it inducts on minimal blocks
  (primitive local actions) instead of a minimal normal subgroup, and replaces Saias's theorem by a self-contained sieve.
  The reviewing agent checked that route as well and found no contradiction between the two.
- `referee_notes.md`: the adversarial review. Verdict: no error and no gap found in the first proof. It confirmed the
  Cameron–Neumann–Teague statement from a citing paper, and could confirm Guralnick's list and Saias's bound only from
  secondary sources; those two should be checked against the original papers.
- Consistency: known elusive degrees (12, 56, p(p+1) for Mersenne primes p, 12^k, ...) do not satisfy the
  hypotheses of the Proposition, as they must not. For b a single prime the Proposition is close to a
  classical theorem of Marušič (degree mp with m ≤ p).
- Not done: Lean formalisation; review by a group theorist or an analytic number theorist.

## Prior work (checked 2026-11-26)

Harper's survey (16 Nov 2026), Cameron's lecture notes and Chen–O'Brien, "Elusive groups from non-split extensions"
(arXiv:2508.12652, their Question 1.2) state the problem as open; web searches for a solution find none. GitHub repository search and the collection repositories we know of: nothing found.
This is a search, not a guarantee. No author has been contacted.
