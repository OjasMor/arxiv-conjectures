import random
from brute import esi_brute
random.seed(2)
def reform(n, adj):
    full=(1<<n)-1; best=0
    for S in range(1<<n):
        nb=0
        for v in range(n):
            if S>>v&1: nb|=adj[v]|(1<<v)
        R=full&~nb
        if any(R>>v&1 and adj[v]&R for v in range(n)): continue
        best=max(best,bin(R).count("1"))
    return best
tot=bad=0
for _ in range(6000):
    n=random.randint(1,9); p=random.choice([.1,.2,.3,.5,.7])
    adj=[0]*n
    for i in range(n):
        for j in range(i+1,n):
            if random.random()<p: adj[i]|=1<<j; adj[j]|=1<<i
    tot+=1
    a,b=esi_brute(n,adj),reform(n,adj)
    if a!=b: bad+=1; print("MISMATCH",n,adj,a,b)
print("general graphs",tot,"mismatches",bad)
