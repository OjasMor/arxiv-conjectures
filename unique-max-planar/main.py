import json, sys, networkx as nx
from um import *
PY=lambda *a: print(*a,flush=True)
W=build()
PY("W n,m",W.number_of_nodes(),W.number_of_edges(),"connected",nx.is_connected(W),"planar",nx.check_planarity(W)[0],
   "simple/no loops",nx.number_of_selfloops(W)==0,"min deg",min(d for _,d in W.degree()))
json.dump({"n":W.number_of_nodes(),"edges":sorted(map(sorted,W.edges()))},open("W781.json","w"))
# validation on paper's graphs
O=nx.Graph(); 
bb=B(); vs=bb.O(); O=bb.G
PY("O n,m",O.number_of_nodes(),O.number_of_edges(),"planar",nx.check_planarity(O)[0])
for k in (4,5):
    r,c,t=solve(O,k,'closed',True); PY("O pUMc k=%d"%k,r,"%.2fs"%t, check(O,c,'closed',True) if r else "")
G7=nx.Graph()
b=B(); core=[b.new() for _ in range(4)]
for x,y in itertools.combinations(core,2): b.e(x,y)
for i,c in enumerate(core):
    for _ in range((2,2,2,1)[i]):
        for v in b.O(): b.e(c,v)
G7=b.G
PY("G7 n,m",G7.number_of_nodes(),G7.number_of_edges(),"planar",nx.check_planarity(G7)[0])
for mode,prop,name,ks in (('closed',True,'pUMc',(6,7)),('open',True,'pUMo',(6,7)),('open',False,'iUMo',(4,5,6)),('closed',False,'iUMc',(3,4))):
    for k in ks:
        r,c,t=solve(G7,k,mode,prop); PY("G7",name,"k=%d"%k,"SAT" if r else "UNSAT","%.2fs"%t, check(G7,c,mode,prop) if r else "")
# K4 with marks: paper says iUMo? selector example only; check small marked K4
K=nx.complete_graph(4); 
for x,y in list(K.edges()): K.add_edge(('m',x,y),x); K.add_edge(('m',x,y),y)
for k in (2,3,4):
    r,c,t=solve(K,k,'open',False); PY("marked K4 iUMo k=%d"%k,r)
# W
for mode,prop,name,ks in (('open',False,'iUMo',(5,6)),('closed',False,'iUMc',(3,4)),('closed',True,'pUMc',(6,7)),('open',True,'pUMo',(6,7))):
    for k in ks:
        r,c,t=solve(W,k,mode,prop); ok=check(W,c,mode,prop) if r else ""
        PY("W",name,"k=%d"%k,"SAT" if r else "UNSAT","%.2fs"%t,"verified" if ok is True else ok)
        if r and name=='iUMo' and k==6: json.dump({str(v):c[v] for v in c},open("W781_iUMo6_colouring.json","w"))
