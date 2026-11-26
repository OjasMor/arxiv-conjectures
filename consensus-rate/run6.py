import numpy as np
from acl import *
print("graph N f  esr(Qbar)  R(Omega-cyclic)  R(ess, all modes)  R-esr")
cnt=tot=0;rows=[]
for name,Ns in (('complete',(3,4,5,6)),('path',(3,4,5,6)),('cycle',(4,5,6,7)),('star',(4,5,6))):
  for N in Ns:
    adj=graph(name,N);dmax=adj.sum(1).max();beta=np.ones(N)/N
    for f in (0.05,0.25,0.5,0.75,0.9,0.99):
        eps=f/(2*dmax);Q=Qs(adj,eps);e,_=esr(sum(Q)/N);Rk,Ra=R_clean(Q,beta);tot+=1;cnt+=Rk>e+1e-9
        print("%-8s %d %.2f  %.8f  %.8f  %.8f  %+.6f %s"%(name,N,f,e,Rk,Ra,Rk-e,"VIOLATES" if Rk>e+1e-9 else ""))
print("conjecture violated (R>esr) in %d of %d settings"%(cnt,tot))
print("\nK4 refined sweep, f=eps/(1/6)")
N=4;adj=graph('complete',N);beta=np.ones(N)/N
for f in np.linspace(0.02,0.98,25):
    Q=Qs(adj,f/6);e,_=esr(sum(Q)/N);Rk,Ra=R_clean(Q,beta);print("  eps=%.5f f=%.3f esr=%.6f R=%.6f gap=%+.6f"%(f/6,f,e,Rk,Rk-e))
