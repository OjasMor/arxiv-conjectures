from mob import *
import time
def sigs(O):
    # partitions of O into parts (nonincreasing) = prime signatures
    def rec(rem,mx):
        if rem==0: yield (); return
        for p in range(min(rem,mx),0,-1):
            for r in rec(rem-p,p): yield (p,)+r
    yield from rec(O,O)
print("== validation: 3 methods agree (up-recursion, down-recursion, direct-grouping brute force)")
for O in range(2,9):
    for s in sigs(O):
        a=mu_bottom_top(s)[0]; b=mu_bottom_top_down(s)
        c=brute_small(s) if O<=7 else None
        assert a==b and (c is None or a==c),(s,a,b,c)
print("all agree for Omega<=8 (brute force Omega<=7)",flush=True)
print("== scan: sig, Omega, mu, (-1)^(Omega+1), status")
viol=[];
import sys
maxO=int(sys.argv[1])
for O in range(2,maxO+1):
    t=time.time()
    for s in sigs(O):
        v=mu_bottom_top(s)[0]; pred=(-1)**(O+1)
        st="ok" if v==0 or (v>0)==(pred>0) else "VIOLATION"
        if len(s)==1 and s[0]>=3 and v!=0: st="PRIMEPOWER-VIOLATION"
        if st!="ok": viol.append((s,O,v,pred))
        print(s,O,v,pred,st,flush=True)
    print("# Omega",O,"done in %.1fs"%(time.time()-t),flush=True)
print("VIOLATIONS:",viol)
