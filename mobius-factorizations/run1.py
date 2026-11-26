from mob import *
# paper table
table={(2,2):-1,(3,3):-3,(4,4):-8,(3,2):2,(4,3):5,(5,4):13,(4,2):-3,(5,3):-8,(6,4):-22,(5,2):4,(6,3):13,(5,5):-18,
(6,2):-5,(2,2,2):-16,(3,2,2):31,(7,2):7,(8,2):-9,(4,2,2):-52,(3,3,2):-72,(2,2,2,2):-312}
bad=0
for sig,v in table.items():
    got=mu_bottom_top(sig)[0]; ok=got==v; bad+=not ok
    print("table",sig,"paper",v,"mine",got,"OK" if ok else "MISMATCH",flush=True)
print("mismatches",bad)
# prime powers 1..10 ; n=16 values; Example collision; simple-prime theorem
print("prime powers",[mu_bottom_top((k,))[0] for k in range(1,11)])
# n=16 explicit
r=mu_bottom_top((4,)); mt=r[2]
for f in [(4,),(3,1),(2,2),(2,1,1),(1,1,1,1)]:
    key=tuple(sorted(((a,) for a in f),reverse=True)); print("16: mu(",f,",16)=",mt[key])
# a(16),a(81),a(36),a(64)
for s in [(4,),(2,2),(6,)]:
    mt=mu_bottom_top(s)[2]; print("a(sig",s,")=",sum(abs(v) for v in mt.values()))
# example 2.2: n=p^3 q^3 r^2, x = p p q q r r pq ; mu(x,n)=92
els,up=upsets((3,3,2))
x=tuple(sorted([(1,0,0)]*2+[(0,1,0)]*2+[(0,0,1)]*2+[(1,1,0)],reverse=True))
top=((3,3,2),); m={}
for e in sorted(els,key=len):
    m[e]=1 if e==top else -sum(m[y] for y in up[e] if y!=e)
print("Example mu(x,n)=",m[x],"(paper 92)")
# simple-prime theorem check: sig with a 1 : (e..,1)
from math import factorial
for sig in [(2,1),(3,1),(2,2,1),(3,2,1),(4,2,1)]:
    mm=sum(sig)-1; 
    pred=(-1)**mm*factorial(mm)
    for e in sig[:-1]: pred//=factorial(e)
    print("thm",sig,mu_bottom_top(sig)[0],pred)
# A369713 a(60)=16 a(24)=8
for s in [(2,1,1),(3,1)]:
    mt=mu_bottom_top(s)[2]; print("a",s,sum(abs(v) for v in mt.values()))
