import json, networkx as nx
from um import *
from pysat.formula import CNF
from pysat.solvers import Solver
G=nx.convert_node_labels_to_integers(build((1,1,1,1),(0,0,0,0)))
print("n,m",G.number_of_nodes(),G.number_of_edges(),"connected",nx.is_connected(G),"planar",nx.check_planarity(G)[0],"mindeg",min(d for _,d in G.degree()))
json.dump({"n":G.number_of_nodes(),"edges":sorted(map(sorted,G.edges()))},open("A1111_n322.json","w"))
cl,e,nv=encode(G,5,'open',False); CNF(from_clauses=cl).to_file("A1111_n322_k5.cnf")
with Solver(name='glucose4',bootstrap_with=cl,with_proof=True) as S:
    r=S.solve(); pr=S.get_proof()
print("glucose4 k=5:", "SAT" if r else "UNSAT", "proof lines",len(pr) if pr else None)
open("A1111_n322_k5.drup","w").write("\n".join(pr)+"\n0\n" if False else "\n".join(pr)+"\n")
r,c,t=solve(G,6,'open',False); print("k=6",r,check(G,c,'open',False))
json.dump({str(v):c[v] for v in c},open("A1111_n322_iUMo6_colouring.json","w"))
