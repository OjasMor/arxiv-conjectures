# Independent plain-Python checker: edge list JSON + colouring JSON -> open-neighbourhood UM check
import json,sys
g=json.load(open(sys.argv[1])); col={int(k):v for k,v in json.load(open(sys.argv[2])).items()}
adj={i:set() for i in range(g["n"])} if "n" in g else {}
for a,b in g["edges"]: adj.setdefault(a,set()).add(b); adj.setdefault(b,set()).add(a)
assert all(a!=b for a,b in g["edges"]) and len({tuple(sorted(e)) for e in g["edges"]})==len(g["edges"]), "not simple"
assert all(adj[v] for v in adj), "isolated vertex"
bad=[v for v in adj if [col[u] for u in adj[v]].count(max(col[u] for u in adj[v]))!=1]
print("n",len(adj),"m",len(g["edges"]),"colours used",sorted(set(col.values())),"violations",len(bad))
