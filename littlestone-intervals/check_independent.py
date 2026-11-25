"""Independent check (our own code, exact rationals) of Conjecture 31 of arXiv:2611.28727.

Definitions taken from the paper:
  T(l) = t + (l - 2^t)/2^t, t = floor(lg l)                      (interpolated log, l >= 1)
  cutting recursion (eq. rlcut):  V(S) = max(0, max over cuts l = u+v (u,v>=1) of a piece l>=2 of
                                  1/2 * (1 + T(u)/2 + T(v)/2 + V(S')))
  greedy rule: cut a largest piece l, t = floor(lg l), into u = max(2^(t-1), l - 2^t), v = l - u
  R(1) = 0, R(l) = 1 - 2^(1-l) + (R(floor(l/2)) + R(ceil(l/2)))/2
Checks:
  A. exact optimum V == greedy value on every multiset of pieces >= 2 with total measure <= NA
  B. V((n)) == R(n) for single rods n <= NB (uses the multiset DP)
  C. supersolution inequality: for every multiset with total <= NC and every cut, one cut then greedy <= greedy
  D. single rods up to ND: every first cut followed by greedy never beats greedy
"""
import sys
from fractions import Fraction as Fr
from functools import lru_cache

def T(l):
    t = l.bit_length() - 1
    return Fr(t) + Fr(l - (1 << t), 1 << t)

def greedy_cut(l):
    t = l.bit_length() - 1
    u = max(1 << (t - 1), l - (1 << t)) if t >= 1 else None
    return u, l - u

@lru_cache(maxsize=None)
def greedy_value(S):
    """S: sorted tuple of pieces >= 2 (units dropped)."""
    if not S:
        return Fr(0)
    l = S[-1]
    u, v = greedy_cut(l)
    rest = tuple(sorted(S[:-1] + tuple(x for x in (u, v) if x >= 2)))
    return Fr(1, 2) * (1 + T(u) / 2 + T(v) / 2 + greedy_value(rest))

def after_cut(S, idx, u, v):
    return tuple(sorted(S[:idx] + S[idx + 1:] + tuple(x for x in (u, v) if x >= 2)))

@lru_cache(maxsize=None)
def opt_value(S):
    best = Fr(0)
    seen = set()
    for idx, l in enumerate(S):
        if l in seen:
            continue
        seen.add(l)
        for u in range(1, l // 2 + 1):
            v = l - u
            val = Fr(1, 2) * (1 + T(u) / 2 + T(v) / 2 + opt_value(after_cut(S, idx, u, v)))
            if val > best:
                best = val
    return best

@lru_cache(maxsize=None)
def R(l):
    if l == 1:
        return Fr(0)
    return 1 - Fr(1, 2 ** (l - 1)) + (R(l // 2) + R((l + 1) // 2)) / 2

def multisets(total, minpart=2, maxpart=None):
    """all sorted tuples of parts >= 2 with sum <= total"""
    out = [()]
    def rec(prefix, remaining, lo):
        for p in range(lo, remaining + 1):
            cur = prefix + (p,)
            out.append(cur)
            rec(cur, remaining - p, p)
    rec((), total, minpart)
    return out

if __name__ == "__main__":
    NA, NB, NC, ND = (int(x) for x in (sys.argv[1:5] or (34, 60, 44, 600)))
    sys.setrecursionlimit(100000)
    ms = multisets(NA)
    bad = sum(1 for S in ms if opt_value(S) != greedy_value(S))
    print(f"A. multisets with total <= {NA}: {len(ms)} states, optimum != greedy in {bad}")
    badB = [n for n in range(1, NB + 1) if opt_value((n,) if n >= 2 else ()) != R(n)]
    print(f"B. single rods n <= {NB} (m = n-1 <= {NB-1}): RL != R(n) for {badB}")
    msC = multisets(NC); viol = 0; cuts = 0
    for S in msC:
        g = greedy_value(S); seen = set()
        for idx, l in enumerate(S):
            if l in seen: continue
            seen.add(l)
            for u in range(1, l // 2 + 1):
                cuts += 1
                if Fr(1, 2) * (1 + T(u) / 2 + T(l - u) / 2 + greedy_value(after_cut(S, idx, u, l - u))) > g:
                    viol += 1
    print(f"C. one cut then greedy vs greedy, total <= {NC}: {len(msC)} states, {cuts} cuts, violations {viol}")
    violD = 0; cutsD = 0
    for n in range(2, ND + 1):
        g = greedy_value((n,))
        assert g == R(n), n
        for u in range(1, n // 2 + 1):
            cutsD += 1
            if Fr(1, 2) * (1 + T(u) / 2 + T(n - u) / 2 + greedy_value(after_cut((n,), 0, u, n - u))) > g:
                violD += 1
    print(f"D. single rods 2..{ND}: greedy == R(n) for all; {cutsD} first cuts, violations {violD}")
