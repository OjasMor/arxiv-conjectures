# Referee report for 2611.19137__1

status: completed cost: $1.6348

REFEREE VERDICT: CORRECT

STATEMENT MATCH: yes — `conj:CornerCovers` is the **lower-corner** conjecture. It says that “for all shortest paths \((u_0,\dots,u_k)\) from \(u\) to \(u'\) in the QBG” there are “covering relations in Bruhat order” \(x'_{u_0}\lessdot\cdots\lessdot x'_{u_k}\), and that at every step “either \(\lambda'_{u_j}\lessdot_I\lambda'_{u_{j+1}}\) or \(\lambda'_{u_j}=\lambda'_{u_{j+1}}\).” The claim uses the correct direction, \(u'=\operatorname{oppC}(\lambda')\), and the correct lifts \(x'_u=t^{\lambda'_u}u\).

The definitions that fix the interpretation are:

- The paper calls \(Q^\vee\) the **coweight lattice** and \(R^\vee\) the **coroot lattice**. It characterizes \(\operatorname{oppC}(\lambda)\) as “the unique maximal length element \(u\) … such that \(\lambda\in\mathcal C_u\).”
- `defn:QBGEdgeReflection` assigns \(r(u\to us_\alpha)=s_{u\alpha}\) for weight zero and \(s_{-u\alpha,1}\) for weight \(\alpha^\vee\). `defn:CornerLower` defines “\(\lambda'_u=\operatorname{pr}(u\to u')\lambda'\),” with the reflections applied **“reading backwards”** along the path.
- `def:IwahoriOrder` defines \(\lambda\le_I\lambda'\) by \(\lambda\in\operatorname{Sh}(\lambda')\): a minimal gallery to \(\lambda'\) can be folded to end at \(\lambda\). Thus a cover is a cover in the coweight order, not just in a displayed sequence of corners.

DEGENERATE OR ALREADY KNOWN IN PAPER: no. The example has irreducible type \(\widetilde A_2\), a regular nonzero endpoint, and all witnesses in \(R^\vee\), hence of the same type. It is **not** lower QBG-regular: \(\lambda'_+-\mathrm{wt}(s_{21}\to s_2)=(1,2,-3)\) is not dominant. This is exactly the restriction the authors propose to drop from `cor:LowerCovers`. They explicitly allow coincident corners; the failure is at a step with **distinct** corners. `prop:CornerLocation` already proves the weak inequalities, not the cover-or-equality assertion. No result cited in the supplied text states the unrestricted conclusion or its disproof.

DETAILS:

**Independent reconstruction.** I wrote a [Python verifier](sandbox:/mnt/data/verify_corner_covers.py) using matrices on simple-root pairings. It builds the finite group by simple generators, constructs the directed QBG from its two length tests, and applies the affine edge reflections backwards. For the Iwahori comparison I also used the **shadow definition directly**: find a shortest word to the gate, allow each crossing to be taken or folded, and collect the end-vertices. This does not assume that projection preserves covers.

As calibration, the code reproduced the weights \((0,1,-1)=\alpha_2^\vee\) for \(s_{12}\to s_1\) and \((1,0,-1)=\alpha_1^\vee+\alpha_2^\vee\) for \(s_{21}\to s_1\) in `table:A2_wt`. It also reproduced the six distinct corners of `eg:lower-QBG-shrunken`.

For the certificate, the outputs in sum-zero triples were:

```text
oppC(2,-3,1)                    s2
all shortest paths from w0      [w0,s21,s2], [w0,id,s2]
reflections on the first path   s_(alpha1,1), s_(theta,1)
corners on the first path       [(-2,1,1), (2,-3,1), (2,-3,1)]
affine lift lengths             [9,10,11]

vertex          reduced word to gate    length
a = (-2,1,1)    120120                    6
b = (2,1,-3)    0120120                   7
c = (2,-3,1)    20120120                  8

a in Sh(b), b in Sh(c)          True, True
full Iwahori interval [a,c]     [(-2,1,1), (2,1,-3), (2,-3,1)]
```

Here `0`, `1`, `2` denote simple generators. The words also verify the submitted witnesses: starting with \(t^a\), prepend \(s_0\), then prepend \(s_2\). Both multiplications increase length by one. Thus the argument using `prop:BruhatImpliesIwahori` is valid, independently of the direct shadow check.

There is a short way to see **why** the first step fails. On the other shortest path, \(w_0\to\mathrm{id}\to s_2\), the middle corner is \(\lambda'_{\mathrm{id}}=\lambda'_+=b\). The paper’s own `prop:CornerLocation` therefore gives \(a\le_I b\le_I c\), and the coordinates make both inequalities strict. The path through \(s_{21}\) skips that vertex in its first step. This disproves (2).

**General proof of (1).** I found no failing step in the submitted proof, using the paper’s lower-polytope theorems.

1. The corner \(\eta=\lambda'_v\) has the type of \(\lambda'\) and belongs to \(P=\operatorname{poly}_{\lambda'}\). Saturation gives \(\eta\le_I\lambda'\), so the opposite-gate corollary gives \(x=t^\eta v\le x'\). The pseudo-Weyl theorem gives \(P\subseteq\eta+vC^-\).
2. Set \(\gamma=v\beta\), \(\beta>0\), and \(m=\langle\gamma,\eta\rangle\). Failure of \(m+\mathbf1_{\gamma<0}\ge0\) means \(m\le-1\) for \(\gamma>0\), or \(m\le-2\) for \(\gamma<0\). In **both** cases the interior of \(x\mathfrak a\) lies below level \(m+1\) in the \(\gamma\)-coordinate and the base interior lies above it. Folding at this separating wall gives \(rx<x\), also in the extended group since \(r\) preserves type. Projection and saturation then give \(r\eta\in P\). But \(r\eta=\eta+v\beta^\vee\notin\eta+vC^-\). This proves the claimed sign inequality without assuming any corner cover.
3. Reindexing the length formula gives summands \(\left|m+\mathbf1_{\gamma<0}\right|\), so the sign inequality gives \(\ell(x'_v)=\langle2\rho,v^{-1}\eta\rangle+\ell(v)\). Substituting `lem:lowerCornerWeight` and summing the QBG edge length changes gives
   \[
   \ell(x'_v)=\ell(x')-d_\Phi(v\to u').
   \]
   Each suffix of a shortest path is shortest, so the lift length increases by one at each step. The two lifts differ by a left affine reflection by `lem:x'_u`. These are Bruhat covers.

I also tested the cone inequalities, length-positivity integers, corner-weight formula, and distance/length identity on 4,240 endpoint–lift pairs in small coweight boxes in types \(A_1,A_2,A_3,B_2,G_2\), using crystallographic Cartan data. All 8,472 tested target-directed shortest-path edges had the required reflection and length change.

**Problem in the paper’s post-conjecture remark.** The authors suggest that showing \(\mathrm{id}\in\mathrm{LP}(x'_u)\) for all \(u\), or obtaining the lift length differences, would suffice for the conjecture. This is correct for **(1), not for (2)**. In the certificate, length positivity holds for all six lifts, yet the first lift lengths are \(9,10\) while the corresponding **gate** lengths are \(6,8\). The proof of `cor:LowerCovers` uses opposite-gate position at each corner to pass from lift lengths to gate lengths; that hypothesis cannot simply be omitted.

WHAT A HUMAN EXPERT SHOULD STILL CHECK:

- For publication of (1), check the all-type formulation against the intended integral root datum. Also, in the source proof of `prop:CornerPolytopeWeylChamber`, case (2), the affine reflection should act on **difference vectors by its linear part**. This removes a spurious \(\sum_j d_j\alpha_i^\vee\) in `eq:Weyl7` without changing the required inequality. The counterexample does not use that proposition.
- Check later versions and related literature for priority. No additional mathematical assumption or computational search is needed to verify the \(\widetilde A_2\) disproof.