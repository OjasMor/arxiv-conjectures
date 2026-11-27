# second, direct (non-order) encoding + other solvers, as an independent cross-check
import json, itertools, sys, time
from pysat.solvers import Solver
def direct(n,adj,k):
    x=lambda v,c: v*k+c   # c in 1..k
    nv=n*k; cl=[]
    for v in range(n):
        cl.append([x(v,c) for c in range(1,k+1)])
        for c,d in itertools.combinations(range(1,k+1),2): cl.append([-x(v,c),-x(v,d)])
    for v in range(n):
        N=sorted(adj[v])
        for c in range(1,k+1):
            nv+=1; g=nv   # g <-> some neighbour has colour > c   (fully defined)
            hi=[x(u,d) for u in N for d in range(c+1,k+1)]
            for l in hi: cl.append([-l,g])
            cl.append([-g]+hi)
            for u,w in itertools.combinations(N,2): cl.append([-x(u,c),-x(w,c),g])
    return cl
def load(f):
    g=json.load(open(f)); n=g["n"]; adj=[set() for _ in range(n)]
    for a,b in g["edges"]: adj[a].add(b); adj[b].add(a)
    return n,adj
for f in sys.argv[1:]:
    n,adj=load(f)
    for k in (5,6):
        cl=direct(n,adj,k)
        for name in ("cadical153","glucose4","minisat22","maplechrono"):
            t=time.time()
            with Solver(name=name,bootstrap_with=cl) as S: r=S.solve()
            print(f,"n=%d"%n,"k=%d"%k,name,"SAT" if r else "UNSAT","%.2fs"%(time.time()-t),flush=True)
