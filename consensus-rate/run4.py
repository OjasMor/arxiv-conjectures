import numpy as np
from acl import *
print("graph N eps/epsmax  esr(Qbar)   R(exact)    R-esr     R>esr?  [R vs 2/3-type bound (N-2)/(N-1)]")
cnt=0;tot=0
for name,Ns in (('complete',(3,4,5,6)),('path',(3,4,5,6)),('cycle',(4,5,6,7)),('star',(4,5,6))):
  for N in Ns:
    adj=graph(name,N);dmax=adj.sum(1).max();beta=np.ones(N)/N
    for f in (0.05,0.25,0.5,0.75,0.9,0.99):
        eps=f/(2*dmax);Q=Qs(adj,eps);Qb=sum(Q)/N
        e,_=esr(Qb);R,_,_=R_exact(Q,beta);tot+=1;cnt+=R>e+1e-9
        print("%-8s %d %.2f   %.8f  %.8f  %+.6f  %s   %.4f"%(name,N,f,e,R,R-e,R>e+1e-9,(N-2)/(N-1)))
print("R>esr in %d of %d settings"%(cnt,tot))
print("\nK4 fine eps sweep (eps/(1/6) from 0.02..0.98):")
N=4;adj=graph('complete',N);beta=np.ones(N)/N;gaps=[]
for f in np.linspace(0.02,0.98,25):
    eps=f/6;Q=Qs(adj,eps);e,_=esr(sum(Q)/N);R,_,_=R_exact(Q,beta);gaps.append(R-e)
    print("  eps=%.5f (=%.3f*max) esr=%.6f R=%.6f gap=%+.6f"%(eps,f,e,R,R-e))
print("min gap",min(gaps),"max",max(gaps))
# numeric sanity: compare Krylov R with full essential spectral radius of L
N=4;Q=Qs(graph('complete',N),1/8);L=Lop(Q,np.ones(N)/N);ev=np.linalg.eigvals(L);ev=ev[np.argsort(-abs(ev))]
print("top |eig(L)| full:",np.round(abs(ev[:6]),6))
