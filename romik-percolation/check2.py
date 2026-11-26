from rk import *
print("== k up to 12 (R_rat at N=k)")
from math import prod
def ASM(n): return prod(F(fa(3*i+1),fa(n+i)) for i in range(n))
for k in range(2,13):
    A=entries(k,k,H_rat,p_rat)
    row=A[2*k-2]; nz=[(j,row[j]) for j in range(2*k) if row[j]!=0]
    a=pfaff(A); b=R_rat(k-1,k)
    print(k,"last white row nonzeros:",nz,"| equal:",a==b,"| =1/A_k:",a==1/ASM(k),"|",a)
print("== R_k(N) for N>k consistent with direct definition, sample k=6,7")
for k in (6,7):
    for N in (k+1,k+2):
        print(k,N,R_def(k,N)==R_rat(k,N))
print("== H_def vs H_rat at N=k for c<=k (sanity) and vanishing for c1>k")
N=6
print(all(H_rat(N,c1,c2)==0 for c1 in range(7,13) for c2 in range(1,13)))
print(all(H_rat(N,c1,c2)==H_def(N,c1,c2) for c1 in range(1,7) for c2 in range(1,7)))
# symbolic R_1,R_2
import sympy as sp
