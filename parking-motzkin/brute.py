"""Backgammon parking, exactly as in arXiv:2611.29890.
Cars 1..n enter in order; car j parks at its preferred spot if empty; otherwise it bumps the
occupant out, takes the spot, and the bumped car goes to the start of the street and parks in the
first empty spot. Out_B = pi_1..pi_n with pi_s = car in spot s.
naive(n): enumerate all n^n lists.  merged(n): same simulation, but identical street states after t cars
are merged with multiplicities (the process depends only on the street state, so this is exact)."""
import sys, itertools
from collections import defaultdict

def step(street, car, p):
    """street: tuple of length n, 0=empty, 1-indexed cars. p is 1-indexed."""
    s = list(street)
    occ = s[p-1]
    s[p-1] = car
    if occ:
        s[s.index(0)] = occ   # bumped car: first empty spot from start
    return tuple(s)

def out_naive(alpha):
    n = len(alpha); s = (0,)*n
    for j, p in enumerate(alpha, 1):
        s = step(s, j, p)
    return s

def naive(n):
    cnt = defaultdict(int)
    for a in itertools.product(range(1, n+1), repeat=n):
        cnt[out_naive(a)] += 1
    return cnt

def merged(n):
    cur = {(0,)*n: 1}
    for car in range(1, n+1):
        nxt = defaultdict(int)
        for st, c in cur.items():
            for p in range(1, n+1):
                nxt[step(st, car, p)] += c
        cur = nxt
    return cur

_cache = {}
def counts(n):
    if n not in _cache: _cache[n] = merged(n)
    return _cache[n]

def target(k, n):
    return tuple(list(range(1, k+1)) + list(range(n, k, -1)))

def catalan(n):
    from math import comb
    return comb(2*n, n)//(n+1)

def motz(N):
    M = [1, 1]
    for m in range(2, N+1):
        M.append(((2*m+1)*M[m-1] + (3*m-3)*M[m-2])//(m+2))
    return M

if __name__ == "__main__":
    NMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 9
    M = motz(40)
    print("== paper example checks ==")
    print("Out_B(1,4,4,3,2,2) =", ''.join(map(str, out_naive((1,4,4,3,2,2)))), "(paper 164325)")
    print("Out_B(1,3,3,1)     =", ''.join(map(str, out_naive((1,3,3,1)))), "(paper 4231)")
    print("== naive vs merged agreement ==")
    for n in range(1, 8):
        a, b = naive(n), counts(n)
        assert dict(a) == dict(b), n
        print("n=%d identical (%d outcomes, total %d)" % (n, len(b), sum(b.values())))
    for n in range(8, NMAX+1): counts(n)
    print("== paper statements ==")
    mins = [1,2,4,8,17,36,75,160,351,726]
    for n in range(1, NMAX+1):
        c = counts(n)
        assert sum(c.values()) == n**n and all(sorted(k)==list(range(1,n+1)) for k in c)
        mn = min(c.values()); mx = max(c.values())
        ident = tuple(range(1, n+1))
        argmins = sorted(''.join(map(str,k)) if n<10 else str(k) for k,v in c.items() if v==mn)
        ok = [c[ident], c[ident[:-2]+(n,n-1)] if n>=2 else None, c[ident[:-3]+(n,n-2,n-1)] if n>=3 else None]
        print("n=%d all n^n=%d ok; max=%d (C_n=%d) min=%d (paper %d %s) argmin=%s; C_n outcomes %s"
              % (n, n**n, mx, catalan(n), mn, mins[n-1], "OK" if mn==mins[n-1] else "MISMATCH", argmins[:4], ok))
        dec = c[tuple(range(n,0,-1))]
        print("   dec n..1: %d vs M_n=%d %s" % (dec, M[n], "OK" if dec==M[n] else "MISMATCH"))
        if n >= 2:
            v = c[target(1, n)]
            print("   1 n..2: %d vs M_{n+1}-M_n=%d %s" % (v, M[n+1]-M[n], "OK" if v==M[n+1]-M[n] else "MISMATCH"))
        if n >= 3:
            v = c[target(2, n)]
            f = M[n+2]-2*M[n+1]+M[n]-M[n-1]
            print("   12 n..3: %d vs M_{n+2}-2M_{n+1}+M_n-M_{n-1}=%d %s" % (v, f, "OK" if v==f else "MISMATCH"))
    print("== target counts A(k,n) ==")
    for n in range(1, NMAX+1):
        print("n=%d:" % n, [counts(n)[target(k, n)] for k in range(0, n)])
