import sympy as sp
z=sp.Symbol('z',positive=True)
Phi=lambda a: (1+sp.erf(a*z/sp.sqrt(2)))/2
phi=lambda a: sp.exp(-a**2*z**2/2)/sp.sqrt(2*sp.pi)
out=open('log.txt','a')
for K,s in ((2,[1,3]),(3,[1,2,5])):
    n=2*K-1
    fs=[Phi(a) for a in s]+[z*phi(a) for a in s[:K-1]]
    M=sp.Matrix(n,n,lambda r,j: sp.diff(fs[j],z,r+1))
    raw=M.det()
    g=phi(s[K-1])
    for a in s[:K-1]: g*=phi(a)**2
    sq=sp.sqrt(2*sp.pi)**n  # reduced drops 1/sqrt(2pi) per column
    import big_formula as bf
    Q=bf.formula(s,K,z)
    r=sp.simplify(raw/(g*Q*sq)) if False else sp.simplify(raw/(g*Q))
    t='RAW minor / (phi-factors * c_K z^N) for K=%d s=%s : %s'%(K,s,r)
    print(t);out.write(t+'\n')
