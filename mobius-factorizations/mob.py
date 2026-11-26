import sys, itertools
from functools import lru_cache
from math import factorial

def all_elements(sig):
    """All multisets of nonzero vectors in N^t summing to sig (sorted tuples)."""
    t=len(sig)
    vecs=[v for v in itertools.product(*[range(a+1) for a in sig]) if any(v)]
    vecs.sort(reverse=True)
    out=[]
    def rec(i,rem,cur):
        if not any(rem): out.append(tuple(cur)); return
        for j in range(i,len(vecs)):
            v=vecs[j]
            if all(v[k]<=rem[k] for k in range(t)):
                cur.append(v); rec(j,tuple(r-x for r,x in zip(rem,v)),cur); cur.pop()
    rec(0,tuple(sig),[])
    return out

def merges(x):
    """all multisets from merging two distinct positions of x (covers going up, plus possibly non-covers; fine)."""
    res=set()
    n=len(x)
    for i in range(n):
        for j in range(i+1,n):
            s=tuple(a+b for a,b in zip(x[i],x[j]))
            y=tuple(sorted(x[:i]+x[i+1:j]+x[j+1:]+(s,),reverse=True))
            res.add(y)
    return res

def upsets(sig):
    """up-set of each element under repeated pairwise merge (= coarsening order)."""
    els=all_elements(sig)
    els.sort(key=len)
    up={}
    for x in els:
        s={x}
        for y in merges(x): s|=up[y]
        up[x]=s
    return els,up

def mu_bottom_top(sig):
    els,up=upsets(sig)
    top=(tuple(sig),)
    mu_to_top={}   # mu(x,top), by increasing |x|... recurse from top
    for x in sorted(els,key=len):   # fewer factors = higher
        if x==top: mu_to_top[x]=1; continue
        mu_to_top[x]=-sum(mu_to_top[y] for y in up[x] if y!=x)
    bottom=tuple(sorted([tuple(1 if k==i else 0 for k in range(len(sig))) for i,a in enumerate(sig) for _ in range(a)],reverse=True))
    return mu_to_top[bottom],len(els),mu_to_top,bottom,els,up

def mu_bottom_top_down(sig):
    """independent method: mu(bottom,z) = -sum_{bottom<=y<z} mu(bottom,y), using down-sets from up-sets."""
    els,up=upsets(sig)
    bottom=tuple(sorted([tuple(1 if k==i else 0 for k in range(len(sig))) for i,a in enumerate(sig) for _ in range(a)],reverse=True))
    down={x:[] for x in els}
    for y in els:
        for z in up[y]:
            if z!=y: down[z].append(y)
    m={}
    for z in sorted(els,key=lambda x:-len(x)):
        if z==bottom: m[z]=1
        else: m[z]=-sum(m[y] for y in down[z])
    top=(tuple(sig),)
    return m[top]

def brute_small(sig):
    """Direct definition on labelled prime factors: coarsening = group the labelled factors; compares as multisets."""
    labels=[i for i,a in enumerate(sig) for _ in range(a)]
    n=len(labels)
    # all set partitions of positions -> element = multiset of exponent vectors
    def setparts(k):
        def rec(i,blocks):
            if i==k: yield [list(b) for b in blocks]; return
            for b in blocks:
                b.append(i); yield from rec(i+1,blocks); b.pop()
            blocks.append([i]); yield from rec(i+1,blocks); blocks.pop()
        yield from rec(0,[])
    def vec(b):
        v=[0]*len(sig)
        for p in b: v[labels[p]]+=1
        return tuple(v)
    els=set(); 
    for sp in setparts(n): els.add(tuple(sorted((vec(b) for b in sp),reverse=True)))
    els=list(els)
    # y<=z iff z coarsening of y: exists grouping of y's vectors summing to z's vectors
    def coarsens(y,z):
        # y list of vectors, assign each to a block of z so sums match
        zs=list(z)
        def rec(i,rem):
            if i==len(y): return all(not any(r) for r in rem)
            seen=set()
            for j,r in enumerate(rem):
                if r in seen: continue
                seen.add(r)
                if all(a<=b for a,b in zip(y[i],r)):
                    new=rem[:j]+[tuple(b-a for a,b in zip(y[i],r))]+rem[j+1:]
                    if rec(i+1,new): return True
            return False
        return rec(0,zs)
    bottom=tuple(sorted([tuple(1 if k==i else 0 for k in range(len(sig))) for i,a in enumerate(sig) for _ in range(a)],reverse=True))
    top=(tuple(sig),)
    els.sort(key=lambda x:-len(x))
    m={bottom:1}
    for z in els:
        if z==bottom: continue
        m[z]=-sum(m[y] for y in els if y in m and y!=z and len(y)>len(z) and coarsens(y,z))
    return m[top]

def omega(sig): return sum(sig)
if __name__=="__main__":
    pass
