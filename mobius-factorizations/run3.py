from mob import *
import time
for s in [(5,5),(6,5),(7,6)]:
    t=time.time(); r=mu_bottom_top(s); d=mu_bottom_top_down(s)
    print("sig",s,"Omega",sum(s),"elements",r[1],"mu(up-rec)",r[0],"mu(down-rec)",d,"predicted sign (-1)^(Omega+1)=",(-1)**(sum(s)+1),"%.1fs"%(time.time()-t),flush=True)
