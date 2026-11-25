a = ffgen((x^4+x+1)*Mod(1,2), 'a);
G = [a^1+a^2+a^3,a^2+a^3,a^0+a^1,a^2+a^3,a^1+a^3,a^0,a^0+a^1+a^3,a^1,a^1,a^0+a^1+a^2,a^0,a^0+a^1+a^3,a^0+a^2,a^0+a^2,a^0+a^1+a^3,a^0+a^1+a^3,0,0;0,a^2+a^3,a^1+a^2,a^0+a^1+a^2,a^1+a^2+a^3,a^0+a^2,a^0+a^1+a^2+a^3,a^1+a^2+a^3,a^0+a^1,a^1+a^3,a^1+a^3,a^0+a^3,a^0+a^3,a^2+a^3,a^3,a^0+a^1,a^0+a^1,0;0,a^2+a^3,a^0+a^1+a^2+a^3,a^0+a^2,a^0+a^3,a^0+a^1+a^2,a^0+a^2,a^1+a^2,a^0+a^2,a^0+a^1,a^2+a^3,a^1+a^2,a^0+a^1+a^3,a^1+a^2+a^3,a^0+a^1,a^3,0,a^0+a^3];
n = matsize(G)[2];
gram = G * mattranspose(G);
print("gram is zero: ", gram == matrix(3,3,i,j,0*a));
bad = 0; forsubset([n,3], s, if(matdet(matrix(3,3,i,j,G[i,s[j]])) == 0, bad++));
print("singular 3x3 column minors: ", bad, " of ", binomial(n,3));
els = concat([0*a], vector(15, i, a^i));
minw = n; cnt = 0;
for(i=1,16, for(j=1,16, for(k=1,16, if(i+j+k>3, c = els[i]*G[1,]+els[j]*G[2,]+els[k]*G[3,]; w = sum(t=1,n, c[t]!=0); cnt++; if(w<minw, minw=w)))));
print("nonzero codewords: ", cnt, "  minimum weight: ", minw, "  (MDS needs ", n-3+1, ")");
quit
