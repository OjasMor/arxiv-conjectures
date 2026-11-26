"""Claimed formula from runs/attempts/2611.29890__1.md:
P_0=1, P_{k+1}(z)=z^2 P_k - z*sum_{j=0..k} C_j P_{k-j};  A(k,n)=sum_{h=0..2k} [z^h]P_k * M_{n-k+h}."""
import sys
from brute import counts, target, catalan, motz

def polys(K):
    P = [[1]]
    for k in range(K):
        new = [0]*(2*(k+1)+1)
        for i, c in enumerate(P[k]): new[i+2] += c
        for j in range(k+1):
            for i, c in enumerate(P[k-j]): new[i+1] -= catalan(j)*c
        P.append(new)
    return P

def claimed(k, n, P, M):
    return sum(c*M[n-k+h] for h, c in enumerate(P[k]))

if __name__ == "__main__":
    NMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 9
    P = polys(NMAX); M = motz(60)
    for k in range(0, 5): print("P_%d coeffs (z^0..):" % k, P[k])
    bad = 0; tot = 0
    print("k  n  brute  formula  status")
    for n in range(1, NMAX+1):
        for k in range(0, n):
            b = counts(n)[target(k, n)]; f = claimed(k, n, P, M); tot += 1
            st = "match" if b == f else "MISMATCH"
            bad += b != f
            print("%d  %d  %d  %d  %s" % (k, n, b, f, st))
    print("cases", tot, "mismatches", bad)
