import numpy as np
from acl import *
def R_power(Q,beta,K=3000):
    n=Q[0].shape[0];Om=np.eye(n)-np.ones((n,n))/n;L=Lop(Q,beta);v=Om.reshape(-1).copy();lg=0
    ratios=[]
    for k in range(K):
        w=L@v; r=np.linalg.norm(w)/np.linalg.norm(v); v=w/np.linalg.norm(w); ratios.append(r)
    return np.mean(ratios[-200:]),ratios[-1]
for name,N,f in (('path',4,0.5),('path',5,0.5),('cycle',4,0.99),('cycle',6,0.99),('complete',4,0.75),('cycle',5,0.5)):
    adj=graph(name,N);eps=f/(2*adj.sum(1).max());Q=Qs(adj,eps);b=np.ones(N)/N
    R,_,L=R_exact(Q,b);ev=np.linalg.eigvals(L);ev=ev[np.argsort(-abs(ev))]
    print(name,N,f,"Krylov R=%.8f power-iter R=%.8f"%(R,R_power(Q,b)[0]),"top |eig L|:",np.round(abs(ev[:4]),8))
