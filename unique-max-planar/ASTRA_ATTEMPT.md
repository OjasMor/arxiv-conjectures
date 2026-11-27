# arXiv:2611.23478 [Con_FLRS]

status: completed cost: $1.5262 incomplete: None

TARGET: \label{Con_FLRS}It holds that
(i) $\iUMc(\mathcal{P})=4$, (ii) $\iUMo(\mathcal{P})=5$, (iii) $\pUMc(\mathcal{P})=6$ and
(iv) $\pUMo(\mathcal{P})\leq7$.

---

VERDICT: **DISPROVED**

STATEMENT: “It holds that (i) \(\iUMc(\mathcal{P})=4\), (ii) \(\iUMo(\mathcal{P})=5\), (iii) \(\pUMc(\mathcal{P})=6\) and (iv) \(\pUMo(\mathcal{P})\leq7\).”

**Both (ii) and (iii) are false.** The graph \(W\) below has \(\iUMo(W)=6\) and \(\pUMc(W)=7\). In particular, the counterexample to **(ii)** goes beyond the results stated in the supplied paper. Part (i) is true. I do not settle (iv): \(W\) itself has \(\pUMo(W)=7\).

DEGENERATE: **no** — \(W\) is a connected simple planar graph on 781 vertices, with no isolated vertices.

CERTIFICATE: [Full labelled edge list of \(W\) (JSON)](sandbox:/mnt/data/UM_counterexample.json) · [Runnable Python generator and verifier](sandbox:/mnt/data/verify_UM.py)

Here is the same certificate in construction form, with the blocks defined below:
```json
{
  "marked_clique_core": [0, 1, 2, 3],
  "A_blocks_per_core_vertex": [2, 2, 2, 2],
  "hubs_per_A_block": 3,
  "path_vertices_per_A_spoke": 6,
  "O_blocks_per_core_vertex": [2, 2, 2, 1],
  "O_cycle_length": 21,
  "O_hubs": [0, 7, 14],
  "O_forward_chord_offsets_at_each_hub": [2, 3, 4, 5, 6, 7]
}
```

ARGUMENT:

### Construction

To **mark** an edge \(uv\), retain the edge and add a new degree-two vertex with neighbours exactly \(u,v\). The key is that in an **improper open** UM-colouring, even though the edge \(uv\) does not require different colours, its mark does: the maximum on the mark’s open neighbourhood \(\{u,v\}\) must be unique.

Start with a \(K_4\) on four core vertices and mark its six edges. At each core vertex \(b\), attach two copies of the following **\(A\)-block**, disjoint except for \(b\):

1. Add three hubs. Make them and \(b\) a \(K_4\), and mark all six edges of this \(K_4\).
2. For each of the three hubs \(h\), add a path \(p_1\ldots p_6\). Join every \(p_i\) to both \(b\) and \(h\).
3. For \(1\le i<6\), add \(q_i\) with neighbours exactly \(b,p_i,p_{i+1}\).
4. For each \(p_i\), mark both \(bp_i\) and \(hp_i\). Call the mark on \(hp_i\) vertex \(t_i\).

These blocks suffice for the counterexample to (ii). To obtain a **single** certificate for both (ii) and (iii), also attach the paper’s \(O\)-blocks at the four core vertices, with multiplicities \(2,2,2,1\). Explicitly, \(O\) is the 21-cycle labelled modulo 21 with the additional edges \(h(h+j)\) for \(h\in\{0,7,14\}\) and \(2\le j\le7\). Attaching it at \(b\) means joining \(b\) to all its vertices.

For planarity, the path along a spoke \(bh\) can be built in a face at that edge: place \(p_1\) next to \(bh\), then place \(p_{i+1}\) inside triangle \(bhp_i\), adjacent to its three corners. This leaves the triangles \(bp_ip_{i+1}\) available for inserting the \(q_i\). All marks can be added afterwards alongside their edges. Each \(O\) is outerplanar, so its cone is planar, and all the blocks are attached to the core at cut vertices.

### Why five colours fail for improper open neighbourhoods

Suppose \(W\) has an iUMo-colouring with at most five colours. By order-preserving relabelling we can use the palette \(\{1,2,3,4,5\}\).

**Claim.** If a core vertex \(b\) has colour at most \(2\), then *each* \(A\)-block at \(b\) supplies a neighbour of \(b\) of colour \(5\).

Fix one block and suppose it supplies no such neighbour. Its three hubs and \(b\) have four distinct colours, by the six marks. All three hubs belong to \(N(b)\), so these four colours are exactly \(1,2,3,4\). Choose the hub \(h\) for which \(b,h\) have colours \(1,2\) in some order.

Consider the path on the spoke \(bh\). Each \(p_i\) differs in colour from both \(b\) and \(h\), by the marks on \(bp_i,hp_i\). It is also a neighbour of \(b\) in this block. Consequently all six path colours belong to \(\{3,4\}\). They **alternate**: if \(p_i,p_{i+1}\) had the same colour, it would be a repeated maximum on
\[
N(q_i)=\{b,p_i,p_{i+1}\}.
\]

Among \(p_2,p_3,p_4,p_5\), exactly two vertices thus have colour \(3\) and have a colour-\(4\) path neighbour on **both** sides. Each of these two vertices needs a colour-\(5\) neighbour to break the tie. For an interior index \(i\), however, every neighbour of \(p_i\) other than \(t_i\) is either \(b\) or a neighbour of \(b\) in this block: these are \(h\), the two path neighbours, \(q_{i-1},q_i\), and the mark on \(bp_i\). None has colour \(5\). Hence \(t_i\) must have colour \(5\) at both indices. These are distinct vertices in \(N(h)\), giving a repeated maximum there. This proves the claim.

Now a core vertex of colour at most \(2\) would receive **two** colour-\(5\) neighbours, one from each block, which is impossible. All four core vertices therefore have colours in \(\{3,4,5\}\). But their six marks require four distinct colours. This contradiction proves
\[
\boxed{\iUMo(\mathcal P)\ \ge\ \iUMo(W)\ \ge\ 6.}
\]

### The closed-neighbourhood parts

For **(iii)**, the paper’s obstruction survives the extra blocks. Here is a short way to verify the gadget step. The small graph \(O\) has no pUMc-colouring with four colours, as independently checked below. Suppose \(W\) had a pUMc-colouring from \(\{1,\ldots,6\}\), and let \(b\) have colour at most \(3\). If an \(O\) at \(b\) omitted colour \(6\), it would use at most four colours, since it also omits the colour of \(b\). For each \(y\in O\), the set \(N_O[y]\) contains a triangle and hence three distinct colours. At most two can be smaller than the colour of \(b\), so the maximum on \(N_O[y]\) is **larger** than the colour of \(b\). Its uniqueness on \(N_W[y]=N_O[y]\cup\{b\}\) therefore gives uniqueness on \(N_O[y]\). This would be a pUMc-colouring of \(O\) with at most four colours.

Thus every \(O\) at such a \(b\) supplies a neighbour of colour \(6\). The first three core vertices carry two copies each, so none can have colour at most \(3\). By properness they use \(4,5,6\). The fourth core vertex then has colour at most \(3\) and sees a \(6\) both in its own \(O\) and in the core. This disproves (iii).

For **(i)**, the verified lower bound \(\iUMc(W)>3\) below suffices. For completeness, the selector upper bound works as follows. In a connected graph choose a set \(D\) starting with one vertex and repeatedly adding a vertex at distance exactly three from the set until none exists. The closed neighbourhoods of distinct chosen vertices are disjoint, their union induces a connected subgraph, and every vertex of the remainder \(R=G-N[D]\) has a neighbour in that union. Contracting the union therefore gives \(K_1\vee R\) as a minor. If \(G\) is planar, \(R\) is outerplanar (delete the universal vertex in a plane embedding). If \(G\) is outerplanar, \(R\) is a linear forest: a cycle in \(R\) would give a \(K_4\) minor in its cone, and a degree-three vertex would give a \(K_{2,3}\) subgraph there.

Apply this first to the planar graph, then componentwise to its outerplanar remainder. Give the two successive chosen sets colours \(4\) and \(3\). On each remaining path select vertices whose closed neighbourhoods partition the path: use positions \(1\bmod 3\) if the order is \(1\bmod 3\), and positions \(2\bmod 3\) otherwise. Give these vertices colour \(2\), and all unselected vertices colour \(1\). Every closed neighbourhood meets the first selected layer that it sees exactly once, and that layer has its largest colour. Thus \(\iUMc(\mathcal P)=4\).

### Code verification and observed output

Run the [verifier](sandbox:/mnt/data/verify_UM.py) with Python, NetworkX and the Z3 shared library:
```sh
python verify_UM.py UM_counterexample.json
```
It reconstructs the graph and compares the full edge list. For the colouring check it uses one Boolean per vertex and candidate colour, with exactly one true per vertex. For every tested neighbourhood \(T\) and colour \(c\) it asserts
\[
\bigl(\text{at most one vertex of }T\text{ has colour }c\bigr)
\quad\lor\quad
\bigl(\text{some vertex of }T\text{ has colour greater than }c\bigr).
\]
On a nonempty \(T\), these clauses are exactly the unique-maximum condition. Edge inequalities are added only in proper mode.

Observed output, including checks of the paper’s \(O\) and \(G_7\) before testing the four invariants on \(W\):
```text
W: n=781 m=1926 connected=True planar=True
O pUMc 4:unsat 5:sat
G7 pUMc 6:unsat 7:sat
G7 pUMo 6:unsat 7:sat
W iUMc 3:unsat 4:sat
W iUMo 5:unsat 6:sat
W pUMc 6:unsat 7:sat
W pUMo 6:unsat 7:sat
```

CONFIDENCE: **99.9%** that the verdict is correct. The most delicate step for (ii) is the exact neighbourhood of an interior \(p_i\): an extra neighbour outside \(N[b]\) could let it escape the forced colour on \(t_i\). The explicit edge construction rules this out, and the full-graph UNSAT check independently confirms the five-colour obstruction.