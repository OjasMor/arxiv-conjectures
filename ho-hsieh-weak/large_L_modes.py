"""Mode-level check for larger L (no 2^L vector). For each pair mode x_j it applies the L/2 layers
exp(i b Z) exp(i v (x Z + s X)) to (1,0) and compares with the ground spinor of -((g+x) Z + s X).
Independent of angles.py except for the angles themselves. Usage: python large_L_modes.py L g [digits]"""
import sys, mpmath as mp
import angles as A
L = int(sys.argv[1]); g = mp.mpf(sys.argv[2]); A.mp.mp.dps = mp.mp.dps = int(sys.argv[3]) if len(sys.argv) > 3 else 300
gam, bet, info = A.angles(L, g)
assert len(gam) == L // 2
worst = mp.mpf(0)
for j in range(1, L // 2 + 1):
    x = -mp.cos((2 * j - 1) * mp.pi / L); s = mp.sqrt(1 - x * x)
    psi = mp.matrix([1, 0])
    for ga, be in zip(gam, bet):
        v, b = 2 * ga, 2 * be
        c, q = mp.cos(v), mp.sin(v)
        U1 = mp.matrix([[c + 1j * q * x, 1j * q * s], [1j * q * s, c - 1j * q * x]])   # exp(i v (xZ+sX))
        U2 = mp.matrix([[mp.exp(1j * b), 0], [0, mp.exp(-1j * b)]])                     # exp(i b Z)
        psi = U2 * (U1 * psi)
    m = g + x; d = mp.sqrt(m * m + s * s)
    t = mp.matrix([m + d, s]); t = t / mp.sqrt((m + d) ** 2 + s * s)
    ov = abs(mp.conj(psi[0]) * t[0] + mp.conj(psi[1]) * t[1]) ** 2
    worst = max(worst, 1 - ov)
print(f"L={L} g={mp.nstr(g, 8)} layers={len(gam)} worst mode infidelity={mp.nstr(worst, 3)}")
