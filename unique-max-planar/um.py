import itertools, json, time, sys
import networkx as nx
from pysat.solvers import Solver

class B:
    def __init__(s): s.G=nx.Graph(); s.n=0
    def new(s):
        v=s.n; s.n+=1; s.G.add_node(v); return v
    def e(s,a,b): s.G.add_edge(a,b)
    def mark(s,a,b):
        m=s.new(); s.e(m,a); s.e(m,b); return m
    def O(s):
        vs=[s.new() for _ in range(21)]
        for i in range(21): s.e(vs[i],vs[(i+1)%21])
        for h in (0,7,14):
            for j in range(2,8): s.e(vs[h],vs[(h+j)%21])
        return vs
def build(a_blocks=(2,2,2,2), o_blocks=(2,2,2,1), core=True, hubs=3, plen=6):
    b=B(); core_v=[b.new() for _ in range(4)]
    for x,y in itertools.combinations(core_v,2): b.e(x,y); b.mark(x,y)
    for ci,c in enumerate(core_v):
        for _ in range(a_blocks[ci]):
            H=[b.new() for _ in range(hubs)]
            K=[c]+H
            for x,y in itertools.combinations(K,2): b.e(x,y); b.mark(x,y)
            for h in H:
                P=[b.new() for _ in range(plen)]
                for i in range(plen-1): b.e(P[i],P[i+1])
                for p in P:
                    b.e(p,c); b.e(p,h); b.mark(c,p); b.mark(h,p)
                for i in range(plen-1):
                    q=b.new(); b.e(q,c); b.e(q,P[i]); b.e(q,P[i+1])
        for _ in range(o_blocks[ci]):
            for v in b.O(): b.e(c,v)
    return b.G

def encode(G,k,mode='iUMo',proper=False,order=None):
    """returns clauses, var map. mode open/closed."""
    nodes=list(G.nodes()); idx={v:i for i,v in enumerate(nodes)}
    cnt=[0]
    def nv(): cnt[0]+=1; return cnt[0]
    # ord vars y[v][c] = colour>=c, c=1..k+1 ; y[v][1]=True, y[v][k+1]=False
    cl=[]; y={}; 
    T=nv(); cl.append([T])
    for v in nodes:
        y[v]={1:T}
        for c in range(2,k+1): y[v][c]=nv()
        y[v][k+1]=-T
        for c in range(2,k+1): cl.append([-y[v][c],y[v][c-1]])
    e={}
    for v in nodes:
        e[v]={}
        for c in range(1,k+1):
            x=nv(); e[v][c]=x
            # x <-> y[c] & ~y[c+1]
            cl.append([-x,y[v][c]]); cl.append([-x,-y[v][c+1]]); cl.append([x,-y[v][c],y[v][c+1]])
    if proper:
        for u,v in G.edges():
            for c in range(1,k+1): cl.append([-e[u][c],-e[v][c]])
    for v in nodes:
        N=list(G.neighbors(v))
        if mode=='closed': N=N+[v]
        if not N: continue
        for c in range(1,k+1):
            if c==k: s=None
            else:
                s=nv()
                for u in N: cl.append([-y[u][c+1],s])
                cl.append([-s]+[y[u][c+1] for u in N])
            for u,w in itertools.combinations(N,2):
                cl.append([-e[u][c],-e[w][c]]+([s] if s else []))
    return cl,e,cnt[0]

def solve(G,k,mode,proper=False,solver='cadical153',want_cnf=None):
    cl,e,nvars=encode(G,k,mode,proper)
    if want_cnf:
        from pysat.formula import CNF
        CNF(from_clauses=cl).to_file(want_cnf)
    t=time.time()
    with Solver(name=solver,bootstrap_with=cl) as S:
        r=S.solve(); model=S.get_model() if r else None
    dt=time.time()-t
    col=None
    if r:
        ms=set(l for l in model if l>0)
        col={v:next(c for c in range(1,k+1) if e[v][c] in ms) for v in G.nodes()}
    return r,col,dt

def check(G,col,mode,proper=False):
    for v in G.nodes():
        N=list(G.neighbors(v))
        if mode=='closed': N.append(v)
        if not N: continue
        m=max(col[u] for u in N)
        if sum(1 for u in N if col[u]==m)!=1: return False
    if proper and any(col[u]==col[v] for u,v in G.edges()): return False
    return True

def brute(G,k,mode,proper=False):
    nodes=list(G.nodes())
    for t in itertools.product(range(1,k+1),repeat=len(nodes)):
        col=dict(zip(nodes,t))
        if check(G,col,mode,proper): return True
    return False
