# Claimed algorithm from attempt 2611.28073__1.md. Input: list of closed intervals (L,R).
INF = float("inf")
def esi_algo(iv):
    n = len(iv)
    # nodes: 0 = s, 1..n = intervals, n+1 = t
    L = [-INF] + [a for a, b in iv] + [INF]
    R = [-INF] + [b for a, b in iv] + [INF]
    order = sorted(range(n + 2), key=lambda i: (L[i], R[i], i))  # topological: arcs need L_i < L_j
    N = n + 2
    best = {}
    dp = [None] * N
    dp[0] = 0
    for jj, j in enumerate(order):
        pass
    # longest path by DP over nodes in order of L; arc i->j requires L_i<L_j, R_i<R_j, F(i,j) pairwise disjoint
    def arc(i, j):
        if not (L[i] < L[j] and R[i] < R[j]): return None
        F = [(L[v], R[v]) for v in range(1, n + 1) if R[i] < L[v] and R[v] < L[j]]
        F.sort()
        for a, b in zip(F, F[1:]):
            if b[0] <= a[1]: return None   # closed intervals intersect
        return len(F)
    val = {0: 0}
    for j in order:
        if j == 0: continue
        bj = None
        for i in order:
            if L[i] >= L[j]: break
            if i not in val or i == n + 1: continue
            w = arc(i, j)
            if w is not None and (bj is None or val[i] + w > bj): bj = val[i] + w
        if bj is not None: val[j] = bj
    return val[n + 1]
