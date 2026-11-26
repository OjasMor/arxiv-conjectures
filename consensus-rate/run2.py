import numpy as np, sympy as sp
from acl import *
print("=== exact rational check K4 eps=1/8 ===")
N=4;eps=sp.Rational(1,8)
def Qs_sym(N,adjl,eps):
    adj=sp.Matrix(adjl); P=2*eps*adj
    for i in range(N): P[i,i]=1-sum(P[i,j] for j in range(N) if j!=i)
    out=[]
    for i in range(N):
        Q=sp.zeros(2*N,2*N); nb=[j for j in range(N) if adj[i,j]]
        for h in range(N):
            if h not in nb: Q[h,h]=1
        for j in nb:
            Q[j,j]+=P[j,j]; Q[j,i]+=P[j,i]
            for h in range(N):
                if adj[j,h] and h!=i: Q[j,N+h]+=P[j,h]
        Q[N+i,i]=1
        for h in range(N):
            if h!=i: Q[N+h,N+h]=1
        out.append(Q)
    return out
adjl=[[0 if i==j else 1 for j in range(N)] for i in range(N)]
Q=Qs_sym(N,adjl,eps);n=2*N
Qb=sum(Q,sp.zeros(n,n))/N
t=sp.symbols('t');print("charpoly Qbar:",sp.factor(Qb.charpoly(t).as_expr()))
Om=sp.eye(n)-sp.ones(n,n)/n
L=sum((sp.kronecker_product(q.T,q.T) for q in Q),sp.zeros(n*n,n*n))/N
v=sp.Matrix(list(Om))
K=[v]
while True:
    M=sp.Matrix.hstack(*K,L*K[-1])
    if M.rank()==len(K): break
    K.append(L*K[-1])
print("Krylov dim",len(K))
Kmat=sp.Matrix.hstack(*K); C=(Kmat.T*Kmat).inv()*Kmat.T*L*Kmat  # companion-ish
cp=sp.factor(C.charpoly(t).as_expr());print("char poly of L on cyclic subspace of Omega:",cp)
rts=sp.Poly(cp,t).nroots(n=30);print("roots:",rts)
print("R exact =",max(abs(r) for r in rts))
print("esr(Qbar) = 5/8 =",sp.Rational(5,8),"; R-esr =",max(abs(r) for r in rts)-sp.Rational(5,8))
