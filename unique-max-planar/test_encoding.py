import random, networkx as nx, itertools
from um import *
random.seed(1); bad=0; tot=0
for trial in range(300):
    n=random.randint(2,6); G=nx.gnp_random_graph(n,random.random())
    for mode in ('open','closed'):
        if mode=='open' and any(d==0 for _,d in G.degree()): continue
        for proper in (False,True):
            for k in (1,2,3):
                r,col,_=solve(G,k,mode,proper)
                b=brute(G,k,mode,proper); tot+=1
                if r!=b: bad+=1; print("MISMATCH",G.edges(),k,mode,proper)
                if r: assert check(G,col,mode,proper)
print("tested",tot,"mismatches",bad)
