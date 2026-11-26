import sys, random
from fractions import Fraction as F
import sympy as sp
from sympy import Poly
z=sp.Symbol('z')
def cols_sym(s_list,K):
    """reduced columns (poly in z, per derivative order 1..2K-1) with phi(s z) factored (and 1/sqrt(2pi))"""
    n=2*K-1
    def col(s,p0):
        out=[];p=p0
        for r in range(n):
            out.append(sp.expand(p)); p=sp.expand(sp.diff(p,z)-s**2*z*p)
        return out
    # first-derivative polys: Phi -> s ; z*phi -> 1 - s^2 z^2 (order-1 deriv of z phi)... order1 of zphi(sz)= phi+z*(-s^2 z)phi
    cs=[col(s,s) for s in s_list]                      # Phi columns, all K
    cz=[col(s,1-s**2*z**2) for s in s_list[:K-1]]     # z*phi columns, K-1
    return cs+cz
def Qred(s_list,K):
    c=cols_sym(s_list,K)
    M=sp.Matrix(2*K-1,2*K-1,lambda r,j:c[j][r])
    return M
def formula(s,K,zv):
    c=sp.Integer((-1)**((K-1)//2))*2**(K-1)*s[K-1]
    for i in range(K-1): c*=s[i]**3
    for i in range(K-1):
        for j in range(i+1,K-1): c*=(s[i]**2-s[j]**2)**4
        c*=(s[i]**2-s[K-1]**2)**2
    return c*zv**((2*K-1)*(K-1))
def check_numeric(K,s,zv):
    M=Qred(s,K).subs(z,zv)
    d=M.det(method='bareiss')
    return d, formula(s,K,zv)
if __name__=="__main__":
    log=open('log.txt','a')
    def P(*a):
        t=' '.join(str(x) for x in a); print(t); log.write(t+'\n'); log.flush()
    # fully symbolic
    for K in (2,3):
        ss=sp.symbols('s1:%d'%(K+1))
        M=Qred(list(ss),K)
        d=sp.factor(M.det(method='berkowitz'))
        f=formula(list(ss),K,z)
        P('SYMBOLIC K=%d  det==formula:'%K, sp.simplify(d-f)==0)
    # exact rational points
    random.seed(1)
    for K in range(2,9):
        ok=True
        for t in range(3 if K>6 else 6):
            s=sorted(set(sp.Rational(random.randint(1,40),random.randint(1,9)) for _ in range(K)))
            while len(s)<K: s=sorted(set(s+[sp.Rational(random.randint(1,60),random.randint(1,9))]))
            zv=sp.Rational(random.randint(1,30),random.randint(1,7))
            d,f=check_numeric(K,s,zv)
            if d!=f: ok=False; P('FAIL',K,s,zv)
        P('K=%d random rational points ok:'%K,ok)
