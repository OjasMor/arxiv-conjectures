# ESI number straight from the paper's definition: B independent and every v in N(B)=N[B]\B has a neighbour in D=V\N[B].
# Empty set allowed (vacuous). Isolated vertex alone is an ESI-set.
def esi_brute(n, adj):  # adj: list of bitmasks
    best = 0
    full = (1 << n) - 1
    for B in range(1 << n):
        c = bin(B).count("1")
        if c <= best: continue
        nb = 0; ok = True
        for v in range(n):
            if B >> v & 1:
                if adj[v] & B: ok = False; break
                nb |= adj[v]
        if not ok: continue
        NB = nb | B          # N[B]
        D = full & ~NB
        N_open = NB & ~B
        for w in range(n):
            if N_open >> w & 1 and not (adj[w] & D): ok = False; break
        if ok: best = c
    return best

def from_edges(n, edges):
    adj = [0]*n
    for a, b in edges: adj[a] |= 1 << b; adj[b] |= 1 << a
    return adj

def interval_adj(iv):
    n = len(iv); adj = [0]*n
    for i in range(n):
        for j in range(i+1, n):
            if max(iv[i][0], iv[j][0]) <= min(iv[i][1], iv[j][1]):
                adj[i] |= 1 << j; adj[j] |= 1 << i
    return adj

def components(n, adj):
    seen = 0; c = 0
    for s in range(n):
        if seen >> s & 1: continue
        c += 1; st = [s]; seen |= 1 << s
        while st:
            u = st.pop()
            m = adj[u] & ~seen
            for w in range(n):
                if m >> w & 1: seen |= 1 << w; st.append(w)
    return c

if __name__ == "__main__":
    path = lambda n: from_edges(n, [(i, i+1) for i in range(n-1)])
    cyc = lambda n: from_edges(n, [(i, (i+1) % n) for i in range(n)])
    ok = True
    for n in range(3, 17):   # paper: es(P_n)=ceil(n/4) (P_2=K_2 is complete component, excluded)
        a = esi_brute(n, path(n)); e = -(-n//4); ok &= a == e
        print("P%d" % n, a, "paper", e, "OK" if a == e else "MISMATCH")
    for n in range(3, 17):   # es(C_n)=floor(n/4)
        a = esi_brute(n, cyc(n)); e = n//4; ok &= a == e
        print("C%d" % n, a, "paper", e, "OK" if a == e else "MISMATCH")
    for n in range(2, 9):    # complete graphs: 0
        a = esi_brute(n, from_edges(n, [(i,j) for i in range(n) for j in range(i+1,n)])); ok &= a == 0
        print("K%d" % n, a, "paper 0 (only complete split graphs have 0)")
    print("ALL MATCH" if ok else "SOME MISMATCH")
