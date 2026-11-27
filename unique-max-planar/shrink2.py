import json, random, networkx as nx
from um import *
from pysat.formula import CNF
PY=lambda *a: print(*a,flush=True)
def unsat5(G):
    if G.number_of_nodes()==0 or any(d==0 for _,d in G.degree()): return False
    r,_,_=solve(G,5,'open',False); return not r
def clean(G):
    G=G.copy(); G.remove_nodes_from([v for v,d in G.degree() if d==0]); return G
PY("== block-count sweep (A blocks only, no O), iUMo k=5 ==")
for ab in [(2,2,2,1),(2,2,2,0),(2,2,1,1),(2,1,1,1),(1,1,1,1),(2,2,1,0)]:
    G=build(ab,(0,0,0,0)); r,_,t=solve(G,5,'open',False)
    PY("A-blocks",ab,"n=%d m=%d"%(G.number_of_nodes(),G.number_of_edges()),"UNSAT" if not r else "SAT","%.2fs"%t)
G=build((2,2,2,0),(0,0,0,0))
if not unsat5(G): G=build((2,2,2,1),(0,0,0,0))
PY("start n=%d"%G.number_of_nodes(),flush=True) if False else PY("start n=%d"%G.number_of_nodes())
random.seed(3)
H=G.copy(); changed=True
while changed:
    changed=False
    vs=list(H.nodes()); random.shuffle(vs)
    for v in vs:
        if v not in H: continue
        H2=H.copy(); H2.remove_node(v); H2=clean(H2)
        if unsat5(H2): H=H2; changed=True
    PY("vertex pass done n=%d m=%d"%(H.number_of_nodes(),H.number_of_edges()))
changed=True
while changed:
    changed=False
    es=list(H.edges()); random.shuffle(es)
    for u,v in es:
        if not H.has_edge(u,v): continue
        H2=H.copy(); H2.remove_edge(u,v); H2=clean(H2)
        if unsat5(H2): H=H2; changed=True
    PY("edge pass done n=%d m=%d"%(H.number_of_nodes(),H.number_of_edges()))
    # vertices may now be removable again
    for v in list(H.nodes()):
        if v not in H: continue
        H2=H.copy(); H2.remove_node(v); H2=clean(H2)
        if unsat5(H2): H=H2; changed=True
best=nx.convert_node_labels_to_integers(H)
PY("BEST n=%d m=%d connected=%s planar=%s mindeg=%d"%(best.number_of_nodes(),best.number_of_edges(),nx.is_connected(best),nx.check_planarity(best)[0],min(d for _,d in best.degree())))
json.dump({"n":best.number_of_nodes(),"edges":sorted(map(sorted,best.edges()))},open("smallest_unsat5.json","w"))
cl,e,nv=encode(best,5,'open',False); CNF(from_clauses=cl).to_file("smallest_unsat5.cnf")
PY("degree seq",sorted((d for _,d in best.degree()),reverse=True)[:12])
