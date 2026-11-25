a = ffgen((x^5+x^2+1)*Mod(1,2), 'a);
G = [a^1+a^2+a^3+a^4,a^0+a^2+a^4,a^1+a^2+a^4,a^1,a^0+a^1+a^2,a^1+a^3,a^0+a^2+a^4,a^0+a^1+a^2+a^3,a^0+a^2,a^1+a^3,a^0+a^2+a^3+a^4,a^1+a^3,a^1+a^3,a^2+a^4,a^0+a^1+a^2+a^3+a^4,a^0,a^2+a^3,a^0+a^3+a^4,a^0+a^3,a^0+a^1+a^2+a^3+a^4,a^3+a^4,a^0+a^1+a^2,a^0+a^2+a^3,a^0+a^4,a^1+a^2+a^3+a^4,a^0+a^1+a^2+a^3+a^4,a^0+a^1+a^2+a^3,a^1+a^2+a^4,a^0+a^1+a^3+a^4,a^1+a^2+a^3,a^0+a^1+a^3,a^1+a^2+a^4,0,0;0,a^0+a^2+a^4,a^0+a^3,a^1+a^2,a^2+a^3+a^4,a^0+a^1+a^2,a^0+a^4,a^3,a^0+a^2+a^3,a^4,a^2+a^3,a^2,a^0+a^1+a^2+a^4,a^0+a^1+a^2+a^3+a^4,a^0+a^1+a^3,a^0+a^1+a^2+a^3,a^1+a^2+a^3+a^4,a^4,a^1+a^2+a^4,a^1,a^1+a^2+a^4,a^2,a^0+a^2,a^0+a^2,a^0+a^2+a^3+a^4,a^1+a^3+a^4,a^1,a^2+a^3+a^4,a^0+a^3,a^0+a^1+a^2+a^4,a^2+a^3,a^1+a^2+a^3,a^2+a^3,0;0,a^0+a^2+a^4,a^1,a^0+a^1+a^2,a^1+a^2,a^0+a^1+a^2+a^4,a^0+a^2,a^0+a^2,a^0+a^1+a^4,a^0+a^3,a^2+a^4,a^3+a^4,a^1+a^2+a^3+a^4,a^0+a^2+a^3,a^1,a^1+a^4,a^0+a^2,a^3,a^0+a^3+a^4,a^3+a^4,a^0+a^1,a^1+a^3,a^0+a^1+a^3,a^3+a^4,a^0+a^1+a^2+a^3+a^4,a^0+a^2+a^4,a^1+a^2+a^4,a^1+a^4,a^1+a^3,a^1+a^3,a^1+a^4,a^0+a^1+a^2+a^4,0,a^0+a^3];
n = matsize(G)[2];
print("q=32 n=", n, "  gram is zero: ", G * mattranspose(G) == matrix(3,3,i,j,0*a));
bad = 0; forsubset([n,3], s, if(matdet(matrix(3,3,i,j,G[i,s[j]])) == 0, bad++));
print("singular 3x3 column minors: ", bad, " of ", binomial(n,3));
quit
