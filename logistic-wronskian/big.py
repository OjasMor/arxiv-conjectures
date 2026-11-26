import random, sympy as sp
from fractions import Fraction as F
def polycols(s,K):
    n=2*K-1
    # represent polys in z as dict via sympy-free int lists evaluated at z=zv numerically: need derivative -> use coefficient lists
    def col(sv,p0):
        out=[];p=p0[:]
        for r in range(n):
            out.append(p)
            dp=[i*p[i] for i in range(1,len(p))]
            q=dp+[0]; 
            sh=[0,0]+p      # z * p shifted: s^2 z p
            L=max(len(q),len(sh)); q+= [0]*(L-len(q)); sh+=[0]*(L-len(sh))
            p=[q[i]-sv*sv*sh[i] if False else q[i]-sv*sv*(sh[i-1] if i>=1 else 0) for i in range(L)]
        return out
    return col
def build(s,K,zv):
    n=2*K-1
    def col(sv,p0):
        out=[];p=list(p0)
        for r in range(n):
            out.append(sum(c*zv**i for i,c in enumerate(p)))
            dp=[i*p[i] for i in range(1,len(p))]+[0]
            zp=[0]+p
            L=max(len(dp),len(zp)); dp+=[0]*(L-len(dp)); zp+=[0]*(L-len(zp))
            p=[dp[i]-sv*sv*zp[i] for i in range(L)]
        return out
    cols=[col(sv,[sv]) for sv in s]+[col(sv,[1,0,-sv*sv]) for sv in s[:K-1]]
    return [[cols[j][r] for j in range(n)] for r in range(n)]
def bareiss(M):
    n=len(M);M=[r[:] for r in M];sign=1;prev=1
    for k in range(n-1):
        if M[k][k]==0:
            for i in range(k+1,n):
                if M[i][k]!=0: M[k],M[i]=M[i],M[k];sign=-sign;break
            else: return 0
        for i in range(k+1,n):
            for j in range(k+1,n):
                M[i][j]=(M[i][j]*M[k][k]-M[i][k]*M[k][j])//prev
        prev=M[k][k]
    return sign*M[n-1][n-1]
def formula(s,K,zv):
    c=(-1)**((K-1)//2)*2**(K-1)*s[K-1]
    for i in range(K-1):
        c*=s[i]**3
        for j in range(i+1,K-1): c*=(s[i]**2-s[j]**2)**4
        c*=(s[i]**2-s[K-1]**2)**2
    return c*zv**((2*K-1)*(K-1))
def P(*a):
    t=' '.join(str(x) for x in a);print(t,flush=True);open('log.txt','a').write(t+'\n')
random.seed(7)
P('--- paper integer checks s=(1..K), z=1')
for K in (2,3,8,12):
    s=list(range(1,K+1));d=bareiss(build(s,K,1));f=formula(s,K,1)
    P('K',K,'det==formula',d==f,'digits',len(str(abs(d))), d if K<4 else '')
P('--- beyond paper: random integer scales, random integer z, exact integer Bareiss')
for K in range(6,21):
    ok=True;cnt=0
    for t in range(4 if K<=16 else 2):
        s=sorted(random.sample(range(1,60),K));zv=random.randint(1,9)
        d=bareiss(build(s,K,zv));cnt+=1
        if d!=formula(s,K,zv): ok=False;P('FAIL',K,s,zv)
    P('K=%d trials=%d ok=%s'%(K,cnt,ok))
