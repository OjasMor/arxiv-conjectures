import numpy as np, itertools
def graph(name,N):
    A=np.zeros((N,N))
    if name=='complete': A=1-np.eye(N)
    elif name=='path':
        for i in range(N-1): A[i,i+1]=A[i+1,i]=1
    elif name=='cycle':
        for i in range(N): A[i,(i+1)%N]=A[(i+1)%N,i]=1
    elif name=='star':
        A[0,1:]=1;A[1:,0]=1
    return A
def P_matrix(adj,eps,Rv=1.0):
    # both directed arcs present: p_ij=eps*(R^-1+R^-1); p_ii=1-sum
    P=2*eps/Rv*adj
    P+=np.diag(1-P.sum(1)); return P
def Qs(adj,eps):
    N=len(adj);P=P_matrix(adj,eps);out=[]
    for i in range(N):
        Q=np.zeros((2*N,2*N))
        nb=[j for j in range(N) if adj[i,j]]
        for h in range(N):
            if h not in nb: Q[h,h]=1          # sum_{h notin N_i} e_h e_h^T (includes i)
        for j in nb:
            Q[j,j]+=P[j,j]; Q[j,i]+=P[j,i]
            for h in range(N):
                if adj[j,h] and h!=i: Q[j,N+h]+=P[j,h]   # Q12
        Q[N+i,i]=1                              # Q21
        for h in range(N):
            if h!=i: Q[N+h,N+h]=1               # Q22 = I - e_i e_i^T
        out.append(Q)
    return out
def esr(M):
    ev=np.linalg.eigvals(M); ev=ev[np.argsort(-abs(ev))]
    k=np.argmin(abs(ev-1)); assert abs(ev[k]-1)<1e-9
    rest=np.delete(ev,k); return max(abs(rest)),ev
def Lop(Q,beta):
    n=Q[0].shape[0]
    # vec(Q^T M Q) with row-major vec: (Q^T kron Q^T) vec(M)
    return sum(b*np.kron(q.T,q.T) for b,q in zip(beta,Q))
def R_exact(Q,beta):
    n=Q[0].shape[0]; Om=np.eye(n)-np.ones((n,n))/n
    L=Lop(Q,beta)
    # restrict to cyclic subspace of Omega: Krylov basis
    v=Om.reshape(-1); basis=[]
    K=[v/np.linalg.norm(v)]
    for _ in range(n*n):
        w=L@K[-1]
        for u in K: w=w-u*(u@w)
        for u in K: w=w-u*(u@w)
        if np.linalg.norm(w)<1e-10: break
        K.append(w/np.linalg.norm(w))
    K=np.array(K).T
    Lr=K.T@L@K
    ev=np.linalg.eigvals(Lr)
    return max(abs(ev)), ev, L
def R_full_disagree(L,n):
    # spectral radius on all eigenmodes except the all-ones (1⊗1) mode: ess spectral radius
    return esr(L)[0]

def R_clean(Q,beta,tol=1e-9):
    """R = spectral radius of L=E[Q^T . Q] on the cyclic subspace of Omega, computed inside the
    invariant kernel of M -> 1^T M 1 (removes the eigenvalue-1 mode exactly)."""
    n=Q[0].shape[0];L=Lop(Q,beta);Om=np.eye(n)-np.ones((n,n))/n
    one=np.ones(n*n)/n
    # orthonormal basis of kernel of functional one^T
    U,S,Vt=np.linalg.svd(one.reshape(1,-1));B=Vt[1:].T
    Lk=B.T@L@B; assert np.linalg.norm(L@B-B@Lk)<1e-9
    ev=np.linalg.eigvals(Lk);Rall=max(abs(ev))
    v=B.T@Om.reshape(-1);K=[v/np.linalg.norm(v)]
    for _ in range(Lk.shape[0]):
        w=Lk@K[-1]
        for _ in range(2):
            for u in K: w=w-u*(u@w)
        if np.linalg.norm(w)<tol: break
        K.append(w/np.linalg.norm(w))
    K=np.array(K).T;Rk=max(abs(np.linalg.eigvals(K.T@Lk@K)))
    return Rk,Rall
