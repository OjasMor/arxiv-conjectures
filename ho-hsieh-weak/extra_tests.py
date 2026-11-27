"""Extra tests: random g, tiny/huge g, g=0 (limit + direct optimisation), remainder scale."""
import random, numpy as np, mpmath as mp
from scipy.optimize import least_squares
from angles import *
from check import simulate, ground, zz_diag
random.seed(7); mp.mp.dps = 120
# remainder relative size
worst = 0
for L in [2,6,10,14]:
    for g in [-50,-1e-4,1e-4,50,0.7]:
        g=mp.mpf(str(g)); info=construct(L,g)
        worst=max(worst, info['rem']/max(abs(c) for c in info['P']))
print("max relative remainder of t-h(x(t)) mod (t-a(x(t))):", mp.nstr(worst,3))
# random g
worst=0; arg=None
for L in range(2,13,2):
    for _ in range(25):
        g = random.choice([-1,1])*10**random.uniform(-3,1.7)
        gam,bet,_=angles(L,mp.mpf(g)); psi=simulate(L,[float(x) for x in gam],[float(x) for x in bet])
        E,v,_=ground(L,g); inf=1-abs(np.vdot(v,psi))**2
        if inf>worst: worst,arg=inf,(L,g)
print("random g (25 per L, |g| in [1e-3,50], both signs), worst infidelity:",f"{worst:.2e}",arg)
# g=0
for L in range(2,13,2):
    cat=np.zeros(2**L); cat[0]=cat[-1]=1/np.sqrt(2)
    out=[]
    for g in ['1e-6','-1e-6','1e-9']:
        gam,bet,_=angles(L,mp.mpf(g)); psi=simulate(L,[float(x) for x in gam],[float(x) for x in bet])
        out.append(1-abs(np.vdot(cat,psi))**2)
    print(f"g->0 limit, L={L}: infidelity to even cat state at g=1e-6,-1e-6,1e-9:", ["%.1e"%o for o in out])
# direct optimisation of L/2 layers at g=0 and a few g
def opt(L,g,tries=60):
    E,v,_=ground(L,g); p=L//2; best=1
    f=lambda th: (lambda psi: np.concatenate([(v.conj()@psi*np.exp(0)).real*0+ (psi - np.vdot(v,psi)*v).real, (psi-np.vdot(v,psi)*v).imag]))(simulate(L,th[:p],th[p:]))
    rng=np.random.default_rng(0)
    for _ in range(tries):
        r=least_squares(f,rng.uniform(-np.pi,np.pi,2*p),xtol=1e-15,ftol=1e-15,gtol=1e-15)
        psi=simulate(L,r.x[:p],r.x[p:]); best=min(best,1-abs(np.vdot(v,psi))**2)
        if best<1e-12: break
    return best
for L in [2,4,6,8]:
    print(f"direct optimisation of L/2={L//2} layers, L={L}: best infidelity g=0:",f"{opt(L,0.0):.1e}", " g=-1.2:",f"{opt(L,-1.2):.1e}"," g=1:",f"{opt(L,1.0):.1e}")
