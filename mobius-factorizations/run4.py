from mob import *
import time,sys
def sigs2(O):  # all parts >=2
    def rec(rem,mx):
        if rem==0: yield (); return
        for p in range(min(rem,mx),1,-1):
            for r in rec(rem-p,p): yield (p,)+r
    yield from rec(O,O)
print("== scan2: signatures with all exponents >=2 (no simple prime): sig, Omega, mu, (-1)^(Omega+1), status")
viol=[]
for O in range(2,int(sys.argv[1])+1):
    t=time.time()
    for s in sigs2(O):
        v=mu_bottom_top(s)[0]; pred=(-1)**(O+1)
        st="ok" if v==0 or (v>0)==(pred>0) else "VIOLATION"
        if len(s)==1 and s[0]>=3 and v!=0: st="PRIMEPOWER-VIOLATION"
        if st!="ok": viol.append((s,O,v,pred))
        print(s,O,v,pred,st,flush=True)
    print("# Omega",O,"done in %.1fs"%(time.time()-t),flush=True)
print("VIOLATIONS:",viol)
