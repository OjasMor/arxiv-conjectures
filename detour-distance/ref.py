# Definition-literal reference: DFS over simple paths, all nonempty proper subsets, maximal-by-inclusion.
import itertools, sys
def detour(n, edges):
    adj=[[] for _ in range(n)]
    for a,b in edges: adj[a].append(b); adj[b].append(a)
    D=[[0]*n for _ in range(n)]
    for u in range(n):
        best=[0]*n
        def dfs(v,vis,l):
            if l>best[v]: best[v]=l
            for x in adj[v]:
                if not vis>>x&1: dfs(x,vis|1<<x,l+1)
        dfs(u,1<<u,0)
        for v in range(n): D[u][v]=best[v]
    return D
def is_ddd(n,D,S):
    for w in range(n):
        if w in S: continue
        vals=[D[w][x] for x in S]
        if len(set(vals))<len(vals): return False
    return True
def numbers(n,edges):
    D=detour(n,edges)
    sets=[]
    for m in range(1,1<<n):
        if m==(1<<n)-1: continue
        S=[i for i in range(n) if m>>i&1]
        if is_ddd(n,D,S): sets.append(m)
    ss=set(sets)
    maxl=[m for m in sets if not any((m|1<<v)!=m and any(((m2&m)==m and m2!=m) for m2 in [m|1<<v]) and (m|1<<v) in ss for v in range(n))]  # placeholder, fixed below
    # proper maximality: no DDD superset at all
    maxl=[m for m in sets if not any(m2!=m and (m2&m)==m for m2 in sets)]
    sz=[bin(m).count('1') for m in maxl]
    return min(sz),max(sz),maxl
def cyc(n): return [(i,(i+1)%n) for i in range(n)]
def path(n): return [(i,i+1) for i in range(n-1)]
def K(n): return [(i,j) for i in range(n) for j in range(i+1,n)]
def wheel(n): return [(0,i) for i in range(1,n)]+[(i,i%(n-1)+1) for i in range(1,n)]
def book(m): # a=0,b=1, x_i=2+2i,y_i=3+2i
    e=[(0,1)]
    for i in range(m): x,y=2+2*i,3+2*i; e+=[(0,x),(x,y),(y,1)]
    return 2+2*m,e
def flower(n): # h=0,c_i=1+i,l_i=1+n+i
    e=[(0,1+i) for i in range(n)]+[(1+i,1+(i+1)%n) for i in range(n)]
    e+=[(1+i,1+n+i) for i in range(n)]+[(0,1+n+i) for i in range(n)]
    return 1+2*n,e
def helm(n):
    e=[(0,1+i) for i in range(n)]+[(1+i,1+(i+1)%n) for i in range(n)]+[(1+i,1+n+i) for i in range(n)]
    return 1+2*n,e
def petersen():
    e=[(i,(i+1)%5) for i in range(5)]+[(i,i+5) for i in range(5)]+[(5+i,5+(i+2)%5) for i in range(5)]
    return 10,e
def cube(k):
    n=1<<k; return n,[(i,i^(1<<b)) for i in range(n) for b in range(k) if i<i^(1<<b)]
def prism(n): return 2*n,[(i,(i+1)%n) for i in range(n)]+[(n+i,n+(i+1)%n) for i in range(n)]+[(i,n+i) for i in range(n)]
def lollipop(m,k):
    e=K(m)+[(m-1+i,m+i) for i in range(k)]
    return m+k,e
if __name__=="__main__":
    def rep(name,n,e,exp):
        lo,hi,_=numbers(n,e); print(f"{name:28s} n={n:2d} dd_D={lo} DD_D={hi}  paper={exp}  {'OK' if exp==(lo,hi) else 'MISMATCH'}",flush=True)
    rep("paw",4,[(0,1),(1,2),(2,3),(3,1)],(2,2))
    for n in range(3,13):
        pass
    # cycles: DD(C_n)=n/r etc
    def cycexp(n):
        def pf(m): return [p for p in range(2,m+1) if m%p==0 and all(p%q for q in range(2,p))]
        ps=pf(n)
        if n%2==1:
            if len(ps)==1 and ps[0]==n: return (1,1)
            return (n//ps[-1], n//ps[0])
        odd=[p for p in ps if p%2]
        return (2, n//odd[0] if odd else 2)
    for n in [5,6,7,8,9,10,12]:
        rep(f"C{n}",n,cyc(n),cycexp(n))
    rep("K5",5,K(5),(1,1)); rep("K6",6,K(6),(1,1))
    rep("W5(K1+C4)",5,wheel(5),(1,1)); rep("W7",7,wheel(7),(1,1))
    for m in (3,4): n,e=book(m); rep(f"book B{m}",n,e,(2,4))
    n,e=flower(4); rep("flower Fl4",n,e,(3,3))
    n,e=flower(5); rep("flower Fl5",n,e,(3,3))
    n,e=helm(3); rep("helm H3",n,e,(2,2))
    n,e=helm(4); rep("helm H4",n,e,(2,2))
    n,e=petersen(); rep("Petersen",n,e,(1,1))
    n,e=cube(3); rep("Q3",n,e,(2,2))
    n,e=prism(3); rep("prism C3xK2",n,e,(1,1))
    n,e=prism(4); rep("prism C4xK2",n,e,(2,2))
    n,e=prism(5); rep("prism C5xK2",n,e,(1,1))
    n,e=lollipop(4,2); rep("lollipop L(4,2) DD=n+1",n,e,("-",3)) if False else None
    n,e=lollipop(4,2); lo,hi,_=numbers(n,e); print("lollipop L(4,2) DD_D",hi,"paper n+1=3", "OK" if hi==3 else "MISMATCH")
    n,e=lollipop(4,3); lo,hi,_=numbers(n,e); print("lollipop L(4,3) DD_D",hi,"paper n+1=4", "OK" if hi==4 else "MISMATCH")
    # 4-cycle with pendant example from paper: DDD=3 with listed maximal sets
    e=[(0,1),(1,2),(2,3),(3,0),(0,4)]  # u=0,x=1,v=2,y=3,l=4
    lo,hi,m=numbers(5,e); print("C4+pendant DD_D",hi,"paper 3", sorted(sorted(i for i in range(5) if s>>i&1) for s in m))
