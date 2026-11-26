# Counting-across-a-gap lemma: if g < a+b, bounds cannot host a+b distinct positive integers for some l.
import itertools
def feasible(bounds):  # distinct positive integers x_i<=bounds_i exist iff sorted k-th bound >= k
    b=sorted(bounds); return all(b[k]>=k+1 for k in range(len(b)))
bad=0;tot=0
for a in range(1,9):
  for b in range(1,9):
    for g in range(1,a+b):   # g<a+b
      tot+=1
      # lemma: exists l in 1..g with infeasible
      if all(feasible([l+a-1]*a+[g-l+b]*b) for l in range(1,g+1)): bad+=1; print("lemma fails",a,b,g)
    g=a+b  # sharpness: g=a+b all l feasible
    if not all(feasible([l+a-1]*a+[g-l+b]*b) for l in range(1,g+1)): print("note: g=a+b also infeasible at some l",a,b)
print("gap lemma checked",tot,"cases, failures",bad)
# equality for cycles C_n
import sys; sys.path.insert(0,'.')
from ref import numbers,cyc
for n in range(5,16):
    lo,hi,_=numbers(n,cyc(n)); print(f"C{n}: DD_D={hi}  bound max(2,floor(n/3))={max(2,n//3)}  {'equal' if hi==max(2,n//3) else 'below'}  (3|n: {n%3==0})",flush=True)
