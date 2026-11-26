import sys
from fractions import Fraction as F
from math import factorial as fa, comb
sys.setrecursionlimit(10000)

def cat(n): return F(comb(2*n,n),n+1)
def binom(n,k): return comb(n,k) if (n>=0 and 0<=k<=n) else 0
def sgn(x): return (x>0)-(x<0)

# ---- definition of p (eq:p-def), zero outside 0<=l<=k<=n
def p(n,k,l):
    if not (0<=l<=k<=n): return F(0)
    return F(fa(n+k-2*l+1)*fa(2*n-k-l+1), fa(k-l)*fa(3*n-k+2-2*l))*(-1)**k*(3*n-3*k+2)*cat(n-k)

def H_def(N,c1,c2):  # eq:H-N-def (valid for integers N>=1); zero if c>N
    if c1>N or c2>N: return F(0)
    t=F(0)
    for l1 in range(0,N-c1+1):
        for l2 in range(0,N-c2+1):
            d=(l2==l1+1)-(l2==l1-1)
            if d: t+=p(N-1,N-c1,l1)*p(N-1,N-c2,l2)*d
    return t

def prod_range(a,b):
    r=F(1)
    for k in range(a,b+1): r*=k
    return r
def Q(N,c):  # prod_{a=1}^{c-1} (N^2-a^2)/(4N^2-a^2)
    r=F(1)
    for a in range(1,c): r*=F(N*N-a*a,4*N*N-a*a)
    return r
def X0(c,j): return 3*c**3*(3*j-1)+3*c**2*(3*j*j-8*j+3)+c*(-17*j*j+19*j-6)-2*j*(2*j-1)*(j-1)
def X1(c,j): return -12*c**3-6*c**2*(4*j-3)-2*c*(12*j*j-10*j-1)-2*(3*j+2)*(2*j-1)*(j-1)

def p_rat(N,c):  # eq:p-rational : (-1)^N p(N-1,N-c,0)
    return (-1)**c*(3*c-1)*cat(c-1)*F(1,2)*Q(N,c)

def H_rat(N,c1,c2):  # Prop H_N-rational, eq:H_N (rational expression, evaluated at N)
    if c1==c2: return F(0)
    if c1<c2: return -H_rat(N,c2,c1)
    pre=F((-1)**(c1-1)*(3*c1-1)*(3*c2-1)*(c1-c2),2*fa(c1+c2))*Q(N,c1)
    t=(c1+1)*prod_range(c1-2*c2+2,2*c1-c2-2)
    for j in range(1,c2):
        num=cat(c1-1)*(j*X0(c1,j)+N*N*X1(c1,j))*j*fa(2*c1-c2-2)*fa(c1+j-2)*fa(2*j)
        den=4*fa(j+1)*fa(2*c1-j-2)*fa(j)*(2*j-1)
        t+=(-1)**(j+1)*F(num,den)*F(1,4*N*N-j*j)*prod_range(c1-2*c2+2,c1-2*j-1)*Q(N,j)
    return pre*t

def entries(N,k,Hf,pf):
    """2k x 2k skew matrix, order white,black for r=0..k-1; Lemma lem:final-entries"""
    def S(m,c):  # sum_{m>=0} binom(c,2s-c-m+2) with m ranging; arg=2s-c+2 -> sum_{j=0}^{arg} binom(c,j)
        return None
    def cumb(c,top): # sum_{m>=0} binom(c, top-m)
        return sum(binom(c,j) for j in range(0,top+1)) if top>=0 else 0
    def f11(r,s):
        t=F(0)
        for c1 in range(r+2,2*r+3):
            for c2 in range(s+2,2*s+3):
                t+=Hf(N,c1,c2)*binom(c1-1,2*r-c1+2)*binom(c2-1,2*s-c2+2)
        return t
    def f00(r,s):
        t=F(0)
        for c1 in range(1,2*r+3):
            for c2 in range(1,2*s+3):
                t+=Hf(N,c1,c2)*cumb(c1,2*r-c1+2)*cumb(c2,2*s-c2+2)
        for c1 in range(1,2*r+3): t+=pf(N,c1)*cumb(c1,2*r-c1+2)
        for c2 in range(1,2*s+3): t-=pf(N,c2)*cumb(c2,2*s-c2+2)
        return t-sgn(s-r)
    def f10(r,s):
        t=F(0)
        for c1 in range(r+2,2*r+3):
            for c2 in range(1,2*s+3):
                t+=Hf(N,c1,c2)*binom(c1-1,2*r-c1+2)*cumb(c2,2*s-c2+2)
        for c1 in range(r+2,2*r+3): t+=pf(N,c1)*binom(c1-1,2*r-c1+2)
        return t+(1 if r==s else 0)
    n=2*k
    A=[[F(0)]*n for _ in range(n)]
    cache={}
    for r in range(k):
        for s in range(k):
            a=f11(r,s); d=f00(r,s); b=f10(r,s)
            c=-f10(s,r)
            A[2*r][2*s]=a; A[2*r][2*s+1]=b; A[2*r+1][2*s]=c; A[2*r+1][2*s+1]=d
    return A

def pfaff(A):
    A=[row[:] for row in A]; n=len(A); res=F(1)
    for i in range(0,n-1,2):
        piv=None
        for j in range(i+1,n):
            if A[i][j]!=0: piv=j;break
        if piv is None: return F(0)
        if piv!=i+1:
            A[i+1],A[piv]=A[piv],A[i+1]
            for row in A: row[i+1],row[piv]=row[piv],row[i+1]
            res=-res
        res*=A[i][i+1]
        for j in range(i+2,n):
            f=A[i][j]/A[i][i+1]
            if f!=0:
                # row/col j -= f * row/col i+1
                for m in range(n): A[j][m]-=f*A[i+1][m]
                for m in range(n): A[m][j]-=f*A[m][i+1]
    return res

def R_def(k,N): return pfaff(entries(N,k,H_def,lambda N,c:(-1)**N*p(N-1,N-c,0) if c<=N else F(0)))
def R_rat(k,N): return pfaff(entries(N,k,H_rat,p_rat))

# limits
def pinf(c): return (-1)**c*(3*c-1)*cat(c-1)/F(2**(2*c-1))
def Hinf(c1,c2):
    if c1==c2: return F(0)
    if c1<c2: return -Hinf(c2,c1)
    pre=F((-1)**(c1-1)*(3*c1-1)*(3*c2-1)*(c1-c2),2**(2*c1-1)*fa(c1+c2))
    t=(c1+1)*prod_range(c1-2*c2+2,2*c1-c2-2)
    for j in range(1,c2):
        num=cat(c1-1)*X1(c1,j)*j*fa(2*c1-c2-2)*fa(c1+j-2)*fa(2*j)
        den=2**(2*j+2)*fa(j+1)*fa(2*c1-j-2)*fa(j)*(2*j-1)
        t+=(-1)**(j+1)*F(num,den)*prod_range(c1-2*c2+2,c1-2*j-1)
    return pre*t
def P_half(k):
    return pfaff(entries(0,k,lambda N,a,b:Hinf(a,b),lambda N,c:pinf(c)))

if __name__=="__main__":
    K=int(sys.argv[1]) if len(sys.argv)>1 else 8
    print("== Step 2: half-plane values vs paper table")
    tab={1:(3,3),2:(59,10),3:(7737,21),4:(6803145,36),5:(40210542795,55),6:(1599678636998003,78),
         7:(428672479245743736177,105),8:(774167330660186496842976913,136)}
    for k in range(1,9):
        v=P_half(k); w=F(tab[k][0],2**tab[k][1])
        print(k,v==w,v)
    print("== check rational formula == definition for N>k")
    ok=True
    for k in range(1,6):
        for N in range(k+1,k+5):
            a=R_def(k,N); b=R_rat(k,N)
            if a!=b: ok=False; print("MISMATCH",k,N,a,b)
    print("def==rational for k<=5, N=k+1..k+4:",ok)
    print("== Step 3: R_k(k) vs R_{k-1}(k) vs 1/A_k")
    from math import prod
    def ASM(n): return prod(F(fa(3*i+1),fa(n+i)) for i in range(n))
    for k in range(2,K+1):
        a=R_rat(k,k); b=R_rat(k-1,k)
        print(k,a==b,"1/A_k ok" if b==1/ASM(k) else "1/A_k FAIL",a,b)
