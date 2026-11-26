import numpy as np
from acl import *
rng=np.random.default_rng(1)
N=4;adj=graph('complete',N);eps=1/8;Q=np.array(Qs(adj,eps));n=2*N
Om=np.eye(n)-np.ones((n,n))/n
Rx,_,L=R_exact(list(Q),np.ones(N)/N)
xi0=np.array([1,0,0,0,1,0,0,0.])
# exact E||Om xi_k||^2 for this init via second-moment operator
M=Om.copy().reshape(-1); vals=[]
for k in range(0,61):
    vals.append(xi0@M.reshape(n,n)@xi0); M=L@M
vals=np.array(vals)
print("exact E||Om xi_k||^2 k=0,1,2,10,30,60:",vals[[0,1,2,10,30,60]])
for k in (20,40,60): print(" ratio v[k]/v[k-1] k=%d: %.8f ; v[k]^(1/k)=%.6f"%(k,vals[k]/vals[k-1],vals[k]**(1/k)))
print("exact asymptotic ratio (R) =",Rx)
# Monte Carlo
runs=2_000_000;K=26
xi=np.tile(xi0,(runs,1));mc=[]
for k in range(K+1):
    mc.append(np.mean(np.sum((xi@Om)**2,axis=1)))   # Om symmetric
    idx=rng.integers(0,N,runs)
    xi=np.einsum('rij,rj->ri',Q[idx],xi)
mc=np.array(mc)
print("MC (2e6 runs) vs exact, k=0,5,10,15,20,25:")
for k in (0,5,10,15,20,25): print("  k=%d MC=%.6e exact=%.6e rel=%.2e"%(k,mc[k],vals[k],mc[k]/vals[k]-1))
sl=np.polyfit(np.arange(10,K),np.log(mc[10:K]),1)[0]; print("MC fitted rate exp(slope) k=10..25:",np.exp(sl)," exact same-window:",np.exp(np.polyfit(np.arange(10,K),np.log(vals[10:K]),1)[0]))
print("MC ratio mc[25]/mc[24]=",mc[25]/mc[24])
# almost-sure / Lyapunov (norm, not squared)
runs=20000;K=400;xi=rng.normal(size=(runs,n));lg=np.zeros(runs)
for k in range(K):
    idx=rng.integers(0,N,runs);xi=np.einsum('rij,rj->ri',Q[idx],xi)
    nr=np.linalg.norm(xi@Om,axis=1);xi=xi@Om*0+xi  # keep
    # renormalize disagreement part only: xi = c*1 + d ; scale d
    m=xi.mean(1,keepdims=True);d=xi-m;s=np.linalg.norm(d,axis=1,keepdims=True);lg+=np.log(s[:,0]);xi=m*0+d/s
print("a.s. Lyapunov rate exp(lambda) (norm):",np.exp(lg.mean()/K)," squared:",np.exp(2*lg.mean()/K)," (vs esr 0.625, R_ms 0.6711, sqrt(R_ms)=%.4f)"%Rx**.5)
