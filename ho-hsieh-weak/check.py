"""Full 2^L state-vector check of the construction in angles.py against direct diagonalisation.
Conventions (Jiang 2611.31308): H_X=-sum X, H_ZZ=-sum ZZ (periodic), H_TFIM=H_ZZ+g H_X,
|Psi>=prod_k exp(-i beta_k H_X) exp(-i gamma_k H_ZZ)|+..+>, layer 1 first.
Usage: python check.py [Lmax]
"""
import sys, numpy as np, mpmath as mp
import scipy.sparse as sp, scipy.sparse.linalg as sla
from angles import angles

def zz_diag(L):
    idx = np.arange(2 ** L); s = 1 - 2 * ((idx[:, None] >> np.arange(L)) & 1)  # z=+1 for bit 0
    return -np.sum(s * np.roll(s, -1, axis=1), axis=1).astype(float)

def apply_hx(psi, beta, L):
    """exp(-i beta H_X) = prod exp(i beta X_j)"""
    c, s = np.cos(beta), np.sin(beta)
    psi = psi.reshape([2] * L)
    for ax in range(L):
        a = np.take(psi, 0, axis=ax); b = np.take(psi, 1, axis=ax)
        psi = np.stack([c * a + 1j * s * b, 1j * s * a + c * b], axis=ax)
    return psi.reshape(-1)

def simulate(L, gam, bet):
    d = zz_diag(L); psi = np.ones(2 ** L, complex) / np.sqrt(2 ** L)
    for gk, bk in zip(gam, bet):
        psi = np.exp(-1j * gk * d) * psi
        psi = apply_hx(psi, bk, L)
    return psi

def ham(L, g):
    d = zz_diag(L); N = 2 ** L
    H = sp.diags(d).tocsr()
    idx = np.arange(N)
    for j in range(L):
        H = H + sp.csr_matrix((-g * np.ones(N), (idx, idx ^ (1 << j))), shape=(N, N))
    return H

def ground(L, g):
    """Ground state in the spin-flip-EVEN sector (prod X = +1).  For |g| << 1 the even/odd splitting
    ~ g^L is below double precision, so an unrestricted eigensolver returns an arbitrary mixture;
    the even-sector ground state is the unique ground state for g != 0 (Perron-Frobenius, and prod Z_j
    conjugation for g<0) and the symmetric cat state at g = 0."""
    N = 2 ** L; idx = np.arange(N); comp = (N - 1) ^ idx
    rep = idx[idx < comp]; M = len(rep)
    S = sp.csr_matrix((np.full(2 * M, 1 / np.sqrt(2)), (np.concatenate([rep, comp[rep]]), np.concatenate([np.arange(M)] * 2))), shape=(N, M))
    He = (S.T @ ham(L, g) @ S).tocsr()
    if M <= 2200:
        w, v = np.linalg.eigh(He.toarray()); w0, v0, gap = w[0], v[:, 0], w[1] - w[0]
    else:
        w, v = sla.eigsh(He, k=3, which='SA', tol=1e-14); o = np.argsort(w); w0, v0, gap = w[o[0]], v[:, o[0]], w[o[1]] - w[o[0]]
    return w0, S @ v0, gap

if __name__ == "__main__":
    Lmax = int(sys.argv[1]) if len(sys.argv) > 1 else 12
    gs = [-3, -1.2, -1, -0.5, -0.01, 0.01, 0.3, 1, 1.5, 4]
    print("g grid:", gs)
    print(f"{'L':>3} " + " ".join(f"{g:>9}" for g in gs) + "   worst")
    for L in range(2, Lmax + 1, 2):
        row = []
        for g in gs:
            gam, bet, _ = angles(L, mp.mpf(str(g)))
            psi = simulate(L, [float(x) for x in gam], [float(x) for x in bet])
            E, v0, gap = ground(L, g)
            row.append(1 - abs(np.vdot(v0, psi)) ** 2)
        print(f"{L:>3} " + " ".join(f"{x:9.1e}" for x in row) + f"   {max(row):.1e}", flush=True)
