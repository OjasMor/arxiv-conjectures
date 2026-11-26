import numpy as np
from acl import *
np.set_printoptions(precision=10,linewidth=150)
N=4;adj=graph('complete',N);eps=1/8
Q=Qs(adj,eps);beta=np.ones(N)/N
for q in Q: assert np.allclose(q.sum(1),1)
Qb=sum(Q)/N
e,ev=esr(Qb);print("esr(Qbar) K4 eps=1/8 =",e); print(sorted(np.round(ev.real,6)))
# paper lemma: s2^(1)=1-(nu^2+1)/(N(nu+1))
nu=3;print("paper s2^(1)=",1-(nu**2+1)/(N*(nu+1)))
# paper Lemma eigenMap check: roots of f for each lambda_i(P)
P=P_matrix(adj,eps);lam=np.sort(np.linalg.eigvalsh(P))[::-1];print("lam(P)",lam)
roots=[]
for l in lam:
    a=-((N-nu)/N+l/N+(nu-1)/(N*(nu+1)));b=-(N-1)/N;c=-(nu-1)/N**2*(l-1/(nu+1))
    roots+=list(np.roots([1,a+b,a*b+c]))
print("lemma roots",sorted(np.round(np.real(roots),6)))
print("eig Qbar   ",sorted(np.round(ev.real,6)))
# theorem: esr per paper
gs=((nu-1)+N*(nu+1)-np.sqrt(N**2*(nu+1)**2-2*N*(nu**3+nu+2)+(nu-1)**2+(nu**2+1)**2))/(nu+1)
print("gamma*",gs,"1-esr(P)",1-max(abs(lam[1:])))
R,evr,L=R_exact(Q,beta);print("R (exact, Krylov of Omega) =",R)
print("sr E[Q^T Om Q] =",max(np.linalg.eigvalsh(sum(q.T@(np.eye(8)-np.ones((8,8))/8)@q for q in Q)/N)))
print("esr^2 =",e**2," esr =",e," R-esr =",R-e)
print("top |eig| of L restricted:",sorted(abs(evr))[::-1][:8])
print("2/3 =",2/3)
