import numpy as np
from acl import *
print("Paper Assumption 1 (eps=R/(2(nu+1)), R=1, beta uniform) regular graphs:")
for name,N in (('complete',3),('complete',4),('complete',5),('complete',6),('complete',8),('cycle',5),('cycle',6),('cycle',8),('cycle',10)):
    adj=graph(name,N);nu=int(adj.sum(1)[0]);eps=1/(2*(nu+1));Q=Qs(adj,eps);e,_=esr(sum(Q)/N);Rk,Ra=R_clean(Q,np.ones(N)/N)
    print("  %-8s N=%d nu=%d eps=%.4f esr=%.6f R=%.6f gap=%+.6f %s"%(name,N,nu,eps,e,Rk,Rk-e,"VIOLATES" if Rk>e+1e-9 else "ok"))
